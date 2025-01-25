label save_drei:
    scene electron with Dissolve(1.5)
    show max2 at right
    maks "Набираю Древу"
    scene electron_call
    show max2 at right
    pause(.5)
    andrei "Алло, че такое?"
    maks "Дядь, выходи через 10 мин, оч надо"
    andrei "Ага, окес"
    andrei "Выхожу"
    miha ")"

    scene vokzal with Dissolve(.5)
    show max1 at right
    maks "Бля, а куда идти то?"
    maks "Дрей же теперь в колизее живет вроде"
    hide max1
    show igor1 at left
    igoryas "По-люб колизей"
    hide igor1
    show gera1
    gera "Михаил, друзья, мы встретились вновь"
    show screen campButton
    gera "Я присоединился чтобы поддержать Вас в эти непростые мнгмновения"
    gera "Увидимся в лагере"
    hide gera1
    "Нажав на кнопку в верхнем углу Вы можете попасть в лагерь"
    "В лагере можно пообщаться и улучшить соратников, а также использовать предметы"
    "Лагерь доступен в любой момент вне боя и окна выбора"
    show max1 at right
    maks "Ну че, куда идем?"
    menu:
        "К Калитке":
            call kalitka_house
        "В Колизей":
            #TODO файт в колизее
            pass
