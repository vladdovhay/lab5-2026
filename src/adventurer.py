from .visitor import Visitor


class Adventurer(Visitor):
    """Герой-шукач пригод."""

    def __init__(self, name, race, gold, quest_level):
        super().__init__(name, race, gold)
        self._quest_level = quest_level

    @property
    def quest_level(self):
        return self._quest_level

    def order(self):
        return "Ростбіф та ель"

    def tip(self):
        # Чим вищий рівень героя, тим щедріші чайові
        return self._quest_level * 2

    def tell_story(self):
        return f"{self.name} розповідає історію про квест рівня {self.quest_level}"

    def __str__(self):
        return f"{super().__str__()} - рівень квесту: {self.quest_level}"

    def __repr__(self):
        return (f"Adventurer('{self.name}', '{self.race}', "
                f"{self.gold}, {self.quest_level})")