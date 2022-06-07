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
            userAction = ui.readForm()

            if userAction == 1:
                bank.showATMs()
            elif userAction == 2:
                userChoise = ui.requirements()

                if userChoise == 'A':
                    higherConsignments = bank.firstRequirement()
                    ui.showMsg('La consignación más alta de cada cajero\n (código cajero, valor consignación)\n', higherConsignments)

                elif userChoise == 'B':
                    lowestWithdrawals = bank.secondRequirement()
                    ui.showMsg('El retiro menor de cada cajero\n (código cajero, valor retiro)\n', lowestWithdrawals)

                elif userChoise == 'C':
                    atmWithMoreTransfers = bank.thirdRequirement()
                    ui.showMsg('El cajero con más transferencias\n (código cajero, número de transferencias)\n', atmWithMoreTransfers)

                elif userChoise == 'D':
                    januaryConsignments = bank.fouthRequeriment()
                    ui.showMsg('El total de consignaciones en Enero del 2021 fue', januaryConsignments)


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
            # Saber si se quiere BORRAR un cajero o una transacción
            deleteType = ui.selectActionType('eliminar')

            bank.showATMs()  # Mostrar cajeros

            # Obtener el codigo del cajero a borrar
            codeATMChosen = ui.deleteForm()

            if deleteType == 1:
                # Borrar los datos del cajero con el código ingresado
                bank.deleteATMByCode(codeATMChosen)

            elif deleteType == 2:
                # Mostrar las transacciones del cajero seleccionado
                bank.showATMTransactions(codeATMChosen)

                # Obtener el índice de la transacción a eliminar
                indexTransaction = ui.getTransactionIndex()

                bank.deleteATMTransaction(codeATMChosen, indexTransaction)

        elif userOption == 0:
            # EXIT
            # Guardar cambios en disco
            bank.saveData()

            mainloop = False
