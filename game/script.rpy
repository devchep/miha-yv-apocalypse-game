# Инициализация всего
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
