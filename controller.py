from view.UI import UI as ui
from model.Bank import Bank
from model.ATM import ATM


if __name__ == '__main__':
    mainloop = True
    ATMs = []  # Colecciona los cajeros
    bank = None

    while mainloop:
        userOption = ui.menu()

        if userOption == 1:
            # CREATE
            atmData = ui.createForm()
            # Instanciar cajero
            atm = ATM(code=atmData['codigo'],
                      status=atm['estado'],
                      model=atmData['modeloCajero'],
                      transactions=atmData['transacciones'])

            ATMs.append(atm)  # Coleccionar cajeros
            bank = Bank(ATMs=ATMs)  # Instanciar banco

        elif userOption == 2:
            # READ
            pass
        elif userOption == 3:
            # UPDATE
            pass
        elif userOption == 4:
            # DELETE
            pass
        elif userOption == 0:
            # EXIT
            mainloop = False