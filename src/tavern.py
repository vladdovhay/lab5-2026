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

    def __len__(self):
        return len(self._visitors)

    def __str__(self):
        return f"Таверна '{self.name}': {len(self._visitors)} відвідувачів"

    def __repr__(self):
        return f"Tavern('{self.name}')"