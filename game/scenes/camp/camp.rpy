label camp_scene:
image camp = "images/camp1.jpg"
show camp at center with Dissolve(1)
hide screen campButton
call show_party_hp
python:
    stayInCamp = True
    while stayInCamp:
        camp = Camp(party, inventory)
        stayInCamp = camp.enter()

hide camp with Dissolve(1)
call hide_party_hp
show screen campButton
return