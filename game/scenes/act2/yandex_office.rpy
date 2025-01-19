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
    diman "Оставьте меня"
    diman "Тут дохуя китайцев"
    diman "Вам пиздец"

    scene diman_hostage_with_koreans with Dissolve(.1)
    play music "./audio/chinese_music.mp3"

    law "米莎，生日快乐"
    first "米莎，生日快乐"
    knee "米莎，生日快乐"
    miha "Погодите"
    miha "Я немного знаю японский"
    miha "Могу c ними договориться"

    menu:
        "こんにちは、Misha.":
            pass
        "今日は。":
            pass
        "どうぞよろしく。":
            pass

    stop music
    call korean_fight

    miha "разьебашили"
    scene hostages with Dissolve(.5)
