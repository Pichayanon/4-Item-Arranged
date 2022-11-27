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

print("╔.★.═════════════════════════════════════════════════════════╗")
print("            Welcome to 4 Item Arranged Game                   ")
print("                     1. Play Game                             ")
print("            2. Check Information Account                      ")
print("                   3. Create Account                          ")
print("╚═════════════════════════════════════════════════════════.★.╝")
choice = int(input("Please choose choice: "))
if choice == 1:
    many_player = choose_many_player()
    if many_player == 2:

        name1 = input(f"Player1, Enter name: ")
        player1 = Player(name1, 1)
        symbol1 = input("Player1, Please enter symbol: ")

        name2 = input(f"Player2, Enter name: ")
        player2 = Player(name2, 2)
        symbol2 = input("Player2, Please enter symbol: ")

        row, column = choose_size_board()
        board = Board({player1: [], player2: []}, row, column)
        board.create_board()
        board.display_board()
        while True:
            colum1 = int(input("P1-Please enter column: "))-1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print("Player1 Win!!!")
                break
            colum2 = int(input("P2-Please enter column: ")) - 1
            item2 = Item(colum2, symbol2)
            board.dic_player[player2].append(item2)
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print("Player2 Win!!!")
                break
    if many_player == 3:
        name1 = input(f"Player1, Enter name: ")
        player1 = Player(name1, 1)
        symbol1 = input("Player1, Please enter symbol: ")

        name2 = input(f"Player2, Enter name: ")
        player2 = Player(name2, 2)
        symbol2 = input("Player2, Please enter symbol: ")

        name3 = input(f"Player3, Enter name: ")
        player3 = Player(name3, 3)
        symbol3 = input("Player3, Please enter symbol: ")

        row, column = choose_size_board()
        board = Board({player1: [], player2: [], player3: []}, row, column)
        board.create_board()
        board.display_board()
        while True:
            colum1 = int(input("P1-Please enter column: "))-1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print("Player1 Win!!!")
                break
            colum2 = int(input("P2-Please enter column: ")) - 1
            item2 = Item(colum2, symbol2)
            board.dic_player[player2].append(item2)
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print("Player2 Win!!!")
                break
            colum3 = int(input("P3-Please enter column: ")) - 1
            item3 = Item(colum3, symbol3)
            board.dic_player[player3].append(item3)
            board.update_board(3)
            board.display_board()
            if board.check_winner():
                print("Player3 Win!!!")
                break
    if many_player == 4:
        name1 = input(f"Player1, Enter name: ")
        player1 = Player(name1, 1)
        symbol1 = input("Player1, Please enter symbol: ")

        name2 = input(f"Player2, Enter name: ")
        player2 = Player(name2, 2)
        symbol2 = input("Player2, Please enter symbol: ")

        name3 = input(f"Player3, Enter name: ")
        player3 = Player(name3, 3)
        symbol3 = input("Player3, Please enter symbol: ")

        name4 = input(f"Player4, Enter name: ")
        player4 = Player(name4, 4)
        symbol4 = input("Player4, Please enter symbol: ")

        row, column = choose_size_board()
        board = Board({player1: [], player2: [], player3: [], player4: []}, row, column)
        board.create_board()
        board.display_board()
        while True:
            colum1 = int(input("P1-Please enter column: ")) - 1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print("Player1 Win!!!")
                break
            colum2 = int(input("P2-Please enter column: ")) - 1
            item2 = Item(colum2, symbol2)
            board.dic_player[player2].append(item2)
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print("Player2 Win!!!")
                break
            colum3 = int(input("P3-Please enter column: ")) - 1
            item3 = Item(colum3, symbol3)
            board.dic_player[player3].append(item3)
            board.update_board(3)
            board.display_board()
            if board.check_winner():
                print("Player3 Win!!!")
                break
            colum4 = int(input("P4-Please enter column: ")) - 1
            item4 = Item(colum4, symbol4)
            board.dic_player[player4].append(item4)
            board.update_board(4)
            board.display_board()
            if board.check_winner():
                print("Player4 Win!!!")
                break




