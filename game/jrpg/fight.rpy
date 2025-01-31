init 3 python:
    class Fight:
        def __init__(self, party, enemyParty, saveName=None):
            self.party = party
            self.enemyParty = enemyParty
            self.saveName = saveName

        def isItemPick(self, pickedMember):
            return pickedMember == "Предмет"

        def pickEnemy(self):
            pickedEnemy = enemyParty.getAliveMembers()[0][1]
            if len(enemyParty.getAliveMembers()) > 1:
                pickedEnemy = renpy.display_menu(enemyParty.getAliveMembers())
            return pickedEnemy

        def castAbility(self, pickedMember):
            pickedAbility = renpy.display_menu(pickedMember.getAvailableAbilities())
            if (pickedAbility.targeted):
                pickedEnemy = self.pickEnemy()
                pickedAbility.useAgainst(pickedEnemy, pickedMember)
            else:
                pickedAbility.use(enemyParty, pickedMember, self.party)

        def useItem(self):
            pickedItem = renpy.display_menu(inventory.getItems())
            side = renpy.display_menu([("Применить на союзника", "союзник"), ("Применить против врага", "враг")])
            if side == "союзник":
                pickedAlly = renpy.display_menu(party.getAliveMembers())
                pickedItem.useInFight(pickedAlly)
            else:
                pickedEnemy = renpy.display_menu(enemyParty.getAliveMembers())
                pickedItem.useAgainstEnemy(pickedEnemy)

        def enemyTurn(self):
            if len(enemyParty.getAliveMembers()) > 0:
                enemy = enemyParty.popNext()
                if enemy is not None:
                    enemy.attack(party)
                    enemyParty.putInAttackQueue(enemy)

        def makeTurn(self):
            pickedMember = renpy.display_menu(party.getMembersForNextAttack())
            if self.isItemPick(pickedMember):
                self.useItem()
            else:
                self.castAbility(pickedMember)

        def turnEnd(self):
            [member.disabledTurnPassed() for member in party.members.values()]

        def wannaContinue(self):
            if party.isWiped():
                renpy.say(None, "Ваша пати разгромлена")
            elif party.mihaIsDead():
                renpy.say(None, "Миха вайпнулся в бою, ничего не имеет смысла больше")
            choice = renpy.display_menu([("Продолжить", "Продолжить"), ("Начать игру заново", "Заново")])
            if choice == "Продолжить":
                if self.saveName is not None:
                    renpy.load(self.saveName)
            else:
                MainMenu(confirm=False)()

        def start(self):
            while not enemyParty.isWiped() and not party.isWiped():
                self.makeTurn()
                self.turnEnd()
                renpy.pause(1)
                self.enemyTurn()

            if party.isWiped() or party.mihaIsDead():
                self.wannaContinue()
            party.healEveryone()