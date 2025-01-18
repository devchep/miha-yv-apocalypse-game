label torop_fight:
python:
    enemy = Torop(65, 25)
    party.healEveryone()

call show_hp
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

while enemy.health > 0 and not party.isWiped():

    python:
        pickedMember = renpy.display_menu(party.getMembersForNextAttack())
        pickedAbility = renpy.display_menu(pickedMember.getAvailableAbilities())
        pickedAbility.useAgainst(enemy)

    pause(1)
    if enemy.health > 0:
        show ball_weapon with Dissolve(.1)
        with vpunch
        hide ball_weapon
        python:
            enemy.attack(party)

hide torop
call hide_hp
