class Hero:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk


class Battle:
    """
    Класс для симуляции боя между героями.
    """

    def fight(self, h1: Hero, h2: Hero):
        # Проверка на мертвых героев в начале боя
        if h1.hp <= 0 and h2.hp <= 0:
            return "Ничья - оба мертвы"
        elif h1.hp <= 0:
            return h2.name
        elif h2.hp <= 0:
            return h1.name

        # Основной цикл боя
        while h1.hp > 0 and h2.hp > 0:
            # Ход первого героя
            h2.hp -= h1.atk

            # Проверка, жив ли второй герой после атаки
            if h2.hp > 0:
                # Ответный удар второго героя
                h1.hp -= h2.atk

        # Определение победителя
        if h1.hp > 0:
            return h1.name
        elif h2.hp > 0:
            return h2.name
        else:
            return "Ничья"