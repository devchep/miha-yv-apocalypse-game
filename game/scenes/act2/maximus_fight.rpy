python:
    bigdamagepunch = Move((15, 0), (0, 15), .10, bounce=True, repeat=True, delay=0)
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
maximus "{b}Немного даже удивительно{/b}"
maximus "{b}Что вам хватило {color=#f00}бездарности, никчемности{/color} придти ко мне{/b}"
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

        show maximus
        maximus "{b}Миха, отлично, а сейчас отойди в сторонку{/b}"
        maximus "{b}Я разберусь с нечистой кровью{/b}"
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        with bigdamagepunch
        python:
            maximus_friend = True
        pause 2
        scene black with Dissolve(3)
        scene black
        nvle "Миха присоединился к Максимусу"
        nvle "Поделился с ним собственной кровью, истинно веря в чистоту собственной крови"
        nvle "Очищенной от потребления ненужного, мусорного, ничтожного, быстро-допаминового контента"
        call vsem_pizda
        return
    "Ебанутый? Я отказываюсь":
        label ready_to_fight_maximus:
        maximus "{b}{color=#f00}Я разочарован{/color}{/b}"
        call show_maximus_hp
        call show_party_hp
        "Бой продолжен"

python:
    enemy.health = 150
$ renpy.save("maximus_fight")
python:
    [member.disabled(1) for member in party.members.values()]

python:
    fight = Fight(party, enemyParty, "maximus_fight")
    fight.start()

python:
    enemy.max_health = 999999999999
maximus "{b}Хм{/b}"
hide maximus
call hide_maximus_hp
call hide_party_hp
stop music
scene gates_chill with Dissolve(.2)
play music "./audio/who_are_you.mp3" volume 0.8
"Максимус исчез"
show max1
maks "Это невероятно"
miha "Да"
maks "Максимус побежден?"
hide max1
miha "Ахахах"
miha "Мы победили?"
if party.contains(Drei):
    show andreiflower
    andrei "Парни я так рад"
    hide andreiflower
if party.contains(Igoryas):
    show igor_dovolen
    igoryas "Мы такие молодцы"
    hide igor_dovolen

scene black
"После боя Максимус больше не появлялся"
scene server_down with Dissolve(.2)
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
with bigdamagepunch
scene server_down_boom
"Мы разьебашили Яндекс.Сервера"
scene all_fine with Dissolve(.2)
"И все пришло в норму"
nvle "Это просто потрясающе"
nvle "Миха с друзьями остановили Яндекс.Вирус"
nvle "А Максимус после получения 1 демеджа исчез навсегда"
nvle "Может он обидился?"
nvle "В любом случае это потрясающая концовка"
nvle "Как хорошо что все вернулось в норму"
nvle "Правда ведь?"
python:
    get_achievement("victory", trans=achievement_transform)
nvle "Все молодцы"
$ MainMenu(confirm=False)()
