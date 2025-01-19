label zheka_fight:
python:
    enemy = Zheka(70, 10)

call show_hp
call show_party_hp
play music "./audio/fight3.mp3" volume 0.1
"Миха начинает бой"
"интуитивно понятно че делать"
"тутора не будет"

while enemy.health > 0 and not party.isWiped():

    python:
        pickedMember = renpy.display_menu(party.getMembersForNextAttack())
        pickedAbility = renpy.display_menu(pickedMember.getAvailableAbilities())
        pickedAbility.useAgainst(enemy, pickedMember)

    pause(1)
    if enemy.health > 0:
        with vpunch
        python:
            enemy.attack(party)

stop music
call hide_hp
call hide_party_hp
