from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -270)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)

    def move_right(self):
        if not (self.xcor() >= 181):
            self.forward(20)

    def move_left(self):
        if not (self.xcor() <= -181):
            self.backward(20)
