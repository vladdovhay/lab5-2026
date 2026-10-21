from .visitor import Visitor


class Troublemaker(Visitor):
    """Проблемний відвідувач, який створює конфлікти."""

    def __init__(self, name, race, gold, rowdiness):
        super().__init__(name, race, gold)
        self._rowdiness = rowdiness

    @property
    def rowdiness(self):
        return self._rowdiness

    def order(self):
        return "Найміцніший грог"

    def tip(self):
        return 0

    def start_fight(self):
        return f"{self.name} починає бійку! (буйність: {self.rowdiness})"

    def __str__(self):
        return f"{super().__str__()} - буйність: {self.rowdiness}"

    def __repr__(self):
        return (f"Troublemaker('{self.name}', '{self.race}', "
                f"{self.gold}, {self.rowdiness})")