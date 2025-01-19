label korean_fight:
python:
    knee_unit = Knee(65, 40)
    law_unit = Law(30, 50)
    first_unit = First(100, 30)
    chinese_lesh = ChineseLesh(90, 30)
    #TODO резет абилок
    party.healEveryone()
    enemyParty = Party()
    enemyParty.addMember(knee_unit)
    enemyParty.addMember(law_unit)
    enemyParty.addMember(first_unit)
    enemyParty.addMember(chinese_lesh)

call show_chinese_hp
call show_party_hp
play music "./audio/fight_chinese.mp3" volume 0.2
"Начался бой"

while not enemyParty.isWiped() and not party.isWiped():

    python:
        pickedMember = renpy.display_menu(party.getMembersForNextAttack())
        pickedAbility = renpy.display_menu(pickedMember.getAvailableAbilities())
        if (pickedAbility.targeted):
            pickedEnemy = renpy.display_menu(enemyParty.getMembersForNextAttack())
            pickedAbility.useAgainst(pickedEnemy, pickedMember)
        else:
            pickedAbility.use(enemyParty, pickedMember)

    pause(1)
    if any(enemy[1].health > 0 for enemy in enemyParty.getMembersForNextAttack()):
        show ball_weapon with Dissolve(.1)
        with vpunch
        hide ball_weapon
        python:
            enemy = enemyParty.popNext()
            if enemy is not None:
                enemy.attack(party)
                enemyParty.putInAttackQueue(enemy)

call hide_chinese_hp
call hide_party_hp
stop music
