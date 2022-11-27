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
        column_ = 6
        row_ = 7
    elif size == 2:
        column_ = 7
        row_ = 8
    elif size == 3:
        column_ = 8
        row_ = 9
    return column_, row_


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
        column, row = choose_size_board()
        # Set Player1
        name_1 = str(input("Player1, Enter name: "))
        password_1 = input("Player1, Enter password: ")
        player_1 = Player(name_1, password_1)
        # check
        symbol_1 = input("Player1, Enter symbol: ")
        item_1 = Item(player_1, symbol_1, 1)
        print("══════════════════════════════════════════════════════════════")
        # Set Player2
        name_2 = str(input("Player2, Enter name: "))
        password_2 = input("Player2, Enter password: ")
        player_2 = Player(name_2, password_2)
        # check
        symbol_2 = input("Player2, Enter symbol: ")
        item_2 = Item(player_2, symbol_2, 2)

        board = Board([item_1, item_2], column, row)
        print("══════════════════════════════════════════════════════════════")
        board.create_board()
        board.display_board()

        # Player Turn
        while True:
            item_1.column = int(input("Player1, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print("Player1 Win!!!")
                break
            item_2.column = int(input("Player2, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print("Player2 Win!!!")
                break

    elif many_player == 3:
        column, row = choose_size_board()

        # Set Player1
        name_1 = str(input("Player1, Enter name: "))
        password_1 = input("Player1, Enter password: ")
        player_1 = Player(name_1, password_1)
        # check
        symbol_1 = input("Player1, Enter symbol: ")
        item_1 = Item(player_1, symbol_1, 1)
        print("══════════════════════════════════════════════════════════════")
        # Set Player2
        name_2 = str(input("Player2, Enter name: "))
        password_2 = input("Player2, Enter password: ")
        player_2 = Player(name_2, password_2)
        # check
        symbol_2 = input("Player2, Enter symbol: ")
        item_2 = Item(player_2, symbol_2, 2)
        print("══════════════════════════════════════════════════════════════")
        # Set Player3
        name_3 = str(input("Player3, Enter name: "))
        password_3 = input("Player3, Enter password: ")
        player_3 = Player(name_3, password_3)
        # check
        symbol_3 = input("Player3, Enter symbol: ")
        item_3 = Item(player_3, symbol_3, 3)
        print("══════════════════════════════════════════════════════════════")
        board = Board([item_1, item_2,item_3], column, row)
        board.create_board()
        board.display_board()

        # Player Turn
        while True:
            item_1.column = int(input("Player1, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print("Player1 Win!!!")
                break
            item_2.column = int(input("Player2, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print("Player2 Win!!!")
                break
            item_3.column = int(input("Player3, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(3)
            board.display_board()
            if board.check_winner():
                print("Player3 Win!!!")
                break

    elif many_player == 4:
        column, row = choose_size_board()

        # Set Player1
        name_1 = str(input("Player1, Enter name: "))
        password_1 = input("Player1, Enter password: ")
        player_1 = Player(name_1, password_1)
        # check
        symbol_1 = input("Player1, Enter symbol: ")
        item_1 = Item(player_1, symbol_1, 1)
        print("══════════════════════════════════════════════════════════════")
        # Set Player2
        name_2 = str(input("Player2, Enter name: "))
        password_2 = input("Player2, Enter password: ")
        player_2 = Player(name_2, password_2)
        # check
        symbol_2 = input("Player2, Enter symbol: ")
        item_2 = Item(player_2, symbol_2, 2)
        print("══════════════════════════════════════════════════════════════")
        # Set Player3
        name_3 = str(input("Player3, Enter name: "))
        password_3 = input("Player3, Enter password: ")
        player_3 = Player(name_3, password_3)
        # check
        symbol_3 = input("Player3, Enter symbol: ")
        item_3 = Item(player_3, symbol_3, 3)
        print("══════════════════════════════════════════════════════════════")
        # Set Player4
        name_4 = str(input("Player4, Enter name: "))
        password_4 = input("Player4, Enter password: ")
        player_4 = Player(name_4, password_4)
        # check
        symbol_4 = input("Player3, Enter symbol: ")
        item_4 = Item(player_4, symbol_4, 4)
        print("══════════════════════════════════════════════════════════════")
        board = Board([item_1, item_2, item_3, item_4], column, row)
        board.create_board()
        board.display_board()

        # Player Turn
        while True:
            item_1.column = int(input("Player1, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print("Player1 Win!!!")
                break
            item_2.column = int(input("Player2, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print("Player2 Win!!!")
                break
            item_3.column = int(input("Player3, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(3)
            board.display_board()
            if board.check_winner():
                print("Player3 Win!!!")
                break
            item_4.column = int(input("Player4, Enter column: ")) - 1
            print("══════════════════════════════════════════════════════════════")
            board.update_board(4)
            board.display_board()
            if board.check_winner():
                print("Player4 Win!!!")
                break



























