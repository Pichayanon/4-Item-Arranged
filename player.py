"""This is a class Player."""
class Player:
    """
    This is a class to create player for game.

    Attributes:
        name (str): Name of player.
        password (str): Password of player.
        data (Data): Data to store player account.
        number (int): Number of players for playing the game.
    """
    def __init__(self, name, password, data, number=0):
        """
        The constructor for Player class.

        Parameters:
            name (str): Name of player.
            password (str): Password of player.
            data (Data): Data to store player account.
            number (int): Number of players for playing the game.
        """
        self.name = name
        self.password = password
        self.data = data
        self.number = number

    @property
    def name(self):
        """Set a name of player"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Set a name of player"""
        if not isinstance(new_name, str):
            raise TypeError("Name must be string")
        self.__name = new_name

    @property
    def password(self):
        """Set a password of player"""
        return self.__password

    @password.setter
    def password(self, new_password):
        """Set a password of player"""
        if new_password == "":
            raise ValueError("Password is empty")
        self.__password = new_password

    @property
    def number(self):
        """Set a number of player"""
        return self.__number

    @number.setter
    def number(self, new_number):
        """Set a number of player"""
        if not isinstance(new_number, int):
            raise TypeError("Number must be integer ")
        self.__number = new_number

    def get_win(self):
        """The function to get win count of player."""
        return self.data.get_score_account(self.name, 'win')

    def get_lose(self):
        """The function to get lose count of player."""
        return self.data.get_score_account(self.name, 'lose')

    def get_draw(self):
        """The function to get draw count of player."""
        return self.data.get_score_account(self.name, 'draw')

    def get_winrate(self):
        """The function to get winrate of player."""
        win = self.data.get_score_account(self.name, "win")
        lose = self.data.get_score_account(self.name, "lose")
        draw = self.data.get_score_account(self.name, "draw")
        return (win / (win + lose + draw)) * 100
