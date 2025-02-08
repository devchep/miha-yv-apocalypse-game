image drones_attack = Movie(play = "./video/drones_attack.webm", loop=False)
init 0 python:
    hugeboom = Move((100, 0), (-100, 0), .10, bounce=True, repeat=True, delay=.275)
    import random
    from operator import attrgetter

    class Item:
        def __init__(self, name, count, power, id):
            self.name = name
            self.count = count
            self.id = id
            self.power = power

        def getFullName(self):
            return "{} x({})".format(self.name, self.count)

        def getPower(self):
            return self.power

        def consume(self, count):
            self.count -= count

        def effectDesc(self):
            return ""

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
            self.vampirism = False

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
            if self.vampirism:
                self.health += strength*enemy.vulnerableRatio

        def hitPureDamage(self, enemy, strength):
            if self.disabled_turns_count > 0:
                renpy.say(None, "Атака не нанесла урона")
                return
            enemy.health -= strength
            if self.vampirism:
                self.health += strength

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

        def addVampirism(self):
            self.vampirism = True

        def react(self, item: Item):
            pass

    class Ability:
        def __init__(self, name, strength):
            self.name = name
            self.strength = strength
            self.targeted = True
            self.active = True

        def useAgainst(self, enemy: Character, character: Character):
            character.hit(enemy, self.strength)
            self.playSound()

        def playSound(self):
            renpy.play("audio/punch.opus")

        def getStateName(self, character: Character):
            return ""

        def setTargeted(self, val):
            self.targeted = val

        def setInactive(self):
            self.active = False

        def getUpgradePhrase(self):
            return "Охх я чувствую силу"

        def reset(self, character: Character):
            self.active = True

        def showCharacter(self, image):
            renpy.show(image, at_list=[left])
            renpy.with_statement(moveinleft)

        def hideCharacter(self, image):
            renpy.hide(image)
            renpy.with_statement(moveoutleft)

        def showCharacterWithSpeed(self, image, timing):
            renpy.show(image, at_list=[left])
            moveinleftcustom = MoveTransition(timing, enter=offscreenleft, enter_time_warp=_warper.easein)
            renpy.with_statement(moveinleftcustom)

        def hideCharacterWithSpeed(self, image, timing):
            renpy.hide(image)
            moveoutleftcustom = MoveTransition(timing, leave=offscreenleft, leave_time_warp=_warper.easeout)
            renpy.with_statement(moveoutleftcustom)

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

        def getNextUpgradePreview(self):
            return [(self.abilities[0].name, "")]

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
            return [(ability.name + ability.getStateName(self), ability) for ability in self.getAbilities() if ability.active]

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

        def resetAbilities(self):
            [ability.reset(self) for ability in self.getAbilities()]

    class Party:
        def __init__(self):
            self.members = {}
            self.attackQueue = []
            self.experience = 0
            self.target = None

        def addMember(self, ally: Character):
            self.members.update({ally.name: ally})
            self.attackQueue.append(ally)

        def deleteMember(self, ally: Character):
            self.members.pop(ally.name)

        def getExp(self, exp):
            self.experience += exp

        def isWiped(self):
            return all(member.health <= 0 for member in self.members.values())

        def getMembersForNextAttack(self):
            aliveMembers = []
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

        def resetHp(self):
            [member.healMax() for member in self.members.values()]

        def resetAbilities(self):
            [member.resetAbilities() for member in self.members.values()]

        def resetCharacters(self):
            for member in self.members.values():
                member.isOffended = False
                member.vulnerableRatio = 1
                member.invincible = False
                member.preparedAttack = 0
                member.disabled_turns_count = 0
                member.vampirism = False

        def resetEverything(self):
            self.resetAbilities()
            self.resetHp()
            self.target = None

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

        def setTarget(self, character: Character):
            self.target = character

        def getCharacterWithMinHp(self):
            return min(filter(lambda x: x.health > 0, self.members.values()),key=attrgetter('health'))

        def getTargetToAttack(self):
            if self.target is not None and self.target.health > 0:
                return self.target

            return self.getCharacterWithMinHp()

    class Enemy(Character):
        def __init__(self, name, health, strength, partyName=None):
            super().__init__(name, health, strength)
            self.partyName = partyName

        def getAttackPower(self):
            return self.strength

        def attack(self, party: Party):
            if len(party.members) > 0:
                partyMemberToAttack = party.getTargetToAttack()
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

        def showCharacter(self, image):
            renpy.show(image, at_list=[right])
            renpy.with_statement(moveinright)

        def hideCharacter(self, image):
            renpy.hide(image)
            renpy.with_statement(moveoutright)
