# Инициализация всего
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
call setup_chars
init 3 python:
    inventory = Inventory()

# Игра начинается здесь:
label start:
    python:
        inventory = Inventory()
        party = Party()
        miha_unit = Miha(60, 6)
        party.addMember(miha_unit)

    call act1

    scene black
    call act2

    return


# Тест сцен:
# label start:
#     python:
#         inventory = Inventory()
#         party = Party()
#         miha_unit = Miha(60, 6)
#         maks_unit = MaxHeyman(65, 10)
#         igoryas_unit = Igoryas(80, 6)
#         drei_unit = Drei(62, 5)
#         party.addMember(miha_unit)
#         party.addMember(maks_unit)
#         party.addMember(igoryas_unit)
#         party.addMember(drei_unit)
#         party.getExp(2)
#
#     show screen campButton
#     call yandex_office
#
#     return
