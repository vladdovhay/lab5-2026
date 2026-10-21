from .visitor import Visitor


class Customer(Visitor):
    """Звичайний відвідувач."""

    def __init__(self, name, race, gold, favorite_drink):
        super().__init__(name, race, gold)
        self._favorite_drink = favorite_drink

    @property
    def favorite_drink(self):
        return self._favorite_drink

    def order(self):
        return self._favorite_drink

    def tip(self):
        return 1

    def __str__(self):
        return f"{super().__str__()} - улюблений напій: {self.favorite_drink}"

    def __repr__(self):
        return (f"Customer('{self.name}', '{self.race}', "
                f"{self.gold}, '{self.favorite_drink}')")