from player import Player
from item import Item


class Board:
    def __init__(self, lst_item, row=0, column=0):
        self.row = row
        self.column = column
        self.lst_item = lst_item
        self.lst_board = []

    def create_board(self):
        for i in range(self.row):
            lst_column = []
            for j in range(self.column):
                lst_column.append(0)
            self.lst_board.append(lst_column)

    def check_slot(self, item):
        pass

    def display_board(self):
        space = "   "
        line = "|---"
        for i in range(len(self.lst_board[0])):
            print(f"|-{i+1}-", end="")
        print("|")
        for row in self.lst_board:
            count = len(row)
            print((line * count) + "|")
            print("|", end="")
            for slot in row:
                if slot == 0:
                    print(space+"|", end="")
                else:
                    i = 0
                    while True:
                        if slot == self.lst_item[i].number:
                            print(f"{self.lst_item[i].symbol:^3}"+"|", end="")
                            break
                        else:
                            i += 1
            print()
        print((line * count) + "|")

    def update_board(self, number):
        i = -1
        while True:
            column = self.lst_item[number-1].column
            if self.lst_board[i][column] == 0:
                self.lst_board[i][column] = self.lst_item[number-1].number
                break
            else:
                i += -1


    def check_winner(self):
        pass


