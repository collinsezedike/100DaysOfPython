from turtle import Turtle

FONT = ("consolas", 30, "bold")
ALIGNMENT = "center"


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_score(self, lives_remaining):
        self.color("#333")
        self.clear()
        self.goto(0, -20)
        self.write(f"Lives: {lives_remaining}", align=ALIGNMENT, font=("courier", 60, "bold"))

    def write_win(self):
        self.color("white")
        self.write("Game over\n You win", align=ALIGNMENT, font=FONT)

    def write_lose(self):
        self.color("white")
        self.write("Game over\nYou lose!", align=ALIGNMENT, font=FONT)
