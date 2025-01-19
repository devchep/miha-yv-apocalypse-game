label show_chinese_hp:
    # Пока впадлу разбираться как нормально сделать
    screen knee_hp:
        text "[knee_unit.name]: [knee_unit.health]/[knee_unit.max_health]" xalign 1.0 yalign 0.05
        bar value knee_unit.health range knee_unit.max_health xalign 1.0 yalign 0.1 xmaximum 200
    screen law_unit_hp:
        text "[law_unit.name]: [law_unit.health]/[law_unit.max_health]" xalign 1.0 yalign 0.15
        bar value law_unit.health range law_unit.max_health xalign 1.0 yalign 0.20 xmaximum 200
    screen first_unit_hp:
        text "[first_unit.name]: [first_unit.health]/[first_unit.max_health]" xalign 1.0 yalign 0.25
        bar value first_unit.health range first_unit.max_health xalign 1.0 yalign 0.3 xmaximum 200
    screen chinese_lesh_hp:
        text "[chinese_lesh.name]: [chinese_lesh.health]/[chinese_lesh.max_health]" xalign 1.0 yalign 0.35
        bar value chinese_lesh.health range chinese_lesh.max_health xalign 1.0 yalign 0.4 xmaximum 200

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

    show screen knee_hp
    show screen law_unit_hp
    show screen first_unit_hp
    show screen chinese_lesh_hp
    if party.contains(Miha) and miha_unit.health>0:
        show screen miha_hp
    if party.contains(Igoryas) and igoryas_unit.health>0:
        show screen igoryas_hp
    if party.contains(MaxHeyman) and maks_unit.health>0:
        show screen maxHeyman_hp
    if party.contains(Drei) and drei_unit.health>0:
        show screen drei_hp
    return

label hide_chinese_hp:
    hide screen knee_hp
    hide screen law_unit_hp
    hide screen first_unit_hp
    hide screen chinese_lesh_hp
    hide screen miha_hp
    hide screen igoryas_hp
    hide screen maxHeyman_hp
    hide screen drei_hp
    return