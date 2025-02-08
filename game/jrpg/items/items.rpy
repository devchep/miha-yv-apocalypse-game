init 2 python:
    # interfaces
    class DogLikes(Item):
        pass

    class CatLikes(Item):
        pass

    class CampItem(Item):
        pass

    class LeshCounter(Item):
        pass

    class FightItem(Item):
        def useInFight(self, character: Ally, fight: Fight):
            pass

        def useAgainstEnemy(self, enemy: Character):
            enemy.react(self)

    class Throwable(Item):
        pass

    class Inventory:
        def __init__(self):
            self.items = dict()

        def loot(self, item: Item):
            self.items.update({item.id: item})
            renpy.say(None, what="Вы получили предмет: "+item.getFullName())

        def useItem(self, item: Item):
            item.count -= 1
            if item.count <= 0:
                self.items.pop(item.id)
                return
            return self.items.update({item.id: item})

        def getItems(self):
            return [(self.menuName(item), item) for item in iter(self.items.values())]

        def getFightItems(self):
            fightItems = []
            for item in iter(self.items.values()):
                if isinstance(item, FightItem):
                    fightItems.append(("{} {}".format(self.menuName(item), item.effectDesc()), item))
            return fightItems

        def getCampItems(self):
            campItems = []
            for item in iter(self.items.values()):
                if isinstance(item, CampItem):
                    campItems.append(("{} {}".format(self.menuName(item), item.effectDesc()), item))
            return campItems

        def menuName(self, item: Item):
            return item.name + "(x"+str(item.count)+")" if item.count > 0 else ""

        def hasThrowables(self):
            throwables = False
            for item in iter(self.items.values()):
                if isinstance(item, Throwable):
                    throwables = True

            return throwables

        def hasDubki(self):
            for i in self.items.values():
                if isinstance(i, KolbasaDubki):
                    return True
            return False

        def getThrowables(self):
            throwables = []
            for item in iter(self.items.values()):
                if isinstance(item, Throwable):
                    throwables.append((self.menuName(item), item))

            return throwables

        def notEmpty(self):
            return any(item.count > 0 for item in self.items.values())

        def choice(self, count, items):
            if count > 1:
                renpy.say(None, what="Выберите предметы в количестве: "+str(count))
            else:
                renpy.say(None, what="Выберите предмет")
            for i in range(count):
                pickedItem = renpy.display_menu([(self.menuName(item), item) for item in items])
                self.loot(pickedItem)
                items = [item for item in items if item != pickedItem]

        def chooseReward(self, items):
            renpy.say(None, what="Вы получили награду")
            if len(items) > 1:
                renpy.say(None, what="Выберете предмет x({})".format(len(items)))
            pickedItem = renpy.display_menu([(self.menuName(item), item) for item in items])
            self.loot(pickedItem)

    class Sosiska(Throwable, DogLikes, CatLikes, FightItem):
        def __init__(self, id):
            super().__init__(name = "Сосиска", count = 4, power = 15, id = id)

        def useInFight(self, character: Ally, fight: Fight):
            character.heal(10)
            renpy.say(character.getRenpyChar(), what="ам ам ам")

    class KolbasaDubki(Throwable, DogLikes, CatLikes, FightItem):
        def __init__(self, id):
            super().__init__(name = "Колбаса Дубки", count = 1, power = 50, id = id)

        def useInFight(self, character: Ally, fight: Fight):
            character.heal(50)
            renpy.say(character.getRenpyChar(), what="ох блин Петр прости меня")

    class ColaNoSugar(Throwable, FightItem):
        def __init__(self, id):
            super().__init__(name = "Кола без сахара", count = 2, power = 5, id = id)

        def useInFight(self, character: Ally, fight: Fight):
            character.heal(5)
            renpy.say(character.getRenpyChar(), what="фу, еще больше пить захотелось")

    class Tortik(LeshCounter, FightItem):
        def __init__(self, id):
            super().__init__(name = "Медовик", count = 1, power = 25, id = id)

        def useInFight(self, character: Ally, fight: Fight):
            character.heal(25)
            renpy.say(character.getRenpyChar(), what="мммм")


    class Energizer(FightItem):
        def __init__(self, id):
            super().__init__(name = "Энергетик", count = 1, power = 50, id = id)

        def useInFight(self, character: Ally, fight: Fight):
            renpy.say(character.getRenpyChar(), what="ебашит меня")
            renpy.say(None, what="{} ходит вне очереди".format(character.name))
            fight.castAbility(character)

        def effectDesc(self):
            return "(Дает союзнику ход без очереди)"

    class Panoramiks(Throwable, FightItem):
        def __init__(self, id):
            super().__init__(name = "Волшебное зелье", count = 1, power = 300, id = id)

        def useInFight(self, character: Ally, fight: Fight):
            character.strength = 300
            renpy.say(character.getRenpyChar(), what="ОЩУЩАЮ СИЛИЩЕ")

        def effectDesc(self):
            return "(+300 к силе атаки)"
