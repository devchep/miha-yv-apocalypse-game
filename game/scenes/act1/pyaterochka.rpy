label pyaterochka:

    scene p-outside

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
    # gera "Привет, Ст-тепа Аф-ф-ф-тарлы"
    # gera "Монка ... гига"
    show gera2 at left
    play audio "audio/gena_gorin_privet_stepa.mp3"
    gera ""
    stepa "Так, линейку я уже купил"
    stepa "Я пойду, да"
    stepa "С Димой в доточку жестко рубать собираемся"
    menu:
        "Вокруг все странно себя ведут, ты не хочешь узнать что происходит?":
            python:
                is_dima_infected = False            
        "Играть-то можете, но выиграть без меня это вряд ли":
            python:
                is_dima_infected = True
    gera "Монка ... гига"
    stepa "Миша, пока"
    hide stepa2
    hide gera2
    show gera1
    gera "Михаил, наконец мы остались наедине"
    gera "Происходят ужасные вещи и время на исходе"
    gera "///////"
    gera "Мы более не можем тратить время на этот разговор"
    gera "Тебе пора"
