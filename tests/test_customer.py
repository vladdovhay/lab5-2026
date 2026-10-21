import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Ліра", "Ельф", 50, "Медовуха")

    def test_attributes(self):
        self.assertEqual(self.customer.name, "Ліра")
        self.assertEqual(self.customer.favorite_drink, "Медовуха")

    def test_order(self):
        self.assertEqual(self.customer.order(), "Медовуха")

    def test_tip(self):
        self.assertEqual(self.customer.tip(), 1)

    def test_str(self):
        expected = "Ліра (Ельф), золото: 50 - улюблений напій: Медовуха"
        self.assertEqual(str(self.customer), expected)

    def test_repr(self):
        expected = "Customer('Ліра', 'Ельф', 50, 'Медовуха')"
        self.assertEqual(repr(self.customer), expected)