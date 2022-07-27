from turtle import Turtle

ALIGNMENT = "center"
FONT = ("consolas", 12, "bold")
ANNOUNCER_FONT = ("consolas", 60, "bold")


class Writer(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#00ff00")
        self.goto(position)
    
    def write_lives(self, lives_remaining):
        self.clear()
        self.write(f"Lives: {lives_remaining}", align=ALIGNMENT, font=FONT)

    def write_level(self, current_level):
        self.clear()
        self.write(f"Level: {current_level}", align=ALIGNMENT, font=FONT)
    
    def write_gameover(self):
        self.pencolor("#fff")
        self.clear()
        self.write("Game over!", align=ALIGNMENT, font=ANNOUNCER_FONT)
