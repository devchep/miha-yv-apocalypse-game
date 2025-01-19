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

    show screen knee_hp
    show screen law_unit_hp
    show screen first_unit_hp
    show screen chinese_lesh_hp
    return

label hide_chinese_hp:
    hide screen knee_hp
    hide screen law_unit_hp
    hide screen first_unit_hp
    hide screen chinese_lesh_hp
    return