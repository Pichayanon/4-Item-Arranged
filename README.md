# 4 Item Arranged
## Project Overview and feature.
4 Item Arranged is a game that allows players to arrange 4 items next to each other vertically, horizontally or diagonally. The player can only choose a column because the item will always fall by the gravity of the world to the lowest row first. If any player can arrange 4 items next to each other first, it will be considered the winner of this game.

## How to play this game?
When entering the game, the game will let you to choose whether to play the game or show the account's information. 
### Play the game
  * When the player enters the game, the game will let players to choose the number of players whether to play 1 or 2 players. If playing with 1 player, it will be playing against bots. Then the game will let the player to enter a name. If there is information of the player, the game will let the player to login. If there is no information of the player, the game will let the player to register. Then the game will let the player to choose the Board size (6x7, 7x8, 8x9). Then the game will show Board. Players can select the column that the item will fall into but cannot select the row. The player who arranges 4 items next to each other horizontally, vertically or diagonally first wins. After the game ends, the game will record the player's win, loss or draw history.

### Show the account's information. 
  * When the player enters the game, the game will let the player to enter a name. If there is information of the player, the game will let  players to choose whether to show the number of wins, losses and draws or show the winrate. If there is no information of the player, the game will show No account in data.

## Program's Requirement
There are **3** Python Modules & Libraries required in this program.
* [turtle](https://docs.python.org/3/library/turtle.html) : Used for write board in turtle graphic.
* [json](https://docs.python.org/3/library/json.html?highlight=json#module-json) : Used for stores player information.
* [random](https://docs.python.org/3/library/random.html) : Used for random column of bot.

## Program Design
### There are **five** ***classes*** in this program.
* **Data** : class for stores player information.
* **Player** : class for create player.
* **Item** : class for create item.
* **Board** : class for create board.
* **Graphic** : class for display board in turtle graphic.
### Integrate all of the classes
* In the main program. When the game starts, game will create a player by **class Player** and store the information in **class Data**. The player and item will be used in the **class Board** in the form of the dictionary, the key is the player, and the value is the list of items to play the game. **class Board** will create board and use **class Graphic** to show board in turtle graphic. When a player selects a column of an item, the game will create an item by **class Item** and store the item in that player's list of items. After each round, the **class Board** checks if there is a winner or not. If there is a winner then the game is over and the player's score is recorded in **class Data**.

## Code Structure
* [main.py](main.py) : Run main program.
* [data.py](data.py) : Contains class Data.
* [player.py](player.py) : Contains class Player.
* [item.py](item.py) : Contains class Item.
* [board.py](board.py) : Contains class Board.
* [graphic.py](graphic.py) : Contains class Graphic.
