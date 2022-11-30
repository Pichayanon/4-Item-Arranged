from player import Player

class Item:
    def __init__(self, column, symbol):
        self.column = column
        self.symbol = symbol
        self.row = 0

    @property
    def column(self):
        return self.__column

    @column.setter
    def column(self, new_column):
        self.__column = new_column

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, new_row):
        self.__row = new_row

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









