class Wallet:
    """ЗАДАЧА: Сложение кошельков через __add__ (новый Wallet) и длина через __len__ (целый баланс)"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __add__(self, other):
        return Wallet("Joint Account", self.balance + other.balance)
    def __len__(self):
        return int(self.balance)
