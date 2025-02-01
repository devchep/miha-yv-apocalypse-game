label save_drei:
    stop music
    play music '/audio/clock_tick.mp3' volume 0.25
    play sound '/audio/chuchuh.mp3' volume 0.2

    scene electron with Dissolve(1.5)
    show maxsit at right
    maks "Набираю Древу"
    scene electron_call
    show maxsit at right
    pause(.5)
    andrei "Алло, че такое?"
    maks "Дядь, выходи через 10 мин, оч надо"
    andrei "Ага, окес"
    andrei "Выхожу"
    miha ")"
    stop sound
    stop music
    scene vokzal with Dissolve(.5)
    show max1 at right
    maks "Бля, а куда идти то?"
    maks "Дрей же теперь в колизее живет вроде"
    hide max1
    show igor1 at left
    igoryas "По-люб колизей"
    hide igor1
    show gera1
    play music "./audio/mysterymorgan.mp3" volume 0.3
    gera "Михаил, друзья, мы встретились вновь"
    show screen campButton
    gera "Я присоединился чтобы поддержать Вас в эти непростые мнгмновения"
    gera "Увидимся в лагере"
    hide gera1
    "Нажав на кнопку в верхнем углу Вы можете попасть в лагерь"
    "В лагере можно пообщаться и улучшить соратников, а также использовать предметы"
    "Лагерь доступен в любой момент вне боя"
    play music "./audio/soundtrack5.mp3" volume 0.3
    show max1 at right
    maks "Ну че, куда идем?"
    menu:
        "К Калитке":
            call kalitka_house
        "В Колизей":
            if party.hasExp():
                play music "./audio/mysterymorgan.mp3" volume 0.3
                show gera1
                gera "Михаил, настойчиво рекомендую перейти в лагерь и использовать весь накопленный опыт перед входом в следующую локацию"
                hide gera1
                play music "./audio/soundtrack5.mp3" volume 0.3
                miha "Да все окей окей, на созвоне"
            call colosseum_scene
            pass
