label igoryas_saved:
    maks "Быстро, идем"
    maks "Осталось мало времени"
    maks "Нужно спецназом залетать в туалет"
    scene srat_komnata with Dissolve(.5)
    show igor_shok
    igoryas "уф"
    igoryas "поехали"
    python:
        hide_all_igoryas()
    show igor_shok_s_telef
    igoryas "сегодня смотрим этот самый"
    igoryas "новую хуйню"
    maks "А ну-ка нахуй"
    play audio "audio/punch.opus"
    with vpunch
    play sound "audio/phone-drop.mp3"
    python:
        hide_all_igoryas()
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
            python:
                hide_all_igoryas()
            show igor_v_govne
            igoryas ")"

    play sound "lush/plankton-augh.mp3" volume 0.5
    unknown ""
    stop sound

    stop music fadeout 5.0
    play music "audio/lush_ambient.mp3" volume 0.02 fadein 10.0 

    maks "Че это за звуки, парни?"

    play sound "lush/imagine-v-spb.ogg" volume 0.3
    unknown ""
    stop sound

    python:
        hide_all_max()
    show max3 at right
    maks "Игорь, прижмись поплотнее к унитазу"

    python:
        hide_all_igoryas()
    show igor_wc_1
    play sound "lush/brat-ti-zaebal-ignorit.mp3"
    lush ""
    stop sound

    python:
        hide_all_max()
    show max4 at right
    maks "Не могу поверить"
    maks "Я о таком только читал"
    maks "Существуют условия, в которых отрицательно заряженный фрик и положительно заряженный фрик могут установить квантово-жопную связь"
    maks "Не могу поверить..."

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

    python:
        hide_all_max()
    show max2 at right
    maks "Дура ты... Нам нужна твоя помощь"
    # не понимаю   | che za dich
    play sound "characters/lesh/lush-che-za-dich.ogg" volume 3
    lush ""
    stop sound

    maks "Мих, помоги, пожалуйста, я не могу"

    python:
        hide_all_lush()
    show lush3 at left

    miha "Появился новый вирус, распространяется очень быстро, нам бы свалить побыстрее, пока есть возможность"
    # eбать ты мне сюжет новой планеты обезьян рассказываешь ? suzhet
    play sound "characters/lesh/lush-suzhet-planeti-obezhan.ogg" volume 2
    lush ""
    stop sound
    
    miha "Нет"
    miha "Люди смотрят короткие видео на платформе Яндекс.Вирус"
    miha "И они очень странно себя ведут, почти как зондбе"
    # чел ну ты понимаешь с какими дегенератами мы живем на одной планете это абсурд это цирк | lush-degenerati
    python:
        hide_all_lush()
    show lush4 at left
    play sound "characters/lesh/lush-degenerati.ogg"
    lush ""
    stop sound
    
    python:
        hide_all_lush()
    show lush7 at left
    play sound "characters/lesh/from-vk/1.ogg"
    lush ""
    stop sound
    
    miha "..."
    miha "Яндекс вообще кажется захватывает все вокруг"
    miha "Cкоро будут Яндекс.Жена Яндекс.Срать Яндекс.Все-вообще"
    # так и шли бы работать в яндекс доставку
    # чето я хуйню сказал
    python:
        hide_all_lush()
    show lush1 at left
    play sound "characters/lesh/lush-poshel-bi-v-yandex-full.ogg" volume 4
    lush ""
    stop sound
    
    python:
        hide_all_lush()
    show lush3 at left
    play sound "characters/lesh/lush-mb-huinyu-skazal.ogg" volume 4
    lush ""
    stop sound

    maks "СТЕПА!! ЭТО НЕ ШУТКИ"
    maks "Я не могу объяснять детали, но когда начнется, то, что начнется..."
    maks "Ты уже не будешь так радоваться"
    # страшно стало после твоих слов ( kogda nachnets)
    python:
        hide_all_lush()
    show lush4 at left
    play sound "characters/lesh/lush-kogda-nachnetsa.ogg" volume 11
    lush ""
    stop sound

    # чьих это рук дело
    python:
        hide_all_lush()
    show lush7 at left
    play sound "characters/lesh/lush-chix-ruk-eto-delo-cut.mp3" volume 3
    lush ""
    stop sound

    # степа мы в опасности, нам нужно сваливать
    python:
        hide_all_max()
    show max_happy at right
    maks "Я рад, что мне не пришлось для вас все разжевывать"
    maks "И рисковать своей жизнью"
    maks "А ты наконец-то меня понял"
    maks "Поможешь нам?"

    # puk + smex
    python:
        hide_all_lush()
    show lush1 at left
    play sound "characters/lesh/from-vk/puk.mp3" volume 8
    lush ""
    stop sound
    python:
        hide_all_lush()
    show lush3 at left
    play sound "characters/lesh/from-vk/2.mp3" volume 2
    lush ""
    stop sound
    play sound "characters/lesh/from-vk/5.ogg" volume 2
    lush ""
    stop sound

    python:
        hide_all_max()
    show max_angry at right
    maks "Только мне стоило подумать, что ты в адеквате"
    maks "Сегодня у Михи вообще-то дэрэ"
    maks "Можно же один день себя вести нормаль-"

    with vpunch
    play audio "audio/punch.opus"
    hide lush1
    python:
        hide_all_igoryas()
    python:
        hide_all_max()
    python:
        hide_all_lush()
    show lush_s_dr at left
    show igor_s_dr at right
    unknown ""

    maks "..."

    python:
        hide_all_lush()
    show lush2 at left
    play sound "characters/lesh/lush-tyzhechka-za-tebya.ogg" volume 3
    lush ""
    stop sound

    python:
        hide_all_igoryas()
    show max2 at right
    maks "У нас не так много времени"

    python:
        hide_all_igoryas()
        hide_all_max()
    show igor_ne_hochet at right
    igoryas "Я понимаю, что дела так себе, но я не хочу в гейропу курить жирный черный член"

    python:
        hide_all_lush()
    show lush_wc_1 at left
    play sound "lush/snesli-dom.ogg" volume 5
    lush ""
    stop sound

    python:
        hide_all_igoryas()
        hide_all_max()
    show max_happy at right
    maks "Я рад, что ты за"
    maks "Давай мы съебем к тебе, в турецкие страны"
    
    # какие турецкие брат, я в сербии
    # lush-ya-v-serbii.ogg
    python:
        hide_all_lush()
    show lush1 at left
    play sound "characters/lesh/lush-ya-v-serbii.ogg" volume 4
    lush ""
    stop sound
    
    python:
        hide_all_max()
    show max3 at right
    python:
        hide_all_max()
    show max4 at right
    maks "Да, я так и сказал"
    maks "У тебя там безопасно? Мы можем приехать?"
    # там это где, это у кого
    # lush-tam-eto-gde.ogg
    python:
        hide_all_lush()
    show lush3 at left
    play sound "characters/lesh/lush-tam-eto-gde.ogg" volume 4
    lush ""
    stop sound

    python:
        hide_all_max()
    show max_angry at right
    maks "Молодец, хорош прям"

    python:
        hide_all_lush()
    show lush4 at left
    play sound "characters/lesh/from-vk/8.mp3" volume 3
    lush ""
    stop sound

    # а че не пон, план какой-то есть
    # lush-plan-est.ogg
    python:
        hide_all_lush()
    show lush7 at left
    play sound "characters/lesh/lush-plan-est.ogg" volume 3
    lush ""
    stop sound

    python:
        hide_all_max()
    show max4 at right
    maks "Степа, я правильно понимаю, что нас в гейропу просто так не пуcтят?"
    maks "Из-за, так сказать, запрета на импорт российского газа"

    python:
        hide_all_lush()
    show lush1 at left
    play sound "characters/lesh/lush-super-ochevidno.ogg" volume 6
    lush ""
    stop sound

    python:
        hide_all_max()
    show max2 at right
    maks "То есть нам нужно избавиться от газа, чтобы нас пропустили?"
    maks "Можешь объяснить, как это сделать?"

    python:
        hide_all_lush()
    show lush3 at left
    play sound "characters/lesh/lush-sha-content.ogg" volume 4
    lush ""
    stop sound

    python:
        hide_all_lush()
    show lush3 at left
    play sound "characters/lesh/lush-viglyadit-uzhasno.ogg" volume 4
    lush ""
    stop sound

    image zakl = Movie(play = "./video/zaklinanie.webm", loop=False, zoom=0.9)
    show zakl at left
    pause(357)
    
    hide zakl
    python:
        hide_all_lush()
    show lush_wc_2 at left
    play sound "characters/lesh/lush-ya-dumal-mne-pizda-VEED.mp3" volume 2
    lush ""
    stop sound

    python:
        hide_all_igoryas()
    show igor_dovolen:
        xalign 0.55
        yalign -0.2
    igoryas "Охуеть дружище!"

    python:
        hide_all_max()
    show maxsit at right
    maks "Охуеть дружище..."

    igoryas "Делаем парни"

    python:
        hide_all_max()
    show max_angry at right
    maks "Да всмысле"

    menu:
        "Ладно, сделаем это быстро":
            python:
                hide_all_lush()
            show lush1 at left
            play sound "characters/lesh/lush-nado-delat-full-VEED.mp3" volume 3
            lush ""
            stop sound

            python:
                hide_all_max()
            show max2 at right
            maks "Наебом пахнет..."

            python:
                hide_all_lush()
            show lush_wc_1  at left
            play sound "characters/lesh/lush-tak-ne-govori.ogg" volume 1.3
            lush ""
            stop sound

            scene black with Dissolve(1)
            menu:
                "Предать огню российский газ":
                    pass
            scene srat_komnata with Dissolve(1)

            miha "Фух"

            show lush7 at left
            play sound "characters/lesh/lush-brat-perdish.ogg" volume 4
            lush ""
            stop sound

            show igor_pretty
            igoryas "Норм"
            show maxsit at right
            maks "Забыли"

            python:
                hide_all_lush()
            show lush_wc_2 at left
            play sound "characters/lesh/lush-v-golos1.ogg" volume 4
            lush ""
            stop sound

            python:
                hide_all_lush()
            show lush7 at left
            play sound "characters/lesh/lush-v-golos-s-klounov.ogg" volume 3 
            lush ""
            stop sound

            play sound "characters/lesh/lush-legendarniy-moment.ogg" volume 2 
            lush ""
            stop sound

            python:
                hide_all_max()
            show max1 at right
            maks "Степ, мы готовы теперь лететь к тебе?"

            python:
                hide_all_lush()
            show lush1 at left
            play sound "characters/lesh/lush-prohodit-VEED.mp3" volume 5
            lush ""
            stop sound

            python:
                hide_all_igoryas()
            show igor_ne_hochet
            igoryas "Я боюсь летать"
            igoryas "Может на электричке?"

            maks "Такой риск может нам дорого обойтись"

            python:
                hide_all_lush()
            show lush_wc_2 at left
            play sound "characters/lesh/lush-bilet-tuda-obratno.ogg" volume 3
            lush ""
            stop sound

            python:
                hide_all_max()
            show max2 at right
            maks "Да не в прямом же смысле"

            python:
                hide_all_lush()
            show lush3 at left
            play sound "characters/lesh/from-vk/5.ogg" volume 4
            lush ""
            stop sound

            python:
                hide_all_igoryas()
            show igor_pretty
            igoryas "До ближайшей элки 3 часа"

            maks "Можем Димана успеть захватить с собой"

            python:
                hide_all_lush()
            show lush4 at left
            play sound "characters/lesh/lush-nixuya-ti-pridumal.ogg" volume 4
            lush ""
            stop sound

            python:
                hide_all_lush()
            show lush7 at left
            play sound "characters/lesh/lush-anti-diman.ogg" volume 3 
            lush ""
            stop sound


            python:
                hide_all_max()
            show max_angry at right
            maks "Тебя вообще кто спросил"

            python:
                hide_all_lush()
            show lush3 at left
            play sound "characters/lesh/lush-zachem.ogg" volume 3
            lush ""
            stop sound

            python:
                hide_all_igoryas()
            show igor_wc_2
            igoryas "За Диманами реально не успеем, он работает сейчас наверно"
            igoryas "Го за Древом, может реально выйдет"
            maks "))"
            miha "))"

            python:
                hide_all_lush()
            show lush7 at left
            play sound "characters/lesh/from-vk/10.ogg" volume 3
            lush ""
            stop sound

            python:
                hide_all_max()
            show max1 at right

            python:
                isZakl = True
            pass
        "Ты ебанутый, живи дальше в своем унитазе, у нас есть дела поважнее":
            python:
                hide_all_igoryas()
            show igor_wc_2

            play sound "characters/lesh/lush-xuesosi.ogg" volume 1.5
            lush ""
            stop sound
            
            python:
                hide_all_lush()

            play sound "characters/lesh/lush-men-v-tilte.ogg" volume 1
            lush ""
            stop sound

            python:
                hide_all_max()
            show max_happy at right
            maks "Найс, Мих"

            python:
                isZakl = False
            
            pass

    maks "Муваем"
        

    python:
        igoryas_unit = Igoryas(80, 6)
        party.addMember(igoryas_unit)
