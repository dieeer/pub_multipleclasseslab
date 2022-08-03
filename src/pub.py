from xmlrpc.client import Boolean


class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till

    def increase_till(self, addition):
        self.till += addition
