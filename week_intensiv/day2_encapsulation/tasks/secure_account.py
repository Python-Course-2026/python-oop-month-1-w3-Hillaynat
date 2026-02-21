class SecureAccount:
    """ЗАДАЧА: Приватный __balance, геттер @property и депозит с проверкой > 0"""
    def __init__(self, bal):
        self.__balance = bal
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
        else:
            raise ValueError