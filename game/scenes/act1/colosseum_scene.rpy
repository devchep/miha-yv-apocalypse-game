label colosseum_scene:
    scene colosseum with Dissolve(2)
    play music "./audio/soundtrack_colo.mp3" volume 0.4
    miha "Блин, а мы в тот колизей пришли хоть?"
    miha "Надо же было так заплутать в городе сестрорецке"
    show igoryas_colo at left
    igoryas "Слушайте, не знаю что нас тут ждет"
    igoryas "Но мне почему-то кажется я готов"
    miha "Оно видно"
    igoryas "Думаю о ней каждый день"
    igoryas "О Римской Империи"
    igoryas "Как хорошо что Андрюха живет в колизее и дарит нам в очередной раз шанс подумать о великом"
    igoryas "Бессмертном"
    miha "Это правда"
    hide igoryas_colo with Dissolve(.5)
    show tigr at right with Dissolve(.5)
    play sound "audio/characters/drei/tigr.mp3"
    miha "Думаю мы все понимаем что сейчас будет"
    stop sound
    menu:
        "Драться с тигром 1x1 в Колизее":
            pass
        "Бежать":
            "Нет, нет, бежать тут некуда"

    call colosseum_fight
    play music "./audio/soundtrack_colo.mp3" volume 0.4
    python:
        inventory.chooseReward([Panoramiks("Панорамикс награда в Колизее")])

    call kalitka_house