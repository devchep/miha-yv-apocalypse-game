label igoryas_saved:
    maks "Быстро, идем"
    maks "Осталось мало времени"
    maks "Нужно спецназом залетать в туалет"
    scene srat_komnata with Dissolve(.5)
    show igor_shok
    igoryas "уф"
    igoryas "поехали"
    hide igor_shok
    show igor_shok_s_telef
    igoryas "сегодня смотрим этот самый"
    igoryas "новую хуйню"
    maks "А ну-ка нахуй"
    play audio "audio/punch.opus"
    with vpunch
    play sound "audio/phone-drop.mp3"
    hide igor_shok_s_telef
    show igor_shok
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
            hide igor_shok
            show igor_v_govne
            igoryas ")"

    play sound "lush/plankton-augh.mp3" volume 0.5
    unknown ""
    stop sound

    stop music fadeout 5.0
    play music "audio/lush_ambient.mp3" volume 0.02 fadein 10.0 

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

    maks "Степа?! Это ты?! Ответь что-нибудь!"

    show lush1 at left

    # puk
    play sound "characters/lesh/lush-puk.ogg"
    lush ""
    stop sound
    # smex
    play sound "characters/lesh/lush-smeh.ogg"
    lush ""
    stop sound

    maks "Дура ты... Нам нужна твоя помощь"
    # не понимаю   | che za dich
    play sound "characters/lesh/lush-che-za-dich.ogg" volume 3
    lush ""
    stop sound

    maks "Мих, помоги, пожалуйста, я не могу"

    # миха объясняет
    miha "Появился новый вирус, распространяется очень быстро, нам бы свалить побыстрее, пока есть возможность"
    # eбать ты мне сюжет новой планеты обезьян рассказываешь ? suzhet
    play sound "characters/lesh/lush-suzhet-planeti-obezhan.ogg" volume 2
    lush ""
    stop sound
    
    miha "Нет"
    miha "Люди смотрят короткие видео на платформе Яндекс.Вирус"
    miha "И они очень странно себя ведут, почти как зондбе"
    # чел ну ты понимаешь с какими дегенератами мы живем на одной планете это абсурд это цирк | lush-degenerati
    play sound "characters/lesh/lush-degenerati.ogg"
    lush ""
    stop sound
    # TODO: пук vk
    # TODO: смех vk
    play sound "characters/lesh/from-vk/1.ogg"
    lush ""
    stop sound
    
    miha "..."
    miha "Яндекс вообще кажется захватывает все вокруг"
    miha "Cкоро будут Яндекс.Жена Яндекс.Срать Яндекс.Все-вообще"
    # так и шли бы работать в яндекс доставку
    # чето я хуйню сказал
    play sound "characters/lesh/lush-poshel-bi-v-yandex-full.ogg" volume 4
    lush ""
    stop sound
    
    play sound "characters/lesh/lush-mb-huinyu-skazal.ogg" volume 4
    lush ""
    stop sound

    maks "СТЕПА!! ЭТО НЕ ШУТКИ"
    maks "Я не могу объяснять детали, но когда начнется, то, что начнется..."
    maks "Ты уже не будешь так радоваться"
    # страшно стало после твоих слов ( kogda nachnets)
    play sound "characters/lesh/lush-kogda-nachnetsa.ogg" volume 11
    lush ""
    stop sound

    # чьих это рук дело
    play sound "characters/lesh/lush-chix-ruk-eto-delo-cut.mp3" volume 3
    lush ""
    stop sound

    # степа мы в опасности, нам нужно сваливать
    maks "Я рад, что мне не пришлось для вас все разжевывать"
    maks "И рисковать своей жизнью"
    maks "А ты наконец-то меня понял"
    maks "Поможешь нам?"

    # puk + smex
    play sound "characters/lesh/from-vk/puk.mp3" volume 8
    lush ""
    stop sound
    play sound "characters/lesh/from-vk/2.mp3" volume 2
    lush ""
    stop sound
    play sound "characters/lesh/from-vk/5.ogg" volume 2
    lush ""
    stop sound

    maks "Только мне стоило подумать, что ты в адеквате"
    maks "Сегодня у Михи вообще-то дэрэ"
    maks "Можно же один день себя вести нормаль-"

    with vpunch
    play audio "audio/punch.opus"
    hide lush1
    hide igor_v_govne
    hide max1
    show lush_s_dr at left
    show igor_s_dr at right
    unknown ""

    maks "..."

    play sound "characters/lesh/lush-tyzhechka-za-tebya.ogg"
    lush ""
    stop sound

    maks "У нас не так много времени"
    igoryas "Я понимаю, что дела так себе, но я не хочу в гейропу курить жирный черный член"

    play sound "lush/snesli-dom.ogg"
    lush ""
    stop sound

    # hide 

    python:
        igoryas_unit = Igoryas(80, 6)
        party.addMember(igoryas_unit)



# TODO: мб вернуть это
    # hide max1
    # show igor1 at left
    # igoryas "Забыли"
    # igoryas "Важно другое"
    # igoryas "Ты мне должен новый пиксель, Максон"
    # igoryas "Мб объяснишь че это было в туалете?"
    # hide igor1
    # show max1 at right
    # miha "Да, реально"
    # maks "Сейчас не могу вам ничего сказать, нужно бежать за Андревом"
    # Затар жижки