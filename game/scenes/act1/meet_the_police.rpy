label meet_the_police:
    stop music
    play sound "audio/siren_coming.mp3"
    scene police_car_incoming
    play music 'audio/fuck_da_police.mp3' volume 0.01
    miha "Черт, только этого мне сейчас не хватало, один раз в жизни вышел на улицу с пистолетом и естееественно меня застопит бобик"
    stop sound
    scene police_car_parked
    miha 'Это что?! Синчина?'
    play audio "audio/car_door.mp3"
    pause 1
    show tanya1
    miha 'Аня, привет, не знал, что ты теперь в органах!'
    tanya 'Здравия желаю, капитан полиции Линчина Татьяна, не Аня, предъявите документы и покажите содержимое рюкзака'
    menu:
        "Наглый подкат":
            python:
                tanya_friend = True
            miha 'Одна тут патрулируешь?)'
            miha 'Как же так, капитан и без напарника?) Прикрыть тебе спину?) У меня и ствол с собой есть)'
            tanya 'Хих, ну мне действительно не помешает напарник' 
            tanya 'К тому же, видно, что ты хороший парень, про ствол смешно придумал.'
            tanya 'Я вообще тебя обыскать решила как предлог диалог завязать) Садись, будешь мигалку включать'
            pass
        "Сыграть дурачка":
            python:
                tanya_friend = False
            pass
            miha 'Капитан, понимаете, паспорт дома забыл, а рюкзака у меня и нет вовсе'
            tanya 'Ка'
            miha 'Что?)'
            tanya 'Капитан'
            miha 'Ну да, капитан, я же так и сказал'
            tanya 'Капитанка'
            tanya 'Как же нет рюкзака, а то что у вас за спиной?'
            miha 'У меня на спине глаз нет'
            tanya 'Понятно, повернитесь спиной ко мне'
            play sound 'audio/handcuffs.mp3'
            'На тебя надели наручники'
            stop sound
            play sound 'audio/backpack_check.mp3'
            "Таня обыскивает рюкзак"
            stop sound
            tanya 'Ооо, ну это точно в отделение'
    stop music
    hide tanya1
    play audio 'audio/car_door.mp3'
    pause 1.5
    play audio 'audio/car_door.mp3'
    pause 2
    scene police_car_inside1
    play sound 'audio/radio_switch.mp3' volume 0.5
    pause 2
    play music 'audio/cranberries_zombie.mp3' volume 0.2
    miha 'Ты всегда хотела работать в полиции?'
    if tanya_friend:
        scene police_car_inside3 
        tanya 'Психолог говорит, что у меня обостренное чувство справедливости'
        tanya 'Думает это связано с тем, что мама била папу'
        tanya 'Поэтому мне с детства нравится приструнять хулиганов'
        tanya 'Даже в школе я всегда была старостой класса, хотя это не самая благодарная работа'
        miha 'Черт, ты наверное хорошая полицейская'
        tanya 'Бываю и плохой)'
    else: 
        tanya 'Это к делу не относится. Не отвлекайте от дороги'
    play sound 'audio/avaria.mp3'
    scene jekan_accident
    pause 2
    play sound 'audio/na_kapot.mp3'
    miha 'Блять!'
    tanya 'Ебать!'
    scene police_car_inside4
    tanya 'Да откуда он выскочил?!'
    miha 'Справа'
    stop music
    play audio 'audio/car_door.mp3'
    pause 1.5
    play audio 'audio/car_door.mp3'
    play audio 'audio/street_sound.mp3' volume 0.1
    play music 'audio/saw_ambient.mp3' volume 0.06
    scene look_at_jekan
    show tanyaback at left
    tanya "Какой кошмар"
    miha "Не спеши расстраиваться"
    miha "Мне кажется я знаю в чем причина"
    miha "Видишь? У него телефон"
    tanya 'Я думала на телефон всё сваливают только родители...'
    miha "Да, но тут все сложнее, поверь мне"
    miha "Многие люди ведут себя странно в последнее время, не замечала?"
    miha "Встречала ли ты тех, кто навязчиво тыкал в тебя своим телефоном?"
    tanya 'Пара фриков попадалась сегодня, но это часть работы'
    miha 'Это не просто фрики, это зараженные Яндекс.Вирусом, не слышала про такой?'
    tanya 'Нет'
    miha 'Это по сути новый тикток, но если посмотрел хотя бы одно видео, то нормальным ты больше не станешь'
    if tanya_friend:
        tanya "Получается, что рано или поздно от них будет не скрыться?"
        miha 'Боюсь, что да...'
        tanya 'Что же нам делать? Мне доложить начальству?'
        miha 'Скорее всего вирус проник во все слои общества, в том числе и во властную верхушку'
        miha 'Думаю мы в такой пизде, что нужно искать безопасное место'
        miha 'Если Яндекс.Вирус заменил тикток у нас...'
        miha 'Значит нам нужно туда, где тикток не уходил'
        tanya "Например?"
        miha 'Да по сути любая страна, кроме США, подойдет'
        miha 'Монголия. Вдруг там вообще интернета нет'
        miha 'Попробовать стоит'
        miha "Ты со мной?"
        tanya 'Да, похоже ты знаешь явно больше меня, напарник'
        stop music
    else:
        tanya 'Хаха и много кто в это поверил?'
        tanya 'Не еби мозга, у меня итак денек веселый намечается, даже если у этого еще пульс есть'
        tanya 'Надеюсь скорая быстро приедет'
        tanya 'Но мы с тобой все равно едем оформляться'
        stop music
        call prison
