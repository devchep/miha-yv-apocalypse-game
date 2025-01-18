label intro:

    scene black
    "Странное чувство"
    "Приятное, интригующее"
    "Как будто друзья любят и подарили подарок такой крутой, с душой"

    scene fromkfc with Dissolve(.5)
    miha "Сука"
    miha "Среда, купон 5050"
    miha "И что вы думаете? 2 колы без сахара"
    miha "Взял чисто на зло этим мразям"
    python:
        inventory.loot(ColaNoSugar("2 колы по купону 5050"))
