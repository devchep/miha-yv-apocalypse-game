image drones_attack = Movie(play = "./video/drones_attack.webm", loop=False)
init 1 python:
    hugepunch = Move((15, 0), (-15, 0), .10, bounce=True, repeat=True, delay=.275)
    hugeboom = Move((100, 0), (-100, 0), .10, bounce=True, repeat=True, delay=.275)
    bigdamagepunch = Move((15, 0), (0, 15), .10, bounce=True, repeat=True, delay=0)
    import random
    from operator import attrgetter
    class Character:
        def __init__(self, name, health, strength):
            self.name = name
            self.health = health
            self.max_health = health
            self.strength = strength
            self.isOffended = False
            self.vulnerableRatio = 1
            self.invincible = False
            self.preparedAttack = 0
            self.disabled_turns_count = 0

        def mayBeOffended(self):
            return False

        def offend(self):
            if self.mayBeOffended():
                renpy.say(None, "Враг оскорбился")
                self.offendEffectAnnounce()
                self.isOffended = True
            else:
                renpy.say(None, "Враг не оскорбился")
                self.offendEffectAnnounce()

        def insultingPhrase(self):
            return random.choice(["Тупой ты дебил"])

        def offendEffectAnnounce(self):
            pass

        def changeVulnerableRatio(self, ratio):
            self.vulnerableRatio = ratio

        def hit(self, enemy, strength):
            if self.disabled_turns_count > 0:
                renpy.say(None, "Атака не нанесла урона")
                return
            enemy.health -= strength*enemy.vulnerableRatio

        def healMax(self):
            self.health = self.max_health

        def heal(self, hp):
            self.health += hp

        def setInvincible(self, val):
            self.invincible = val

        def setPreparedAttack(self, val):
            self.preparedAttack = val

        def disabled(self, turns):
            self.disabled_turns_count = turns

        def disabledTurnPassed(self):
            if self.disabled_turns_count > 0:
                self.disabled_turns_count -= 1

        def getRenpyChar(self):
            return None

        def react(self, item: Item):
            pass

    class Ability:
        def __init__(self, name, strength):
            self.name = name
            self.strength = strength
            self.targeted = True

        def useAgainst(self, enemy: Character, character: Character):
            character.hit(enemy, self.strength)
            self.playSound()

        def playSound(self):
            renpy.play("audio/punch.opus")

        def getStateName(self, character: Character):
            return ""

        def setTargeted(self, val):
            self.targeted = val

        def getUpgradePhrase(self):
            return "Охх я чувствую силу"

    class SkillBranch:
        def __init__(self, name, abilities):
            self.name = name
            self.abilities = abilities
            self.lvl = 1

        def hasUpgrades(self):
            return len(self.abilities) > 0

        def getNextUpgrade(self):
            self.lvl += 1
            return self.abilities.pop(0)

        def getName(self):
            return self.name + " (lvl {})".format(self.lvl)

    class Ally(Character):
        def __init__(self, name, health, strength, partyName):
            super().__init__(name, health, strength)
            self.partyName = partyName
            self.level = 0
            self.abilities = []
            self.skillBranches = []

        def getAbilities(self):
            return self.abilities

        def getAvailableAbilities(self):
            return [(ability.name + ability.getStateName(self), ability) for ability in self.getAbilities()]

        def hasDialog(self, act):
            return False

        def lvlup(self):
            self.level += 1

        def getAvailableUpgrades(self):
            return [(skillBranch.getName(), skillBranch) for skillBranch in self.skillBranches]

        def canUpgrade(self):
            return any(skillBranch.hasUpgrades() for skillBranch in self.skillBranches)

        def upgrade(self, ability: Ability):
            self.lvlup()
            self.abilities.append(ability)

    class Party:
        def __init__(self):
            self.members = {}
            self.attackQueue = []
            self.experience = 0

        def addMember(self, ally: Character):
            self.members.update({ally.name: ally})
            self.attackQueue.append(ally)

        def getExp(self, exp):
            self.experience += exp

        def isWiped(self):
            return all(member.health <= 0 for member in self.members.values())

        def getMembersForNextAttack(self):
            aliveMembers = []
            aliveMembers.append(("Применить предмет", "Предмет"))
            for member in iter(self.members.values()):
                if member.health > 0:
                    aliveMembers.append((member.partyName, member))

            return aliveMembers

        def getMembersWithUpgrades(self):
            upgradeCandidates = []
            for member in iter(self.members.values()):
                if member.canUpgrade():
                    upgradeCandidates.append((member.name, member))

            return upgradeCandidates

        def getAliveMembers(self):
            aliveMembers = []
            for member in iter(self.members.values()):
                if member.health > 0:
                    aliveMembers.append((member.name, member))

            return aliveMembers

        def healEveryone(self):
            [member.healMax() for member in self.members.values()]

        def contains(self, instance):
            return any(isinstance(member, instance) for member in self.members.values())

        def containsAlive(self, instance):
            return any(isinstance(member[1], instance) for member in self.getAliveMembers())

        def popNext(self):
            while len(self.attackQueue) > 0:
                nextAttackMember = self.attackQueue.pop(0)
                if nextAttackMember.health > 0:
                    return nextAttackMember
            return None

        def putInAttackQueue(self, member: Character):
            if member.health > 0:
                return self.attackQueue.append(member)

        def hasExp(self):
            return self.experience > 0

        def useExp(self, amount):
            self.experience -= amount

        def mihaIsDead(self):
            return not self.containsAlive(Miha)

    class NonTarget:
        def __init__(self):
            pass

        def use(self, party: Party, character: Character):
            pass

        def playSound(self):
            renpy.play("audio/punch.opus")

    class Enemy(Character):
        def __init__(self, name, health, strength, partyName=None):
            super().__init__(name, health, strength)
            self.partyName = partyName

        def getAttackPower(self):
            return self.strength

        def attack(self, party: Party):
            if len(party.members) > 0:
                partyMemberToAttack = min(filter(lambda x: x.health > 0, party.members.values()),key=attrgetter('health'))
                partyMemberToAttack.health -= self.getAttackPower()
                renpy.with_statement(vpunch)
                self.playAttackSound()
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())

        def attack_phrase(self):
            return random.choice(["Пизда вам"])

        def playAttackSound(self):
            renpy.play("audio/punch.opus")

        def react(self, item: Item):
            renpy.say(None, "Враг никак не отреагировал")

    class Tupoi:
        def mayBeOffended(self):
            return True

        def getAttackPower(self):
            return self.strength*2 if self.isOffended else self.strength

        def offendEffectAnnounce(self):
            renpy.say(None, "Атаки врага стали в 2 раза сильнее")

    class Zheka(Tupoi, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Учебный Крип", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["ууу суки", "на", "бью"])

        def insultingPhrase(self):
            return random.choice([
            "Я тебя буду называть Ев, потому что имя с содержанием 'гений' внутри тебе ну никак не подходит)",
            "Знаешь, никогда тебя за человека то и не считал"
            ])

        def getRenpyChar(self):
            return creep

    class Tigr(Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Тигр", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["rawr", "raaawr", "raaaawr"])

        def insultingPhrase(self):
            return random.choice([
                "Кис-кис-кис дурачок",
                "Кыш епта отсюдова",
            ])

        def getRenpyChar(self):
            return tigr

        def playAttackSound(self):
            renpy.play("audio/characters/drei/rawr.mp3")

        def cat_sound(self):
            renpy.play("audio/characters/drei/meow.mp3")

        def cat_attack_phrase(self):
            return random.choice(["Meow", "Meoow", "Meeeoow"])

        def react(self, item: Item):
            if isinstance(item, CatLikes):
                self.strength -= item.getPower()
                item.consume(1)
                if self.strength > 15:
                    renpy.say(None, what="Врагу очень понравилась прикормка")
                    renpy.say(None, what="Атаки врага стали слабее")
                else:
                    self.playAttackSound = self.cat_sound
                    self.attack_phrase = self.cat_attack_phrase
                    self.cat_sound()
                    renpy.say(self.getRenpyChar(), what="Meow")
                    renpy.say(None, what="Враг стал ласковый")
                    self.strength = 0

    class Tiktoker:
        def mayBeOffended(self):
            return True

        def getAttackPower(self):
            return self.strength*self.getAttackResult() if self.isOffended else self.strength

        def getAttackResult(self):
            return random.choice([1, 0])

        def offendEffectAnnounce(self):
            renpy.say(None, 'Враг временно имеет шанс промахнуться с вероятностью 50%%')

    class Torop(Tiktoker, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Тороп", health = health, strength = strength)
            self.drones_appearance = 0

        def attack_phrase(self):
            return random.choice(["я вам покажу", "я вам обязательно покажу", "вы у меня посмотрите"])

        def insultingPhrase(self):
            return random.choice([
            "Твои тиктоки на таком дне, опуститься чуть ниже и просто уже дерьмом сдавит как батискаф",
            "Че ты там мячиком)",
            "Что ты там покажешь епта, мать в канаве?"
            ])

        def attack(self, party: Party):
            if self.health <= self.max_health / 2:
                renpy.say(self.getRenpyChar(), what="Пизда Вам)")
                if self.drones_appearance == 0:
                    renpy.show("drones_attack", at_list=[right])
                    renpy.say(self.getRenpyChar(), what="Готовьтесь детки")
                    renpy.hide("drones_attack")
                    renpy.play("audio/bigbruh.mp3")
                    renpy.say(None, what="Все кринжанули и не смогут нанести урон в следующем ходу")
                    [member.disabled(1) for member in party.members.values()]
                    self.drones_appearance += 1

                [self.hit(member, 34) for member in party.members.values()]
                renpy.play("audio/bigboom.mp3")
                renpy.show("lancet")
                renpy.with_statement(Dissolve(.2))
                renpy.with_statement(hugeboom)
                renpy.hide("lancet")
                return

            if len(party.members) > 0:
                renpy.show("ball_weapon")
                renpy.with_statement(Dissolve(.1))
                renpy.with_statement(vpunch)
                renpy.hide("ball_weapon")
                partyMemberToAttack = min(filter(lambda x: x.health > 0, party.members.values()),key=attrgetter('health'))
                partyMemberToAttack.health -= self.getAttackPower()
                self.playAttackSound()
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())

        def getRenpyChar(self):
            return torop

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Chinese:
        def mayBeOffended(self):
            return False

        def getAttackPower(self):
            return self.strength

        def insultingPhrase(self):
            return random.choice([
                "Ваш вождь жестко слабый",
                "Тупой ты китаец, слышишь меня?"
            ])

        def offendEffectAnnounce(self):
            renpy.say(None, 'Враг нихуя не понял')

    class Knee(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Knee", health = health, strength = strength, partyName = "Knee")

        def attack_phrase(self):
            return random.choice(["tekkeno panch", "feng wey atak"])

        def getRenpyChar(self):
            return knee

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Law(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Law", health = health, strength = strength, partyName = "Law")

        def attack_phrase(self):
            return random.choice(["huuuuuuuyaaaaa", "ai", "kiyaaaa"])

        def getRenpyChar(self):
            return law

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class First(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "FrontMan", health = health, strength = strength, partyName = "001")

        def attack_phrase(self):
            return random.choice([
                "Wanna play a hero?",
                 "I will show you the truth"
             ])

        def getRenpyChar(self):
            return first

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class ChineseLesh(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Лещ Dage", health = health, strength = strength, partyName = "Лещ Dage")

        def attack_phrase(self):
            return random.choice([
                "AHAHAHAHAHAH",
                 "ahahahahahhahahaahhaahh"
             ])

        def getRenpyChar(self):
            return chineseLesh

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Insult(Ability):
        def __init__(self):
            super().__init__(name = "Прокричать оскорбления", strength = 0)

        def useAgainst(self, enemy: Character, character: Character):
            self.playSound()
            renpy.say(None, enemy.insultingPhrase())
            enemy.offend()

        def playSound(self):
            renpy.play("audio/characters/miha/laugh.mp3")

    class Shoulder(Ability):
        def __init__(self):
            super().__init__(name = "Влететь с плеча в лоха", strength = 30)

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.with_statement(hugepunch)
            renpy.pause(1)

    class AoeShoulder(Ability):
        def __init__(self):
            super().__init__(name = "Трактором с плеча прокатиться по всем", strength = 30)
            self.setTargeted(False)

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.with_statement(hugepunch)
            renpy.pause(1)

        def use(self, party: Party, character: Character):
            self.playSound()
            [character.hit(enemy, self.strength) for enemy in party.members.values()]

    class Smoke(Ability, NonTarget):
        def __init__(self):
            super().__init__(name = "Дымка 50 никотина", strength = 1)
            self.setTargeted(False)

        def useAgainst(self, enemy: Character, character: Character):
            self.playSound()
            enemy.changeVulnerableRatio(2)

        def use(self, party: Party, character: Character):
            self.playSound()
            [enemy.changeVulnerableRatio(2) for enemy in party.members.values()]
            renpy.say(None, "Враги ахуели с этой прикормки")
            renpy.say(None, "Атаки против врагов стали в 2 раза сильнее")

        def playSound(self):
            renpy.play("audio/characters/igoryas/smoke.mp3")
            renpy.pause(4)


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
                    character.hit(enemy, enemy.max_health - 10)
                else:
                    character.hit(enemy, enemy.health)

                renpy.with_statement(bigdamagepunch)
                renpy.pause(.1)
                self.playDeadlyBlowSound()

                character.setInvincible(False)
                character.setPreparedAttack(0)
                self.setTargeted(False)
                return

            self.setup(character)

        def use(self, party: Party, character: Character):
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

    class Miha(Ally):
        def __init__(self, health, strength):
            super().__init__("Миха", health, strength, "ход Михой")

        def getAbilities(self):
            return [Insult()]

        def getRenpyChar(self):
            return miha

    class MaxHeyman(Ally):
        def __init__(self, health, strength):
            super().__init__("Макс", health, strength, "ход Максом")
            self.abilities = [Shoulder()]
            self.skillBranches = [SkillBranch("Максон машина ппц", [AoeShoulder()])]

        def getRenpyChar(self):
            return maks

    class Igoryas(Ally):
        def __init__(self, health, strength):
            super().__init__("Игоряс", health, strength, "ход Игорясом")

        def getAbilities(self):
            return [Smoke()]

        def getRenpyChar(self):
            return igoryas


    class Drei(Ally):
        def __init__(self, health, strength):
            super().__init__("Дрюс", health, strength, "ход Дрюсом")
            self.abilities = [DeadlyBlow()]

        def getAbilities(self):
            return self.abilities

        def getRenpyChar(self):
            return andrei