class Product:
    """Вспомогательный класс товара"""

    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price


class WarehouseManager:
    """
    ЗАДАЧА: Логика склада.
    1. add_product(product): добавляет объект Product в self.items.
    2. filter_by_category(cat): возвращает список ОБЪЕКТОВ только этой категории.
    3. get_total_value(): возвращает сумму цен всех товаров на складе (float/int).
    """

    def __init__(self):
        self.items = []

    def add_product(self, product: Product):
        self.items.append(product)

    def filter_by_category(self, category: str):
        result = []
        for product in self.items:
            if product.category == category:
                result.append(product)
        return result

    def get_total_value(self):

        total = 0
        for product in self.items:
            total += product.price
        return total