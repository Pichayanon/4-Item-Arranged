import random
from player import Player
from data import Data
from board import Board
from item import Item
from graphic import Graphic

def set_player(data: Data, number: int) -> Player:
    """
    create player for game.

    Get name and password from player.

    Parameters:
    data (Data): data to store player account.
    number (int) : number of players for playing the game.

    Returns:
    Player : player for game
    """
    player_name = str(input("Enter name: "))
    password = str(input(f"{player_name}, Enter password: "))
    player_ = Player(player_name, password, data, number)
    while not data.login(player_):
        player_name = str(input("Enter name: "))
        password = str(input(f"{player_name}, Enter password: "))
        player_ = Player(player_name, password, data, number)
    return player_

def set_many_player() -> int:
    """Let the player choose the number of players and return it"""
    print("╔.★.═════════════════════════════════════════════╗")
    print(f"{'How many player do you want to play':^51}")
    print("            1 Player                              ")
    print("            2 Player                              ")
    print("╚═════════════════════════════════════════════.★.╝")
    m_player = input("How many player do you want to play: ")
    while m_player not in ['1', '2']:
        m_player = input("You can choose 1 or 2 player: ")
    return m_player

def set_symbol(symbol_lst: list[str]) -> str:
    """Let the player choose symbol of item and return it"""
    symbol_selected = str(input(f"Enter symbol {symbol_lst}: "))
    while symbol_selected not in symbol_lst:
        symbol_selected = str(input(f"Enter symbol {symbol_lst}: "))
    return symbol_selected

def set_choice_information() -> int:
    """Let the player choose choice to show information and return it"""
    print("╔.★.═════════════════════════════════════════════╗")
    print("            1. Show win,lose and draw game        ")
    print("            2. Show winrate                       ")
    print("╚═════════════════════════════════════════════.★.╝")
    i_choice = input("Please select choice: ")
    while i_choice not in ['1', '2']:
        print("Incorrect choice, please select again")
        i_choice = input("Please select choice: ")
    return i_choice

def set_board() -> int:
    """Let the player choose size of board and return it"""
    print("╔.★.═════════════════════════════════════════════╗")
    print(f"{'What size of board do you want to play':^51}")
    print("            1. 6x7                                ")
    print("            2. 7x8                                ")
    print("            3. 8x9                                ")
    print("╚═════════════════════════════════════════════.★.╝")
    size_selected = input("Select size of board: ")
    while size_selected not in ['1', '2', '3']:
        print("Incorrect choice, please select again")
        size_selected = input("Select size of board: ")
    if size_selected == '1':
        row_, column_ = 6, 7
    elif size_selected == '2':
        row_, column_ = 7, 8
    elif size_selected == '3':
        row_, column_ = 8, 9
    return row_, column_

def play_1player(data_):
    """Play this game with 1 player"""
    symbol_ = ['*', 'O']  # set symbol that player can use
    # set player
    player = set_player(data_, 1)
    symbol = set_symbol(symbol_)
    # set bot
    bot = Player("bot", '1234', data_, number=99999)
    symbol_bot = 'X'
    # set board
    row, column = set_board()
    board = Board({player: [], bot: []}, row, column)
    board.create_board()
    graphic = Graphic(board)
    graphic.create_board()
    # set game play
    round_ = 0  # set start round
    while True:
        # player turn
        colum = int(input(f"{player.name}, Enter column: ")) - 1
        # check column selected in range column of board or not
        while (colum < 0) or (colum > column - 1):
            print(f"No column : {colum + 1}")
            colum = int(input("Enter column again: ")) - 1
        # check column selected that have free slot or not
        while not board.check_slot(colum):
            print(f"{colum + 1} is full.")
            colum = int(input("Enter column again: ")) - 1
        # set item of player
        item = Item(symbol, colum)
        # update board
        board.dic_player[player].append(item)
        board.update_board(1)
        graphic.display_board()
        # check win
        if board.check_winner():
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"{'You is winner!':^51}")
            print("╚═════════════════════════════════════════════.★.╝")
            # update account of player
            data_.update_account(player.name, "win")
            break
        round_ += 1  # player not win round += 1

        # bot turn
        # random column bot in range (0, column of board)
        colum_bot = random.randint(0, column - 1)
        # check column selected that have free slot or not
        while not board.check_slot(colum_bot):
            colum_bot = random.randint(0, column - 1)
        print(f"Bot select column : {colum_bot + 1}")
        # set item of bot
        item_bot = Item(symbol_bot, colum_bot)
        # update board
        board.dic_player[bot].append(item_bot)
        board.update_board(99999)
        graphic.display_board()
        # check win
        if board.check_winner():
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"{'You is loser!':^51}")
            print("╚═════════════════════════════════════════════.★.╝")
            # update account of player
            data_.update_account(player.name, "lose")
            break
        round_ += 1  # bot not win round += 1

        # check when game is draw
        if round_ == (column * row):
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"{'This game is draw!!!!':^51}")
            print("╚═════════════════════════════════════════════.★.╝")
            data_.update_account(player.name, "draw")
            break

