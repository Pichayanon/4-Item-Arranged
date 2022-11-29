from data import Data
from player import Player
from item import Item
from board import Board
import random

def choose_many_player():
    print("╔.★.═════════════════════════════════════════════════════════╗")
    print("          How many player do you want to play                 ")
    print("          1 Player                                            ")
    print("          2 Player                                            ")
    print("          3 Player                                            ")
    print("╚═════════════════════════════════════════════════════════.★.╝")
    player = int(input("How many player do you want to play: "))
    return player

def choose_size_board():
    print("╔.★.═════════════════════════════════════════════════════════╗")
    print("         What size of board do you want to play               ")
    print("         1. 6x7                                               ")
    print("         2. 7x8                                               ")
    print("         3. 8x9                                               ")
    print("╚═════════════════════════════════════════════════════════.★.╝")
    size = int(input("Please choose choice: "))
    if size == 1:
        row_, column_ = 6, 7
    elif size == 2:
        row_, column_ = 7, 8
    elif size == 3:
        row_, column_ = 8, 9
    return row_, column_

def set_player(number, data_):
    name = str(input(f"Player {number}, Enter name: "))
    password = input(f"{name}, Enter password: ")
    player = Player(name, password, data_, number)
    if data.check_account(player):
        if data_.check_password(player):
            return player
        else:
            n = 0
            print("Wrong password, You can try again 3 time.")
            while not data_.check_password(player):
                if n == 3:
                    n -= 2
                    return set_player(number, data_)
                else:
                    n += 1
                password = input(f"Enter password again round {n}:  ")
                player = Player(name, password, data_, number)
            return player
    else:
        return player

def set_symbol(symbol_lst):
    symbol = str(input(f"{player1.name}, Please enter symbol {symbol_lst}: "))
    while symbol not in symbol_lst:
        symbol = str(input(f"{player1.name}, Please enter symbol {symbol_lst}: "))
    return symbol

def set_bot(data_):
    bot_ = Player("bot", 1234, data_, number=99999)
    return bot_


print("╔.★.═════════════════════════════════════════════════════════╗")
print("            Welcome to 4 Item Arranged Game                   ")
print("╚═════════════════════════════════════════════════════════.★.╝")
print("               1. Play Game                                   ")
print("               2. Show Information Account                    ")
print("═════════════════════════.★.══════════════════════════════════")


