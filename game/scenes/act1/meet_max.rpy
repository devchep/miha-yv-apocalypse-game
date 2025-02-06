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
            call max_dab_up
            show max1
            maks "..."
            maks "уфф хорошенький"
            pass
    maks "Крч некогда объяснять, это пизда"
    maks "Нужно скорее к Игоряну"
    miha "..."
    maks "Надо сваливать, здесь небезопасно"
    maks "Быстро собирайся"
    maks "Берем только самое необходимое"
    maks "Что тебе нужно?"
    menu:
        "Нужно в пятерочку за сосисками":
            maks "Хм"
            maks "Мы сейчас не в кинотеатр, ну ладно..."
            call pyaterochka
            pass
        "Слушай, странные вещи происходят, ничего не знаешь об этом?":
            maks "Все по ходу станет ясно, доверься мне"
            maks "Погнали в пятерку закуп делать"
            menu:
                'Я вспомнил, у меня заказ прямо сегодня нужно выполнить':
                    maks "Это пиздец, Мих"
                    call home_wasps
                    pass
                "Конечно, погнали":
                    call pyaterochka
                    pass

    python:
        maks_unit = MaxHeyman(65, 10)
        party.addMember(maks_unit)

    hide max1