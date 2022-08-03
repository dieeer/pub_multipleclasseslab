import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 40.00, 21, 0)
        self.drink = Drink("Bud", 3.50, 2)
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    
    def test_increase_till(self):
        self.pub.increase_till(2.5)
        self.assertEqual(102.5, self.pub.till)

