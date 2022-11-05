from player import Player
from item import Item


class Board:
    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column
        self.lst = []

    def create_board(self):
        for i in range(self.row):
            lst_column = []
            for j in range(self.column):
                lst_column.append(0)
            self.lst.append(lst_column)

    def get_lst_board(self):
        return self.lst

    def check_slot(self, item):
        pass

    def display_board(self):
        space = "   "
        line = "|---"
        for row in self.lst:
            count = len(row)
            print((line * count) + "|")
            print("|", end="")
            for slot in row:
                if slot == 0:
                    print(space+"|", end="")
                else:
                    print(f"{self.item.get_item()}:^3")
            print()
        print((line * count) + "|")

    def update_board(self, item):
        for row in self.lst:
            if row[item.get_column()] == 0:
                row[item.get_column()] == item.get_number()
            else:
                pass






    def check_winner(self):
        pass


