class Player:
    def __init__(self, name, password, data, number=0, score=[0, 0, 0]):
        self.name = name
        self.password = password
        self.data = data
        self.number = number
        self.score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("Name must be string")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        self.__number = new_number

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        self.__score = new_score

    def get_win(self):
        return self.data.get_score(self, "win")

    def get_lose(self):
        return self.data.get_score(self, "lose")

    def get_draw(self):
        return self.data.get_score(self, "draw")

    def get_winrate(self):
        win = self.data.get_score(self, "win")
        lose = self.data.get_score(self, "lose")
        draw = self.data.get_score(self, "draw")
        return (win/(win+lose+draw))*100

