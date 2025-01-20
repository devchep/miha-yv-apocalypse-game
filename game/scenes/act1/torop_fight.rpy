label torop_fight:
python:
    enemy = Torop(65, 25)
    party.healEveryone()
    drei_unit = Drei(62, 5)
    party.addMember(drei_unit)

call show_hp
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

while enemy.health > 0 and not party.isWiped():

    python:
        pickedMember = renpy.display_menu(party.getMembersForNextAttack())
        pickedAbility = renpy.display_menu(pickedMember.getAvailableAbilities())
        pickedAbility.useAgainst(enemy, pickedMember)

    pause(1)
    if enemy.health > 0:
        python:
            enemy.attack(party)

hide torop
call hide_hp
call hide_party_hp
stop music
