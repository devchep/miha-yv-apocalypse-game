label korean_fight:
python:
    knee_unit = Knee(65, 40)
    law_unit = Law(30, 50)
    first_unit = First(100, 30)
    chinese_lesh = ChineseLesh(90, 30)
    #TODO 1: резет абилок?
    enemyParty = Party()
    enemyParty.addMember(knee_unit)
    enemyParty.addMember(law_unit)
    enemyParty.addMember(first_unit)
    enemyParty.addMember(chinese_lesh)

call show_chinese_hp
call show_party_hp
play music "./audio/fight_chinese.mp3" volume 0.2
"Начался бой"

python:
    fight = Fight(party, enemyParty)
    fight.start()

call hide_chinese_hp
call hide_party_hp
stop music
