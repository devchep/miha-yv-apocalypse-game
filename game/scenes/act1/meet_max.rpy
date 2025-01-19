label meet_max:
    scene fromkfc
    show max1
    maks "Здарова Мих"
    menu:
        "Йоу Максоон":
            pass
        "Смачный здарова Макс":
            call dab_up
            maks "..."
            maks "уфф хорошенький"
            pass
    maks "Крч некогда объяснять, это пизда"
    maks "Нужно скорее к Игоряну"
    miha "..."
    maks "Надо сваливать, здесь небезопасно"
    miha "Мне кое-что надо, есть время?"
    maks "Только быстро"
    maks "Только самое необходимое"
    maks "Что тебе нужно?"
    menu:
        "Нужно в пятерочку за сосисками":
            maks "Надеюсь это тебе РЕАЛЬНО необходимо"
            python:
                inventory.loot(Sosiska("пачка сосисок из пятерки"))
            pass
        "Да ниче, погнали":
            maks "Муваем"
            pass

    python:
        maks_unit = MaxHeyman(65, 10)
        party.addMember(maks_unit)

    hide max1

    scene alexandrovskaya with Dissolve(.5)
    show max1
    maks "Бля, хоть бы успели, промедление может стоить ему жизни"
    miha "Есть план?"
    play sound "audio/sobaka1.ogg"
    pause(2)
    maks "СУка, собаки не в клетках, как не вовремя!"
    stop sound
    play sound "audio/sobaka2.ogg"
    pause(1)
    maks "Ну они нас нахуй порвут, нужен абуз и срочно"
    stop sound
    miha "Ща"
    python:
        inventory.loot(ColaNoSugar("2 колы по купону 5050"))
    menu:
        "Кинуть:" (action = 1) if inventory.hasThrowables():
            python:
                pickedItem = renpy.display_menu(inventory.getItems())
                inventory.useItem(pickedItem)
            pass
        "Стоим афк":
            pause(4)
            maks "Ну так что?"
            miha "Да бля"
            miha "Не придумал"
            maks "Ты угараешь? Сейчас не до троллинга"
            play sound "audio/sobaka2.ogg"
            pause(1)
            menu:
                "Кинуть:" (action = 1) if inventory.hasThrowables():
                    python:
                        pickedItem = renpy.display_menu(inventory.getItems())
                        inventory.useItem(pickedItem)
                    pass
                "Уйти":
                    miha "Ну нахуй, в пизду"
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
        maks "Заебумба! Сработало!"
        stop sound

        call igoryas_saved

    elif pickedItem.name == "Кола без сахара":
        play sound "audio/sobaka_fu.ogg"
        pause(2)
        play sound "audio/sobaka_bez_sahara.ogg"
        pause(3)
        play sound "audio/sobaka_no_way.ogg"
        pause(6)
        play sound "audio/sobaka_miha_idi_nahui.ogg"
        pause(2)
        maks "Мы в такой хуйне, Мих"
        maks "Нам больше никогда туда не пройти, можешь писать Игоряну некролог, я хз"
        stop sound
        miha "Ну пиздец че"
        menu:
            "Уйти":
                return

    hide max1
    hide igor1