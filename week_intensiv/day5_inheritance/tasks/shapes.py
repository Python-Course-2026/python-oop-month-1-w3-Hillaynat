import math


class Shape:
    def get_area(self):
        return 0


class Circle(Shape):
    """
    Класс круга.
    Переопределяет get_area для расчета площади круга.
    """

    def __init__(self, radius):
        """
        Конструктор класса Circle.

        Args:
            radius (float): Радиус круга
        """
        self.radius = radius

    def get_area(self):
        """
        Возвращает площадь круга: π * r²

        Returns:
            float: Площадь круга
        """
        return math.pi * self.radius ** 2


class Square(Shape):
    """
    Класс квадрата.
    Переопределяет get_area для расчета площади квадрата.
    """

    def __init__(self, side):
        """
        Конструктор класса Square.

        Args:
            side (float): Длина стороны квадрата
        """
        self.side = side

    def get_area(self):
        """
        Возвращает площадь квадрата: сторона * сторона

        Returns:
            float: Площадь квадрата
        """
        return self.side * self.side