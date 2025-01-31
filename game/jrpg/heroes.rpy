image drones_attack = Movie(play = "./video/drones_attack.webm", loop=False)
init 2 python:
    hugeboom = Move((100, 0), (-100, 0), .10, bounce=True, repeat=True, delay=.275)
    import random
    from operator import attrgetter

    class Miha(Ally):
        def __init__(self, health, strength):
            super().__init__("Миха", health, strength, "ход Михой")

        def getAbilities(self):
            return [Insult()]

        def getRenpyChar(self):
            return miha

    class MaxHeyman(Ally):
        def __init__(self, health, strength):
            super().__init__("Макс", health, strength, "ход Максом")
            self.abilities = [Shoulder()]
            self.skillBranches = [SkillBranch("Максон - Машина ппц", [AoeShoulder()])]

        def getRenpyChar(self):
            return maks

    class Igoryas(Ally):
        def __init__(self, health, strength):
            super().__init__("Игоряс", health, strength, "ход Игорясом")
            self.abilities = [Smoke()]
            self.skillBranches = [SkillBranch("Игорь - Стена", [TheWall()])]

        def getAbilities(self):
            return self.abilities

        def getRenpyChar(self):
            return igoryas


    class Drei(Ally):
        def __init__(self, health, strength):
            super().__init__("Дрюс", health, strength, "ход Дрюсом")
            self.abilities = [DeadlyBlow()]

        def getAbilities(self):
            return self.abilities

        def getRenpyChar(self):
            return andrei

    class Tupoi:
        def mayBeOffended(self):
            return True

        def getAttackPower(self):
            return self.strength*2 if self.isOffended else self.strength

        def offendEffectAnnounce(self):
            renpy.say(None, "Атаки врага стали в 2 раза сильнее")

    class Zheka(Tupoi, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Учебный Крип", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["ууу суки", "на", "бью"])

        def insultingPhrase(self):
            return random.choice([
            "Я тебя буду называть Ев, потому что имя с содержанием 'гений' внутри тебе ну никак не подходит)",
            "Знаешь, никогда тебя за человека то и не считал"
            ])

        def getRenpyChar(self):
            return creep

    class Tigr(Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Тигр", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["rawr", "raaawr", "raaaawr"])

        def insultingPhrase(self):
            return random.choice([
                "Кис-кис-кис дурачок",
                "Кыш епта отсюдова",
            ])

        def getRenpyChar(self):
            return tigr

        def playAttackSound(self):
            renpy.play("audio/characters/drei/rawr.mp3")

        def cat_sound(self):
            renpy.play("audio/characters/drei/meow.mp3")

        def cat_attack_phrase(self):
            return random.choice(["Meow", "Meoow", "Meeeoow"])

        def react(self, item: Item):
            if isinstance(item, CatLikes):
                self.strength -= item.getPower()
                item.consume(1)
                if self.strength > 15:
                    renpy.say(None, what="Врагу очень понравилась прикормка")
                    renpy.say(None, what="Атаки врага стали слабее")
                else:
                    self.playAttackSound = self.cat_sound
                    self.attack_phrase = self.cat_attack_phrase
                    self.cat_sound()
                    renpy.say(self.getRenpyChar(), what="Meow")
                    renpy.say(None, what="Враг стал ласковый")
                    self.strength = 0

    class Tiktoker:
        def mayBeOffended(self):
            return True

        def getAttackPower(self):
            return self.strength*self.getAttackResult() if self.isOffended else self.strength

        def getAttackResult(self):
            return random.choice([1, 0])

        def offendEffectAnnounce(self):
            renpy.say(None, 'Враг временно имеет шанс промахнуться с вероятностью 50%%')

    class Torop(Tiktoker, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Тороп", health = health, strength = strength)
            self.drones_appearance = 0

        def attack_phrase(self):
            return random.choice(["я вам покажу", "я вам обязательно покажу", "вы у меня посмотрите"])

        def insultingPhrase(self):
            return random.choice([
            "Твои тиктоки на таком дне, опуститься чуть ниже и просто уже дерьмом сдавит как батискаф",
            "Че ты там мячиком)",
            "Что ты там покажешь епта, мать в канаве?"
            ])

        def attack(self, party: Party):
            if self.health <= self.max_health / 2:
                renpy.say(self.getRenpyChar(), what="Пизда Вам)")
                if self.drones_appearance == 0:
                    renpy.show("drones_attack", at_list=[right])
                    renpy.say(self.getRenpyChar(), what="Готовьтесь детки")
                    renpy.hide("drones_attack")
                    renpy.play("audio/bigbruh.mp3")
                    renpy.say(None, what="Все кринжанули и не смогут нанести урон в следующем ходу")
                    [member.disabled(1) for member in party.members.values()]
                    self.drones_appearance += 1

                [self.hit(member, 34) for member in party.members.values()]
                renpy.play("audio/bigboom.mp3")
                renpy.show("lancet")
                renpy.with_statement(Dissolve(.2))
                renpy.with_statement(hugeboom)
                renpy.hide("lancet")
                return

            if len(party.members) > 0:
                renpy.show("ball_weapon")
                renpy.with_statement(Dissolve(.1))
                renpy.with_statement(vpunch)
                renpy.hide("ball_weapon")
                partyMemberToAttack = min(filter(lambda x: x.health > 0, party.members.values()),key=attrgetter('health'))
                partyMemberToAttack.health -= self.getAttackPower()
                self.playAttackSound()
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())

        def getRenpyChar(self):
            return torop

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Chinese:
        def mayBeOffended(self):
            return False

        def getAttackPower(self):
            return self.strength

        def insultingPhrase(self):
            return random.choice([
                "Ваш вождь жестко слабый",
                "Тупой ты китаец, слышишь меня?"
            ])

        def offendEffectAnnounce(self):
            renpy.say(None, 'Враг нихуя не понял')

    class Knee(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Knee", health = health, strength = strength, partyName = "Knee")

        def attack_phrase(self):
            return random.choice(["tekkeno panch", "feng wey atak"])

        def getRenpyChar(self):
            return knee

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Law(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Law", health = health, strength = strength, partyName = "Law")

        def attack_phrase(self):
            return random.choice(["huuuuuuuyaaaaa", "ai", "kiyaaaa"])

        def getRenpyChar(self):
            return law

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class First(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "FrontMan", health = health, strength = strength, partyName = "001")

        def attack_phrase(self):
            return random.choice([
                "Wanna play a hero?",
                 "I will show you the truth"
             ])

        def getRenpyChar(self):
            return first

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class ChineseLesh(Chinese, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Лещ Dage", health = health, strength = strength, partyName = "Лещ Dage")

        def attack_phrase(self):
            return random.choice([
                "AHAHAHAHAHAH",
                 "ahahahahahhahahaahhaahh"
             ])

        def getRenpyChar(self):
            return chineseLesh

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Maximus(Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Максимус", health = health, strength = strength, partyName = "Максимус")

        def attack_phrase(self):
            return random.choice([""])

        def getRenpyChar(self):
            return maximus

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")
