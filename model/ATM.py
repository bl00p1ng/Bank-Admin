import re


class ATM:
    def __init__(self, code='Sin código', status="Sin definir", model=000, transactions=[], zone=0):
        self.__code = code
        self.__status = status
        self.__model = model
        self.__transactions = transactions
        self.__zone = zone


    def showATMData(self):
        """
        Mostar de forma visual los datos del cajero
        """

        print(f'\n********* Cajero: {self.__code} *********')
        print('+---------------+-----------------+')
        print(f'| Estado:       | {self.__status}')
        print(f'| Modelo:       | {self.__model}')
        print(f'| Zona:         | {self.__zone}')
        print('+---------------+-----------------+')
        print('|         TRANSACCIONES           |')
        print(f"+{''.join(['-']) * 21}+{''.join(['-']) * 11}+")
        for transaction in self.__transactions:
            print(f'| Fecha:              | {transaction["fechaMovimiento"]}')
            print(f'| Monto:              | {transaction["monto"]}')
            print(f'| Tipo de Cuenta:     | {transaction["tipoCuenta"]}')
            print(f'| Tipo de Movimiento: | {transaction["tipoMovimiento"]}')
            print(f"+{''.join(['-']) * 33}+")


    def showTransactions(self):
        """
        Muestra las transacciones del cajero junto a su índice
        """

        print('+---------------------------------+')
        print('|         TRANSACCIONES           |')
        for index, transaction in enumerate(self.__transactions):
            print('+---------------------------------+')
            print(f'| --> INDICE: {index}                   |')
            print(f"+{''.join(['-']) * 21}+{''.join(['-']) * 11}+")
            print(f'| Fecha:              | {transaction["fechaMovimiento"]}')
            print(f'| Monto:              | {transaction["monto"]}')
            print(f'| Tipo de Cuenta:     | {transaction["tipoCuenta"]}')
            print(f'| Tipo de Movimiento: | {transaction["tipoMovimiento"]}')
            print(f"+{''.join(['-']) * 33}+")


    def getConsignment(self):
        """
        Obtiene las consignaciones
        Retona:
            consignmentValues: lista con los valores de las consignaciones
        """
        
        consignments = list(filter(lambda t: t['tipoMovimiento'] == 'consignacion', self.__transactions))
        consignmentValues = list(map(lambda c: c['monto'], consignments))

        return consignmentValues


    def getWithdrawal(self):
        """
        Obtiene los retiros del cajero
        Retona:
            withdrawalValues: lista con los valores de los retiros
        """
        
        withdrawals = list(filter(lambda t: t['tipoMovimiento'] == 'retiro', self.__transactions))
        withdrawalValues = list(map(lambda c: c['monto'], withdrawals))

        return withdrawalValues


    def countTransfers(self):
        """
        Cuenta la cantidad de transferencias del cajero
        Retorna:
            transferNumber: la cantidad de transferencias del cajero
        """

        transferNumber = len(list(filter(lambda t: t['tipoMovimiento'] == 'transferencia', self.__transactions)))

        return transferNumber


    def getJanuaryConsignments(self):
        """
        Obtiene las consignaciones hechas en enero de 2021
        Retona:
            januaryConsignments: cantidad de consignaciones hechas en enero del 2021
        """
        
        consignments = list(filter(lambda t: t['tipoMovimiento'] == 'consignacion', self.__transactions))
        januaryConsignments = list(filter(lambda c: re.search(r'-01-2021', c['fechaMovimiento']), consignments))

        return januaryConsignments


    # GETTERS
    def getCode(self):
        return self.__code


    def getStatus(self):
        return self.__status


    def getModel(self):
        return self.__model


    def getZone(self):
        return self.__zone


    def getTransactions(self):
        return self.__transactions


    # SETTERS
    def setStatus(self, newStatus):
        self.__status = newStatus


    def setModel(self, newModel):
        self.__model = newModel


    def setZone(self, newZone):
        self.__zone = newZone