def play_2player(data_):
    """Play game with 2 player"""
    symbol_ = ['*', 'X', 'O']  # set symbol that player can use
    # set player1
    player1 = set_player(data_, 1)
    symbol1 = set_symbol(symbol_)
    symbol_.remove(symbol1)
    # set player2
    player2 = set_player(data_, 2)
    symbol2 = set_symbol(symbol_)
    # set board
    row, column = set_board()
    board = Board({player1: [], player2: []}, row, column)
    board.create_board()
    graphic = Graphic(board)
    graphic.create_board()
    # set game play
    round_ = 0  # set start round
    while True:
        # player1 turn
        colum1 = int(input(f"{player1.name}, Enter column: ")) - 1
        # check column selected in range column of board or not
        while (colum1 < 0) or (colum1 > column - 1):
            print(f"No column : {colum1 + 1}")
            colum1 = int(input("Enter column again: ")) - 1
        # check column selected that have free slot or not
        while not board.check_slot(colum1):
            print(f"{colum1 + 1} is full.")
            colum1 = int(input("Enter column again: ")) - 1
        # set item of player 1
        item1 = Item(symbol1, colum1)
        # update board
        board.dic_player[player1].append(item1)
        board.update_board(1)
        graphic.display_board()
        # check win
        if board.check_winner():
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"{player1.name+' is winner!':^51}")
            print("╚═════════════════════════════════════════════.★.╝")
            # update account of player1 and player2
            data_.update_account(player1.name, "win")
            data_.update_account(player2.name, "lose")
            break
        round_ += 1  # player1 not win round += 1

        # player2 turn
        colum2 = int(input(f"{player2.name}, Enter column: ")) - 1
        # check column selected in range column of board or not
        while (colum2 < 0) or (colum2 > column - 1):
            print(f"No column : {colum2 + 1}")
            colum2 = int(input("Enter column again: ")) - 1
        # check column selected that have free slot or not
        while not board.check_slot(colum2):
            print(f"{colum2 + 1} is full.")
            colum2 = int(input("Enter column again: ")) - 1
        # set item of player 2
        item2 = Item(symbol2, colum2)
        # update board
        board.dic_player[player2].append(item2)
        board.update_board(2)
        graphic.display_board()
        # check win
        if board.check_winner():
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"{player2.name+' is winner!':^51}")
            print("╚═════════════════════════════════════════════.★.╝")
            # update account of player1 and player2
            data_.update_account(player1.name, "lose")
            data_.update_account(player2.name, "win")
            break
        round_ += 1  # player2 not win round += 1

        # check when game is draw
        if round_ == (column * row):
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"{'This game is draw!!!!':^51}")
            print("╚═════════════════════════════════════════════.★.╝")
            data_.update_account(player1, "draw")
            data_.update_account(player2, "draw")
            break


print("╔.★.═════════════════════════════════════════════╗")
print("       Welcome to 4 Item Arranged Game            ")
print("╚═════════════════════════════════════════════.★.╝")
print("            1. Play Game                          ")
print("            2. Show Information Account           ")
print("═════════════════════════.★.══════════════════════")
choice = input("Please select choice: ")
while choice not in ['1', '2']:
    print("Incorrect choice")
    choice = input("Please select choice again: ")
# Play game
if choice == '1':
    data_play = Data("data.json")  # set file that collect data
    many_players = ''
    # check that not equal 1, 2, back or not.
    while many_players not in ['1', '2']:
        many_players = set_many_player()
        # 1 player
        if many_players == '1':
            play_1player(data_play)
        # 2 player
        elif many_players == '2':
            play_2player(data_play)
# Show information of account
elif choice == '2':
    data_play = Data("data.json")  # set file that collect data
    name = input("Please enter name: ")  # input name of player
    # check data have account player or not
    while not data_play.check_account(name):
        print("No account in data")
        name = input("Please enter name: ")
    information_selected = ''
    # check that not equal 1, 2, back or not.
    while information_selected not in ['1', '2']:
        information_selected = set_choice_information()
        player_inform = Player(name, data_play.get_password(name), data_play)
        # show win, lose and draw count
        if information_selected == '1':
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"▶ Name: {name}")
            print(f"▶ Win game: {player_inform.get_win()}.")
            print(f"▶ Lose game: {player_inform.get_lose()}.")
            print(f"▶ Draw game: {player_inform.get_draw()}.")
            print("╚═════════════════════════════════════════════.★.╝")
        # show winrate
        elif information_selected == '2':
            print("╔.★.═════════════════════════════════════════════╗")
            print(f"▶ Name: {name}")
            print(f"▶ Winrate: {player_inform.get_winrate():.2f}.")
            print("╚═════════════════════════════════════════════.★.╝")
        # back
        elif information_selected == 'back':
            continue
