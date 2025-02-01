label kalitka_house:
    scene kalitka with Dissolve(.5)
    pause 1
    miha "Кхм"
    show maxwait at right
    pause 1
    miha "Ну че, мы удивлены?"
    maks "Да бля, дефолт"
    maks "Он заебал, звоню"
    hide maxwait
    scene kalitka_call
    show max1 at right
    andrei "Бля"
    andrei "5 сек"
    andrei "Бегу"
    andrei "Все"
    scene kalitka
    pause 1
    stop music
    play sound "audio/subway-surfers.mp3" volume 0.2
    pause 2
    stop sound
    maks "Суууука"
    play sound "audio/subway-surfers.mp3" volume 0.2 loop
    show max1 at right
    maks "Это пиздец..."
    maks "Слышите?"    # TODO добавить чекер количества пати, чтобы обращение соответствовало числу
    maks "Андрею жопа"
    maks "Помните Жекана?"   # TODO добавить чекер, пройдена ли сцена с Жеканом (если не было можно типа "хз зачем вспомнил")
    maks "Вот Дрюс тоже уже этот.."
    maks "Ебанулся"
    maks "Если мы будем тупить, то все друзья возьмут с него пример"
    maks "И их будет уже не узнать"
    maks "Здесь походу не успели"
    maks "Сваливаем"
    menu:
        "Разбить калитку":
            play sound "audio/minus-kalitka.mp3"
            scene dom_dreya
            call torop_fight

            play music "./audio/soundtrack5.mp3" volume 0.3
            show drei1 at left
            andrei "Это ахуеть"
            andrei "Спасибо, парни"
            andrei "Он приехал с Дыбенко показать мне видео"
            andrei "Я люто не хотел смотреть"
            andrei "Не хотел кринжевать"
            andrei "А теперь даже блин интересно стало что там"
            miha "Слушай, по-моему с ним все нормально"
            menu:
                "Посмотреть телефон":
                    call yandex_virus_death
                "Не смотреть":
                    pass
            hide drei1
            show max1 at right
            maks "Едем спасать Диманов"
            miha "Куда?"
            maks "В офис Яндекса, он же вроде в Яндексе"

        "Уйти":
            pass
    stop sound

    return
