label save_drei:
    scene electron
    show max2 at right
    maks "звоним Андрею"
    scene electron_call
    show max2 at right
    andrei "Да"
    maks "Чел, выходи через 10 мин, оч надо"
    andrei "Ага, окес"
    andrei "Выхожу"
    miha ")"
    scene kalitka with Dissolve(.5)
    pause 3
    miha "Кхм"
    pause 3
    miha "Ну че"
    show max1 at right
    maks "Да бля, дефолт"
    maks "Звоню"
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
    maks "Сука"
    play sound "audio/subway-surfers.mp3" volume 0.2 loop
    show max1 at right
    maks "Это пиздец..."
    maks "Слышите?"
    maks "Андрею конец"
    maks "Помните Жекана?"
    maks "Вот Дрюс тоже уже этот.."
    maks "Ебанулся"
    maks "Это причина по которой нам нужно спасти как можно больше друзей"
    maks "Чтобы они остались в своем уме"
    maks "Здесь не успели"
    maks "Срочно уходим"
    menu:
        "Разбить калитку":
            play sound "audio/minus-kalitka.mp3"
            scene dom_dreya
            call torop_fight

            show drei1 at left
            andrei "Это ахуеть"
            andrei "Спасибо, парни"
            andrei "Он приехал с Дыбенко показать мне видео"
            andrei "На этой новой платформе"
            andrei "Яндекс.Вирус"
            andrei "Я люто не хотел смотреть, полюб не смешной"
            andrei "Не хотел кринжевать"
        "Уйти":
            pass
    stop sound

    return
