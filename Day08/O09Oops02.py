
class Player:

    def __init__(self):         # constructor
        print("Player Initialized.......")

    def get_runs(self):
        print("runs scored......")

    def __del__(self):
        print("Player object deleted......")

sachin = Player()       # calls the constructor
sourav = Player()
sachin.__init__()
print("-" * 60)

sachin.get_runs()
sourav.get_runs()

del sachin

print("-" * 60)


