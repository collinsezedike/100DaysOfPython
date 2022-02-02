from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(position)

    def up(self):
        if not (self.ycor() > 215): 
            self.forward(20)

    def down(self):
        if not (self.ycor() < -200):
            self.backward(20)


