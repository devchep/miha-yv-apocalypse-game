label intro:

    scene black
    "Странное чувство"
    "Приятное, интригующее"
    "Как будто друзья любят и подарили подарок такой крутой, с душой"
    
    play music "./audio/kfc_ambient.mp3" volume 0.1
    scene kfc with Dissolve(2)

    show grisha at right
    play audio 'audio/punch.opus'
    with vpunch
    grisha 'Просыпайтесь, долбаебка'
    grisha 'И так спите сладенько'
    grisha 'Ням-ням'
    hide grisha

    miha "Ох и сладенько я поспал"
    miha "Хорошо, что сегодня среда"
    miha "И как же хорошо, что сегодня не два твистера"
    miha "Но кола то почему сука без сахара"
    python:
        inventory.loot(ColaNoSugar("2 колы по купону 5050"))
    miha "А вообще, день странный, будто что-то начинается"
    miha "Ладно, пойду что ли домой"
    stop music