label alexandrovskaya_ariving:
    play music '/audio/clock_tick.mp3' volume 0.25
    play sound '/audio/chuchuh.mp3' volume 0.2

    scene electron with Dissolve(1.5)
    show maxsit at right
    pause(1)
    miha "К чему такая спешка?"
    maks "Я сам до конца не понимаю что происходит"
    maks "Но всё вокруг меняется очень быстро"
    maks "Нельзя никому доверять"
    maks "Поэтому я спешу собрать всех наших"

    stop music
    stop sound
    play music '/audio/clock_tick.mp3' volume 0.1
    play audio "./audio/alexandrovskaya_ambient.mp3" volume 0.5
    scene alexandrovskaya with Dissolve(1.5)
    show max1
    maks "Наше промедление может стоить ему жизни"

    # cюда передвинул файт с жеканом
    stop music
    play sound "audio/subway-surfers.mp3" volume 0.2
    pause 1
    stop sound
    maks "Блядь"
    play sound "audio/subway-surfers.mp3" volume 0.1 loop
    maks "Кто-то из них идет"
    hide max1
    show creep at left
    creep "Че"
    creep "стоите?"

    show max1 at right
    maks "Ни в коем случае не смотри, что он нам покажет"
    hide max1

    creep "Тут капец вообще"
    creep "Смотрите"
    stop sound

    menu:
        "Атаковать":
           miha "Не буду я твою херню смотреть"
        "Че там у тебя":
            play music "./audio/soundtrack5.mp3" volume 0.3
            call yandex_virus_death

    call zheka_fight
    hide creep
    play music "./audio/soundtrack5.mp3" volume 0.3
    show max1 at right
    maks "Надеюсь мы его не кокнули"
    maks "Нас же повяжут"
    miha "Да я и не против"
    # TODO: спрайт макса
    maks "??"
    scene zhekan_dead with Dissolve(.5)
    miha "По-моему с ним все нормально"
    menu:
        "Взять телефон Жекана":
            call yandex_virus_death
        "Уйти":
            pass

    scene alexandrovskaya with Dissolve(.5)
    show max1 at right

    maks "Идем за Игорем"
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
    menu:
        "Кинуть:" (action = 1) if inventory.hasThrowables():
            python:
                pickedItem = renpy.display_menu(inventory.getThrowables())
                inventory.useItem(pickedItem)
            pass
        "Ниче не делать":
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
                        pickedItem = renpy.display_menu(inventory.getThrowables())
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