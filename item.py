from player import Player


class Item:
    def __init__(self, player):
        self.player = player
        self.symbol = ""
        self.column = 0

    def create_symbol(self, symbol):
        self.symbol = symbol

    def set_column(self, new_column):
        self.column = new_column

    def get_column(self):
        return self.column

    def get_item(self):
        return self.symbol

    def get_player(self):
        return self.player.get_name()

    def get_number(self):
        return self.player.get_number()









