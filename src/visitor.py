from abc import ABC, abstractmethod


class Visitor(ABC):
    """Базовий абстрактний клас відвідувача таверни."""

    def __init__(self, name, race, gold):
        # інкапсуляція
        self._name = name
        self._race = race
        self._gold = gold

    @property
    def name(self):
        return self._name

    @property
    def race(self):
        return self._race

    @property
    def gold(self):
        return self._gold

    def pay(self, amount):
        """Заплатити за замовлення."""
        if amount > self._gold:
            raise ValueError("Недостатньо золота")
        self._gold -= amount

    @abstractmethod
    def order(self):
        """Що замовляє відвідувач."""

    @abstractmethod
    def tip(self):
        """Скільки чайових залишає відвідувач."""

    def __str__(self):
        return f"{self.name} ({self.race}), золото: {self.gold}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.race}', {self.gold})"