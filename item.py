from player import Player


class Item:
    def __init__(self, symbol):
        self.player = Player
        self.symbol = symbol

    def get_item(self, name):
        if self.player.get_name() == name:
            return self.symbol
        else:
            return "Invalid"








