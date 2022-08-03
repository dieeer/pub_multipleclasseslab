class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def reduce_wallet(self, subtraction):
        self.wallet -= subtraction

    def buy_drink(self, drink, pub):
        drink_price = drink.price
        self.reduce_wallet(drink_price)
        pub.increase_till(drink_price)
        