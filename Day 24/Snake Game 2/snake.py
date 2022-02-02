from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.body = []
        self.make_snake()
        self.head = self.body[0]

    def make_snake(self):
        x_axis = 0
        for _ in range(3):
            new_body = Turtle(shape="square")
            new_body.penup()
            new_body.color('white')
            # new_body.speed("fastest")
            new_body.setposition(x_axis, 0)
            x_axis -= MOVE_DISTANCE
            self.body.append(new_body)

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            new_pos = self.body[index - 1].position()
            self.body[index].goto(new_pos)
        self.body[0].forward(MOVE_DISTANCE)

    def add_tail(self):
        tail = Turtle(shape="square")
        tail.penup()
        tail.color('white')
        last_tail_x_cor = self.body[-1].xcor() 
        last_tail_y_cor = self.body[-1].ycor()
        tail.setposition(last_tail_x_cor, last_tail_y_cor)
        # x_axis -= MOVE_DISTANCE
        self.body.append(tail)

    def game_over(self):
        for body in self.body:
            body.hideturtle()
        self.body.clear()
        self.make_snake()
        self.head = self.body[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

