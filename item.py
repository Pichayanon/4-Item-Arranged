"""This is a class Item."""
class Item:
    """
    This is a class to create item for game.

    Attributes:
        symbol (str): The symbol of item.
        column (int): The column of the board where the item is.
        row (int): The row of the board where the item is.
    """
    def __init__(self, symbol, column, row=0):
        """
        The constructor for Item class.

        Parameters:
            symbol (str): The symbol of item.
            column (int): The column of the board where the item is.
            row (int): The row of the board where the item is.
        """
        self.symbol = symbol
        self.column = column
        self.row = row

    @property
    def symbol(self):
        """Set a symbol of item"""
        return self.__symbol

    @symbol.setter
    def symbol(self, new_symbol):
        """Set a symbol of item"""
        self.__symbol = new_symbol

    @property
    def column(self):
        """Set a column of item"""
        return self.__column

    @column.setter
    def column(self, new_column):
        """Set a column of item"""
        self.__column = new_column

    @property
    def row(self):
        """Set a row of item"""
        return self.__row

    @row.setter
    def row(self, new_row):
        """Set a row of item"""
        if not isinstance(new_row, int):
            raise TypeError("Row must be integer")
        self.__row = new_row
