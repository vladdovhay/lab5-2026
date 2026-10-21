import unittest
from src.tavern import Tavern
from src.customer import Customer
from src.adventurer import Adventurer
from src.troublemaker import Troublemaker


class TestTavern(unittest.TestCase):
    def setUp(self):
        self.tavern = Tavern("П'яний дракон")
        self.customer = Customer("Ліра", "Ельф", 50, "Медовуха")
        self.hero = Adventurer("Арагорн", "Людина", 200, 5)
        self.guy = Troublemaker("Грумбл", "Гоблін", 20, 8)

    def test_add_visitor(self):
        self.tavern.add_visitor(self.customer)
        self.assertEqual(len(self.tavern), 1)

    def test_add_invalid_visitor(self):
        with self.assertRaises(TypeError):
            self.tavern.add_visitor("Не відвідувач")

    def test_remove_visitor(self):
        self.tavern.add_visitor(self.customer)
        self.tavern.remove_visitor(self.customer)
        self.assertEqual(len(self.tavern), 0)

    def test_remove_missing_visitor(self):
        with self.assertRaises(ValueError):
            self.tavern.remove_visitor(self.customer)

    def test_str(self):
        self.tavern.add_visitor(self.customer)
        self.assertEqual(str(self.tavern), "Таверна 'П'яний дракон': 1 відвідувачів")

    def test_repr(self):
        self.assertEqual(repr(self.tavern), "Tavern('П'яний дракон')")