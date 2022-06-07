from turtle import update


class UI:
    def menu():
        """
        Mostrar el menu principal
        """

        print("""
 ____              _                  _           _       
|  _ \            | |        /\      | |         (_)      
| |_) | __ _ _ __ | | __    /  \   __| |_ __ ___  _ _ __  
|  _ < / _` | '_ \| |/ /   / /\ \ / _` | '_ ` _ \| | '_ \ 
| |_) | (_| | | | |   <   / ____ \ (_| | | | | | | | | | |
|____/ \__,_|_| |_|_|\_\ /_/    \_\__,_|_| |_| |_|_|_| |_|

:: Administrar cajeros y transacciones

1 --> Crear cajero y añadir transacciones
2 --> Mostar cajeros y sus transacciones
3 --> Actualizar cajero/transacción
4 --> Borrar cajero/transacción
0 --> Salir
        """)

        userOption = int(input('--> Ingresa una opción: '))
        return userOption


    def selectActionType(msg):
        """
        Determina sobre que datos se va a realizar una operación del CRUD
        Recibe por parametros:
            msg: Es un mensaje personalizado que se mostrará en el input()

        Retorna:
            1: En caso de que la operción se realice sobre los cajeros
            2: En caso de que la operción se realice sobre las transacciones
        """

        print(f"""
:: Deseas {msg} un cajero o una transacción

1 -> Cajero
2 -> Transacción
        """)

        actionType = int(input(f'-> Elije una opción: '))

        return actionType


    # CREATE
    def createForm():
        """
        Crea un cajero junto a sus respectivas transacciones
        """

        # Datos del cajero
        print(':: Datos del cajero')
        code = input('-> Ingresa el código del cajero: ')
        status = input('-> Ingresa el estado del cajero("Fuera  de Servicio", "Operando" o "Cerrado"): ').capitalize()
        model = int(input('-> Ingresa el modelo del cajero: '))
        zone = int(input('-> Ingresa la zona: '))

        # Ingresar transacciones
        makeOther = True
        transactionsCreated = []

        print(':: Datos de las transacciones')
        # Crear la cantidad de transacciones que desee el usuario
        while makeOther:
            date = input('-> Ingresa la fecha(DD-MM-AAAA): ')
            value = int(input('-> Ingresa el monto de la transacción: '))
            accountType = input('-> Ingresa el tipo de cuenta: ').lower()
            transactionType = input('-> Ingresa el tipo de transacción: ').lower()

            transactionsCreated.append({'fechaMovimiento': date, 
                                        'monto': value, 
                                        'tipoCuenta': accountType, 
                                        'tipoMovimiento': transactionType})

            makeOther = int(input('--> Quieres añadir otra transacción (1 - SI | 2 - NO): '))
            makeOther = True if makeOther == 1 else False

        return {'codigo': code, 
                'estado': status,
                'modeloCajero': model,
                'zona': zone,
                'transacciones': transactionsCreated}


    # UPDATE
    def updateForm():
        """
        Obtener el código del cajero a actualizar
        Retorna:
            codeATMChosen: el código del cajero a actualizar
        """

        print('\n***** ACTUALIZAR DATOS *****\n')
        codeATMChosen = input('-> Ingresa el código del cajero que quieres actualizar: ')

        return codeATMChosen


    def getNewATMData():
        """
        Recopila los datos a actualizar de un cajero
        Retorna:
            Una tupla con los datos a actualizar
        """

        newStatus = input('-> Ingresa el estado nuevo del cajero("Fuera  de Servicio", "Operando" o "Cerrado"): ').capitalize()
        newModel = int(input('-> Ingresa el modelo del cajero: '))
        newZone = int(input('-> Ingresa la zona: '))

        return (newStatus, newModel, newZone)


    def getNewTransactionData():
        """
        Recopila los datos a actualizar de una transacción
        Retorna:
            index: el índice de la transacción a actualizar
            Una tupla con los datos a actualizar de la transacción
        """

        index = int(input('-> Ingresa el índice de la transacción a actualizar: '))
        newdate = input('-> Ingresa la fecha(DD-MM-AAAA): ')
        newValue = int(input('-> Ingresa el monto de la transacción: '))
        newAccountType = input('-> Ingresa el tipo de cuenta: ').lower()
        newTransactionType = input('-> Ingresa el tipo de transacción: ').lower()

        return index, (newdate, newValue, newAccountType, newTransactionType)
