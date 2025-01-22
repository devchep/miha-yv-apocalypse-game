label yandex_office:

    scene office with Dissolve(.5)
    miha "Мужики, это оно?"
    show max1 at right
    maks "По-люб"
    maks "Я другой офис не знаю"
    miha "..."
    scene hostages with Dissolve(.5)
    miha "Слушай, знакомое место"
    miha "Надеюсь Диман не в заложниках"

    scene diman_hostage with Dissolve(.5)

    diman "Мужики, уходите"
    diman "Тут дохуя китайцев"
    diman "Вам пиздец"

    scene diman_hostage_with_koreans with Dissolve(.1)
    play music "./audio/chinese_music.mp3"

    law "йуо йуооо йоооооии"
    first "Better get out of here"
    knee "hoho, wona fighte?"
    chineseLesh "yksi kaksi kolme"
    miha "Погодите"
    miha "Я немного знаю японский"
    miha "Могу c ними договориться"

    menu:
        "кони чи ва, ваташи ва Миша дес":
            pass
        "ана та ва ока са ре тей мас":
            pass
        "Дорогие азиатские братья, произошло недоразумение, отпустите, пожалуйста, этого человека":
            pass

    stop music
    call korean_fight

    miha "разьебашили"
    scene hostages with Dissolve(.5)
