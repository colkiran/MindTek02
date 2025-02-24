
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @staticmethod
    def CalcAvg(runs, balls):
        return (runs / balls * 100)

ply1 = Player('Rahul', 32)
ply1.get_details()
print("-" * 60)

ply1.runs = 78
print(f"Strike Rate is :{Player.CalcAvg(78, 60)}")
