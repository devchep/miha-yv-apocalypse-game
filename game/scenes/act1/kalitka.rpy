label kalitka_house:
    scene kalitka with Dissolve(.5)
    pause 3
    miha "Кхм"
    pause 3
    miha "Ну че, мы удивлены?"
    show max1 at right
    maks "Да бля, дефолт"
    maks "Он заебал, звоню"
    scene kalitka_call
    show max1 at right
    andrei "Бля"
    andrei "5 сек"
    andrei "Бегу"
    andrei "Все"
    scene kalitka
    pause 2
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

            #TODO 1: проебали
            show drei1 at left
            andrei "Это ахуеть"
            andrei "Спасибо, парни"
            andrei "Он приехал с Дыбенко показать мне видео"
            andrei "На этой новой платформе"
            andrei "Я люто не хотел смотреть, полюб не смешной"
            andrei "Не хотел кринжевать"

            hide drei1
            show max1 at right
            maks "Едем спасать Диманов"
            miha "Куда?"
            maks "В офис Яндекса, он же вроде в Яндексе"

        "Уйти":
            pass
    stop sound

    return
