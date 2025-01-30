# Инициализация всего
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
call setup_chars
init 3 python:
    inventory = Inventory()

# Игра начинается здесь:
# label start:
#     python:
#         inventory = Inventory()
#         party = Party()
#         miha_unit = Miha(60, 6)
#         party.addMember(miha_unit)
#
#     call act1
#
#     scene black
#     call act2
#
#     return


# Тест сцен:
label start:
    python:
        inventory = Inventory()
        party = Party()
        miha_unit = Miha(60, 6)
        party.addMember(miha_unit)

    call meet_maximus
    call path_to_maximus

    return
