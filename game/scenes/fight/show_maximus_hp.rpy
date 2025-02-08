label show_maximus_hp:
    screen maximus_hp:
        vbox:
            xalign 1.0
            yalign 0.00
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "{b}[enemy.name]: [enemy.max_health]/[enemy.max_health]{/b}"
        bar value enemy.max_health range enemy.max_health xalign 1.0 yalign 0.05 xmaximum 2000 ymaximum 45

    show screen maximus_hp
    return

label hide_maximus_hp:
    hide screen maximus_hp
    return