class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False


class SavingsAccount(Account):
    """Сберегательный счет: нельзя снимать больше, чем есть (уже в родителе)"""
    pass


class BusinessAccount(Account):
    """
    Бизнес-счет:
    1. Комиссия за каждый перевод (transfer) – 5% от суммы.
    2. Позволяет уходить в минус до лимита -1000.
    """

    def withdraw(self, amount):
        """
        Переопределенный метод снятия с учетом возможности ухода в минус до -1000.

        Args:
            amount (float): Сумма для снятия

        Returns:
            bool: True если снятие успешно, False если недостаточно средств с учетом лимита
        """
        if self._balance - amount >= -1000:
            self._balance -= amount
            return True
        return False


class BankPro:
    """
    ЗАДАЧА: Реализовать логику перевода между счетами.
    Метод transfer(from_acc, to_acc, amount):
    1. Если from_acc – BusinessAccount, сумма списания = amount + 5% комиссии.
    2. Если на from_acc недостаточно средств (с учетом его правил withdraw), вернуть "Ошибка".
    3. Если всё ок:
       - Считать деньги с from_acc.
       - Зачислить amount (без комиссии!) на to_acc.
       - Вернуть "Успех".
    """

    def transfer(self, from_acc, to_acc, amount):
        """
        Осуществляет перевод между счетами.

        Args:
            from_acc (Account): Счет отправителя
            to_acc (Account): Счет получателя
            amount (float): Сумма перевода

        Returns:
            str: "Успех" если перевод выполнен, "Ошибка" если недостаточно средств
        """
        # Определяем сумму списания в зависимости от типа счета отправителя
        if isinstance(from_acc, BusinessAccount):
            # Для бизнес-счета: сумма + 5% комиссии
            withdrawal_amount = amount * 1.05  # amount + 5%
        else:
            # Для обычного счета: просто сумма
            withdrawal_amount = amount

        # Пытаемся снять деньги со счета отправителя
        if from_acc.withdraw(withdrawal_amount):
            # Если снятие успешно, зачисляем сумму (без комиссии) получателю
            to_acc.deposit(amount)
            return "Успех"
        else:
            # Если недостаточно средств
            return "Ошибка"