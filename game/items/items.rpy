init python:
    # interfaces
    class Item:
        def __init__(self, name, count, id):
            self.name = name
            self.count = count
            self.id = id

    class Throwable(Item):
        pass

    class DogLikes(Item):
        pass

    # inventory
    class Inventory:
        def __init__(self):
            self.items = dict()

        def loot(self, item: Item):
            self.items.update({item.id: item})

        def useItem(self, item: Item):
            item.count -= 1
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


    # actual items
    class Sosiska(Throwable, DogLikes):
        def __init__(self, id):
            self.name = "Сосиска"
            self.count = 4
            self.id = id

    # actual items
    class ColaNoSugar(Throwable):
        def __init__(self, id):
            self.name = "Кола без сахара"
            self.count = 2
            self.id = id