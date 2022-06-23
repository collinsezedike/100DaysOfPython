import random
from turtle import Screen, Turtle

from paddle import Paddle
from ball import Ball
from block import RedBlocks, OrangeBlocks, YellowBlocks
from writer import Writer
import time

BALL_SPEED = 0.05


def draw_wall():
    wall = Turtle()
    wall.hideturtle()
    wall.color("white")
    wall.pensize(10)
    wall.penup()
    wall.goto(-250, -300)
    wall.pendown()
    wall.setheading(90)
    wall.forward(600)
    wall.setheading(wall.heading() - 90)
    wall.forward(494)
    wall.setheading(wall.heading() - 90)
    wall.forward(600)
    wall.setheading(wall.heading() - 90)


def restart_game():
    ball.goto(0, 0)
    ball.setheading(random.randint(45, 135))
    if ball.heading() in range(81, 101):
        ball.setheading(random.randint(45, 135))


screen = Screen()
screen.setup(width=500, height=600)
screen.bgcolor("black")
screen.title("Breakout")
draw_wall()
screen.tracer(0)

paddle = Paddle()
ball = Ball()
writer = Writer()

# the blocks
redblocks = RedBlocks()
orangeblocks = OrangeBlocks()
yellowblocks = YellowBlocks()

screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

lives = 5
has_won = False

while lives:
    screen.update()
    time.sleep(BALL_SPEED)
    ball.move()

    # if the ball collides with the walls
    if ball.xcor() >= 230 or ball.xcor() <= -230:
        ball.bounce_x()
    if ball.ycor() >= 280:
        ball.bounce_y()

    # if the ball hits the paddle
    if ball.distance(paddle) <= 50:
        ball.bounce_y()

    # if the ball hits a red block
    for block in redblocks.blocks:
        if ball.distance(block) < 20:
            block.hideturtle()
            block.goto(10000, 10000)  # go to a very far away place beyond the screen coordinates
            redblocks.blocks.remove(block)
            ball.bounce_y()
            BALL_SPEED *= 0.8  # increase the ball speed

    # if the ball hits an orange block
    for block in orangeblocks.blocks:
        if ball.distance(block) < 20:
            block.hideturtle()
            block.goto(10000, 10000)  # go to a very far away place beyond the screen coordinates
            orangeblocks.blocks.remove(block)
            ball.bounce_y()
            BALL_SPEED *= 0.9  # increase the ball speed

    # if the ball hits a yellow block
    for block in yellowblocks.blocks:
        if ball.distance(block) < 20:
            block.hideturtle()
            block.goto(10000, 10000)  # go to a very far away place beyond the screen coordinates
            yellowblocks.blocks.remove(block)
            ball.bounce_y()
            BALL_SPEED *= 1.01  # increase the ball speed

    # if the player fails to catch the ball
    if ball.ycor() <= -290:
        lives -= 1
        restart_game()
        BALL_SPEED = 0.05
    writer.write_score(lives)

    # if the player has cleared all the blocks
    if len(redblocks.blocks) == 0 and len(orangeblocks.blocks) == 0 and len(yellowblocks.blocks) == 0:
        has_won = True
        break

if has_won:
    writer.write_win()
else:
    writer.write_lose()

screen.exitonclick()
