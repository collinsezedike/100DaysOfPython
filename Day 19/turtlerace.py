from turtle import Turtle, Screen, width
import random

turtle_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def draw_track():
    """Creates a referee turtle that draws a race track"""
    referee = Turtle()
    referee.pensize(2)
    referee.color('white')
    referee.hideturtle()

    referee.setheading(270)
    referee.penup()
    referee.goto(-210, 150)
    referee.pendown()
    referee.forward(300) 

    y_axis = 150
    for _ in range(7):
        referee.setheading(0)
        referee.penup()
        referee.goto(-240, y_axis)
        referee.pendown()
        referee.forward(470)
        y_axis -= 50

    referee.setheading(270)
    referee.penup()
    referee.goto(210, 150)
    referee.pendown()
    referee.forward(300) 


def random_dist():
    return random.randint(0, 10)


screen = Screen()
screen.bgcolor('chocolate')
screen.setup(width= 500, height=400)


turtles_list = []
y_postion = -125
for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(turtle_colours[index])
    new_turtle.goto(-230, y_postion)
    y_postion += 50
    turtles_list.append(new_turtle)

draw_track()

user_bet = screen.textinput(
    title="Make your bet", 
    prompt="Which turtle will win the race? Enter a colour (Red/Orange/Yellow/Green/Blue/Purple)").lower()
has_winner = False
while not has_winner:
    for turtle in turtles_list:
        turtle.forward(random_dist())
        if turtle.xcor() > 195:
            has_winner = True
            winner = turtle.pencolor()

if user_bet == winner:
    print(f"You won!. The winner was the {winner} turtle.")
else:
    print(f"You lost. The winner was the {winner} turtle.")

screen.exitonclick()
