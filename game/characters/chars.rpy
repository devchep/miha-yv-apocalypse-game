init 1 python:
    import random
    from operator import attrgetter
    class Character:
        def __init__(self, name, health, strength):
            self.name = name
            self.health = health
            self.strength = strength

    class Ally(Character):
        def __init__(self, name, health, strength):
            self.name = name
            self.health = health
            self.strength = strength

        def attack(self, character: Character):
            character.health -= self.strength

    class Party:
        def __init__(self):
            self.members = {}

        def addMember(self, ally: Ally):
            self.members.update({ally.name: ally})

        def isWiped(self):
            return all(member.health <= 0 for member in self.members.values())

        def getMembersForNextAttack(self):
            return [(member.name, member) for member in iter(self.members.values())]

    class Enemy(Character):
        def __init__(self, name, health, strength):
            self.name = name
            self.health = health
            self.max_health = health
            self.strength = strength

        def attack(self, party: Party):
            if len(party.members) > 0:
                partyMemberToAttack = min(party.members.values(),key=attrgetter('health'))
                partyMemberToAttack.health -= self.strength

        def attack_phrase(self):
            return random.choice(["Пизда вам"])

    class Zheka(Enemy):
        def __init__(self, health, strength):
            self.name = "Учебный Крип"
            self.health = health
            self.max_health = health
            self.strength = strength

        def attack_phrase(self):
            return random.choice(["ууу суки", "на", "бью"])

    class Miha(Ally):
        def __init__(self, health, strength):
            self.name = "Миха"
            self.health = health
            self.strength = strength

    class Max(Ally):
        def __init__(self, health, strength):
            self.name = "Макс"
            self.health = health
            self.strength = strength

    class Igoryas(Ally):
        def __init__(self, health, strength):
            self.name = "Игоряс"
            self.health = health
            self.strength = strength