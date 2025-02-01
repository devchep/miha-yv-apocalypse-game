image yandex_virus = Movie(play = "./video/yandex_virus_death.webm", loop=False)
label yandex_virus_death:
    stop music
    show yandex_virus at left
    pause(357)
    "Миха заражен Яндекс.Вирусом"
    scene maximus-revive with Dissolve(.5)
    play sound "audio/characters/respawn.mp3"
    "Но некая сила перемещает туда, где все началось"
    menu:
        "В начало":
            stop sound
            $ MainMenu(confirm=False)()