# Инициализация всего
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
call setup_chars
init 3 python:
    inventory = Inventory()

label splashscreen:
    $ renpy.movie_cutscene("video/boot_intro.webm", loops=0, stop_music=False)
    return

# Игра начинается здесь:
label start:
    python:
        inventory = Inventory()
        party = Party()
        miha_unit = Miha(60, 6)
        party.addMember(miha_unit)
        isZakl = False

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
#         diman_unit = Diman(63, 5)
#         party.addMember(miha_unit)
#         party.addMember(maks_unit)
#         party.addMember(igoryas_unit)
#         party.addMember(drei_unit)
#         party.addMember(diman_unit)
#         party.getExp(4)
#
#     python:
#         inventory.loot(ColaNoSugar("2 колы по купону 5050"))
#         inventory.choice(
#             2,
#             [
#                 Sosiska("Пачка сосисок из пятерки"),
#                 Tortik("Медовичок"),
#                 Energizer("Адреналин черный")
#             ]
#         )
#
#     show screen campButton
#     ""
#     call meet_maximus
#
#     return
