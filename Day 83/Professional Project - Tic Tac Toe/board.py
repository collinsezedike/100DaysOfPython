class Board:

    def __init__(self):
        self.board = []
        for _ in range(3):
            self.row = ["-" for _ in range(3)]
            self.board.append(self.row)

    def show_board(self):
        for row in self.board:
            print("\t", end=" ")
            print(" | ".join(row))
            if self.board.index(row) != 2:
                print("\t———————————")

    def add_entry(self, entry: str, coordinates: tuple):
        self.board[coordinates[0]][coordinates[1]] = entry
