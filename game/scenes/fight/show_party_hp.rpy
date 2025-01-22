label show_party_hp:
    # Пока впадлу разбираться как нормально сделать
    screen miha_hp:
        vbox:
            xalign 0.0
            yalign 0.05
            frame:
                padding 10, 10, 10, 10
                background "#E4E4E4"
                text "[miha_unit.name]: [miha_unit.health]/[miha_unit.max_health]"
        bar value miha_unit.health range miha_unit.max_health xalign 0.0 yalign 0.1 xmaximum 225 left_bar "#215831"  right_bar "#CFC1EC"

    screen igoryas_hp:
        vbox:
            xalign 0.0
            yalign 0.15
            frame:
                padding 10, 10, 10, 10
                background "#E4E4E4"
                text "[igoryas_unit.name]: [igoryas_unit.health]/[igoryas_unit.max_health]"
        bar value igoryas_unit.health range igoryas_unit.max_health xalign 0.0 yalign 0.2 xmaximum 265 left_bar "#E2AD59"  right_bar "#F0D5AA"
    screen maxHeyman_hp:
        vbox:
            xalign 0.0
            yalign 0.25
            frame:
                padding 10, 10, 10, 10
                background "#E4E4E4"
                text "[maks_unit.name]: [maks_unit.health]/[maks_unit.max_health]"
        bar value maks_unit.health range maks_unit.max_health xalign 0.0 yalign 0.3 xmaximum 235 left_bar "#2A28C3"  right_bar "#B49AE8"
    screen drei_hp:
        vbox:
            xalign 0.0
            yalign 0.35
            frame:
                padding 10, 10, 10, 10
                background "#E4E4E4"
                text "[drei_unit.name]: [drei_unit.health]/[drei_unit.max_health]"
        bar value drei_unit.health range drei_unit.max_health xalign 0.0 yalign 0.4 xmaximum 230 left_bar "#2CADD1"  right_bar "#4B8692"

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