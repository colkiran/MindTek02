
class Player:

    team_head_name=""

    @classmethod
    def set_head_name(cls, name):
        Player.team_head_name = name

    @classmethod
    def get_head_name(cls):
        print(Player.team_head_name)


Player.set_head_name('Kevin')
Player.get_head_name()


