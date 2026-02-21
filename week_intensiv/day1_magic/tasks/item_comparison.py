class Item:
    """ЗАДАЧА: Сравнение товаров по цене через __lt__ и по всем полям через __eq__"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price < other.price
    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price == other.price and self.name == other.name