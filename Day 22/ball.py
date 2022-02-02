from turtle import Turtle

MOVE_DISTANCE = 20


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
    
        self.angle = 45
        self.startspeed = 0.1
        self.movespeed = self.startspeed
        self.shape("circle")
        self.color("blue")
        self.penup()

    def move(self):
        self.setheading(self.angle)
        self.forward(MOVE_DISTANCE)

    def bounce_y(self):
        self.angle = 360 - self.angle

    def bounce_x(self):
        self.angle = 180 - self.angle
