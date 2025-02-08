label gera_fight:
python:
    enemy = Gera(500, 90)
    enemyParty = Party()
    enemyParty.addMember(enemy)

call show_enemy_hp
call show_party_hp
$ renpy.save("gera_fight")
show gera_axe
"Начался бой"
$ renpy.music.set_volume(0.1, 0, channel='music')

python:
    fight = Fight(party, enemyParty, "gera_fight")
    fight.startReverse()

call hide_enemy_hp
call hide_party_hp
stop music
