from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager:

    def __init__(self):
        self.all_cars = []
        self.pace = STARTING_MOVE_DISTANCE
        self.upper_range = 6

    def make_car(self):
        random_chance = random.randint(1, self.upper_range)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, (random.randint(-230, 230)))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.pace)

    def level_up(self):
        self.pace += MOVE_INCREMENT
        if not self.upper_range <= 1:
            self.upper_range -= 1

