from ctypes import alignment
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Consolas", "15", "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.setposition(0,275)
        self.score = 0
    
    def game_over(self):
        # self.setposition(0,275)
        self.home()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()
        