label show_hp:
    screen enemy_hp:
        text "[enemy.name]: [enemy.health]/[enemy.max_health]" xalign 1.0 yalign 0.05
        bar value enemy.health range enemy.max_health xalign 1.0 yalign 0.1 xmaximum 200

    show screen enemy_hp
    return

label hide_hp:
    hide screen enemy_hp
    return