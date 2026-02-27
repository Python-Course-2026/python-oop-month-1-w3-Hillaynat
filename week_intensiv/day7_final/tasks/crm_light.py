class Client:
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Client(id={self.client_id}, name='{self.name}')"


class CRM:
    """
    ЗАДАЧА: Управление клиентами.
    1. add_client(client): добавляет объект Client в список self.clients.
    2. get_client(client_id): возвращает объект клиента по ID или None.
    3. delete_client(client_id): удаляет клиента из списка.
    4. update_client(client_id, **kwargs): находит клиента и обновляет его
       атрибуты (name, email), переданные в kwargs.
    """

    def __init__(self):
        self.clients = []

    def add_client(self, client: Client):
        self.clients.append(client)

    def get_client(self, client_id):
        """
        Возвращает объект клиента по ID или None, если клиент не найден.

        Args:
            client_id: ID клиента для поиска

        Returns:
            Client or None: Найденный клиент или None
        """
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def delete_client(self, client_id):
        """
        Удаляет клиента из списка по ID.

        Args:
            client_id: ID клиента для удаления
        """
        # Находим индекс клиента с указанным ID
        for i, client in enumerate(self.clients):
            if client.client_id == client_id:
                del self.clients[i]
                break

    def update_client(self, client_id, **kwargs):
        """
        Обновляет атрибуты клиента.

        Пример: update_client(1, name="New Name") должен изменить только имя.
        Используйте setattr(obj, key, value) для динамического обновления.

        Args:
            client_id: ID клиента для обновления
            **kwargs: Пары ключ-значение для обновления атрибутов
        """
        # Находим клиента
        client = self.get_client(client_id)

        # Если клиент найден, обновляем его атрибуты
        if client:
            for key, value in kwargs.items():
                # Проверяем, что атрибут существует у объекта Client
                if hasattr(client, key):
                    setattr(client, key, value)