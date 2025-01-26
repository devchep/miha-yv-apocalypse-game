label intro:

    scene black
    "Странное чувство"
    "Приятное, интригующее"
    "Как будто друзья любят и подарили подарок такой крутой, с душой"

    scene kfc with Dissolve(1)
    scene black with Dissolve(1)
    scene kfc with Dissolve(1)

    play music "./audio/soundtrack6.mp3" volume 0.3
    miha "Ох и сладенько я поспал"
    miha "Хорошо, что сегодня среда"
    miha "И как же хорошо, что сегодня не два твистера"
    miha "Но кола то почему сука без сахара"
    python:
        inventory.loot(ColaNoSugar("2 колы по купону 5050"))
    miha "А вообще, день странный, будто что-то начинается"
    miha "Ладно, пойду что ли домой"