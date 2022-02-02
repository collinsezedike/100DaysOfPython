from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.7, stretch_len= 0.7)
        self.color("red")
        self.speed("fastest")
        self.change_position()
    
    def change_position(self):
        x_cor = random.randint(-265, 265)
        y_cor = random.randint(-265, 265)
        self.goto(x_cor, y_cor)