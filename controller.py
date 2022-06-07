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
            bank.showATMs()  # Mostrar cajeros

            # Obtener el codigo del cajero a actualizar y los datos a actualizar
            codeATMChosen = ui.updateForm()

            # Saber si se quiere actualizar un cajero o una transacción
            updateType = ui.selectActionType('actualizar')

            # Actulizar datos del cajero
            if updateType == 1:
                # Obtener los datos a actualizar del CAJERO
                atmDataToUpdate = ui.getNewATMData()

                # Actualizar los datos del cajero con el código ingresado
                bank.updateATMDataByCode(codeATMChosen, atmDataToUpdate)

            # Actualizar transacción
            elif updateType == 2:
                # Mostrar las transacciones del cajero seleccionado
                bank.showATMTransactions(codeATMChosen)

                # Obtener los datos a actualizar de la TRANSACCIÓN
                index, transactionDataToUpdate = ui.getNewTransactionData()

                # Actualizar los datos de la transacción del cajero con el código ingresado
                bank.updateTransactionData(codeATMChosen, transactionDataToUpdate, index)



        elif userOption == 4:
            # DELETE
            pass
        elif userOption == 0:
            # EXIT
            mainloop = False