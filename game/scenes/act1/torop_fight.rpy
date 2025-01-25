label torop_fight:
python:
    enemy = Torop(65, 25)
    enemyParty = Party()
    enemyParty.addMember(enemy)
    drei_unit = Drei(62, 5)
    party.addMember(drei_unit)

call show_enemy_hp
call show_party_hp
play music "./audio/fight2.mp3" volume 0.1
"Вы вступили в бой"
show torop at right
torop "Дрюс, да посмотри"
hide torop
show drei1 at left
andrei "Не, нихуя"
andrei "Не буду я твой кал смотреть"

hide drei1

show torop at right

python:
    fight = Fight(party, enemyParty)
    fight.start()

hide torop
call hide_enemy_hp
call hide_party_hp
stop music
