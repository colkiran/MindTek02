"""
any class that we declare in python is a child class of object class
object class is the base class of any class that we declare
"""
class Player:               # pascal casing
    def get_runs(self):     # methods
        print("runs scored.....")

# sachin is an object of Player Class
sachin = Player()               # it should call the constructor (calls the default                                     constructor)
print(type(sachin))

sachin.get_runs()

print("-" * 60)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))