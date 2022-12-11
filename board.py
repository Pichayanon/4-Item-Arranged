"""This is a class Board."""
class Board:
    """
    This is a class to create a game board.

    Attributes:
        dict_player (dict): The dict whose key is player and
        whose value is the list of the item.
        row (int): Number of board rows.
        column (int): Number of board columns.
    """

    def __init__(self, dict_player, row=0, column=0):
        """
        The constructor for Board class.

        Parameters:
            dict_player (dict): The dict whose key is player and
            whose value is the list of the item.
            row (int): Number of board rows.
            column (int): Number of board columns.
        """
        self.dict_player = dict_player
        self.row = row
        self.column = column
        self.lst_board = []

    @property
    def dict_player(self):
        """dict_player property"""
        return self.__dict_player

    @dict_player.setter
    def dict_player(self, new_dict):
        """Set dict_player"""
        self.__dict_player = new_dict

    @property
    def row(self):
        """row property"""
        return self.__row

    @row.setter
    def row(self, new_row):
        """Set row"""
        self.__row = new_row

    @property
    def column(self):
        """column property"""
        return self.__column

    @column.setter
    def column(self, new_column):
        """Set column"""
        self.__column = new_column

    def create_board(self):
        """The function to create game board."""
        for _ in range(self.row):
            lst_column = []
            for _ in range(self.column):
                lst_column.append(0)
            self.lst_board.append(lst_column)

    def display_board(self):
        """The function to display game board."""
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
                    for key, val in self.dict_player.items():
                        if slot == key.number:
                            print(f"{val[-1].symbol:^3}"+"┇", end="")
                        else:
                            pass
            print()
        print((line * count) + "┇")

    def check_slot(self, column):
        """The function to check slot in column of game board that free
        or not."""
        lst_check = []
        for row in self.lst_board:
            lst_check.append(row[column])
        if 0 in lst_check:
            return True
        return False

    def update_board(self, number):
        """The function to update game board"""
        for key, val in self.dict_player.items():
            i = -1
            while True:
                if key.number == number:
                    column = val[-1].column
                    if self.lst_board[i][column] == 0:
                        self.lst_board[i][column] = number
                        val[-1].row = i
                        break
                    i -= 1
                else:
                    break

    def check_winner(self):
        """The function to check game board have winner or not"""
        len_r = len(self.lst_board)
        len_c = len(self.lst_board[0])
        while len_c-4 >= 0:
            for row in self.lst_board:
                if row[len_c - 1] == row[len_c - 2] == \
                        row[len_c - 3] == row[len_c - 4] != 0:
                    return True
            len_c -= 1
        while len_r-4 >= 0:
            for column in range(len(self.lst_board[0])):
                if self.lst_board[len_r - 1][column] == \
                        self.lst_board[len_r - 2][column] == \
                        self.lst_board[len_r - 3][column] == \
                        self.lst_board[len_r - 4][column] != 0:
                    return True
            len_r -= 1

        len_r2 = len(self.lst_board)
        while len_r2-4 >= 0:
            len_c2 = len(self.lst_board[0])
            while len_c2-4 >= 0:
                if self.lst_board[len_r2 - 1][len_c2 - 1] == \
                        self.lst_board[len_r2 - 2][len_c2 - 2] == \
                        self.lst_board[len_r2 - 3][len_c2 - 3] == \
                        self.lst_board[len_r2 - 4][len_c2 - 4] != 0:
                    return True
                len_c2 -= 1
            len_r2 -= 1

        len_r3 = len(self.lst_board)
        while len_r3-4 >= 0:
            len_c3 = 0
            while len_c3+4 <= len(self.lst_board[0]):
                if self.lst_board[len_r3 - 1][len_c3] == \
                        self.lst_board[len_r3 - 2][len_c3 + 1] == \
                        self.lst_board[len_r3 - 3][len_c3 + 2] == \
                        self.lst_board[len_r3 - 4][len_c3 + 3] != 0:
                    return True
                len_c3 += 1
            len_r3 -= 1
