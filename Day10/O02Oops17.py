
class Animal:

    def __init__(self):
        print("Animal Ctor....")
        self.age = '1 yr'

    def eat(self):
        print("Animals eat.....")


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("Bird Ctor.....")
        self.weight = '1 kg'

    def fly(self):
        print('Birds Fly......')

class Chicken(Bird):

    def message(self):
        print("Chickens are breeded for consumption.....")

    # override the parent class properties
    def fly(self):
        print("Chicken's seldom fly.....")



chick = Chicken()
chick.message()

print("-" * 60)
# Bird (parent)
chick.fly()       #  calls local method
print(chick.weight)

print("-" * 60)
# animal (Ascestor)
chick.eat()
print(chick.age)

print("-" * 60)
print(chick.__dict__)
