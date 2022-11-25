class Player:
    def __init__(self, name, number, password, score=0):
        self.name = name
        self.number = number
        self.password = password
        self.score = score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            raise TypeError("name must be string")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        if isinstance(self, new_number):
            self.__number = new_number
        else:
            raise TypeError("number must be integer")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, new_score):
        self.__score = new_score


