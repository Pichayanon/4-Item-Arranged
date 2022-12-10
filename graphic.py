"""This is a class Graphic."""
import turtle
class Graphic:
    """
    This is a class to display game in turtle graphic.

    Attributes:
        board (Board): The board of game
    """
    def __init__(self, board):
        """
        The constructor for Item class.

        Parameters:
            board (Board): The board of game
        """
        self.board = board
        self.turtle = turtle.Turtle(visible=None)
        self.screen = turtle.Screen()
        self.screen.title("4 Arranged Item Game")
        self.screen.setup(width=600, height=700)

    def create_board(self):
        """The function to display empty game board."""
        self.turtle.penup()
        dis_c = (600 / (self.board.column + 2))
        dis_r = (700 / (self.board.row + 4))
        set_c = -300 + dis_c
        set_r = 350 - dis_r
        self.turtle.setposition(set_c + (dis_c / 2), set_r - dis_r)
        style = ("Courier", round(dis_r), "italic")
        self.turtle.speed(0)
        self.turtle.speed(0)
        for column in range(self.board.column):
            self.turtle.write(column + 1, font=style, align="center")
            self.turtle.forward(dis_c)
        self.turtle.setposition(set_c, set_r)
        n_row = 1
        while n_row <= self.board.row + 1:
            for column in range(self.board.column):
                self.turtle.pendown()
                self.turtle.forward(dis_c)
                self.turtle.right(90)
                self.turtle.forward(dis_r)
                self.turtle.right(90)
                self.turtle.forward(dis_c)
                self.turtle.right(90)
                self.turtle.forward(dis_r)
                self.turtle.right(90)
                self.turtle.forward(dis_c)
            n_row += 1
            set_r -= dis_r
            self.turtle.penup()
            self.turtle.setposition(set_c, set_r)

    def display_board(self):
        """The function to display item in game board."""
        for val in self.board.dic_player.values():
            dis_c = (600 / (self.board.column + 2))
            dis_r = (700 / (self.board.row + 4))
            set_c = -300 + (dis_c / 2)
            set_r = 350 - (dis_r / 2)
            self.turtle.pensize(3)
            style = ("Courier", 50, "italic")
            self.turtle.speed(0)
            for item in val:
                if item.column >= 0:
                    x_coordinate = set_c + (dis_c * (item.column + 1))
                    y_coordinate = set_r + (dis_r * (item.row - 0.5))
                    self.turtle.penup()
                    self.turtle.setposition(x_coordinate, -y_coordinate)
                    self.turtle.penup()
                    self.turtle.write(item.symbol, font=style, align="center")
                else:
                    pass
