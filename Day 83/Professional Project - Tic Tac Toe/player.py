import random
import time


def who_go_first(players: list):
    # The player with "X" should go first
    global first_player, second_player
    for player in players:
        if player.symbol == "X":
            first_player = player
        else:
            second_player = player
    return first_player, second_player


def change_symbol(players: list):
    global player1, player2
    for player in players:
        if isinstance(player, Human):
            player1 = player
            break  # gets the first human player and break the loop immediately
    players.remove(player1)
    player2 = players[0]  # the second player, whether computer or human will be the only player left in the list

    new_symbol = input(f"{player1.name}, pick your tribe; 'X' or 'O': ").upper()
    while new_symbol not in ["O", "X"]:
        new_symbol = input(f"Don't be that guy, {player1.name}! Pick a valid tribe: 'X' or 'O': ").upper()
    player1.symbol = new_symbol  # change human player symbol
    if player1.symbol == "O":  # if user chooses "O", then computer should be X
        player2.symbol = "X"
    else:
        player2.symbol = "O"  # else, change player 2 symbol back to "O"
    return who_go_first(players=[player1, player2])


def create_players():
    mode = input("Single(s) or Multiplayer(m) mode: ").lower()

    if mode.startswith("m"):  # If user chooses multiplayer
        player1_name = input("\nPlayer 1, enter your name: ")
        player2_name = input("Player 2, enter your name: ")
        player1 = Human(player1_name, symbol="X")
        player2 = Human(player2_name, symbol="O")
    else:
        username = input("\nEnter your name: ")
        user_symbol = input(f"{username.title()}, pick your tribe; 'X' or 'O': ").upper()
        while user_symbol not in ["O", "X"]:
            user_symbol = input(f"Don't be that guy, {username.title()}! Pick a valid tribe: 'X' or 'O': ").upper()
        player1 = Human(username, user_symbol)
        player2 = Computer()
        if player1.symbol == "O":  # if user chooses "O", then computer should be X
            player2.symbol = "X"
    return who_go_first(players=[player1, player2])


class Player:

    def __init__(self, name: str, symbol: str):
        self.name = name.title()
        self.symbol = symbol
        self.score = 0

    def get_score(self):
        return self.score

    def add_point(self):
        self.score += 1


class Human(Player):

    def __init__(self, name, symbol):
        super().__init__(name=name, symbol=symbol)

    def play(self, current_board):
        """Returns the coordinates on the board to play at"""
        correct_position = False
        while not correct_position:
            play_at = input("Play at? (row, column) e.g 1,1: ").replace("(", "").replace(")", "").replace(",", "")
            if len(play_at) == 2:  # check if user provided ONLY two numbers
                play_at = tuple(play_at)
                try:
                    play_at_row = int(play_at[0]) - 1
                    play_at_col = int(play_at[1]) - 1
                except ValueError:
                    print("Wrong input")
                else:
                    # check if the coordinate is within the board index
                    if play_at_row in range(3) and play_at_col in range(3):
                        if current_board[play_at_row][play_at_col] == "-":  # check if the spot if playable
                            return play_at_row, play_at_col
                        else:
                            print("Can't play there")
                    else:
                        print("Wrong input! Out of range.")
            else:
                print("Wrong input! Invalid Entry")


class Computer(Player):

    def __init__(self):
        super().__init__(name="Computer", symbol="O")

    def play(self, current_board):
        """Returns the coordinates on the board to play at"""
        time.sleep(1)  # delays the computer response to add suspense
        correct_position = False
        while not correct_position:
            play_at = tuple((random.randint(0, 2), random.randint(0, 2)))
            if current_board[play_at[0]][play_at[1]] == "-":  # check if the spot if playable
                return play_at
