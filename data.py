from player import Player
import json

class Data:
    def __init__(self, filename, player):
        self.filename = filename
        self.player = Player

    def create_player(self, player):
        new_data = {
            player.name: {
                "password": player.password,
                "score": player.score
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent =4)
        else:
            if data[player.name] in data:
                raise KeyError("can't create player, player ")
            else:
                data.update_player(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent =4)


    def update_player(self):
        pass

    def get_winrate(self):
        pass

    def get_wincount(self):
        pass

    def get_losecount(self):
        pass

    def test(self):
        pass
