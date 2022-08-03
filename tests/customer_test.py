import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 40.00, 21, 0)
        self.customer2 = Customer("Buster", 5.0, 17, 15)
        self.drink = Drink("Bud", 3.50, 2)
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(40.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)

    def test_age_checked__True(self):
        self.assertEqual(True, self.customer.age_checked())

    def test_age_checked__False(self):
        self.assertEqual(False, self.customer2.age_checked())

    def test_customer_has_drunknness(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_drunkenness_checked(self):
        self.assertEqual(True, self.customer.drunkenness_checked())

    def test_drunkenness_checked(self):
        self.assertEqual(False, self.customer2.drunkenness_checked())

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.5)
        self.assertEqual(36.50, self.customer.wallet)

    def test_buy_drink(self): 
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(36.50, self.customer.wallet)
        self.assertEqual(103.50, self.pub.till)
        self.assertEqual(2, self.customer.drunkenness)