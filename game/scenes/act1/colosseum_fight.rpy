label colosseum_fight:
python:
    enemy = Tigr(100, 40)
    enemyParty = Party()
    enemyParty.addMember(enemy)

call show_enemy_hp
call show_party_hp
play music "./audio/fight2.mp3" volume 0.1
"Вы вступили в бой"

python:
    fight = Fight(party, enemyParty)
    fight.start()

call hide_enemy_hp
call hide_party_hp
stop music
