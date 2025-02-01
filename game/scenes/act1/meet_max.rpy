label meet_max:
    scene fromkfc with Dissolve(2)
    play music 'audio/meetmax_pesona_ost.mp3' volume 0.08
    show max1
    maks "Здарова Мих"
    menu:
        "Йоу Максоон":
            pass
        "Смачный здарова Макс":
            hide max1
            show maxdab at left
            call dab_up
            maks "..."
            maks "уфф хорошенький"
            hide maxdab
            show max1
            pass
    maks "Крч некогда объяснять, это пизда"
    maks "Нужно скорее к Игоряну"
    miha "..."
    maks "Надо сваливать, здесь небезопасно"
    miha "Мне кое-что надо, есть время?"
    maks "Только быстро"
    maks "Только самое необходимое"
    maks "Что тебе нужно?"
    #TODO бро у меня заказ, давай бб
    menu:
        "Нужно в пятерочку за сосисками":
            maks "Надеюсь это тебе РЕАЛЬНО необходимо"
            maks "..."
            call pyaterochka
            pass
        "Да ниче, погнали":
            maks "Муваем"
            call meet_the_police
            pass
        'Я вспомнил, у меня заказ прямо сегодня нужно выполнить':
            maks "Это пиздец, Мих"
            # call home
            call meet_the_police
            pass

    python:
        maks_unit = MaxHeyman(65, 10)
        party.addMember(maks_unit)

    hide max1