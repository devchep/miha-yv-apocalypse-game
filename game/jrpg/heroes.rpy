image drones_attack = Movie(play = "./video/drones_attack.webm", loop=False)
init 3 python:
    hugeboom = Move((100, 0), (-100, 0), .10, bounce=True, repeat=True, delay=.275)
    import random
    from operator import attrgetter

    class Miha(Ally):
        def __init__(self, health, strength):
            super().__init__("Миха", health, strength, "ход Михой")
            self.abilities = [Insult()]
            self.skillBranches = [
                SkillBranch("Стаки ходов", [StackTurns()]),
                SkillBranch("Ульта Михи", [MihaUlt()])
            ]

        def getRenpyChar(self):
            return miha

    class MaxHeyman(Ally):
        def __init__(self, health, strength):
            super().__init__("Макс", health, strength, "ход Максом")
            self.abilities = [Shoulder()]
            self.skillBranches = [SkillBranch("Машиной проехаться по всем врагам", [AoeShoulder()])]

        def getRenpyChar(self):
            return maks

    class Igoryas(Ally):
        def __init__(self, health, strength):
            super().__init__("Игоряс", health, strength, "ход Игорясом")
            self.abilities = [Smoke()]
            self.skillBranches = [
                SkillBranch("Провокация", [TheWall()]),
                SkillBranch("Вампиризм", [Vampirism()]),
            ]

        def getRenpyChar(self):
            return igoryas


    class Drei(Ally):
        def __init__(self, health, strength):
            super().__init__("Дрюс", health, strength, "ход Дрюсом")
            self.abilities = [DeadlyBlow()]

        def getRenpyChar(self):
            return andrei

    class Diman(Ally):
        def __init__(self, health, strength):
            super().__init__("Диман", health, strength, "ход Диманом")
            self.abilities = [CatHeal()]
            self.skillBranches = [
                SkillBranch("Ульта", [DimanUlt()])
            ]

        def getRenpyChar(self):
            return diman

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
                if self.strength > 15:
                    renpy.say(None, what="Атаки врага стали слабее")
                    renpy.say(None, what="Враг просит еще")
                else:
                    self.playAttackSound = self.cat_sound
                    self.attack_phrase = self.cat_attack_phrase
                    self.cat_sound()
                    renpy.say(self.getRenpyChar(), what="Meow")
                    renpy.say(None, what="Враг стал ласковый")
                    self.strength = 0
            if isinstance(item, ColaNoSugar):
                get_achievement("tigr-ne-govno", trans=achievement_transform)
                renpy.show('tigr_mem')
                renpy.pause()
                renpy.hide('tigr_mem')


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

                [self.hit(member, 25) for member in party.members.values()]
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
                partyMemberToAttack = party.getTargetToAttack()
                partyMemberToAttack.health -= self.getAttackPower()
                self.playAttackSound()
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())

        def getRenpyChar(self):
            return torop

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")

    class Gera(Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Гера", health = health, strength = strength)
            self.round = 1

        def attack_phrase(self):
            return ""

        def playAxeSound(self, choice):
            if choice == 1:
                 renpy.play("audio/bigboom.mp3")
            elif choice == 2:
                renpy.play("audio/characters/gera/axe2.mp3")
            elif choice == 3:
                renpy.play("audio/bigboom.mp3")

        def attack(self, party: Party):
            renpy.sound.play("audio/characters/gera/kakoi_topor.mp3", loop = False)
            choice = renpy.display_menu([("Топор1", 1), ("Топор2", 2), ("Топор3", 3)])
            topor = random.choice([1, 2, 3])

            if (self.round > 4):
                renpy.show("maximus")
                renpy.say(maximus, "{b}Довольно{/b}")
                renpy.with_statement(hugeboom)
                renpy.play("audio/bigboom.mp3")
                renpy.play("audio/bigboom.mp3")
                renpy.with_statement(hugeboom)
                self.health = -100
                renpy.say(maximus, "")
                return

            self.round += 1
            if topor == choice:
                renpy.say(self.getRenpyChar(), what="Молодец")
                return

            [self.hit(member, 25) for member in party.members.values()]
            renpy.sound.stop()
            self.playAxeSound(choice)
            renpy.show("gera_attack"+str(choice % 2 + 1))
            renpy.with_statement(Dissolve(.2))
            renpy.with_statement(hugeboom)
            renpy.hide("gera_attack"+str(choice % 2 + 1))
            return

        def getRenpyChar(self):
            return gera

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

        def react(self, item: Item):
            if isinstance(item, LeshCounter):
                self.health = -100
                renpy.play("lush/plankton-augh.mp3")
                renpy.say(self.getRenpyChar(), what="")

    class Maximus(Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Максимус", health = health, strength = strength, partyName = "Максимус")

        def attack_phrase(self):
            return random.choice([""])

        def getRenpyChar(self):
            return maximus

        def playAttackSound(self):
            renpy.play("audio/fireball.mp3")


    class Gay:
        def mayBeOffended(self):
            return True

        def getAttackPower(self):
            return self.strength

        def attack(self, party: Party):
            for i in range(2):
                x = random.choice(list(party.members.values()))
                x.disabled(1)
                x.health -= self.getAttackPower()
                self.playAttackSound()
                renpy.say(self.getRenpyChar(), what=self.attack_phrase())
                renpy.say(None, f'{x.name} не может наносить урон')

        def insultingPhrase(self):
            return random.choice([
                "Тебе бы даже Игорь не присунул",
                "Ты кончил или пукнул?",
                "Мне больше трапы нравятся",
            ])

        def offendEffectAnnounce(self):
            renpy.say(None, f'Ой ну прям')

    class Anal(Gay, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Анальный говносос", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["*Пукнул спермой*"])

        def getRenpyChar(self):
            return anal

        def playAttackSound(self):
            renpy.play("audio/cum-fart.mp3")
    
    class Hunt(Gay, Enemy):
        def __init__(self, health, strength):
            super().__init__(name = "Hunter", health = health, strength = strength)

        def attack_phrase(self):
            return random.choice(["*Пукнул спермой*"])

        def getRenpyChar(self):
            return hunter

        def playAttackSound(self):
            renpy.play("audio/cum-fart.mp3")
