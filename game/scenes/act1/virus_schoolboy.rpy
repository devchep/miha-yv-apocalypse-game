label virus_schoolboy:
    play audio 'audio/birds_tweet.mp3'
    scene homeoutside
    pause 3
    play music 'audio/sigmaboy.mp3' volume 0.05 fadein 1
    boy 'Эй Эй Эй'
    boy 'Стой стой стой'
    boy 'Смари смари смари'
    miha 'Не хочу, отстань'
    boy 'Слышь бля, а ну-ка быстро посмотрел сюда'
    menu:
        'Я же СКА ЗАЛ - НЕ ХОЧУ (выстрелить)':
            show gun at right
            pause 2
            boy 'Ну давай давай, боюсь прям'
            play music 'audio/birdsaftershot.mp3'
            pause 3
            scene black with Dissolve(3)
            stop music
            call meet_the_police
        'О господи, ну что там у тебя':
            call yandex_virus_death

