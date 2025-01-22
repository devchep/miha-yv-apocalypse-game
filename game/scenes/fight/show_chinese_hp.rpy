label show_chinese_hp:
    # Пока впадлу разбираться как нормально сделать
    screen knee_hp:
        vbox:
            xalign 1.0
            yalign 0.05
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[knee_unit.name]: [knee_unit.health]/[knee_unit.max_health]"
        bar value knee_unit.health range knee_unit.max_health xalign 1.0 yalign 0.1 xmaximum 230
    screen law_unit_hp:
        vbox:
            xalign 1.0
            yalign 0.15
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[law_unit.name]: [law_unit.health]/[law_unit.max_health]"
        bar value law_unit.health range law_unit.max_health xalign 1.0 yalign 0.20 xmaximum 210
    screen first_unit_hp:
        vbox:
            xalign 1.0
            yalign 0.25
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[first_unit.name]: [first_unit.health]/[first_unit.max_health]"
        bar value first_unit.health range first_unit.max_health xalign 1.0 yalign 0.3 xmaximum 335
    screen chinese_lesh_hp:
        vbox:
            xalign 1.0
            yalign 0.35
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[chinese_lesh.name]: [chinese_lesh.health]/[chinese_lesh.max_health]"
        bar value chinese_lesh.health range chinese_lesh.max_health xalign 1.0 yalign 0.4 xmaximum 310

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