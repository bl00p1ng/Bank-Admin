class ATM:
    def __init__(self, code='Sin código', status="Sin definir", model=000, transactions=[], zone=0):
        self.code = code
        self.status = status
        self.model = model
        self.transactions = transactions
        self.zone = zone