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
        for atm in self.__ATMs:
            atm.showATMData()