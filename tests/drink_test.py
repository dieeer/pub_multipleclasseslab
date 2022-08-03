import unittest
from src.drink import Drink
from src.customer import Customer
from src.pub import Pub

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Dave", 40.00)
        self.drink = Drink("Bud", 3.50)
        
    def test_drink_has_name(self):
        self.assertEqual("Bud", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(3.50, self.drink.price)