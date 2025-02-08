label path_to_maximus:

    play music "./audio/heavyrain.mp3" volume 0.5
    play audio "./audio/maximus_path.mp3" volume 0.3
    scene path_to_maximus1 with Dissolve(.5)
    if party.contains(MaxHeyman):
        show max1:
            xalign 0.25
            yalign 0.85
        maks "Там, в холле дворца, он не мог нас не заметить"
        maks "Это точно спланировано"
        maks "Нам нельзя идти дальше"
        maks "Это гроб"
        miha "И что ты предлагаешь"
        miha "Не идти за Максимусом, сьебаться в гейропу нюхать пуки Люша?"
        maks "..."
        hide max1

    "Пробираясь сквозь ливень, мрак, скверну"
    "Мы видели десятки тысяч зараженных вирусом людей"
    "Еще больше - впавших в Яндекс.Дзен"
    scene path_to_maximus2 with Dissolve(.2)
    "Мы приближались к логову Максимуса"
    if party.contains(Drei):
        show drei1 at left
        andrei "Слушай, я тут знаешь о чем подумал"
        andrei "Если Максимус полная противоположность Максона"
        andrei "То если Максон - человек"
        andrei "Максимус..."
        hide drei1

    "Всю дорогу далее мы молчали"

    scene black with Dissolve(.2)

    miha "Что это?"
    play music "./audio/maximus_theme2.mp3" volume 0.5
    "Вы увидели впереди огромные, наполненные энергией красные врата"
    scene gates1 with Dissolve(.2)
    "Будто ведущие пряником в ад"
    "Увидев их, мы поняли, что все преграды до них"
    "Были самой простой частью нашего пути"
    scene gates_lomo with Dissolve(.2)
    "Смотря на них, зная, что за ними"
    "Нас разрывало от ужаса"
    "Сильнейшего, непреодолимого желания убежать"
    miha "Мы проделали весь этот путь"
    miha "Чтобы встретить его"
    miha "Я боюсь"
    miha "Ебать как сильно"
    menu:
        "Войти во врата":
            pass

    stop audio
    scene gates_enter with Dissolve(.2)
    call maximus_fight
