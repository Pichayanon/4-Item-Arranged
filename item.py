from player import Player


class Item:
    def __init__(self, player, symbol, number):
        self.player = player
        self.symbol = symbol
        self.number = number
        self.column = 0

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, new_symbol):
        self.__symbol = new_symbol

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, new_column):
        self.__column = new_column

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number):
        if isinstance(new_number, int):
            self.__number = new_number
        else:
            raise TypeError("number must be integer")







