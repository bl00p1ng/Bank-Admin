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