class Device:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def toggle(self):
        self.is_on = not self.is_on


class Light(Device):
    """
    Класс света, наследующийся от Device.

    ЗАДАЧА: Наследование и расширение.
    1. Конструктор принимает brand и brightness (от 0 до 100).
    2. Метод work() возвращает:
       "Свет включен, яркость: X%" если is_on True,
       "Свет выключен" если is_on False.
    """

    def __init__(self, brand, brightness):
        """
        Конструктор класса Light.

        Args:
            brand (str): Бренд устройства
            brightness (int): Яркость света (от 0 до 100)
        """
        # Вызываем конструктор родительского класса для инициализации brand и is_on
        super().__init__(brand)

        # Добавляем новый атрибут brightness
        # Можно добавить проверку, что яркость в допустимых пределах
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            # Если яркость вне диапазона, устанавливаем значение по умолчанию
            self.brightness = 50
            print(f"Предупреждение: яркость должна быть от 0 до 100. Установлено значение 50.")

    def work(self):
        """
        Возвращает строку с состоянием света.

        Returns:
            str: Описание состояния света
        """
        if self.is_on:
            return f"Свет включен, яркость: {self.brightness}%"
        else:
            return "Свет выключен"