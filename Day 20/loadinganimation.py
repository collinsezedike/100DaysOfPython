from turtle import Turtle, Screen
import time
import turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = []
x_axis = 0
for _ in range(4):
    snake_body = Turtle(shape="circle")
    snake_body.shapesize(0.25)
    snake_body.penup()
    snake_body.color('white')
    snake.append(snake_body)

game_on = True
while game_on:
    screen,update()
    time.sleep(0.1)
    
    for index in range(len(snake)-1, 0,-1):
        new_pos = snake[index - 1].position()
        snake[index].goto(new_pos)
    snake[0].forward(15)
    snake[0].left(45)


screen.exitonclick()