choice = int(input("Please choose choice: "))
data = Data("data.json")
if choice == 1:
    many_player = choose_many_player()
    if many_player == 1:
        board_row, board_column = choose_size_board()
        print(f"▶ How many player: {many_player} Player")
        print(f"▶ Board size: {board_row}x{board_column}")
        player1 = set_player(1, data)
        symbol1 = set_symbol(["X", "O", "#"])
        bot = set_bot(data)
        symbol_bot = "*"
        board = Board({player1: [], bot: []}, board_row, board_column)
        board.create_board()
        board.display_board()
        round_ = 0
        while True:
            colum1 = int(input(f"{player1.name}, Please enter column: "))-1
            while colum1 > board_column-1:
                colum1 = int(input(f"No column {colum1 + 1}, Please enter column again: ")) - 1
            while not board.check_slot(colum1):
                colum1 = int(input(f"{colum1 + 1} is full, Please enter column again: "))-1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print(f"{player1.name} Win!!!")
                data.update_data(player1, "win")
                break
            else:
                round_ += 1
            colum_bot = random.randint(0, board_column-1)
            print(f"Bot, colum: {colum_bot}")
            while not board.check_slot(colum_bot):
                colum_bot = random.randint(0, board_column-1)
                print(f"{colum_bot-1} is full, Bot select new colum: {colum_bot}")
            item_bot = Item(colum_bot, symbol_bot)
            board.dic_player[bot].append(item_bot)
            board.update_board(99999)
            board.display_board()
            if board.check_winner():
                print(f"{player1.name} Lose!!!")
                data.update_data(player1, "lose")
                break
            else:
                round_ += 1

            if round_ == (board_column*board_row):
                print("This game is draw!!!!")
                data.update_data(player1, "draw")
                break

    elif many_player == 2:
        board_row, board_column = choose_size_board()
        print(f"▶ Many player: {many_player} Player")
        print(f"▶ Board size: {board_row}x{board_column}")
        symbol_can_use = ["*", "X", "O", "#"]
        player1 = set_player(1, data)
        symbol1 = set_symbol(symbol_can_use)
        player2 = set_player(2, data)
        symbol_can_use.remove(symbol1)
        symbol2 = set_symbol(symbol_can_use)
        board = Board({player1: [], player2: []}, board_row, board_column)
        board.create_board()
        board.display_board()
        round_ = 0
        while True:
            colum1 = int(input(f"{player1.name}, Please enter column: "))-1
            while colum1 > board_column-1:
                colum1 = int(input(f"No column {colum1 + 1}, Please enter column again: ")) - 1
            while not board.check_slot(colum1):
                colum1 = int(input(f"{colum1+1} is full, Please enter column again: "))-1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print(f"{player1.name} Win!!!")
                data.update_data(player1, "win")
                data.update_data(player2, "lose")
                break
            else:
                round_ += 1

            colum2 = int(input(f"{player2.name}, Please enter column: "))-1
            while colum2 > board_column-1:
                colum2 = int(input(f"No column {colum2 + 1}, Please enter column again: "))-1
            while not board.check_slot(colum2):
                colum2 = int(input(f"{colum2+1} is full, Please enter column again: "))-1
            item2 = Item(colum2, symbol2)
            board.dic_player[player2].append(item2)
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print(f"{player2.name} Win!!!")
                data.update_data(player1, "lose")
                data.update_data(player2, "win")
                break
            else:
                round_ += 1

            if round_ == (board_column*board_row):
                print("This game is draw!!!!")
                data.update_data(player1, "draw")
                data.update_data(player2, "draw")
                break
    elif many_player == 3:
        board_row, board_column = choose_size_board()
        print(f"▶ Many player: {many_player} Player")
        print(f"▶ Board size: {board_row}x{board_column}")
        symbol_can_use = ["*", "X", "O", "#"]
        player1 = set_player(1, data)
        symbol1 = set_symbol(symbol_can_use)
        symbol_can_use.remove(symbol1)
        player2 = set_player(2, data)
        symbol2 = set_symbol(symbol_can_use)
        symbol_can_use.remove(symbol2)
        player3 = set_player(3, data)
        symbol3 = set_symbol(symbol_can_use)
        board = Board({player1: [], player2: [], player3: []}, board_row, board_column)
        board.create_board()
        board.display_board()
        round_ = 0
        while True:
            colum1 = int(input(f"{player1.name}, Please enter column: "))-1
            while colum1 > board_column-1:
                colum1 = int(input(f"No column {colum1 + 1}, Please enter column again: ")) - 1
            while not board.check_slot(colum1):
                colum1 = int(input(f"{colum1+1} is full, Please enter column again: "))-1
            item1 = Item(colum1, symbol1)
            board.dic_player[player1].append(item1)
            board.update_board(1)
            board.display_board()
            if board.check_winner():
                print(f"{player1.name} Win!!!")
                data.update_data(player1, "win")
                data.update_data(player2, "lose")
                data.update_data(player3, "lose")
                break
            else:
                round_ += 1

            colum2 = int(input(f"{player2.name}, Please enter column: "))-1
            while colum2 > board_column-1:
                colum2 = int(input(f"No column {colum2 + 1}, Please enter column again: "))-1
            while not board.check_slot(colum2):
                colum2 = int(input(f"{colum2+1} is full, Please enter column again: "))-1
            item2 = Item(colum2, symbol2)
            board.dic_player[player2].append(item2)
            board.update_board(2)
            board.display_board()
            if board.check_winner():
                print(f"{player2.name} Win!!!")
                data.update_data(player1, "lose")
                data.update_data(player2, "win")
                data.update_data(player3, "lose")
                break
            else:
                round_ += 1

            colum3 = int(input(f"{player3.name}, Please enter column: "))-1
            while colum3 > board_column-1:
                colum3 = int(input(f"No column {colum3 + 1}, Please enter column again: "))-1
            while not board.check_slot(colum3):
                colum3 = int(input(f"{colum3+1} is full, Please enter column again: "))-1
            item3 = Item(colum3, symbol3)
            board.dic_player[player3].append(item3)
            board.update_board(3)
            board.display_board()
            if board.check_winner():
                print(f"{player3.name} Win!!!")
                data.update_data(player1, "lose")
                data.update_data(player2, "lose")
                data.update_data(player3, "win")
                break
            else:
                round_ += 1

            if round_ == (board_column*board_row):
                print("This game is draw!!!!")
                data.update_data(player1, "draw")
                data.update_data(player2, "draw")
                data.update_data(player3, "draw")
                break
        pass
elif choice == 2:
    print("╔.★.═════════════════════════════════════════════════════════╗")
    print("            1. Show win game                                  ")
    print("            2. Show lose game                                 ")
    print("            3. Show winrate                                   ")
    print("╚═════════════════════════════════════════════════════════.★.╝")
    choice = int(input("Enter choice: "))
    player_show = set_player(1, data)
    if choice == 1:
        print(f"▶ Name: {player_show.name}")
        print(f"▶ Win game: {player_show.get_win()}.")
    elif choice == 2:
        print(f"▶ Name: {player_show.name}")
        print(f"▶ Lose game: {player_show.get_lose()}.")
    elif choice == 3:
        print(f"▶ Name: {player_show.name}")
        print(f"▶ Winrate: {player_show.get_winrate()} percent:")






