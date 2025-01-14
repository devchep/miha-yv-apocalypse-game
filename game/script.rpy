# Инициализация всего
call setup_chars
init python:
    inventory = Inventory()

# Игра начинается здесь:
label start:

#     show screen inventory_display_toggle
    call intro

    return
