# Инициализация всего
call setup_chars
init python:
    inventory = Inventory()

# Игра начинается здесь:
label start:
    python:
        inventory = Inventory()
#     show screen inventory_display_toggle
    call intro
    scene black
    "конец интро"

    return
