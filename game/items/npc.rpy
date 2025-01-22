init 2 python:
    class Sobaki:
        def __init__(self):
            pass

        def approves(self, item: Item):
            approve = False
            if isinstance(item, DogLikes):
                approve = True
            return approve
