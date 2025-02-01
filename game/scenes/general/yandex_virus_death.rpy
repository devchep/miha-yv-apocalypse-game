image yandex_virus = Movie(play = "./video/yandex_virus.webm", loop=False, zoom=0.9)
transform center_pos:
    xalign 0.45
    yalign 0.63
label yandex_virus_death:
    stop music
    show smartphone:
        xalign 0.45
        yalign 0.63
    show yandex_virus:
        xalign 0.452
        yalign 0.63
        zoom 0.6
    pause(357)
    "Миха заражен Яндекс.Вирусом"
    scene maximus-revive with Dissolve(.5)
    play sound "audio/characters/respawn.mp3"
    "Но некая сила перемещает туда, где все началось"
    menu:
        "В начало":
            stop sound
            $ MainMenu(confirm=False)()