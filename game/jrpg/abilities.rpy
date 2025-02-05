init 2 python:
    hugepunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
    bigdamagepunch = Move((15, 0), (0, 15), .10, bounce=True, repeat=True, delay=0)

    class NonTarget:
        def __init__(self):
            pass

        def use(self, fight: Fight, character: Character):
            pass

        def playSound(self):
            renpy.play("audio/punch.opus")

    class Insult(Ability):
        def __init__(self):
            super().__init__(name = "Прокричать оскорбления (Эффект зависит от особенностей врага)", strength = 0)

        def useAgainst(self, enemy: Character, character: Character):
            self.playSound()
            renpy.say(None, enemy.insultingPhrase())
            enemy.offend()

        def playSound(self):
            renpy.play("audio/characters/miha/laugh.mp3")

    class Shoulder(Ability):
        def __init__(self):
            super().__init__(name = "Влететь с плеча в лоха (-30)", strength = 30)

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.with_statement(hugepunch)
            renpy.pause(1)

    class AoeShoulder(Ability):
        def __init__(self):
            super().__init__(name = "Трактором с плеча прокатиться по всем (-30 всем противникам)", strength = 30)
            self.setTargeted(False)

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.with_statement(hugepunch)
            renpy.pause(1)

        def use(self, fight: Fight, character: Character):
            [character.hit(enemy, self.strength) for enemy in fight.enemyParty.members.values()]
            self.playSound()

    class Smoke(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Дымка 50 никотина (Ослабляет противников)", strength = 1)
            self.setTargeted(False)

        def useAgainst(self, enemy: Character, character: Character):
            self.playSound()
            enemy.changeVulnerableRatio(2)

        def use(self, fight: Fight, character: Character):
            self.playSound()
            [enemy.changeVulnerableRatio(2) for enemy in fight.enemyParty.members.values()]
            renpy.say(None, "Враги ахуели с этой прикормки")
            renpy.say(None, "Атаки против врагов стали в 2 раза сильнее")

        def playSound(self):
            renpy.play("audio/characters/igoryas/smoke.mp3")
            renpy.pause(4)

    class TheWall(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Встать стеной (+60HP, Провокация)", strength = 1)
            self.setTargeted(False)

        def use(self, fight: Fight, character: Character):
            fight.party.setTarget(character)
            character.health += 60
            self.playSound()
            renpy.say(character.getRenpyChar(), "Я щит Ваааргуса")

        def playSound(self):
            renpy.play("audio/characters/igoryas/taunt.mp3")
            renpy.pause(1)

    class ReleaseTurns(Ability, NonTarget):
        def __init__(self, turns):
            super().__init__(name = "Совершить ходы х({})".format(turns), strength = 1)
            self.turns = turns
            self.setTargeted(False)

        def use(self, fight: Fight, character: Character):
            self.playSound()
            renpy.say(character.getRenpyChar(), "Поехали")
            character.abilities = [ability for ability in character.abilities if not isinstance(ability, ReleaseTurns) and not isinstance(ability, StackTurns)]
            for i in range(self.turns):
                turnExecuted = True
                if not fight.isOver():
                    turnExecuted = False
                    while not turnExecuted:
                        turnExecuted = fight.makeTurnNoItems()
            character.abilities.append(StackTurns())
            renpy.say(character.getRenpyChar(), "Все")

        def playSound(self):
            renpy.play("audio/characters/miha/theworldo.mp3")
            renpy.pause(1)

    class StackTurns(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Настакать ходы (Текущее значение: х1)", strength = 1)
            self.stack = 1
            self.setTargeted(False)

        def playSound(self):
            renpy.play("audio/characters/miha/sonic_ring.mp3")
            renpy.pause(1)

        def use(self, fight: Fight, character: Character):
            self.stack += 1
            self.name = "Настакать ходы (Текущее значение: х{})".format(self.stack)
            self.playSound()
            character.abilities = [ability for ability in character.abilities if not isinstance(ability, ReleaseTurns)]
            character.abilities.append(ReleaseTurns(self.stack))

    class DeadlyBlow(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Смертельный удар", strength = 70)
            self.setTargeted(False)

        def playDeadlyBlowSound(self):
            renpy.play("audio/characters/drei/deadly_blow.wav")
            renpy.pause(1)

        def playSetupSound(self):
            renpy.play("audio/characters/drei/setup_deadly_blow.wav")
            renpy.pause(1)

        def useAgainst(self, enemy: Character, character: Character):
            if character.preparedAttack > 0:
                if enemy.health > 50:
                    character.hitPureDamage(enemy, enemy.max_health - 10)
                else:
                    character.hitPureDamage(enemy, enemy.health)

                renpy.with_statement(bigdamagepunch)
                renpy.pause(.1)
                self.playDeadlyBlowSound()

                character.setInvincible(False)
                character.setPreparedAttack(0)
                self.setTargeted(False)
                return

            self.setup(character)

        def use(self, fight: Fight, character: Character):
            self.setup(character)

        def setup(self, character):
            character.setPreparedAttack(1)
            self.playSetupSound()
            character.setInvincible(True)
            self.setTargeted(True)
            renpy.say(None, 'Дрей ушел в инвиз')

        def getStateName(self, character: Character):
            if character.preparedAttack > 0:
                return ""
            else:
                return " (Подготовка)"

        def reset(self, character: Character):
            character.setInvincible(False)
            character.setPreparedAttack(0)
            self.setTargeted(False)

#         class (Ability, NonTarget):
#         def __init__(self):
#             super().__init__(name = "", strength = 70)
#             self.setTargeted(False)
#
#         def playDeadlyBlowSound(self):
#             renpy.play("audio/characters/drei/deadly_blow.wav")
#             renpy.pause(1)
#
#         def playSetupSound(self):
#             renpy.play("audio/characters/drei/setup_deadly_blow.wav")
#             renpy.pause(1)
#
#         def useAgainst(self, enemy: Character, character: Character):
#             if character.preparedAttack > 0:
#                 if enemy.health > 50:
#                     character.hit(enemy, enemy.max_health - 10)
#                 else:
#                     character.hit(enemy, enemy.health)
#
#                 renpy.with_statement(bigdamagepunch)
#                 renpy.pause(.1)
#                 self.playDeadlyBlowSound()
#
#                 character.setInvincible(False)
#                 character.setPreparedAttack(0)
#                 self.setTargeted(False)
#                 return
#
#             self.setup(character)
#
#         def use(self, enemyParty: Party, character: Character, myParty: Party):
#             self.setup(character)
#
#         def setup(self, character):
#             character.setPreparedAttack(1)
#             self.playSetupSound()
#             character.setInvincible(True)
#             self.setTargeted(True)
#             renpy.say(None, 'Дрей ушел в инвиз')
#
#         def getStateName(self, character: Character):
#             if character.preparedAttack > 0:
#                 return ""
#             else:
#                 return " (Подготовка)"
