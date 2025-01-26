screen campButton():
    vbox xalign 0.02 yalign 0.05:
        imagebutton:
            idle im.Scale("images/home_button.png", 78, 74)
            hover im.Scale("images/camp_button.png", 261, 100.02)
            action Function(renpy.call_in_new_context, label="camp_scene")

init 3 python:
    class Camp:
        def __init__(self, party: Party, inventory: Inventory):
            self.party = party
            self.inventory = inventory

        def isItemPick(self, pickedOption):
            return pickedOption == "Предмет"

        def isLeave(self, pickedOption):
            return pickedOption == "Выйти"

        def isUpgrade(self, pickedOption):
            return pickedOption == "Прокачка"

        def getCampOptions(self):
            campOptions = []
            if self.inventory.notEmpty():
                campOptions.append(("Применить предмет", "Предмет"))

            if self.party.experience > 0 and any(member.canUpgrade() for member in iter(self.party.members.values())):
                campOptions.append(("Прокачать братанчика: х{} очков опыта доступно".format(self.party.experience), "Прокачка"))

            campOptions.append(("Выйти из лагеря", "Выйти"))
            return campOptions

        def enter(self):
            pickedOption = renpy.display_menu(self.getCampOptions())
            if self.isItemPick(pickedOption):
                self.useItem()
            elif self.isLeave(pickedOption):
                return False
            elif self.isUpgrade(pickedOption):
                self.upgrade(party)
            return True

        def camp_menu(self, options):
            options.append(("Назад", "Назад"))
            picked = renpy.display_menu(options)
            if picked == "Назад":
                renpy.jump("camp_beginning")
            return picked

        def useItem(self):
            pickedItem = self.camp_menu(inventory.getItems())
            pickedAlly = self.camp_menu(party.getAliveMembers())
            pickedItem.useInFight(pickedAlly)

        def upgrade(self, party):
            pickedMember = self.camp_menu(party.getMembersWithUpgrades())
            skillBranch = self.camp_menu(pickedMember.getAvailableUpgrades())

            newAbility = skillBranch.getNextUpgrade()
            pickedMember.upgrade(newAbility)
            party.useExp(1)
            renpy.say(pickedMember.getRenpyChar(), what=newAbility.getUpgradePhrase())
