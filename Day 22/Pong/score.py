from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 200, "bold")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("grey")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(0, -150)
        self.display_score()
    
    def display_score(self):
        self.write(f"{self.l_score}-{self.r_score}", align=ALIGNMENT, font= FONT)

    def update_score(self):
        self.clear()
        self.display_score()
        
        
