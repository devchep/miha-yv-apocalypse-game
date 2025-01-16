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
                self.isOffended = True

        def insultingPhrase(self):
            return random.choice(["Тупой ты дебил"])

        def changeVulnerableRatio(self, ratio):
            renpy.say(None, "Враг стал уязвим")
            renpy.say(None, "Все атаки в "+str(ratio)+" раза сильнее")
            self.vulnerableRatio = ratio

        def hit(self, strength):
            self.health -= strength*self.vulnerableRatio

    class Ability:
        def __init__(self, name, strength):
            self.name = name
            self.strength = strength

        def useAgainst(self, character: Character):
            character.hit(self.strength)
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

        def addMember(self, ally: Ally):
            self.members.update({ally.name: ally})

        def isWiped(self):
            return all(member.health <= 0 for member in self.members.values())

        def getMembersForNextAttack(self):
            aliveMembers = []
            for member in iter(self.members.values()):
                if member.health > 0:
                    aliveMembers.append((member.partyName, member))

            return aliveMembers

    class Enemy(Character):
        def __init__(self, name, health, strength):
            super().__init__(name, health, strength)

        def getAttackPower(self):
            return self.strength

        def attack(self, party: Party):
            if len(party.members) > 0:
                partyMemberToAttack = min(party.members.values(),key=attrgetter('health'))
                partyMemberToAttack.health -= self.getAttackPower()
                renpy.play("audio/punch.opus")
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())

        def attack_phrase(self):
            return random.choice(["Пизда вам"])

        def getRenpyChar(self):
            return None

    class Tupoi:
        def mayBeOffended(self):
            return True

        def getAttackPower(self):
            return self.strength*2 if self.isOffended else self.strength

    class Zheka(Tupoi, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Учебный Крип", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["ууу суки", "на", "бью"])

        def insultingPhrase(self):
            return random.choice([
            "Я тебя буду называть Ев, потому что имя с 'гений' внутри тебе ну никак не подходит)",
            "Знаешь, никогда тебя за человека то и не считал"
            ])

        def getRenpyChar(self):
            return creep

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