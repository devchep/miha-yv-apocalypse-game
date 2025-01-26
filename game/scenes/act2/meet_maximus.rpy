label meet_maximus:

    play music "./audio/heavyrain.mp3" volume 0.5
    scene maximus_path2 with Dissolve(.5)
    "Всю дорогу до Максимуса мы молчали"
    "Мы все знали, что Максимус спокойно мог нас найти сам"
    "Но он верно хотел чтобы мы истощились"
    "Путь был невыносим, мучителен"
    "Проклят"
    scene maximus_path3 with Dissolve(.2)
    "Пробираясь сквозь мрак, ливень"
    "Мы видели десятки тысяч зараженных вирусом людей"
#     scene maximus_path4 with Dissolve(.2)
    "Еще больше - впавших в Яндекс.Дзен"
    "Мы дошли к вратам"
    play music "./audio/maximus_theme2.mp3" volume 0.5
    "Увидев их, мы поняли, что все преграды до них"
    scene gates1 with Dissolve(.2)
    "Были самой простой частью нашего пути"
    scene gates2 with Dissolve(.2)
    "Смотря на них, зная, что за ними"
    "Нас разрывало от ужаса"
    "Сильнейшего, неизбежного желания убежать"
    miha "Мы проделали этот путь"
    miha "Чтобы встретить его"
    miha "Я боюсь"
    miha "Ебать как сильно"
    menu:
        "Войти во врата":
            pass

    call maximus_fight
