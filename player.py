"""This is a class Player."""
class Player:
    """
    This is a class to create player for game.

    Attributes:
        name (str): Name of player.
        data (Data): Data to store player account.
        number (int): Number of players for playing the game.
    """
    def __init__(self, name, data, number=0):
        """
        The constructor for Player class.

        Parameters:
            name (str): Name of player.
            data (Data): Data to store player account.
            number (int): Number of players for playing the game.
        """
        self.name = name
        self.data = data
        self.number = number

    @property
    def name(self):
        """name property"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Set a name of player"""
        if not isinstance(new_name, str):
            raise TypeError("Name must be string")
        self.__name = new_name

    @property
    def data(self):
        """data property"""
        return self.__data

    @data.setter
    def data(self, new_data):
        """Set a data of player"""
        self.__data = new_data

    @property
    def number(self):
        """number property"""
        return self.__number

    @number.setter
    def number(self, new_number):
        """Set a number of player"""
        if not isinstance(new_number, int):
            raise TypeError("Number must be integer ")
        self.__number = new_number

    def login(self, password):
        """The function to login player."""
        data_account = self.data.get_data(self.name)
        if data_account["password"] == password:
            print("------------ Login success -------------")
            print(f"{'Welcome back '+self.name:^40}")
            print("----------------------------------------")
            return True
        print("Incorrect password")
        return False

    def register(self, password):
        """The function to register player."""
        print("---------- Create new account ----------")
        print(f"{'Name: '+self.name:^40}")
        print(f"{'Password: '+password:^40}")
        print("----------------------------------------")
        self.data.create_account(self.name, password)

    def get_win(self):
        """The function to get win count of player."""
        data_account = self.data.get_data(self.name)
        return data_account["score"]["win"]

    def get_lose(self):
        """The function to get lose count of player."""
        data_account = self.data.get_data(self.name)
        return data_account["score"]["lose"]

    def get_draw(self):
        """The function to get draw count of player."""
        data_account = self.data.get_data(self.name)
        return data_account["score"]["draw"]

    def get_winrate(self):
        """The function to get winrate of player."""
        data_account = self.data.get_data(self.name)
        win = data_account["score"]["win"]
        lose = data_account["score"]["lose"]
        draw = data_account["score"]["draw"]
        return (win / (win + lose + draw)) * 100
