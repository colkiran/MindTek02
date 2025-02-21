"""
self will have the name of the object that called the method
all instance variables will be stored in a dictionary __dict__ of the object
"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_detials(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player('Sachin', 35)
ply1.get_detials()
print("-" * 60)

ply2 = Player('Rahul', 32)
ply2.get_detials()
print("-" * 60)

ply2.runs = 150
print(f"ply2 :{ply2.__dict__}")

print("-" * 60)
print(f"ply1 :{ply1.__dict__}")
