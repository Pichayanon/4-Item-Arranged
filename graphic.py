from board import Board
from player import Player
from data import Data
import turtle
import time

class Graphic:
    def __init__(self, board):
        self.board = board

    def create_board(self):
        turtle_create = turtle.Turtle(visible=None)
        screen = turtle.Screen()
        screen.setup(width=50*self.board.column, height=50*self.board.row)
        turtle_create.penup()
        set_x = -(50*self.board.column)/2
        set_y = (50*self.board.row)/2
        turtle_create.setposition(set_x, set_y)
        turtle_create.speed(0)
        dis_x = 50
        n = 1
        while n <= self.board.row:
            for column in range(self.board.column):
                turtle_create.pendown()
                turtle_create.forward(dis_x)
                turtle_create.right(90)
                turtle_create.forward(dis_x)
                turtle_create.right(90)
                turtle_create.forward(dis_x)
                turtle_create.right(90)
                turtle_create.forward(dis_x)
                turtle_create.right(90)
                turtle_create.forward(dis_x)
            n += 1
            set_y -= 50
            turtle_create.penup()
            turtle_create.setposition(set_x, set_y)

    def display_board(self):
        for key, val in self.board.dic_player.items():
            set_x = (-(50 * self.board.column) / 2) + 25
            set_y = ((50 * self.board.row) / 2) + 50
            turtle_display = turtle.Turtle(visible=None)
            turtle_display.color("red")
            style = ("Courier", 50, "italic")
            turtle_display.penup()
            turtle_display.setposition(set_x, set_y)
            turtle_display.speed(0)
            dis_x = 50
            for item in val:
                if item.column >= 0:
                    x = set_x + (dis_x * item.column)
                    y = set_y + (dis_x * item.row)
                    turtle_display.penup()
                    turtle_display.setposition(x, -y)
                    turtle_display.penup()
                    turtle_display.write(item.symbol, font=style, align="center")


                else:
                    pass



    def display_text(self):
        pass
