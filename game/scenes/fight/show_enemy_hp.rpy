label show_enemy_hp:
    screen enemy_hp:
        vbox:
            xalign 1.0
            yalign 0.05
            frame:
                padding 10, 10, 10, 10
                background "#EBEBEB"
                text "[enemy.name]: [enemy.health]/[enemy.max_health]"
        bar value enemy.health range enemy.max_health xalign 1.0 yalign 0.1 xmaximum 240

    show screen enemy_hp
    return

label hide_enemy_hp:
    hide screen enemy_hp
    return