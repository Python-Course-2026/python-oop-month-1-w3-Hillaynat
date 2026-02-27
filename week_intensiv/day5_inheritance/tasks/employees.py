class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


class Developer(Employee):
    """
    Класс разработчика с бонусом к зарплате.
    """

    def __init__(self, name, base_salary, bonus):
        """
        Конструктор класса Developer.

        Args:
            name (str): Имя сотрудника
            base_salary (float): Базовая зарплата
            bonus (float): Бонус к зарплате
        """
        # Вызываем конструктор родительского класса для инициализации name и base_salary
        super().__init__(name, base_salary)
        # Добавляем новый атрибут bonus
        self.bonus = bonus

    def calculate_salary(self):
        """
        Переопределенный метод расчета зарплаты.
        Возвращает базовую зарплату + бонус.
        """
        return self.base_salary + self.bonus