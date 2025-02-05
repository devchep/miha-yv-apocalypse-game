init 1 python:
    class Fight:
        def __init__(self, party, enemyParty, saveName=None):
            self.party = party
            self.enemyParty = enemyParty
            self.saveName = saveName

        def isItemPick(self, pick):
            return pick == "Предмет"

        def fight_menu(self, options):
            executeTurn = True
            options.append(("Назад", "Назад"))
            picked = renpy.display_menu(options)
            if picked == "Назад":
                executeTurn = False
            return picked, executeTurn

        def pickEnemy(self):
            pickedEnemy = enemyParty.getAliveMembers()[0][1]
            if len(enemyParty.getAliveMembers()) > 1:
                pickedEnemy = renpy.display_menu(enemyParty.getAliveMembers())
            return pickedEnemy

        def castAbility(self, pickedMember):
            pickedAbility, executeTurn = self.fight_menu(pickedMember.getAvailableAbilities())
            if not executeTurn:
                return False

            if (pickedAbility.targeted):
                pickedEnemy = self.pickEnemy()
                pickedAbility.useAgainst(pickedEnemy, pickedMember)
            else:
                pickedAbility.use(self, pickedMember)
            return True

        def useItem(self):
            pickedItem, executeTurn = self.fight_menu(inventory.getFightItems())
            if not executeTurn:
                return False

            sidePick, executeTurn = self.fight_menu([("Применить на союзника", "союзник"), ("Применить против врага", "враг")])
            if not executeTurn:
                return False

            if sidePick == "союзник":
                pickedAlly, executeTurn = self.fight_menu(party.getAliveMembers())
                if not executeTurn:
                    return False
                pickedItem.useInFight(pickedAlly, self)
                inventory.useItem(pickedItem)
            else:
                pickedEnemy, executeTurn = self.fight_menu(enemyParty.getAliveMembers())
                if not executeTurn:
                    return False
                pickedItem.useAgainstEnemy(pickedEnemy)
                inventory.useItem(pickedItem)
            return True

        def enemyTurn(self):
            if len(enemyParty.getAliveMembers()) > 0:
                enemy = enemyParty.popNext()
                if enemy is not None:
                    enemy.attack(party)
                    enemyParty.putInAttackQueue(enemy)

        def makeTurn(self):
            turnExecuted = True
            pickedOption = renpy.display_menu([("Применить предмет", "Предмет")] + party.getMembersForNextAttack())

            if self.isItemPick(pickedOption):
                turnExecuted = self.useItem()
                self.makeTurnNoItems() if turnExecuted else _
            else:
                turnExecuted = self.castAbility(pickedOption)
            return turnExecuted

        def makeTurnNoItems(self):
            pickedOption = renpy.display_menu(party.getMembersForNextAttack())
            return self.castAbility(pickedOption)

        def turnEnd(self):
            [member.disabledTurnPassed() for member in party.members.values()]

        def wannaContinue(self):
            if party.isWiped():
                renpy.say(None, "Ваша пати разгромлена")
            elif party.mihaIsDead():
                renpy.say(None, "Миха вайпнулся в бою, ничего не имеет смысла больше")
            choice = renpy.display_menu([("Драться снова", "Драться снова"), ("Начать игру заново", "Заново")])
            if choice == "Драться снова":
                if self.saveName is not None:
                    renpy.load(self.saveName)
            else:
                MainMenu(confirm=False)()

        def isOver(self):
            return enemyParty.isWiped() or party.isWiped()

        def start(self):
            while not self.isOver():
                turnExecuted = False
                while not turnExecuted:
                    turnExecuted = self.makeTurn()
                self.turnEnd()
                renpy.pause(1)
                self.enemyTurn()

            if party.isWiped() or party.mihaIsDead():
                self.wannaContinue()
            party.resetEverything()