from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Consolas", 15, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.setposition(0, 275)
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
    
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.score += 1
        self.display_score()
        