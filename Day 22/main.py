from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

KEYS = ["Up", "Down", "w", "s"]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=600)
screen.title("Pong")
screen.tracer(0)

def draw_boundary():
    bound = Turtle()
    bound.hideturtle()
    bound.color("white")
    bound.penup()
    bound.goto(-520, 280)
    bound.setheading(270)
    bound.pendown()
    for _ in range(2):
        bound.forward(550)
        bound.left(90)
        bound.forward(1050)
        bound.left(90)


draw_boundary()
right_paddle = Paddle((440, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(key=KEYS[0], fun=right_paddle.up)
screen.onkeypress(key=KEYS[1], fun=right_paddle.down)
screen.onkeypress(key=KEYS[2], fun=left_paddle.up)
screen.onkeypress(key=KEYS[3], fun=left_paddle.down)


screen.tracer(0)
game_on = True
while game_on:    
    screen.update()
    time.sleep(ball.movespeed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 260 or ball.ycor() < -250:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 415) or (ball.distance(left_paddle) < 50 and ball.xcor() < -425):
        ball.movespeed *= 0.9
        ball.bounce_x()

    # If right paddle misses
    if ball.xcor() > 490:
        ball.home()
        ball.movespeed = ball.startspeed
        ball.angle = 225
        score.l_score += 1
        score.update_score()

    # If left paddle misses
    elif ball.xcor() < -500:
        ball.home()
        ball.movespeed = ball.startspeed 
        ball.angle = 45
        score.r_score += 1
        score.update_score()


screen.exitonclick()
