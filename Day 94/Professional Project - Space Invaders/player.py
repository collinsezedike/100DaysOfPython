from turtle import Turtle
from bullet import Bullet


class Player(Turtle):

    def __init__(self, position):
        super().__init__()

        self.goto(position)
        self.penup()
        self.setheading(90)
        self.color("#00ff00")
        self.shape("turtle")
        self.bullet = Bullet(self.pos(), self.heading(), self.color()[0])
        # initialized a bullet with the player instead of using a 
        # boolean variable to check if it is the first shot
        self.bullet.goto(1000, 1000)
        # the first bullet is trashed so it doesn't appear 
        # with the player at the start of the game

    def move_left(self):
        if self.xcor() > -210:
            self.setx(self.xcor() - 10)
    
    def move_right(self):
        if self.xcor() < 210:
            self.setx(self.xcor() + 10)

    def shoot(self):
        if self.bullet.ycor() < 500:
            self.bullet.fire()
        else:
            self.bullet = Bullet(self.pos(), self.heading(), self.color()[0])
