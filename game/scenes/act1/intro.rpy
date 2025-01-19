label intro:

    scene black
    "Странное чувство"
    "Приятное, интригующее"
    "Как будто друзья любят и подарили подарок такой крутой, с душой"

    scene kfc with Dissolve(1)
    scene black with Dissolve(1)
    scene kfc with Dissolve(1)

    miha "Ох и сладенько я поспал"
    miha "Хорошо, что сегодня среда"
    miha "И как же хорошо, что сегодня не два твистера"
    miha "Но день странный, будто что-то начинается"

    python:
        inventory.loot(ColaNoSugar("2 колы по купону 5050"))
