label meet_the_police:
    play audio "audio/siren_coming.mp3"
    scene police_car_incoming
    miha "Черт, только этого мне сейчас не хватало, один раз в жизни вышел на улицу с пистолетом и естееественно меня застопит бобик"
    scene police_car_parked
    miha 'Это что?! Синчина?'
    play audio "audio/car_door.mp3"
    show tanya1
    miha 'Аня, привет, не знал, что ты теперь в органах!'
    tanya 'Здравия желаю, капитан полиции Линчина Татьяна, не Аня, предъявите документы и покажите содержимое рюкзака'
    menu:
        "Наглый подкат":
            tanya_friend = True
            pass
        "Сыграть дурачка":
            tanya_friend = False
            pass
    if tanya_friend == True:
        miha 'Как же так, капитан и без напарника?) Прикрыть тебе спину?) У меня и ствол с собой есть)'
        tanya 'Хих, ну мне действительно не помешает напарник, к тому же, видно, что ты хороший парень, про ствол смешно придумал. Я вообще тебя обыскать решила, потому что нужен был предлог диалог завязать) Садись, будешь мигалку включать'
    else:
        miha 'Капитан, понимаете, паспорт дома забыл, а рюкзака у меня и нет вовсе'
        tanya 'Ка'
        miha 'Что?)'
        tanya 'Капитан'
        miha 'Ну да, капитан, я же так и сказал'
        tanya 'Капитанка'
        tanya 'Как же нет рюкзака, а то что у вас за спиной?'
        miha 'У меня на спине глаз нет'
        tanya 'Понятно, повернитесь спиной ко мне'
        play audio 'audio/handcuffs.mp3'
        'На тебя надели наручники'
        play audio 'audio/backpack_check.mp3'
        "Таня обыскивает рюкзак"
        tanya 'Ооо, ну это точно в отделение'
    hide tanya1
    play audio 'audio/car_door.mp3'
    pause 1
    play audio 'audio/car_door.mp3'
    scene police_car_inside1
    play audio 'audio/radio_switch.mp3'
    play audio 'audio/cranberries_zombie.mp3'
    miha 'Ты всегда хотела работать в полиции?'
    if tanya_friend == True:
        scene police_car_inside3 
        tanya 'Да, я даже в школе была старостой, тогда я окончательно убедилась'
    else tanya 'Это к делу не относится. Не отвлекайте от дороги'
    play sound 'audio/avaria.mp3'
    scene jekan_accident
    pause 2.5
    play sound 'audio/na_kapot.mp3'
    miha 'Блять!'
    tanya 'Ебать!'