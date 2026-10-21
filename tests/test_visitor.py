import unittest
from src.visitor import Visitor


class DummyVisitor(Visitor):
    """Тестовий підклас, щоб перевірити базовий клас."""

    def order(self):
        return "Вода"

    def tip(self):
        return 0


class TestVisitor(unittest.TestCase):
    def setUp(self):
        self.visitor = DummyVisitor("Грім", "Орк", 100)

    def test_attributes(self):
        self.assertEqual(self.visitor.name, "Грім")
        self.assertEqual(self.visitor.race, "Орк")
        self.assertEqual(self.visitor.gold, 100)

    def test_cannot_create_abstract(self):
        with self.assertRaises(TypeError):
            Visitor("Тест", "Ельф", 10)

    def test_pay(self):
        self.visitor.pay(30)
        self.assertEqual(self.visitor.gold, 70)

    def test_pay_not_enough_gold(self):
        with self.assertRaises(ValueError):
            self.visitor.pay(500)

    def test_str(self):
        self.assertEqual(str(self.visitor), "Грім (Орк), золото: 100")

    def test_repr(self):
        self.assertEqual(repr(self.visitor), "DummyVisitor('Грім', 'Орк', 100)")