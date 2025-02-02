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

    play sound "lush/plankton-augh.mp3" volume 0.5
    unknown ""
    stop sound

    maks "Че это за звуки, парни?"

    play sound "lush/imagine-v-spb.ogg" volume 0.65
    unknown ""
    stop sound

    maks "Игорь, прижмись поплотнее к унитазу"

    play sound "lush/brat-ti-zaebal-ignorit.mp3"
    lush ""
    stop sound

    maks "Не могу поверить"
    maks "Я о таком только читал"
    maks "Существуют условия, в которых отрицательно заряженный фрик и положительно заряженный фрик могут установить квантово-жопную связь"
    maks "Не могу поверить"

    play sound "lush/eto-kakaya-to-huinya.ogg"
    lush ""
    stop sound

    maks "Возможно, это наш шанс"
    maks "Думаю, до Люша не доберется угроза и нам нужно к нему"
    igoryas "Я не хочу в гейропу курить жирный черный член

    play sound "lush/snesli-dom.ogg"
    lush ""
    stop sound

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
           miha "Не буду я твою херню смотреть"
        "Че там у тебя":
            play music "./audio/soundtrack5.mp3" volume 0.3
            python:
                party.deleteMember(igoryas_unit)
            hide creep
            show igoryas_join_zheka with Dissolve(.5)
            igoryas "ыхыхыхыхыхых"
            igoryas "Слушайте"
            igoryas "Здесь вообще капееец"
            igoryas "Идите сюда скорей"
            menu:
                "Атаковать обоих":
                    miha "Не будем мы вашу хероту смотреть"
                "Ладно, че там у вас":
                    call yandex_virus_death

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