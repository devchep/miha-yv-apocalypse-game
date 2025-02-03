label prison:
    stop music
    play audio 'audio/lamps.mp3'
    scene cageinside
    show tanya2
    play sound 'audio/cageclose.mp3'
    pause 1
    show cage
    tanya 'Вот, посиди, подумай над своим поведением'
    miha '...'
    miha 'А что на ужин?'
    hide tanya2
    tanya 'Не знаю'
    miha '...'
    miha '...'
    miha 'Мдаа в тюряге в ВК оно как-то интереснее было'
    miha 'Начаааальник, когда ужин у нас?'
    play audio 'audio/prison_maximus.mp3'
    pause 2
    hide cage
    show maximus_alt
    show cage
    maximus 'Ну здравствуй'
    miha 'ТЫ?'
    maximus 'Я'
    miha 'Ну конечно же'
    maximus 'Хаха, какая ирония, Миха'
    maximus "Базовая человеческая потребность - делиться чем-то приятным глазу оборачивается трагедией, разделяющей общество"
    miha 'Что ты сделал с Таней?'
    maximus "Не перебивай, про неё речи не идёт"
    maximus "Ты, вероятно, думаешь: злодей снова раскрывает свой замысел - как это банально..."
    maximus "Но я исключением не стану"
    maximus "Более того, кто здесь злодей - вопрос открытый"
    maximus "Ведь моя маленькая затея лишь немного ускорит естественный отбор"
    maximus "Каждый волен решать сам: остаться в мире живых и среди избранных или расщепиться"
    maximus "Раз уж вы так любите делиться..."
    play audio 'audio/maximus_laugh.mp3'
    pause 4
    maximus 'Довольно'
    maximus "Пришло время определиться - избранный или мертвый"
    menu:
        "Ты жалок, пришел ко мне на свидание в обезьянник...":
            python:
                maximus_friend = False
            miha 'Рассказываешь мне свои байки'
            miha "Ничего ты не понимаешь"
            miha 'Сила не в том, чтобы избавиться от слабых'
            miha 'А в принятии'
            miha 'Уходи, не надейся, что я попрошу подробностей твоих безумных хобби'
            maximus 'Пустая трата времени, чтож, тогда по плохому'
        "Допустим ты меня заинтересовал":
            python:
                maximus_friend = True
            maximus 'Отлично, в таком случае мне нужна маленькая услуга'
            maximus "Чтобы оказаться среди избранных, мне нужна твоя кровь, отданная добровольно"
            miha "Сколько тебе нужно?"
            maximus 'Как комарик укусит'
            stop sound
            stop music
            play audio 'audio/concussion.mp3' volume 0.1
            pause 2
            play audio 'lush/plankton-augh.mp3' volume 0.1
            scene prison_ceiling with Dissolve(1)
            scene black with Dissolve(1)
            scene prison_ceiling with Dissolve(1)
            scene black with Dissolve(1)
            scene podval_maximus1 with Dissolve(1)
            scene black with Dissolve(1)
            scene podval_maximus2 with Dissolve(1)
            stop audio
            scene black with Dissolve(1)
            play music 'audio/maximus_palace.mp3'
            scene ptrg_upper with Dissolve(1)
            show maximus_alt at left
            maximus 'Ну вот, я же говорил'
            image maximus_postsplit = Movie(play = "./video/maximus_postsplit.webm", loop=True)
            show maximus_postsplit
            pause 60








