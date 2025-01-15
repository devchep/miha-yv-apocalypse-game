label intro:

scene black
"Странное чувство"
"Приятное, интригующее"
"Как будто друзья любят и подарили подарок такой крутой, с душой"

scene fromkfc with Dissolve(.5)
"Сука"
"Среда, купон 5050"
"И что вы думаете? 2 колы без сахара"
"Взял чисто на зло этим мразям"
python:
    inventory.loot(ColaNoSugar("2 колы по купону 5050"))

show max1
maks "Здарова Мих"
menu:
    "Йоу Макс":
        pass
    "Смачный здарова Макс":
        call dab_up
        maks "..."
        maks "уфф"
        pass
maks "Кароче некогда говорить, это пездец"
maks "Нам срочно нужно спасать Игоряна"
miha "..."
maks "Скорее идем, здесь небезопасно"
miha "У меня есть время подготовиться?"
maks "Только быстро"
maks "Мы не хотим здесь задерживаться"
maks "Что тебе нужно?"
menu:
    "Нужно в пятерочку за сосисками":
        maks "..."
        python:
            inventory.loot(Sosiska("пачка сосисок из пятерки"))
        pass
    "Да ниче, погнали":
        maks "Го"
        pass

hide max1

scene alexandrovskaya with Dissolve(.5)
show max1
maks "Действуем быстро"
maks "Нам нужно спасти Игоря"
miha "Понял"
play sound "audio/sobaka1.ogg"
pause(2)
maks "Бля собаки Гаряна"
stop sound
play sound "audio/sobaka2.ogg"
pause(1)
maks "Ноу вей пройти"
stop sound
miha "Погоди, есть идея"
python:
    inventory.loot(ColaNoSugar("2 колы по купону 5050"))
menu:
    "Кинуть:" (action = 1) if inventory.hasThrowables():
        python:
            pickedItem = renpy.display_menu(inventory.getItems())
            inventory.useItem(pickedItem)
        pass
    "Ниче не делать":
        pause(4)
        maks "Ну че?"
        miha "Да бля"
        miha "Не придумал"
        maks "Нам надо как-то пройти мэн, иначе не успеем"
        play sound "audio/sobaka2.ogg"
        pause(1)
        menu:
            "Кинуть:" (action = 1) if inventory.hasThrowables():
                python:
                    pickedItem = renpy.display_menu(inventory.getItems())
                    inventory.useItem(pickedItem)
                pass
            "Уйти":
                miha "Впизду"
                miha "Боюсь собак"
                return
    "Уйти":
        miha "Впизду"
        miha "Боюсь собак"
        return

if Sobaki().approves(pickedItem):
    play sound "audio/metanie-success.mp3" fadein 1 volume 0.7
    pause(1)
    play sound "audio/sobaka_spasibo.ogg" fadeout 1 volume 0.2
    pause(1)
    miha "Изи"
    stop sound
    play sound "audio/sobaka3.ogg" volume 0.1
    maks "Ахуеть, сработало"
    stop sound

    call igoryas_saved

elif pickedItem.name == "Кола без сахара":
    play sound "audio/sobaka_fu.ogg" volume 0.7
    pause(2)
    play sound "audio/sobaka_bez_sahara.ogg" volume 0.7
    pause(3)
    play sound "audio/sobaka_no_way.ogg"
    pause(6)
    play sound "audio/sobaka_miha_idi_nahui.ogg" volume 0.7
    pause(2)
    maks "Это пиздец, Мих"
    maks "Нам больше никогда туда не пройти"
    stop sound
    miha "Бля"
    menu:
        "Уйти":
            return
