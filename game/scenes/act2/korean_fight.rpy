label korean_fight:
python:
    knee_unit = Knee(65, 40)
    law_unit = Law(30, 50)
    first_unit = First(100, 30)
    chinese_lesh = ChineseLesh(90, 30)
    #TODO 1: резет абилок
    enemyParty = Party()
    enemyParty.addMember(knee_unit)
    enemyParty.addMember(law_unit)
    enemyParty.addMember(first_unit)
    enemyParty.addMember(chinese_lesh)

call show_chinese_hp
call show_party_hp
play music "./audio/fight_chinese.mp3" volume 0.2
$ renpy.save("korean_fight")
"Начался бой"

python:
    fight = Fight(party, enemyParty, "korean_fight")
    fight.start()

python:
    diman_unit = Diman(63, 5)
    party.addMember(diman_unit)

python:
    party.getExp(2)
call hide_chinese_hp
call hide_party_hp
stop music
