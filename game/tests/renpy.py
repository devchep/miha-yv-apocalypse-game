class RenpyFake:
    def __init__(self):
        self.allSaid = {}

    def say(self, who, what):
        if who is None:
            who = 'narrator'
        self.allSaid.update({who: what})

    def play(self, path):
        pass


creep = ""

renpy = RenpyFake()