label show_party_hp:
    # Пока впадлу разбираться как нормально сделать
    screen miha_hp:
        text "[miha_unit.name]: [miha_unit.health]/[miha_unit.max_health]" xalign 0.0 yalign 0.05
        bar value miha_unit.health range miha_unit.max_health xalign 0.0 yalign 0.1 xmaximum 200
    screen igoryas_hp:
        text "[igoryas_unit.name]: [igoryas_unit.health]/[igoryas_unit.max_health]" xalign 0.0 yalign 0.15
        bar value igoryas_unit.health range igoryas_unit.max_health xalign 0.0 yalign 0.2 xmaximum 240
    screen maxHeyman_hp:
        text "[maks_unit.name]: [maks_unit.health]/[maks_unit.max_health]" xalign 0.0 yalign 0.25
        bar value maks_unit.health range maks_unit.max_health xalign 0.0 yalign 0.3 xmaximum 220
    screen drei_hp:
        text "[drei_unit.name]: [drei_unit.health]/[drei_unit.max_health]" xalign 0.0 yalign 0.35
        bar value drei_unit.health range drei_unit.max_health xalign 0.0 yalign 0.4 xmaximum 220

    if party.contains(Miha) and miha_unit.health>0:
        show screen miha_hp
    if party.contains(Igoryas) and igoryas_unit.health>0:
        show screen igoryas_hp
    if party.contains(MaxHeyman) and maks_unit.health>0:
        show screen maxHeyman_hp
    if party.contains(Drei) and drei_unit.health>0:
        show screen drei_hp
    return

label hide_party_hp:
    hide screen miha_hp
    hide screen igoryas_hp
    hide screen maxHeyman_hp
    hide screen drei_hp
    return