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

    def create_account(self, name, password):
        """The function to create account."""
        new_account = {
            name: {
                "password": password,
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
            data.update(new_account)
            with open(self.filename, "w") as data_file:
                json.dump(data, data_file, indent=4)

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
            return name in list(data.keys())
        except FileNotFoundError:
            return False
        except KeyError:
            return False

    def get_data(self, name):
        """The function for get data of account"""
        try:
            with open(self.filename, "r") as data_file:
                data = json.load(data_file)
            return data[name]
        except FileNotFoundError:
            print("No data file fount")
        except KeyError:
            return False

