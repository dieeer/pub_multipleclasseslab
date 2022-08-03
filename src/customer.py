class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def reduce_wallet(self, subtraction):
        self.wallet -= subtraction

    def age_checked(self):
        if self.age >= 18:
            return True
        else:
            return False
    
    def drunkenness_checked(self):
        if self.drunkenness <= 10:
            return True
        else:
            return False

    def buy_drink(self, drink, pub):
        drink_price = drink.price
        drink_units = drink.units
        if self.age_checked() & self.drunkenness_checked():
            self.reduce_wallet(drink_price)
            pub.increase_till(drink_price)
            self.drunkenness += drink_units
        else:
            print("no sale")
        