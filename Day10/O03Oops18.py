
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("Animals eat.....")

    def fun(self):
        print("Fun method of Animal class")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def walk(self):
        print("Person walks.....")

    def fun(self):
        print("Fun method of person class")


class Girl(Animal, Person):

    def __init__(self):
        super().__init__()          # calls the parent class Ctor
        Person.__init__(self)
        print("Girl Ctor.....")
        self.g = 30

    def talk(self):
        print("Girls talk.....")

mary = Girl()
mary.eat()
mary.walk()
mary.talk()

print("-" * 60)
mary.fun()

print("-" * 60)
print(Girl.mro())           # method resolution order

print("-" * 60)
print(mary.__dict__)
