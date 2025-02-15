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
            self.showCharacter("smeshnoi_ti_dai_sfotkau")
            renpy.say(character.getRenpyChar(), enemy.insultingPhrase())
            self.hideCharacter("smeshnoi_ti_dai_sfotkau")
            enemy.offend()

        def playSound(self):
            renpy.play("audio/characters/miha/laugh.mp3")

    class Shoulder(Ability):
        def __init__(self):
            super().__init__(name = "Ебнуть трубой (-30)", strength = 30)

        def useAgainst(self, enemy: Character, character: Character):
            character.hit(enemy, self.strength)
            self.showCharacter("max_pipe")
            self.playSound()
            self.hideCharacter("max_pipe")

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.with_statement(hugepunch)
            renpy.pause(0.5)

    class AoeShoulder(Ability):
        def __init__(self):
            super().__init__(name = "Трактором с плеча прокатиться по всем (-30 выбранному, -15 всем противникам рядом)", strength = 30)
            self.setTargeted(False)

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.with_statement(hugepunch)
            renpy.with_statement(hugepunch)
            renpy.pause(1)

        def use(self, fight: Fight, character: Character):
            pickedEnemy = renpy.display_menu(fight.enemyParty.getAliveMembers())
            character.hit(pickedEnemy, 30)
            [character.hit(enemy, 15) for enemy in fight.enemyParty.members.values() if enemy != pickedEnemy]
            self.playSound()

    class Vampirism(Ability):
        def __init__(self):
            super().__init__(name = "Высадка вампиров (Дает вампиризм всем союзникам)", strength = 30)
            self.setTargeted(False)

        def use(self, fight: Fight, character: Character):
            renpy.sound.play("audio/characters/igoryas/vampire.mp3", loop = False)
            self.showCharacterWithSpeed("vampire", 1.5)
            renpy.show("vampirism")
            renpy.pause(.2)
            [member.addVampirism() for member in fight.party.members.values()]
            self.hideCharacterWithSpeed("vampire", 1.5)
            renpy.hide("vampirism")
            renpy.say(None, what="Все парни получили вампиризм")
            renpy.sound.stop()

    class CatHeal(Ability):
        def __init__(self):
            super().__init__(name = "Спасение котят (+20HP Всем союзникам) (Шанс на успех 50%) (Может сработать не больше 1 раза за бой)", strength = 30)
            self.setTargeted(False)

        def use(self, fight: Fight, character: Character):
            choice = random.choice([1, 2])
            if choice == 1:
                self.showCharacterWithSpeed("diman_kittens", 0.5)
                renpy.sound.play("audio/charactedrs/diman/diman_heal.mp3", loop = False)
                renpy.show("heal_screen")
                renpy.sound.play("audio/characters/drei/meow.mp3", loop = False)
                renpy.pause(.2)
                [member.healWithLimit(30) for member in fight.party.members.values()]
                renpy.hide("heal_screen")
                renpy.pause(.1)
                self.hideCharacterWithSpeed("diman_kittens", 1.2)
                renpy.sound.stop()
                self.setInactive()
            else:
                renpy.sound.play("audio/hell_no_man.mp3", loop = False)
                self.showCharacterWithSpeed("diman_nasral", 0.2)
                renpy.pause(3)
                self.hideCharacterWithSpeed("diman_nasral", 0.1)
                renpy.sound.stop()

    class DimanUlt(Ability):
        def __init__(self):
            super().__init__(name = "Ультануть (Урон по противникам -50, Урон по союзникам -15) (Противники обездвижены) (Доступно 1 раз за бой)", strength = 30)
            self.setTargeted(False)

        def use(self, fight: Fight, character: Character):
            renpy.sound.play("audio/characters/diman/diman_scream.mp3", loop = False)
            self.showCharacterWithSpeed("diman_scream", 0.1)
            renpy.pause(.2)
            renpy.with_statement(hugepunch)
            renpy.with_statement(hugepunch)
            renpy.with_statement(hugepunch)
            [member.dealDamage(15) for member in fight.party.members.values()]
            [enemy.dealDamage(50) for enemy in fight.enemyParty.members.values()]
            renpy.pause(.5)
            self.hideCharacterWithSpeed("diman_scream", 1.2)
            renpy.sound.stop()
            renpy.say(None, 'Противник ахуел')
            self.setInactive()
            fight.makeTurnNoItems()

    class MihaUlt(Ability):
        def __init__(self):
            super().__init__(name = "Нанести 15 урона (Каждый ход урон удваивается) (Доступно 1 раз за бой)", strength = 30)
            self.currentDamageStack = 15
            self.name = "Нанести {} урона (Каждый ход урон удваивается)".format(self.currentDamageStack)

        def useAgainst(self, enemy: Character, character: Character):
            renpy.sound.play("audio/characters/miha/miha_bell.mp3", loop = False)
            self.showCharacterWithSpeed("miha_god_fist", 0.1)
            renpy.with_statement(hugepunch)
            renpy.with_statement(hugepunch)
            character.hit(enemy, self.currentDamageStack)
            renpy.with_statement(hugepunch)
            renpy.with_statement(hugepunch)
            renpy.pause(.5)
            self.hideCharacterWithSpeed("miha_god_fist", 1.2)
            renpy.sound.stop()
            self.setInactive()

        def turnPassed(self):
            self.currentDamageStack *= 2
            self.name = "Нанести {} урона (Каждый ход урон удваивается)".format(self.currentDamageStack)

        def reset(self, character: Character):
            self.active = True
            self.targeted = True
            self.currentDamageStack = 15
            self.name = "Нанести {} урона (Каждый ход урон удваивается)".format(self.currentDamageStack)

    class Smoke(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Дымка 50 никотина (Ослабляет противников)", strength = 1)
            self.setTargeted(False)

        def useAgainst(self, enemy: Character, character: Character):
            self.playSound()
            enemy.changeVulnerableRatio(2)

        def use(self, fight: Fight, character: Character):
            self.playSound()
            self.showCharacter("igor_smoke")
            renpy.pause(1)
            [enemy.changeVulnerableRatio(2) for enemy in fight.enemyParty.members.values()]
            self.hideCharacter("igor_smoke")
            renpy.say(None, "Враги ахуели с этой прикормки")
            renpy.say(None, "Атаки против врагов стали в 2 раза сильнее")

        def playSound(self):
            renpy.play("audio/characters/igoryas/smoke.mp3")
            renpy.pause(1)

    class TheWall(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Встать стеной (+60HP, Провокация) (Доступно 1 раз за бой)", strength = 1)
            self.setTargeted(False)

        def use(self, fight: Fight, character: Character):
            fight.party.setTarget(character)
            character.health += 60
            self.showCharacter("thewall")
            self.playSound()
            renpy.say(character.getRenpyChar(), random.choice(["Че, уже не смешно?)", "Подвиньтесь", "Ну здарова"]))
            self.hideCharacter("thewall")
            self.setInactive()

        def playSound(self):
            renpy.play("audio/characters/igoryas/taunt.mp3")
            renpy.pause(0.2)

    class ReleaseTurns(Ability, NonTarget):
        def __init__(self, turns):
            super().__init__(name = "Совершить ходы х({})".format(turns), strength = 1)
            self.turns = turns
            self.setTargeted(False)

        def releasePhrase(self, character):
            if self.turns > 5:
                renpy.say(character.getRenpyChar(), "АХХАХААХАХАХ")
            elif self.turns > 3:
                renpy.say(character.getRenpyChar(), "Пиздец настакал вы ща ахуеете")
            else:
                renpy.say(character.getRenpyChar(), "Это пиздец ща будет")

        def endPhrase(self, character):
            if self.turns > 3:
                renpy.say(character.getRenpyChar(), "Стаки большого кончились")
            else:
                renpy.say(character.getRenpyChar(), "Стаки кончились")

        def use(self, fight: Fight, character: Character):
            self.playSound()
            self.showCharacter("theworldo")
            self.releasePhrase(character)
            self.hideCharacter("theworldo")
            character.abilities = [ability for ability in character.abilities if not isinstance(ability, ReleaseTurns) and not isinstance(ability, StackTurns)]
            for i in range(self.turns):
                turnExecuted = True
                if not fight.isOver():
                    turnExecuted = False
                    while not turnExecuted:
                        turnExecuted = fight.makeTurnNoItems()
            character.abilities.append(StackTurns())
            self.endPhrase(character)

        def playSound(self):
            renpy.play("audio/characters/miha/theworldo.mp3")

    class StackTurns(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Настакать ходы (Текущее значение: х1)", strength = 1)
            self.stack = 1
            self.setTargeted(False)

        def playSound(self):
            renpy.play("audio/characters/miha/sonic_ring.mp3")
            self.showCharacterWithSpeed("miha_stackaet", 0.3)
            renpy.pause(.2)
            self.hideCharacterWithSpeed("miha_stackaet", 0.3)
            renpy.say(None, "Вы настакали ходы: х({})".format(self.stack))

        def use(self, fight: Fight, character: Character):
            self.stack += 1
            self.name = "Настакать ходы (Текущее значение: х{})".format(self.stack)
            self.playSound()
            character.abilities = [ability for ability in character.abilities if not isinstance(ability, ReleaseTurns)]
            character.abilities.append(ReleaseTurns(self.stack))

        def reset(self, character: Character):
            self.stack = 1
            self.name = "Настакать ходы (Текущее значение: х{})".format(self.stack)
            character.abilities = [ability for ability in character.abilities if not isinstance(ability, ReleaseTurns)]

    class DeadlyBlow(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Смертельный удар", strength = 70)
            self.setTargeted(False)

        def playDeadlyBlowSound(self):
            renpy.play("audio/characters/drei/deadly_blow.wav")

        def playSetupSound(self):
            renpy.play("audio/characters/drei/setup_deadly_blow.wav")
            renpy.pause(0.2)

        def useAgainst(self, enemy: Character, character: Character):
            if character.preparedAttack > 0:
                if enemy.health > 50:
                    character.hitPureDamage(enemy, enemy.max_health - 10)
                else:
                    character.hitPureDamage(enemy, enemy.health)

                renpy.with_statement(bigdamagepunch)
                self.showCharacterWithSpeed("drei-deadly-blow", 0.1)
                self.playDeadlyBlowSound()
                self.hideCharacterWithSpeed("drei-deadly-blow", 0.1)

                character.setInvincible(False)
                character.setPreparedAttack(0)
                self.setTargeted(False)
                renpy.pause(0.2)
                return

            self.setup(character)

        def use(self, fight: Fight, character: Character):
            self.setup(character)

        def setup(self, character):
            character.setPreparedAttack(1)
            self.playSetupSound()
            character.setInvincible(True)
            self.setTargeted(True)
            self.showCharacter("drei-invise")
            renpy.say(None, 'Дрей ушел в инвиз')
            self.hideCharacter("drei-invise")

        def getStateName(self, character: Character):
            if character.preparedAttack > 0:
                return ""
            else:
                return " (Подготовка)"

        def reset(self, character: Character):
            self.active = True
            character.setInvincible(False)
            character.setPreparedAttack(0)
            self.setTargeted(False)

    class DeadlyBlow(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Смертельный удар", strength = 70)
            self.setTargeted(False)

        def playDeadlyBlowSound(self):
            renpy.play("audio/characters/drei/deadly_blow.wav")

        def playSetupSound(self):
            renpy.play("audio/characters/drei/setup_deadly_blow.wav")
            renpy.pause(0.2)

        def useAgainst(self, enemy: Character, character: Character):
            if character.preparedAttack > 0:
                if enemy.health > 50:
                    character.hitPureDamage(enemy, enemy.max_health - 10)
                else:
                    character.hitPureDamage(enemy, enemy.health)

                renpy.with_statement(bigdamagepunch)
                self.showCharacterWithSpeed("drei-deadly-blow", 0.1)
                self.playDeadlyBlowSound()
                self.hideCharacterWithSpeed("drei-deadly-blow", 0.1)

                character.setInvincible(False)
                character.setPreparedAttack(0)
                self.setTargeted(False)
                renpy.pause(0.2)
                return

            self.setup(character)

        def use(self, fight: Fight, character: Character):
            self.setup(character)

        def setup(self, character):
            character.setPreparedAttack(1)
            self.playSetupSound()
            character.setInvincible(True)
            self.setTargeted(True)
            self.showCharacter("drei-invise")
            renpy.say(None, 'Дрей ушел в инвиз')
            self.hideCharacter("drei-invise")

        def getStateName(self, character: Character):
            if character.preparedAttack > 0:
                return ""
            else:
                return " (Подготовка)"

        def reset(self, character: Character):
            self.active = True
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
