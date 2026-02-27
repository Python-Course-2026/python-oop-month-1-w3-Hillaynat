class Event:
    """Класс-контейнер для данных о событии"""

    def __init__(self, title: str, date: str, participants: int):
        self.title = title
        self.date = date  # Формат "ГГГГ-ММ-ДД"
        self.participants = participants


class EventPlanner:
    """
    ЗАДАЧА: Аналитика событий.
    1. get_events_on_date(date): возвращает список НАЗВАНИЙ (str) событий на эту дату.
    2. get_total_participants(): возвращает общее число участников всех событий.
    """

    def __init__(self):
        self.events = []

    def add_event(self, event):
        # Добавляет объект Event в список
        self.events.append(event)

    def get_events_on_date(self, date):
        """
        Возвращает список названий событий на указанную дату.

        Args:
            date (str): Дата в формате "ГГГГ-ММ-ДД"

        Returns:
            list: Список названий событий (str)
        """
        result = []
        for event in self.events:
            if event.date == date:
                result.append(event.title)
        return result

    def get_total_participants(self):
        """
        Возвращает общее количество участников всех событий.

        Returns:
            int: Сумма participants по всем событиям
        """
        total = 0
        for event in self.events:
            total += event.participants
        return total