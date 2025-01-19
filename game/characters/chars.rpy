init 1 python:
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
            renpy.say(None, "Враг стал уязвим")
            renpy.say(None, "Все атаки против Врага стали в "+str(ratio)+" раза сильнее")
            self.vulnerableRatio = ratio

        def hit(self, strength):
            self.health -= strength*self.vulnerableRatio

        def healMax(self):
            self.health = self.max_health

    class Ability:
        def __init__(self, name, strength):
            self.name = name
            self.strength = strength

        def useAgainst(self, enemy: Character, character: Character = None):
            enemy.hit(self.strength)
            self.playSound()

        def playSound(self):
            renpy.play("audio/punch.opus")


    class Ally(Character):
        def __init__(self, name, health, strength, partyName):
            super().__init__(name, health, strength)
            self.partyName = partyName

        def getAvailableAbilities(self):
            return [(ability.name, ability) for ability in self.getAbilities()]

        def getAbilities(self):
            return []

    class Party:
        def __init__(self):
            self.members = {}
            self.attackQueue = []

        def addMember(self, ally: Character):
            self.members.update({ally.name: ally})
            self.attackQueue.append(ally)

        def isWiped(self):
            return all(member.health <= 0 for member in self.members.values())

        def getMembersForNextAttack(self):
            aliveMembers = []
            for member in iter(self.members.values()):
                if member.health > 0:
                    aliveMembers.append((member.partyName, member))

            return aliveMembers

        def healEveryone(self):
            [member.healMax() for member in self.members.values()]

        def contains(self, instance):
            return any(isinstance(member, instance) for member in self.members.values())

        def popNext(self):
            while len(self.attackQueue) > 0:
                nextAttackMember = self.attackQueue.pop(0)
                if nextAttackMember.health > 0:
                    return nextAttackMember
            return None

        def putInAttackQueue(self, member: Character):
            if member.health > 0:
                return self.attackQueue.append(member)

    class Enemy(Character):
        def __init__(self, name, health, strength, partyName=None):
            super().__init__(name, health, strength)
            self.partyName = partyName

        def getAttackPower(self):
            return self.strength

        def attack(self, party: Party):
            if len(party.members) > 0:
                partyMemberToAttack = min(party.members.values(),key=attrgetter('health'))
                partyMemberToAttack.health -= self.getAttackPower()
                self.playAttackSound()
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())

        def attack_phrase(self):
            return random.choice(["Пизда вам"])

        def getRenpyChar(self):
            return None

        def playAttackSound(self):
            renpy.play("audio/punch.opus")

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

        def attack_phrase(self):
            return random.choice(["я вам покажу", "я вам обязательно покажу", "вы у меня посмотрите"])

        def insultingPhrase(self):
            return random.choice([
            "Твои тиктоки на таком дне, опуститься чуть ниже и просто уже дерьмом сдавит как батискаф",
            "Че ты там мячиком)",
            "Что ты там покажешь епта, мать в канаве?"
            ])

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
            super().__init__(name = "001", health = health, strength = strength, partyName = "001")

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
            super().__init__(name = "ChineseLesh", health = health, strength = strength, partyName = "ChineseLesh")

        def attack_phrase(self):
            return random.choice([
                "AHAHAH",
                 "ahahahahahhahahaahhaahh"
             ])

        def getRenpyChar(self):
            return chineseLesh

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Insult(Ability):
        def __init__(self):
            super().__init__(name = "Прокричать оскорбления", strength = 0)

        def useAgainst(self, character: Character):
            self.playSound()
            renpy.say(None, character.insultingPhrase())
            character.offend()

        def playSound(self):
            renpy.play("audio/characters/miha/laugh.mp3")

    class Shoulder(Ability):
        def __init__(self):
            super().__init__(name = "Трактором влететь с плеча", strength = 30)

        def playSound(self):
            renpy.play("audio/characters/max/shoulder.mp3")
            renpy.pause(1)

    class Smoke(Ability):
        def __init__(self):
            super().__init__(name = "Дымка 50 никотина", strength = 1)

        def useAgainst(self, character: Character):
            self.playSound()
            character.changeVulnerableRatio(2)

        def playSound(self):
            renpy.play("audio/characters/igoryas/smoke.mp3")
            renpy.pause(4)

    class Critical(Ability):
        def __init__(self):
            super().__init__(name = "Крит", strength = 70)

        def playSound(self):
            renpy.play("audio/characters/drei/critical.mp3")
            renpy.pause(1)

        def useAgainst(self, enemy: Character, character: Character):
            phase = "ez"
            if enemy.health > 50:
                enemy.health -= enemy.max_health - 10
                phase = "Бля, неваншот"
            else:
                enemy.health -= enemy.health

            self.playSound()
            renpy.say(character.getRenpyChar(), what=phase)

    class Miha(Ally):
        def __init__(self, health, strength):
            super().__init__("Миха", health, strength, "ход Михой")

        def getAbilities(self):
            return [Insult()]

    class MaxHeyman(Ally):
        def __init__(self, health, strength):
            super().__init__("Макс", health, strength, "ход Максом")

        def getAbilities(self):
            return [Shoulder()]

    class Igoryas(Ally):
        def __init__(self, health, strength):
            super().__init__("Игоряс", health, strength, "ход Игорясом")

        def getAbilities(self):
            return [Smoke()]

    class Drei(Ally):
        def __init__(self, health, strength):
            super().__init__("Дрюс", health, strength, "ход Дрюсом")

        def getAbilities(self):
            return [Critical()]

        def getRenpyChar(self):
            return andrei