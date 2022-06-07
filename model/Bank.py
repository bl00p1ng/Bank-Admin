import json
from model.ATM import ATM


class Bank:
    def __init__(self, name="Banco Bummer :)"):
        self.__name = name
        self.__ATMs = []

        # Los cajeros por defecto son los que se cargan desde la db
        db = dict()  # Almacena los datos del JSON como diccionarios

        try:
            with open('resources/data/db.json', 'r') as f:
                db = json.load(f)
        except:
            print("Error cargando el archivo JSON!!")

        # Instanciar clases
        atmCodes = list(db.keys())

        for code in atmCodes:
            status = db[code]['estado']
            model = db[code]['modeloCajero']
            transactions = db[code]['transacciones']
            zone = db[code]['zona']
            atm = ATM(code=code, status=status, model=model, transactions=transactions, zone=zone)

            self.__ATMs.append(atm)


    def addATM(self, atm):
        """
        Agrega un nuevo cajero a la lista de cajeros del banco
        Recibe por parametro un diccionario con los datos del 
        cajero ingresados por el usuario.
        """

        code = atm['codigo']
        status = atm['estado']
        model = atm['modeloCajero']
        transactions = atm['transacciones']
        zone = atm['zona']
        atm = ATM(code=code, status=status, model=model, transactions=transactions, zone=zone)

        self.__ATMs.append(atm)


    def showATMs(self):
        """
        Recorre todos los cajeros y les ordena que muestren atributos
        """
        for atm in self.__ATMs:
            atm.showATMData()


    def updateATMDataByCode(self, code, newData):
        """
        Busca un cajero por su código y actualiza sus datos
        Recibe por parámetro:
            code: el código del cajero a buscar
            newData:los datos que se van a actualizar en el cajero
        """

        for atm in self.__ATMs:
            if atm.getCode() == code:
                # Actulizar datos
                atm.setStatus(newData[0])
                atm.setModel(newData[1])
                atm.setZone(newData[2])


    def showATMTransactions(self, code):
        """
        Busca un cajero por su código y muestra sus transacciones enumeradas
        Recibe por parámetro:
            code: el código del cajero a buscar
        """
        for atm in self.__ATMs:
            if atm.getCode() == code:
                atm.showTransactions()


    def updateTransactionData(self, code, newData, index):
        """
        Busca un cajero por su código y actualiza una de sus transacciones
        Recibe por parámetro:
            code: el código del cajero a buscar
            newData: los datos que se van a actualizar en la transaccion
            index: el índice de la transacción a actualizar
        """

        for atm in self.__ATMs:
            if atm.getCode() == code:
                for tindex, transaction in enumerate(atm.getTransactions()):
                    if tindex == index:
                        transaction['fechaMovimiento'] = newData[0]
                        transaction['monto'] = newData[1]
                        transaction['tipoCuenta'] = newData[2]
                        transaction['tipoMovimiento'] = newData[3]


    def deleteATMByCode(self, code):
        """
        Busca un cajero por su código y borra sus datos
        Recibe por parámetro:
            code: el código del cajero a buscar
        """

        for index, atm in enumerate(self.__ATMs):
            if atm.getCode() == code:
                self.__ATMs.pop(index)


    def deleteATMTransaction(self, code, index):
        """
        Busca un cajero por su código y borra una de sus transacciones
        Recibe por parámetro:
            code: el código del cajero a buscar
            index: el índice de la transacción a eliminar
        """

        for atm in self.__ATMs:
            if atm.getCode() == code:
                atm.getTransactions().pop(index)