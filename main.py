from data import Data
from player import Player
from item import Item
from board import Board

# print("--------------------------------------------------------")
# print("1. Play Game")
# print("2. Show Information of Player")
# print("--------------------------------------------------------")
# # choice = int(input("Please choose choice: "))

# Set Player1
name_1 = str(input("Player1, Enter name: "))
password_1 = input("Player1, Enter password: ")
player_1 = Player(name_1, password_1)
# check
symbol_1 = input("Player1, Enter symbol: ")
item_1 = Item(player_1, symbol_1, 1)

# Set Player2
name_2 = str(input("Player2, Enter name: "))
password_2 = input("Player2, Enter password: ")
player_2 = Player(name_2, password_2)
# check
symbol_2 = input("Player2, Enter symbol: ")
item_2 = Item(player_2, symbol_2, 2)

# Display board
board = Board([item_1, item_2], 6, 8)
board.create_board()
board.display_board()

# Player Turn
while True:
    item_1.column = int(input("Player1, Enter column: ")) - 1
    board.update_board(1)
    board.display_board()
    if board.check_winner():
        break
    item_2.column = int(input("Player2, Enter column: ")) - 1
    board.update_board(2)
    board.display_board()
    if board.check_winner():
        break






















