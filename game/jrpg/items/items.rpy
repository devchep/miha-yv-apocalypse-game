init 1 python:
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

    class Sosiska(Throwable, DogLikes, CatLikes, FightItem):
        def __init__(self, id):
            super().__init__(name = "Сосиска", count = 4, power = 15, id = id)

        def useInFight(self, character: Character):
            character.heal(10)
            renpy.say(character.getRenpyChar(), what="ам ам ам")
            self.count -= 1