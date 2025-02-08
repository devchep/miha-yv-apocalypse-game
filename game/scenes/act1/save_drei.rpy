label gay_hp:
    screen anal_hp:
        vbox:
            xalign 1.0
            yalign 0.05
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[anal_unit.name]: [anal_unit.health]/[anal_unit.max_health]"
        bar value anal_unit.health range anal_unit.max_health xalign 1.0 yalign 0.1 xmaximum 230
    screen hunt_hp:
        vbox:
            xalign 1.0
            yalign 0.15
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[hunt_unit.name]: [hunt_unit.health]/[hunt_unit.max_health]"
        bar value hunt_unit.health range hunt_unit.max_health xalign 1.0 yalign 0.20 xmaximum 210

    show screen anal_hp
    show screen hunt_hp
    return

label gay_fight:
    play music "./audio/gachi.mp3" volume 0.2 fadein 5
    show gay_scene with Dissolve(.5)
    python:
        anal_unit = Anal(65, 40)
        hunt_unit = Hunt(50, 30)
        enemyParty = Party()
        enemyParty.addMember(anal_unit)
        enemyParty.addMember(hunt_unit)

    unknown ""

    call gay_hp
    call show_party_hp

    unknown ""

    python:
        fight = Fight(party, enemyParty, "gay")
        fight.start()

    hide screen anal_hp
    hide screen hunt_hp
    call hide_party_hp
    pass

label beaten:
    scene black with Dissolve(.5)
    maks "Вау"
    maks "Действительно получилось"
    scene lushwelcome with Dissolve(.5)

    play sound "characters/lesh/lush-guide-po-belgrade.ogg" volume 2
    lush ""
    stop sound

    show max4 at right
    maks "Как-то у тебя тут не богато"
    maks "В холодильнике попка от колбасы да кусочек масла"

    play sound "characters/lesh/lush-tvorog.ogg" volume 2
    lush ""
    stop sound

    show igor_pretty at left
    igoryas "Вот это приключение вышло"
    igoryas "Даже не верится"

    play sound "characters/lesh/lush-razrabi-genii.ogg" volume 2
    lush ""
    stop sound

    scene black with Dissolve(8)

    $ MainMenu(confirm=False)()

    return

label serbia:
    scene electron with Dissolve(.5)
    show babka:
        xalign 0.8
        yalign 0.4
    show max_happy at right
    maks "Я рад, парни"
    maks "Чувствую, что это правильный выбор"

    play music "./audio/village-people-ymca.mp3" volume 0.2 fadein 5
    scene gay_parad with Dissolve(.5)

    show lush_jetpack at right

    play sound "characters/lesh/lush-anal-govnosos.ogg" volume 1
    lush ""
    stop sound

    show double_gay at left
    anal '{i}Дечко где бежиш, још нисмо готови' (what_color="#ff00ec")
    
    maks "Здесь что, гей парад проходит?"

    play sound "characters/lesh/lush-prohodit.ogg" volume 2
    lush ""
    stop sound

    menu:
        "Вписываем за Люша, парни":
            if party.contains(Drei) and inventory.hasDubki():
                show drei1
                andrei "Миха, стой"
                andrei "У меня есть идея"
                andrei "Степа, сними штаны, закинь их себе на шею"
                andrei "И повернись к ним голенькой попкой!"

                play sound "characters/lesh/lush-poteryalsya-posle-tvoih-slov.ogg" volume 2
                lush ""
                stop sound

                python:
                    hide_all_lush()
                show lush5 at right

                play sound "characters/lesh/lush-mne-pizda.ogg" volume 2
                lush ""
                stop sound

                python:
                    hide_all_drei()
                    hide_all_lush()
                hide double_gay

                scene black with Dissolve(.5)
                show podnoshenie with Dissolve(.5)

                play sound "characters/drei/ugoshenia.mp3" volume 2
                andrei ""
                stop sound

                jump beaten
                return
            else:
                call gay_fight
                pass
                return
        "Я разберусь сам":
            show ya_mikhail
            maks "Не получилось походу"
            maks "Парни, помогаем"

            call gay_fight
            jump beaten
            pass
    return

label maybe_serbia:
    scene vokzal with Dissolve(.5)
    show igor_pretty at left
    igoryas "Элка до Сербии через 15 минут"
    show max4 at right
    maks "А до города через 5 минут"
    maks "Может это.."
    maks "Как-то не хочется бросать Диманов"
    igoryas "Не хочется у пчелки в попке"
    igoryas "Ты понял короче"
    miha "Макс, ты задумался о том, как правильно поступить?"
    maks "Да"
    miha "Как всегда решение придется принимать мне?"
    maks "Да..."
    menu:
        "Влада":
            pass
        "Маша":
            pass
    
    python:
        hide_all_max()
    show max_angry at right
    maks "Да ты ск"
    maks "А если серьезно"

    menu:
        "Идемо у Србију да једемо плескавицу":
            jump serbia
            pass
        "Ты прав, Диман, бы нас не бросил":
            jump act2
            pass

    return

label save_drei:
    stop music
    play music '/audio/clock_tick.mp3' volume 0.25
    play sound '/audio/chuchuh.mp3' volume 0.2

    scene electron with Dissolve(1.5)
    show maxsit at right
    maks "Набираю Древу"
    scene electron_call
    show maxsit at right
    pause(.5)
    andrei "Алло, че такое?"
    maks "Дядь, выходи через 10 мин, оч надо"
    andrei "Ага, окес"
    andrei "Выхожу"
    miha ")"
    stop sound
    stop music
    scene vokzal with Dissolve(.5)
    show max1 at right
    maks "Бля, а куда идти то?"
    maks "Дрей же теперь в колизее живет вроде"
    hide max1
    show igor1 at left
    igoryas "По-люб колизей"
    hide igor1
    show gera1
    play music "./audio/mysterymorgan.mp3" volume 0.3
    gera "Михаил, друзья, мы встретились вновь"
    show screen campButton
    gera "Я присоединился, чтобы поддержать Вас в это непростое время"
    gera "Увидимся в лагере"
    hide gera1
    "Нажав на кнопку в верхнем углу Вы можете попасть в лагерь"
    "В лагере можно пообщаться и улучшить компаньонов, а также использовать предметы"
    "Лагерь доступен в любой момент вне боя"
    play music "./audio/soundtrack5.mp3" volume 0.3
    show max1 at right
    maks "Ну че, куда идем?"
    menu:
        "К Калитке":
            if party.hasExp():
                play music "./audio/mysterymorgan.mp3" volume 0.3
                show gera1
                gera "Михаил, настойчиво рекомендую перейти в лагерь и использовать весь накопленный опыт перед входом в следующую локацию"
                hide gera1
                play music "./audio/soundtrack5.mp3" volume 0.3
                miha "Да все окей окей, на созвоне"
            call kalitka_house
        "В Колизей":
            if party.hasExp():
                play music "./audio/mysterymorgan.mp3" volume 0.3
                show gera1
                gera "Михаил, настойчиво рекомендую перейти в лагерь и использовать весь накопленный опыт перед входом в следующую локацию"
                hide gera1
                play music "./audio/soundtrack5.mp3" volume 0.3
                miha "Да все окей окей, на созвоне"
            call colosseum_scene
            pass

    if isZakl:
        jump maybe_serbia
    else:
        python:
            hide_all_drei()
        show max1 at right
        maks "Едем спасать Диманов"
        miha "Куда?"
        maks "Huawei Technologies Co Ltd, Bantian, Huawei Base, Longgang District, Shenzhen, Guangdong, 518100"
        miha "Ну да"

    return