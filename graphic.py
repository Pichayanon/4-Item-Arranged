from board import Board
from player import Player
from data import Data
import turtle
import time

class Graphic:
    def __init__(self, board):
        self.board = board

    def create_board(self):
        turtle_create_b = turtle.Turtle(visible=None)
        turtle_create_n = turtle.Turtle(visible=None)
        screen = turtle.Screen()
        screen.setup(width=600, height=700)
        turtle_create_b.penup()
        turtle_create_n.penup()
        dis_c = (600/(self.board.column+2))
        dis_r = (700/(self.board.row+4))
        set_c = -300+dis_c
        set_r = 350-dis_r
        turtle_create_b.setposition(set_c, set_r)
        turtle_create_n.setposition(set_c+(dis_c/2), set_r-dis_r)
        style = ("Courier", round(dis_r), "italic")
        turtle_create_b.speed(0)
        turtle_create_n.speed(0)
        for column in range(self.board.column):
            turtle_create_n.write(column+1, font=style, align="center")
            turtle_create_n.forward(dis_c)
        n = 1
        while n <= self.board.row+1:
            for column in range(self.board.column):
                turtle_create_b.pendown()
                turtle_create_b.forward(dis_c)
                turtle_create_b.right(90)
                turtle_create_b.forward(dis_r)
                turtle_create_b.right(90)
                turtle_create_b.forward(dis_c)
                turtle_create_b.right(90)
                turtle_create_b.forward(dis_r)
                turtle_create_b.right(90)
                turtle_create_b.forward(dis_c)
            n += 1
            set_r -= dis_r
            turtle_create_b.penup()
            turtle_create_b.setposition(set_c, set_r)

    def display_board(self):
        for key, val in self.board.dic_player.items():
            dis_c = (600 / (self.board.column + 2))
            dis_r = (700 / (self.board.row + 4))
            set_c = -300 + (dis_c/2)
            set_r = 350 - (dis_r/2)
            turtle_display = turtle.Turtle(visible=None)
            turtle_display.color("red")
            turtle_display.pensize(3)
            style = ("Courier", 50, "italic")
            turtle_display.speed(0)
            for item in val:
                if item.column >= 0:
                    x = set_c + (dis_c * (item.column+1))
                    y = set_r + (dis_r * (item.row-0.5))
                    turtle_display.penup()
                    turtle_display.setposition(x, -y)
                    turtle_display.penup()
                    turtle_display.write(item.symbol, font=style, align="center")
                else:
                    pass


