init 3 python:
    class Fight:
        def __init__(self, party, enemyParty):
            self.party = party
            self.enemyParty = enemyParty

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
                pickedAbility.use(enemyParty, pickedMember)

        def useItem(self):
            pickedItem = renpy.display_menu(inventory.getItems())
            side = renpy.display_menu([("Применить на союзника", "союзник"), ("Применить против врага", "враг")])
            if side == "союзник":
                pickedAlly = renpy.display_menu(party.getAliveMembers())
                pickedItem.useInFight(pickedAlly)
            else:
                pickedEnemy = renpy.display_menu(enemyParty.getAliveMembers())
                pickedItem.useInFight(pickedEnemy)

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

        def start(self):
            while not enemyParty.isWiped() and not party.isWiped():
                self.makeTurn()
                self.turnEnd()
                renpy.pause(1)
                self.enemyTurn()
