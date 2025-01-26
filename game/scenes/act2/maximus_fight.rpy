label maximus_fight:
python:
    enemy = Maximus(100000000000, 100)
    enemyParty = Party()
    enemyParty.addMember(enemy)

call show_maximus_hp
call show_party_hp
play music "./audio/maximus_theme_fight.mp3" volume 0.7
$ renpy.save("maximus_fight")
"Вы вступили в бой"
show maximus
maximus "{b}Немного даже удивительно это{/b}"
maximus "{b}Вам хватило {color=#f00}бездарности, никчемности{/color} придти ко мне{/b}"
maximus "{b}Даже когда вы все прекрасно понимали{/b}"
python:
    [member.disabled(4) for member in party.members.values()]

python:
    fight = Fight(party, enemyParty, "maximus_fight")
    fight.start()

hide maximus
call hide_maximus_hp
call hide_party_hp
stop music
