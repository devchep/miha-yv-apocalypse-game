transform end_of_hall_right:
    xalign 0.6
    yalign 0.59

label meet_maximus:

    menu:
        "Войти":
            pass
    play music "./audio/meet_maximus.mp3" volume 0.5
    scene maximus_hall with Dissolve(.5)
    show maximus_smol at end_of_hall_right
    maximus "{b}Ты же помнишь {color=#f00}уговор{/color}{/b}"
    "кто-то: мы уже заразили 97\% населения, все будет сделано в срок, я Вас уверяю!"
    show gera_cautious at right
    gera "Товарищи"
    gera "Тихо, прячемся"
    hide gera_cautious
    miha "Ну конечно, Максимус"
    show gera_cautious at right
    gera "Тссс"
    hide gera_cautious
    menu:
        "Спрятаться":
            pass
        "Выйти на похуй на Максимуса":
            "не лучший мув)"

    maximus "{b}Эх, последний ящик на сегодня{/b}"
    maximus "{b}Даже немного жалко на такое {color=#f00}ничтожество{/color}{/b}"
    maximus "{b}Давай, Сайонара{/b}"
