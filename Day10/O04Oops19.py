
# overriding the parent class constructor

class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = '1 yr'

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def __init__(self):         # overriding the parent class Ctor
        super().__init__()      # calls the parent class Ctor
        print("Bird Ctor.....")
        self.weight = '1 kg'

    def fly(self):
        print("Birds fly.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 60)
print(cuckoo.__dict__)
