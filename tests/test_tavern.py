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

    def _fill(self):
        self.tavern.add_visitor(self.customer)
        self.tavern.add_visitor(self.hero)
        self.tavern.add_visitor(self.guy)

    def test_search_by_name(self):
        self._fill()
        result = self.tavern.search("арагорн")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "Арагорн")

    def test_search_by_race(self):
        self._fill()
        result = self.tavern.search("гоблін")
        self.assertEqual(len(result), 1)

    def test_filter_by_type(self):
        self._fill()
        heroes = self.tavern.filter_by_type(Adventurer)
        self.assertEqual(len(heroes), 1)
        self.assertIsInstance(heroes[0], Adventurer)

    def test_filter_by_min_gold(self):
        self._fill()
        rich = self.tavern.filter_by_min_gold(50)
        self.assertEqual(len(rich), 2)

    def test_sort_by_gold(self):
        self._fill()
        result = self.tavern.sort_by_gold()
        self.assertEqual(result[0].name, "Грумбл")
        self.assertEqual(result[-1].name, "Арагорн")

    def test_sort_by_gold_reverse(self):
        self._fill()
        result = self.tavern.sort_by_gold(reverse=True)
        self.assertEqual(result[0].name, "Арагорн")

    def test_sort_by_name(self):
        self._fill()
        result = self.tavern.sort_by_name()
        self.assertEqual(result[0].name, "Арагорн")

    def test_serve_all(self):
        self._fill()
        result = self.tavern.serve_all()
        self.assertEqual(len(result), 3)
        self.assertIn("Ліра замовляє: Медовуха", result)

    def test_total_tips(self):
        self._fill()
        # 1 (Customer) + 10 (Adventurer) + 0 (Troublemaker)
        self.assertEqual(self.tavern.total_tips(), 11)