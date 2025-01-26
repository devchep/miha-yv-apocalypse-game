label zheka_fight:
python:
    enemy = Zheka(70, 10)
    enemyParty = Party()
    enemyParty.addMember(enemy)

call show_enemy_hp
call show_party_hp
play music "./audio/fight3.mp3" volume 0.1

$ renpy.save("zheka_fight")
"Миха начинает бой"
"интуитивно понятно че делать"
"тутора не будет"

python:
    fight = Fight(party, enemyParty, "zheka_fight")
    fight.start()

    party.getExp(1)
stop music
call hide_enemy_hp
call hide_party_hp
