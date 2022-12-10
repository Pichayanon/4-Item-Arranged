"""This is a class Data."""
import json
class Data:
    """
    This is a class for store player account.

    Attributes:
        filename (str): Name of file for store player account.
    """
    def __init__(self, filename):
        """
        The constructor for Data class.

        Parameters:
            filename (str): Name of file for store player account.
        """
        self.filename = filename

    def login(self, player):
        """The function for player login."""
        new_account = {
            player.name: {
                "password": player.password,
                "score": {
                    "win": 0,
                    "lose": 0,
                    "draw": 0
                }
            }
        }
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(self.filename, "w") as data_file:
                json.dump(new_account, data_file, indent=4)
        else:
            if player.name in list(data.keys()):
                if data[player.name]["password"] == player.password:
                    print("╔.★.═════════════════════════════════════════════╗")
                    print(f"{'Login success':^51}")
                    print(f"{'Welcome back '+player.name:^51}")
                    print("╚═════════════════════════════════════════════.★.╝")
                    return True
                print("Incorrect password")
                return False
            else:
                print("╔.★.═════════════════════════════════════════════╗")
                print(f"{'Create new account':^51}")
                print(f"{'Name: '+player.name:^51}")
                print(f"{'Password: '+player.password:^51}")
                print("╚═════════════════════════════════════════════.★.╝")
                data.update(new_account)
                with open(self.filename, "w") as data_file:
                    json.dump(data, data_file, indent=4)
                return True

    def update_account(self, name, status):
        """The function for update account of player."""
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if status == "win":
                data[name]["score"]["win"] += 1
            elif status == "lose":
                data[name]["score"]["lose"] += 1
            elif status == "draw":
                data[name]["score"]["draw"] += 1
            with open(self.filename, "w") as data_file:
                json.dump(data, data_file, indent=4)

    def check_account(self, name):
        """The function for check account in data or not"""
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if name in list(data.keys()):
                return True
            return False

    def get_password(self, name):
        """The function to get password of account"""
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if name in list(data.keys()):
                return data[name]["password"]
            else:
                print("No name account")

    def get_score_account(self, name, status):
        """The function to get score of account."""
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print("No data file fount")
        else:
            if status == "win":
                return data[name]["score"]["win"]
            if status == "lose":
                return data[name]["score"]["lose"]
            if status == "draw":
                return data[name]["score"]["draw"]
