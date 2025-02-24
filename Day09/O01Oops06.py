
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fn, ln, age):
        print("factory....")
        return cls(f'{fn} {ln}', age)           #calls constructor

ply1 = Player("Virat", 36)
ply1.get_details()
print("-" * 60)

ply2 = Player.createPlayer('Rohit', 'Sharma', 38)
ply2.get_details()
