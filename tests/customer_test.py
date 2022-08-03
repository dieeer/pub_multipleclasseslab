import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 40.00)
        self.drink = Drink("Bud", 3.50)
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Dave", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(40.00, self.customer.wallet)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.5)
        self.assertEqual(36.50, self.customer.wallet)

    def test_buy_drink(self): 
        self.customer.buy_drink(self.drink, self.pub)
        self.assertEqual(36.50, self.customer.wallet)
        self.assertEqual(103.50, self.pub.till)