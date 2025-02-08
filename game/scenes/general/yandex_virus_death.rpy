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
    "Ты заражен Яндекс.Вирусом"
    scene black with Dissolve(1.5)
    "И листал тиктоки пока не кончился Яндекс.Плюс"
    scene yandex_zen with Dissolve(1.5)
    "А после впал в Яндекс.Дзен {color=#000000}навсегда{/color}"
    play sound "audio/characters/respawn.mp3"
    scene maximus-revive with Dissolve(.5)
    pause(2)
    "Некая неудержимая сила перемещает тебя туда, где все началось"
    menu:
        "Предаться этой силе":
            stop sound
            $ MainMenu(confirm=False)()