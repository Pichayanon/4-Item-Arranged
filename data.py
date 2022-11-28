from player import Player
import json

class Data:
    def __init__(self, name):
        self.name = name

    def create_player(self, player):
        new_player = {
            player.name: {
                "password": player.password,
                "score": {
                    "win": player.score[0],
                    "lose": player.score[1],
                    "draw": player.score[2]
                }
            }
        }
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_player, data_file, indent=4)
        else:
            lst_name = [name for name in data.keys()]
            if player.name in lst_name:
                if player.password == data[player.name]["password"]:
                    data.update(new_player)
                    with open("data.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                else:
                    print("wrong password")
            else:
                data.update(new_player)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
    def get_information(self, player, inform):
        try:
            with open("data.json", "r") as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if inform == "win":
                return player.score[0]
            elif inform == "lose":
                return player.score[1]
            elif inform == "draw":
                return player.score[2]

    def update_data(self, player, status):
        try:
            with open("data.json", "r") as data_file:
                data_dict = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if status == "win":
                player.score[0] += 1
            elif status == "lose":
                player.score[1] += 1
            elif status == "draw":
                player.score[2] += 1
            with open("data.json", "w") as data_file:
                json.dump(data_dict, data_file, indent=4)
