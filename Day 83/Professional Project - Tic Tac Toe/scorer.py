from board import Board
from player import Player


def display_score(player1: Player, player2: Player):
    print(f"{player1.name}: {player1.get_score()} {player2.name}: {player2.get_score()}")


def update_score(player: Player):
    player.add_point()


def declare_winner(board_obj: Board, player: Player):
    board_obj.show_board()  # so that it shows the board before declaring the winner
    print(f"{player.name} won!")
    update_score(player)


def declare_tie(board_obj: Board):
    board_obj.show_board()  # so that it shows the board before declaring a tie
    print("A tie!")
    return


def check_win(current_board, player_symbol=None):
    # check horizontal winning
    for row in current_board:
        filled_row = all(item == player_symbol for item in row)
        if filled_row:
            return True

    # check vertical winning
    for index in range(3):
        col_items = [row[index] for row in current_board]
        filled_col = all(item == player_symbol for item in col_items)
        if filled_col:
            return True

    # check dexter diagonal winning (\)
    for _ in range(3):
        diag_items = [row[current_board.index(row)] for row in current_board]
        filled_diag = all(item == player_symbol for item in diag_items)
        if filled_diag:
            return True

    # check sinister diagonal winning (/)
    for _ in range(3):
        diag_items = [row[2 - current_board.index(row)] for row in current_board]
        filled_diag = all(item == player_symbol for item in diag_items)
        if filled_diag:
            return True

    # otherwise, it is either a tie or the game is not yet complete
    # check if game is incomplete
    for row in current_board:
        if "-" in row:
            return False
    # otherwise, it's a tie
    return None
