class Bank:
    def __init__(self, name="Banco Bummer :)", ATMs=[]):
        self.__name = name
        self.__ATMs = []

        for atm in ATMs:
            self.__ATMs.append(atm)