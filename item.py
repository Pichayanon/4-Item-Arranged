from player import Player


class Item:
    def __init__(self, player, symbol):
        self.player = Player
        self.symbol = symbol
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







