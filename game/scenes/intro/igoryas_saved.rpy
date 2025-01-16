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

scene alexandrovskaya with Dissolve(.5)
show max1 at right
maks "Ладно, гайзы"
maks "Нам следуе"
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

python:
    miha_unit = Miha(60, 6)
    igoryas_unit = Igoryas(80, 6)
    maks_unit = MaxHeyman(60, 10)
    party.addMember(miha_unit)
    party.addMember(igoryas_unit)
    party.addMember(maks_unit)

menu:
    "Атаковать":
        "Миха начинает бой"
        call zheka_fight
        hide creep
        show max1 at right
        maks "Надеюсь мы его не кокнули"
        maks "Нас же повяжут"
        maks "Мих, ты этим говном управлял"
    "Че там у тебя":
        pass
