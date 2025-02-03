init 0 python:
    # interfaces
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

    class Throwable(Item):
        pass

    class DogLikes(Item):
        pass

    class CatLikes(Item):
        pass

    class FightItem(Item):
        def useInFight(self, character: Character):
            pass

        def useAgainstEnemy(self, enemy: Character):
            enemy.react(self)
            self.count -= 1

    # inventory
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

        def menuName(self, item: Item):
            return item.name + "(x"+str(item.count)+")" if item.count > 0 else ""

        def hasThrowables(self):
            throwables = False
            for item in iter(self.items.values()):
                if isinstance(item, Throwable):
                    throwables = True

            return throwables

        def notEmpty(self):
            return any(item.count > 0 for item in self.items.values())

        def choice(self, count, items):
            if count > 1:
                renpy.say(None, what="Выберите предметы в количестве "+str(count))
            else:
                renpy.say(None, what="Выберите предмет")
            for i in range(count):
                pickedItem = renpy.display_menu([(self.menuName(item), item) for item in items])
                self.loot(pickedItem)
                items = [item for item in items if item != pickedItem]

        def chooseReward(self, items):
            renpy.say(None, what="Поздравляем")
            renpy.say(None, what="Выберите награду")
            pickedItem = renpy.display_menu([(self.menuName(item), item) for item in items])
            self.loot(pickedItem)

    # actual items
    class Sosiska(Throwable, DogLikes, CatLikes, FightItem):
        def __init__(self, id):
            super().__init__(name = "Сосиска", count = 4, power = 15, id = id)

        def useInFight(self, character: Character):
            character.heal(10)
            renpy.say(character.getRenpyChar(), what="ам ам ам")
            self.count -= 1

    class KolbasaDubki(Throwable, DogLikes, CatLikes, FightItem):
        def __init__(self, id):
            super().__init__(name = "Колбаса Дубки", count = 1, power = 50, id = id)

        def useInFight(self, character: Character):
            character.heal(50)
            renpy.say(character.getRenpyChar(), what="ох блин Петр прости меня")
            self.count -= 1

    class ColaNoSugar(Throwable, FightItem):
        def __init__(self, id):
            super().__init__(name = "Кола без сахара", count = 2, power = 5, id = id)

        def useInFight(self, character: Character):
            character.heal(5)
            renpy.say(character.getRenpyChar(), what="фу, еще больше пить захотелось")
            self.count -= 1

    class Tortik(Throwable, FightItem):
        def __init__(self, id):
            super().__init__(name = "Медовик", count = 1, power = 20, id = id)

        def useInFight(self, character: Character):
            character.heal(20)
            renpy.say(character.getRenpyChar(), what="мммм")
            self.count -= 1

    class Panoramiks(Throwable, FightItem):
        def __init__(self, id):
            super().__init__(name = "Зелье Панорамикс", count = 1, power = 300, id = id)

        def useInFight(self, character: Character):
            character.strength = 300
            renpy.say(character.getRenpyChar(), what="ОЩУЩАЮ СИЛИЩЕ")
            self.count -= 1
