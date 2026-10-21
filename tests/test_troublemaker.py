import unittest
from src.troublemaker import Troublemaker


class TestTroublemaker(unittest.TestCase):
    def setUp(self):
        self.guy = Troublemaker("Грумбл", "Гоблін", 20, 8)

    def test_attributes(self):
        self.assertEqual(self.guy.name, "Грумбл")
        self.assertEqual(self.guy.rowdiness, 8)

    def test_order(self):
        self.assertEqual(self.guy.order(), "Найміцніший грог")

    def test_tip(self):
        self.assertEqual(self.guy.tip(), 0)

    def test_start_fight(self):
        self.assertIn("починає бійку", self.guy.start_fight())

    def test_str(self):
        expected = "Грумбл (Гоблін), золото: 20 - буйність: 8"
        self.assertEqual(str(self.guy), expected)

    def test_repr(self):
        expected = "Troublemaker('Грумбл', 'Гоблін', 20, 8)"
        self.assertEqual(repr(self.guy), expected)