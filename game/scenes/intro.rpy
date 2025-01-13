label intro:

scene black
"Странное чувство"
"Приятное, интригующее"
"Как будто друзья любят и подарили подарок такой крутой, с душой"

scene fromkfc with Dissolve(.5)
"Ладно, закупил крылешек иду подхаваться"

show max1
maks "Здарова Мих"
menu:
    "Йоу Макс":
        pass
    "Смачный здарова Макс":
        call dab_up
        maks "..."
        maks "уфф"
        pass
maks "Кароче некогда говорить, это пездец"
maks "Нам срочно нужно спасать Игоряна"
miha "..."
maks "Скорее идем, здесь небезопасно"
miha "У меня есть время подготовиться?"
maks "Только быстро"
maks "Мы не хотим здесь задерживаться"
maks "Что тебе нужно?"
menu:
    "Нужно в пятерочку за сосисками":
        maks "..."
        pass
    "Да ниче, погнали":
        maks "Го"
        pass

hide max1

scene alexandrovskaya with Dissolve(.5)
show max1
maks "Действуем быстро"
maks "Нам нужно спасти Игоря"
miha "Понял"
play sound "audio/sobaka1.ogg"
pause(2)
maks "Бля собаки Гаряна"
stop sound
play sound "audio/sobaka2.ogg"
pause(1)
maks "Ноу вей пройти"
stop sound
miha "Погоди, есть идея"
menu:
    "Кинуть сосиску":
        pass
    "Ниче не делать":
        pause(4)
        maks "Ну че?"
        miha "Да бля"
        miha "Не придумал"
        maks "Нам надо как-то пройти мэн, иначе не успеем"
        play sound "audio/sobaka2.ogg"
        pause(1)
        menu:
            "Кинуть сосиску":
                pass

play sound "audio/metanie-sosiski.mp3" fadein 1 volume 0.7
pause(1)
play sound "audio/sobaka_spasibo.ogg" fadeout 1 volume 0.2
pause(1)
miha "Изи"
stop sound
play sound "audio/sobaka3.ogg" volume 0.1
maks "Ахуеть, откуда?"
stop sound
maks "А, понял)"
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
play sound "audio/subway-surfers.mp3" volume 0.1
maks "Гайзы"
hide max1
show creep at left
creep "Че _?"

show max1 at right
maks "Ни в коем случае смотрите что он вам покажет"
hide max1

menu:
    "Атаковать":
        pass
    "Че там у тебя":
        pass

maks "Надеюсь мы его не кокнули"
maks "Нас же повяжут"
maks "Мих, ты этим говном управлял"
maks ""