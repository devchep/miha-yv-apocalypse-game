label igoryas_saved:
    maks "Быстро, идем"
    maks "Осталось мало времени"
    maks "Нужно спецназом залетать в туалет"
    scene srat_komnata with Dissolve(.5)
    show igor_sret1
    igoryas "уф"
    igoryas "поехали"
    hide igor_sret1
    show igor_sret_s_telefonom
    igoryas "сегодня смотрим этот самый"
    igoryas "новую хуйню"
    maks "А ну-ка нахуй"
    play audio "audio/punch.opus"
    with vpunch
    play sound "audio/phone-drop.mp3"
    hide igor_sret_s_telefonom
    show igor_sret1
    igoryas "йэ бляяять"
    igoryas "Максооон это че было"
    show max1 at right
    maks "Слава богу мы тебя спасли дружище"
    maks "Идем с нами скорее"
    maks "Только подотрись"
    menu:
        "Здарова Гаряс":
            call dab_up
            miha "Э"
            miha "А руки помыл?"
            igoryas ")"

    python:
        igoryas_unit = Igoryas(80, 6)
        party.addMember(igoryas_unit)

    scene alexandrovskaya with Dissolve(.5)
    show max1 at right
    maks "Ладно, гайзы"
    maks "Нам следуе"
    stop music
    play sound "audio/subway-surfers.mp3" volume 0.2
    pause 1
    stop sound
    maks "Блядь"
    play sound "audio/subway-surfers.mp3" volume 0.1 loop
    maks "Гайс"
    maks "Кто-то из них идет"
    hide max1
    show creep at left
    creep "Че"
    creep "стоите?"

    show max1 at right
    maks "Ни в коем случае не смотрите что он вам покажет"
    hide max1

    creep "Тут капец вообще"
    creep "Смотрите"
    stop sound

    menu:
        "Атаковать":
            call zheka_fight
            hide creep
            play music "./audio/soundtrack5.mp3" volume 0.3
            show max1 at right
            maks "Надеюсь мы его не кокнули"
            maks "Нас же повяжут"
            maks "Мих, ты этим говном управлял"
            scene zhekan_dead with Dissolve(.5)
            miha "Слушай, по-моему с ним все нормально"
            menu:
                "Взять телефон Жекана":
                    call yandex_virus_death
                "Уйти":
                    pass
            hide max1
            show igor1 at left
            igoryas "Забыли"
            igoryas "Важно другое"
            igoryas "Ты мне должен новый пиксель, Максон"
            igoryas "Мб объяснишь че это было в туалете?"
            hide igor1
            show max1 at right
            miha "Да, реально"
            maks "Сейчас не могу вам ничего сказать, нужно бежать за Андревом"
            # Затар жижки

        "Че там у тебя":
            play music "./audio/soundtrack5.mp3" volume 0.3
            #TODO 1: -Игоряс
            "Проебали"
