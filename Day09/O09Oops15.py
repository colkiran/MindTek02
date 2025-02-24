
class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, val):
        self.__price = val

    @price.deleter
    def price(self):
        self.__price = 0

coke = Product(120)
print(coke.price)

coke.price = 85
print(coke.price)

del coke.price
print(coke.price)

coke.price = 150
print(coke.price)
