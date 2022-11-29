from player import Player

class Item:
    def __init__(self, column, symbol):
        self.column = column
        self.symbol = symbol

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, new_column):
        self.__column = new_column

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, new_symbol):
        self.__symbol = new_symbol

    def get_column(self):
        return self.__column

    def get_symbol(self):
        return self.__symbol









