from view.UI import UI as ui
from model.Bank import Bank


if __name__ == '__main__':
    mainloop = True
    bank = Bank()

    while mainloop:
        userOption = ui.menu()

        if userOption == 1:
            # CREATE
            atmData = ui.createForm()  # Obtiene datos del usuario
            bank.addATM(atmData)

        elif userOption == 2:
            # READ
            print('\n***** MOSTRAR CAJEROS Y SUS TRANSACCIONES *****\n')
            bank.showATMs()

        elif userOption == 3:
            # UPDATE
            pass
        elif userOption == 4:
            # DELETE
            pass
        elif userOption == 0:
            # EXIT
            mainloop = False