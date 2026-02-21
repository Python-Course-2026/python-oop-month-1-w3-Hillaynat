class SmartPoint:
    """ЗАДАЧА: Реализовать __str__ (Точка(x, y)) и __repr__ (SmartPoint(x=x, y=y))"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Точка({self.x}, {self.y})"

    def __repr__(self):
        return f"SmartPoint(x={self.x}, y={self.y})"