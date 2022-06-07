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


    # GETTERS
    def getCode(self):
        return self.__code


    def getTransactions(self):
        return self.__transactions


    # SETTERS
    def setStatus(self, newStatus):
        self.__status = newStatus


    def setModel(self, newModel):
        self.__model = newModel


    def setZone(self, newZone):
        self.__zone = newZone
