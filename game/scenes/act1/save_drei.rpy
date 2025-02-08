label maybe_serbia:
    scene vokzal with Dissolve(.5)
    show igor_pretty at left
    igoryas "Элка до Сербии через 15 минут"
    show max4 at right
    maks "А до города через 5 минут"
    maks "Может это.."
    maks "Как-то не хочется бросать Диманов"
    igoryas "Не хочется у пчелки в попке"
    igoryas "Ты понял короче"
    miha "Макс, ты задумался о том, как правильно поступить?"
    maks "Да"
    miha "Как всегда решение придется принимать мне?"
    maks "Да..."
    menu:
        "Влада":
            pass
        "Маша":
            pass
    
    python:
        hide_all_max()
    show max_angry at right
    maks "Да ты ск"
    maks "А если серьезно"

    menu:
        "Идемо у Србију да једемо плескавицу":
            jump serbia
            pass
        "Ты прав, Диман, бы нас не бросил":
            jump act2
            pass

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
    gera "Я присоединился, чтобы поддержать Вас в это непростое время"
    gera "Увидимся в лагере"
    hide gera1
    "Нажав на кнопку в верхнем углу Вы можете попасть в лагерь"
    "В лагере можно пообщаться и улучшить компаньонов, а также использовать предметы"
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

    if isZakl:
        jump maybe_serbia
    else:
        python:
            hide_all_drei()
        show max1 at right
        maks "Едем спасать Диманов"
        miha "Куда?"
        maks "Huawei Technologies Co Ltd, Bantian, Huawei Base, Longgang District, Shenzhen, Guangdong, 518100"
        miha "Ну да"

    return