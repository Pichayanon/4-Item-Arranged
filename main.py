from data import Data
from player import Player
from item import Item
from board import Board

def choose_many_player():
    print("╔.★.═════════════════════════════════════════════════════════╗")
    print("          How many player do you want to play                 ")
    print("           2 Player  :  3 Player  :  4 Player                 ")
    print("╚═════════════════════════════════════════════════════════.★.╝")
    player = int(input("How many player do you want to play: "))
    return player

def choose_size_board():
    print("╔.★.═════════════════════════════════════════════════════════╗")
    print("         What size of board do you want to play               ")
    print("            1. 6x7     2. 7x8     3. 8x9                      ")
    print("╚═════════════════════════════════════════════════════════.★.╝")
    size = int(input("Please choose choice: "))
    if size == 1:
        row_, column_ = 6, 7
    elif size == 2:
        row_, column_ = 7, 8
    elif size == 3:
        row_, column_ = 8, 9
    return row_, column_

def set_player(number):
    name = input(f"Player {number}, Enter name: ")
    password = input(f"Player {number}, Enter password: ")
    data = Data(name)
    player = Player(name, password, data, number)
    if player.check_player():
        if player.check_password():
            return player
        else:
            while not player.check_password():
                password = input("Wrong password, Enter password again: ")
                player = Player(name, password, data, number)
            return player
    else:
        return player


print("╔.★.═════════════════════════════════════════════════════════╗")
print("            Welcome to 4 Item Arranged Game                   ")
print("╚═════════════════════════════════════════════════════════.★.╝")
print("                   1. Play Game                               ")
print("               2. Show Information Account                    ")
print("═════════════════════════.★.══════════════════════════════════")
choice = int(input("Please choose choice: "))

if choice == 1:
    many_player = choose_many_player()
    if many_player == 2:
        board_row, board_column = choose_size_board()
        print(f"▶ Many player : {many_player} Player")
        print(f"▶ Board size : {board_row}x{board_column}")
        player1 = set_player(1)
        symbol1 = input(f"{player1.name}, Please enter symbol: ")
        player2 = set_player(2)
        symbol2 = input(f"{player2.name}, Please enter symbol: ")
        board = Board({player1: [], player2: []}, board_row, board_column)
        board.create_board()
        board.display_board()
        while True:
            colum1 = int(input(f"{player1.name}, Please enter column: "))-1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print(f"{player1.name} Win!!!")
                player1.update_player("win")
                player2.update_player("lose")
                break
            colum2 = int(input(f"{player2.name}, Please enter column: ")) - 1
            item2 = Item(colum2, symbol2)
            board.dic_player[player2].append(item2)
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print(f"{player2.name} Win!!!")
                player1.update_player("lose")
                player2.update_player("win")
                break



    elif many_player == 3:
        board_row, board_column = choose_size_board()
        print(f"▶ Many player : {many_player} Player")
        print(f"▶ Board size : {board_row}x{board_column}")
    elif many_player == 4:
        board_row, board_column = choose_size_board()
        print(f"▶ Many player : {many_player} Player")
        print(f"▶ Board size : {board_row} x {board_column}")


elif choice ==2:
    pass






