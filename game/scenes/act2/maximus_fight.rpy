label maximus_fight:
python:
    enemy = Maximus(100000000000, 100)
    enemyParty = Party()
    enemyParty.addMember(enemy)

call show_maximus_hp
call show_party_hp
play music "./audio/maximus_theme_fight.mp3" volume 0.7
"Вы вступили в бой"
show maximus
maximus "{b}Причина тряски?{/b}"
maximus "{b}Немного даже удивительно это{/b}"
maximus "{b}Вам хватило {color=#f00}бездарности, никчемности{/color} придти ко мне{/b}"
maximus "{b}Учитывая что нет ни малейшего шанса на выживание{/b}"
maximus "{b}Но сегодня особый день{/b}"
"Бой приостановлен"
call hide_maximus_hp
call hide_party_hp
maximus "{b}Миха, я даю тебе возможность{/b}"
maximus "{b}Примкнуть ко мне{/b}"
maximus "{b}Цепляйся же за нее{/b}"
maximus "{b}Зубами, логтями, хер его знает{/b}"
menu:
    "Я отказываюсь":
        jump ready_to_fight_maximus
    "Продолжай":
        maximus "{b}Ты отдаешь мне свою кровь{/b}"
        maximus "{b}А затем мы делаем Яндекс.Сплит{/b}"
menu:
    "Я в деле":
        maximus "{b}Наш Слон{/b}"
        "Бой остановлен"
        stop music
        call hide_maximus_hp
        call hide_party_hp
        hide maximus
        scene gera_fight with Dissolve(.1)
        show gera1
        play music "./audio/mysterymorgan.mp3" volume 0.3
        gera "Михаил"
        gera "Я подозревал что это может произойти"
        hide gera1
        show gera_axe at right
        gera "Нас раскинуло по разные стороны в этом конфикте"
        hide gera_axe
        play music "./audio/metalcore1.mp3" volume 0.5
        show gera_mad
        gera "Готовься угадывать топоры"
        gera "Уебище"
        hide gera_mad
        call gera_fight
        hide gera_axe
        maximus "{b}Отлично, а сейчас отойди в сторонку, я с твоими напердышами разберусь{/b}"
        python:
            maximus_friend = True
        pause 2
        scene black with Dissolve(3)
        call maximus_palace_split
        return
    "Ебанутый? Я отказываюсь":
        label ready_to_fight_maximus:
        maximus "{b}{color=#f00}Я разочарован{/color}{/b}"
        call show_maximus_hp
        call show_party_hp
        "Бой продолжен"

$ renpy.save("maximus_fight")
python:
    [member.disabled(4) for member in party.members.values()]

python:
    fight = Fight(party, enemyParty, "maximus_fight")
    fight.start()

hide maximus
call hide_maximus_hp
call hide_party_hp
stop music
