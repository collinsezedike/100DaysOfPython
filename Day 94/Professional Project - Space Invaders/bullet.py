from turtle import Turtle


class Bullet(Turtle):

    def __init__(self, position, direction, color):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(position)
        self.setheading(direction)
        self.color(color)

    def fire(self, bullet_speed=10):
        self.showturtle()
        self.forward(bullet_speed)
