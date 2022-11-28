from player import Player
import json

class Data:
    def __init__(self, filename):
        self.filename = filename

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
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(self.filename, "w") as data_file:
                json.dump(new_player, data_file, indent=4)
        else:
            lst_name = [name for name in data.keys()]
            if player.name in lst_name:
                pass
            else:
                data.update(new_player)
                with open(self.filename, "w") as data_file:
                    json.dump(data, data_file, indent=4)

    def get_password(self, player):
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            return data[player.name]["password"]

    def get_lst_player(self):
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            lst_name = [name for name in data.keys()]
            return lst_name

    def get_information(self, player, inform):
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if inform == "win":
                return data[player.name]["score"]["win"]
            elif inform == "lose":
                return data[player.name]["score"]["lose"]
            elif inform == "draw":
                return data[player.name]["score"]["draw"]

    def update_data(self, player, status):
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if status == "win":
                player.score[0] += 1
                data[player.name]["score"]["win"] += 1
            elif status == "lose":
                player.score[1] += 1
                data[player.name]["score"]["lose"] += 1
            elif status == "draw":
                player.score[2] += 1
                data[player.name]["score"]["draw"] += 1
            with open(self.filename, "w") as data_file:
                json.dump(data, data_file, indent=4)
