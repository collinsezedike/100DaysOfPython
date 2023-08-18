import scorer
from board import Board
from player import Human, create_players, change_symbol


def main():
    print("\nTIC TAC TOE")
    print("The battle of the Xs and the Os.")
    print("What tribe shall vanquish?\n")

    board = Board()
    first_player, second_player = create_players()

    while True:  # game continues until user decides not to play again     
        game_over = False
        while not game_over:

            # first player plays
            if isinstance(first_player, Human) or isinstance(second_player, Human):
                board.show_board()  # show the board to human players before they play
            print(f"{first_player.name}'s turn")
            board.add_entry(first_player.symbol, coordinates=first_player.play(board.board))
            # checks if it is a draw 
            if scorer.check_win(board.board, first_player.symbol) is None:
                scorer.declare_tie(board)
                scorer.display_score(first_player, second_player)
                game_over = True
            # checks if first player won
            elif scorer.check_win(board.board, first_player.symbol):
                scorer.declare_winner(board, player=first_player)
                scorer.display_score(first_player, second_player)
                game_over = True
            # if the first player has neither won nor drawn, the second player plays
            else:
                board.show_board()  # show the board before the second player plays            
                print(f"{second_player.name}'s turn")
                board.add_entry(second_player.symbol, coordinates=second_player.play(board.board))
                # checks if the second player won
                if scorer.check_win(board.board, second_player.symbol):
                    scorer.declare_winner(board, player=second_player)
                    scorer.display_score(first_player, second_player)
                    game_over = True

        # prompt to play again
        play_again = input("\nWould you like to play another? (yes/no) ").lower()
        if play_again.startswith("y"):
            board = Board()
            first_player, second_player = change_symbol(players=[first_player, second_player])
        else:
            return


main()
print("\nThanks for playing. Hope you enjoyed the game.")
print("If you enjoyed the game, follow me on twitter @collinsezedike to see the other amazing stuff I am building.\n")
