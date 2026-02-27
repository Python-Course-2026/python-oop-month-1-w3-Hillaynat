class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Participant:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.inventory = []


class Market:
    """
    ЗАДАЧА: Реализовать метод deal(buyer, seller, item).
    1. Проверить, есть ли у buyer достаточное денег (money >= item.price).
    2. Если денег нет, вызвать ValueError("Недостаточно средств").
    3. Если деньги есть:
       - Вычесть цену из денег buyer.
       - Добавить цену к деньгам seller.
       - Добавить item в список buyer.inventory.
    """

    def deal(self, buyer: Participant, seller: Participant, item: Item):
        """
        Осуществляет сделку между покупателем и продавцом.

        Args:
            buyer (Participant): Покупатель
            seller (Participant): Продавец
            item (Item): Товар для покупки

        Returns:
            None

        Raises:
            ValueError: Если у покупателя недостаточно средств
        """
        # Проверяем, достаточно ли денег у покупателя
        if buyer.money < item.price:
            raise ValueError("Недостаточно средств")

        # Выполняем сделку
        buyer.money -= item.price  # Снимаем деньги с покупателя
        seller.money += item.price  # Добавляем деньги продавцу
        buyer.inventory.append(item)  # Добавляем товар в инвентарь покупателя

        # Можно добавить информационное сообщение (опционально)
        print(f"Сделка совершена: {buyer.name} купил {item.name} за {item.price} у {seller.name}")