import unittest
from src.adventurer import Adventurer


class TestAdventurer(unittest.TestCase):
    def setUp(self):
        self.hero = Adventurer("Арагорн", "Людина", 200, 5)

    def test_attributes(self):
        self.assertEqual(self.hero.name, "Арагорн")
        self.assertEqual(self.hero.quest_level, 5)

    def test_order(self):
        self.assertEqual(self.hero.order(), "Ростбіф та ель")

    def test_tip(self):
        self.assertEqual(self.hero.tip(), 10)

    def test_tell_story(self):
        self.assertEqual(self.hero.tell_story(),
                         "Арагорн розповідає історію про квест рівня 5")

    def test_str(self):
        expected = "Арагорн (Людина), золото: 200 - рівень квесту: 5"
        self.assertEqual(str(self.hero), expected)

    def test_repr(self):
        expected = "Adventurer('Арагорн', 'Людина', 200, 5)"
        self.assertEqual(repr(self.hero), expected)