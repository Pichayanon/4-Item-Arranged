from player import Player
from item import Item

class Board:
    def __init__(self, dic_player, row=0, column=0):
        self.dic_player = dic_player
        self.row = row
        self.column = column
        self.lst_board = []

    def create_board(self):
        for i in range(self.row):
            lst_column = []
            for j in range(self.column):
                lst_column.append(0)
            self.lst_board.append(lst_column)

    def display_board(self):
        space = "   "
        line = "┇━━━"
        count = len(self.lst_board[0])
        print((line * count) + "┇")
        for i in range(len(self.lst_board[0])):
            print(f"┇{i+1:^3}", end="")
        print("┇")
        for row in self.lst_board:
            print((line * count) + "┇")
            print("┇", end="")
            for slot in row:
                if slot == 0:
                    print(space+"┇", end="")
                else:
                    for key, val in self.dic_player.items():
                        if slot == key.number:
                            print(f"{val[-1].symbol:^3}"+"┇", end="")
                        else:
                            pass
            print()
        print((line * count) + "┇")

    def check_slot(self, column):
        lst_check = []
        for row in self.lst_board:
            lst_check.append(row[column])
        if 0 in lst_check:
            return True
        else:
            return False

    def update_board(self, number):
        for key, val in self.dic_player.items():
            i = -1
            while True:
                if key.number == number:
                    column = val[-1].column
                    if self.lst_board[i][column] == 0:
                        self.lst_board[i][column] = number
                        val[-1].row = i
                        break
                    else:
                        i -= 1
                else:
                    break

    def check_winner(self):
        r = len(self.lst_board)
        c = len(self.lst_board[0])
        while c-4 >= 0:
            for row in self.lst_board:
                if row[c-1] == row[c-2] == row[c-3] == row[c-4] != 0:
                    return True
            c -= 1
        while r-4 >= 0:
            for column in range(len(self.lst_board[0])):
                if self.lst_board[r-1][column] == self.lst_board[r-2][column] == self.lst_board[r-3][column] == self.lst_board[r-4][column] != 0:
                    return True
            r -= 1
        n = len(self.lst_board)
        while n-4 >= 0:
            m = len(self.lst_board[0])
            while m-4 >= 0:
                if self.lst_board[n-1][m-1] == self.lst_board[n-2][m-2] == self.lst_board[n-3][m-3] == self.lst_board[n-4][m-4] != 0:
                    return True
                m -= 1
            n -= 1

        a = len(self.lst_board)
        while a-4 >= 0:
            b = 0
            while b+4 <= len(self.lst_board[0]):
                if self.lst_board[a-1][b] == self.lst_board[a-2][b+1] == self.lst_board[a-3][b+2] == self.lst_board[a-4][b+3] != 0:
                    return True
                b += 1
            a -= 1












