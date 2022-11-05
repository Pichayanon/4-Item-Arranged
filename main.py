from player import Player
from item import Item
from board import Board

player1 = Player("Kew",1)
player2 = Player("Mook",2)

item1 = Item(player1)
item2 = Item(player2)
item1.create_symbol("#")
item2.create_symbol("*")

x = Board(3,5)
x.create_board()
print(x.get_lst_board())
x.display_board()
n = 0
a = "Lose"
i = 0
while a != "Win":
    i += 1
    column = int(input("Enter column: "))
    if i % 2 != 0:
        item1.set_column(column)
        x.update_board(item1)
        print(x.get_lst_board())
    elif i % 2 == 0:
        item2.set_column(column)
        x.update_board(item2)
        print(x.get_lst_board())









