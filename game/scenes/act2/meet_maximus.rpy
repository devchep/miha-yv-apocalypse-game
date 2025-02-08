transform hall_maximus_pos:
    xalign 0.55
    yalign 0.62
transform hall_zlodei_pos:
    xalign 0.45
    yalign 0.63
transform hall_hide_maximus_pos:
    xalign 0.85
    yalign 0.5
transform hall_hide_zlodei_pos:
    xalign 0.75
    yalign 0.51
transform hall_hide_yashik_pos:
    xalign 0.77
    yalign 0.51

image maximusPortal:
    "./images/sprites/maximus/maximus_portal1.png"
    0.2 #this part defines how long to wait before next frame
    "./images/sprites/maximus/maximus_portal2.png"
    0.3
    "./images/sprites/maximus/maximus_portal3.png"
    0.4
    "./images/sprites/maximus/maximus_portal4.png"
    0.3
    "./images/sprites/maximus/maximus_portal5.png"
    0.2

label meet_maximus:
    scene petergof with Dissolve(.5)
    miha "Мы тут"
    miha "Петергофский дворец"
    scene entrance1 with Dissolve(.5)
    menu:
        "Войти":
            pass
    play music "./audio/meet_maximus.mp3" volume 0.1
    scene maximus_hall with Dissolve(.5)
    show maximus_smol at hall_maximus_pos
    show zlodei1_smol at hall_zlodei_pos
    maximus "{b}Ты же помнишь {color=#f00}уговор{/color}{/b}"
    zlodei_1 "Мы уже заразили 97\% населения"
    zlodei_1 "Все будет сделано в срок, я Вас уверяю!"
    show gera_cautious at right
    gera "Товарищи"
    gera "Тихо"
    hide gera_cautious
    miha "Ну конечно, Максимус"
    show gera_cautious at right
    gera "Тссс, они нас не заметили"
    gera "Необходимо спрятаться"
    hide gera_cautious
    menu:
        "Спрятаться за колонну":
            hide maximus_smol
            hide zlodei1_smol
            pass
        "Поздороваться с Максимусом":
            hide maximus_smol
            play sound "audio/death-bong.mp3"
            show gera_scared at right with Dissolve(0.5)
            hide gera_scared with Dissolve(1.65)
            stop sound
            show maximus with Dissolve(.1)
            maximus '{b}Божечки{/b}'
            hide zlodei1_smol
            maximus '{b}Я чуть ли не потратил свой последний на сегодня ящик{/b}'
            maximus '{b}ББ ДАуничи{/b}'
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            play sound "audio/characters/maximus/yashik.mp3"
            play sound "audio/bigboom.mp3"
            scene yashik_death with flashbulb
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            with bigdamagepunch
            pause 1
            scene black
            show maximus with Dissolve(.1)
            maximus '{b}Какие же вы ничтожные{/b}'
            maximus '{b}САМИ{/b} пришли ко мне...'
            maximus 'На {b}что{/b} вы вообще рассчитывали?'
            maximus 'Но за {b}Яндекс.Доставку{/b} крови благодарю'
            maximus 'А сейчас прошу меня извинить, у меня планы'
            python:
                get_achievement("blya_derzhi_yashik", trans=achievement_transform)
            python:
                maximus_friend = False
            call maximus_palace_split
            return

    scene maximus_hall_hide
    show maximus_smol at hall_hide_maximus_pos
    show zlodei1_smol at hall_hide_zlodei_pos
    pause(0.8)
    maximus "{b}Надо же{/b}"
    maximus "{b}Последний ящик остался на сегодня{/b}"
    maximus "{b}Даже обидно тратить ящик на такое {color=#f00}ничтожество{/color}{/b}"
    zlodei_1 "Нет не надо пожалуйста все будет сделано"
    maximus "{b}Давай, Сайонара{/b}"
    play sound "audio/characters/maximus/yashik.mp3"
    pause(0.2)
    show yashik_smol at hall_hide_yashik_pos with flashbulb
    pause(1)
    maximus "{b}Почти все готово{/b}"
    maximus "{b}Не в срок, конечно, благодаря {color=#f00}бездарям{/color}{/b}"
    maximus "{b}Завтра Миха сделает выбор{/b}"
    maximus "{b}Надеюсь верный{/b}"

    hide maximus_smol
    play sound "audio/characters/maximus/portal_sound.mp3"
    show maximusPortal at hall_hide_maximus_pos
    pause(1.5)
    hide maximusPortal
    pause(0.5)
    play music "./audio/soundtrack_act2_hall.mp3" volume 0.5
    miha "Это был пиздец"
    miha "Что он имел в виду сделает выбор?"
    show gera1
    gera "Михаил, это наш шанс"
    gera "Максимус имеет Cool-Down на использование ящика"
    gera "Он восстановится лишь завтра"
    gera "Нам нужно отправиться в его логово прямо сейчас"
    miha "Отправиться в логово Максимуса не звучит как полный пиздец?"
    gera "Подтверждаю"
    gera "Но больше такого шанса не будет"
    menu:
        "В путь":
            call path_to_maximus