from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


def draw_boundary():
    bound = Turtle()
    bound.hideturtle()
    bound.color("white")
    bound.penup()
    bound.goto(-271, 271)
    bound.setheading(270)
    bound.pendown()
    for _ in range(4):
        bound.forward(542)
        bound.left(90)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Loading")
screen.tracer(0)

draw_boundary()
snake = Snake()
food = Food()
score = ScoreBoard()
score.display_score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)


game_on = True
while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
 
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.add_tail()
        score.update_score()

    if snake.head.xcor() > 269 or snake.head.xcor() < -269 or snake.head.ycor() > 269 or snake.head.ycor() < -269:
        score.game_over()
        food.change_position()
        snake.game_over()
        
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            score.game_over()
            food.change_position()
            snake.game_over()   

screen.exitonclick()
