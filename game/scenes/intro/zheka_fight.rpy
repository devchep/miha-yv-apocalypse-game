label zheka_fight:
python:
    enemy = Zheka(70, 10)

call show_hp
"интуитивно понятно че делать"
"тутора не будет"

while enemy.health > 0 and not party.isWiped():

    python:
        pickedMember = renpy.display_menu(party.getMembersForNextAttack())
        pickedMember.attack(enemy)

    if enemy.health > 0:
        creep "[enemy.attack_phrase()]"
        python:
            enemy.attack(party)

call hide_hp
