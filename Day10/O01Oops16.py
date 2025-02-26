"""
Recap
-----
1. class
2. object
3. isinstance()
4. __init__()
5. self, __dict__
6. class attribute
7. class method, cls, @classmethod
8. static method
9. Operator Overloading (Magic methods), __str__, __eq__, __gt__
__add__, __sub__,......
10. private variable __price
11. property(), @ property - setter, getter and deleter
"""

# inheritance
class Animal:
    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds Fly......")

class Fish(Animal):

    def swim(self):
        print("Fishes swim......")

cuckoo = Bird()         # Animal class constructor will get executed
cuckoo.eat()            # calls the eat method from animal class
cuckoo.fly()

print("-" * 60)

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 60)

print(f'cuckooo :{cuckoo.__dict__}')
print(f'dolphin :{dolphin.__dict__}')
