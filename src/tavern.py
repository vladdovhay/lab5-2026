from .visitor import Visitor


class Tavern:
    """Клас-менеджер, що керує колекцією відвідувачів."""

    def __init__(self, name):
        self._name = name
        self._visitors = []

    @property
    def name(self):
        return self._name

    def add_visitor(self, visitor):
        if not isinstance(visitor, Visitor):
            raise TypeError("Можна додавати тільки об'єкти Visitor")
        self._visitors.append(visitor)

    def remove_visitor(self, visitor):
        if visitor not in self._visitors:
            raise ValueError("Такого відвідувача немає в таверні")
        self._visitors.remove(visitor)

    def get_all(self):
        # Повертаємо копію, щоб не можна було змінити список ззовні
        return list(self._visitors)

    def search(self, keyword):
        """Пошук за ім'ям або расою."""
        keyword = keyword.lower()
        return [v for v in self._visitors
                if keyword in v.name.lower() or keyword in v.race.lower()]

    def filter_by_type(self, visitor_type):
        """Фільтр за типом відвідувача (Customer, Adventurer...)."""
        return [v for v in self._visitors if isinstance(v, visitor_type)]

    def filter_by_min_gold(self, min_gold):
        return [v for v in self._visitors if v.gold >= min_gold]

    def sort_by_gold(self, reverse=False):
        return sorted(self._visitors, key=lambda v: v.gold, reverse=reverse)

    def sort_by_name(self):
        return sorted(self._visitors, key=lambda v: v.name)

    def serve_all(self):
        """Поліморфізм: у кожного типу відвідувача свій order()."""
        return [f"{v.name} замовляє: {v.order()}" for v in self._visitors]

    def total_tips(self):
        """Поліморфізм: у кожного типу відвідувача свій tip()."""
        return sum(v.tip() for v in self._visitors)

    def __len__(self):
        return len(self._visitors)

    def __str__(self):
        return f"Таверна '{self.name}': {len(self._visitors)} відвідувачів"

    def __repr__(self):
        return f"Tavern('{self.name}')"