class Order:
    def __init__(self, order_id, address):
        self.order_id = order_id
        self.address = address
        self.status = "In processing"  # Статусы: "In processing", "Delivered"


class Courier:
    def __init__(self, name):
        self.name = name
        self.is_busy = False


class DeliveryService:
    """
    ЗАДАЧА: Реализовать метод deliver(order, courier).
    1. Если курьер занят (is_busy), вернуть "Курьер занят".
    2. Если свободен:
       - Установить courier.is_busy в True.
       - Изменить order.status на "Delivered".
       - Вернуть "Заказ {id} доставлен курьером {name}".
    """

    def deliver(self, order: Order, courier: Courier):
        """
        Обрабатывает доставку заказа указанным курьером.

        Args:
            order (Order): Заказ для доставки
            courier (Courier): Курьер, который должен доставить заказ

        Returns:
            str: Сообщение о результате доставки
        """
        # Проверяем, занят ли курьер
        if courier.is_busy:
            return "Курьер занят"

        # Если курьер свободен
        courier.is_busy = True  # Помечаем курьера как занятого
        order.status = "Delivered"  # Меняем статус заказа

        # Возвращаем сообщение о успешной доставке
        return f"Заказ {order.order_id} доставлен курьером {courier.name}"