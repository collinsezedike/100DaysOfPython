from operator import methodcaller
from turtle import Turtle
from bullet import Bullet
import random


class Soldier(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("turtle")
        self.setheading(270)
        self.color("#ff0000")
        self.bullet = Bullet(self.pos(), self.heading(), self.color()[0])   
        # initialized a bullet with the soldier instead of using a 
        # boolean variable to check if it is the first shot
        self.bullet.goto(-1000, -1000)
        # the first bullet is trashed so it doesn't appear 
        # with the soldier at the start of the game
            

class Invaders:
    
    def __init__(self):
        self.soldiers = []
        
        self.direction = "left"    # initial direction
        self.forward_speed = 0.000001
        self.sideward_speed = 2
        self.bullet_speed = 10
         
    def create_army(self, position):
        self.soldiers.clear()
        start_xcor = position[0]
        for _ in range(3):
            for _ in range(10):
                new_soldier = Soldier()
                new_soldier.goto(position)
                self.soldiers.append(new_soldier)
                position = (position[0]+35, position[1])
            position = (start_xcor, position[1]-30)

    def level_up(self, position):
        self.forward_speed *= 2.5
        self.sideward_speed += 1
        self.bullet_speed += 2
        self.create_army(position)

    def move(self):
        # leftest_soldier = self.soldiers[0]
        # rightest_soldier = self.soldiers[-1]
        leftest_soldier = min(self.soldiers, key=methodcaller("xcor"))
        rightest_soldier = max(self.soldiers, key=methodcaller("xcor"))

        if leftest_soldier.xcor() <= -210:
            self.direction = "right"
        elif rightest_soldier.xcor() >= 210:
            self.direction = "left"

        if self.direction == "left":
            self.go_left()
        else:
            self.go_right()

    def go_left(self):
        for soldier in self.soldiers:
            soldier.setx(soldier.xcor()-self.sideward_speed)
            soldier.forward(self.forward_speed)

    def go_right(self):
        for soldier in self.soldiers:
            soldier.setx(soldier.xcor()+self.sideward_speed)
            soldier.forward(self.forward_speed)

    def shoot(self, limit):
        if any(soldier.bullet.ycor() > limit for soldier in self.soldiers):
            soldier = self.get_shooter(limit)
            soldier.bullet.fire(self.bullet_speed)
        else:
            soldier = random.choice(self.soldiers)
            soldier.bullet = Bullet(soldier.pos(), soldier.heading(), soldier.color()[0])
            soldier.bullet.fire(self.bullet_speed)

    def get_shooter(self, limit: int):
        for shooter in self.soldiers:
            if shooter.bullet.ycor() > limit:
                return shooter
