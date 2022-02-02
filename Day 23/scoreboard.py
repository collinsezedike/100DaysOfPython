from turtle import Turtle
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 265)
        self.level = 1
        self.hideturtle()

    def display_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.display_level()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 20, "bold"))