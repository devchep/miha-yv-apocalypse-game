label pyaterochka:

    scene p-outside with Dissolve(1.5)

    show stepa1
    stepa "Миша привет"
    hide stepa1

    scene p-inside
    show stepa2 at right

    stepa "Че покупаешь здесь?"
    miha "Coсиськи"
    stepa "Сосиськи это как колбаса"
    stepa "А колбасу я на севере видел"
    stepa "Назвается дубки"
    stepa "А дубки это же у нас, здесь"
    stepa "А у них дубков нет"
    stepa "Кстати, тебе тоже привез"
    python:
        inventory.loot(KolbasaDubki("Подарок с Севера от Степы"))
    # gera "Привет, Ст-тепа Аф-ф-ф-тарлы"
    # gera "Монка ... гига"
    show gera2 at left
    play sound "audio/gena_gorin_privet_stepa.mp3"
    gera ""
    stepa "Так, линейку я уже купил"
    stepa "Я пойду, да"
    stop sound
    stepa "С Димой в доточку жестко рубать собираемся"
    hide gera2
    menu:
        "Вокруг все странно себя ведут, ты не хочешь узнать что происходит?":
            python:
                is_dima_infected = False            
        "Играть-то можете, но выиграть без меня это вряд ли":
            python:
                is_dima_infected = True
    show gera2 at left
    gera "Монка ... гига"
    stepa "Миша, пока"
    hide stepa2
    hide gera2
    show gera1
    play music "./audio/mysterymorgan.mp3" volume 0.3
    gera "Михаил, наконец мы остались наедине"
    gera "Происходят ужасные вещи и время на исходе"
    gera "Вам следует быть предельно осторожным"
    gera "Вы не можете себе позволить умереть в бою"
    gera "///////"
    gera "Мы более не можем тратить время на этот разговор"
    gera "Вам пора"
    hide gera2
    play music "./audio/soundtrack4.mp3" volume 0.3
    miha "Так, я хотел закупиться"
    python:
        inventory.choice(
            1,
            [Sosiska("пачка сосисок из пятерки"), Tortik("Медовичок")]
        )
