from turtle import Turtle, Screen

tom = Turtle()
tom.penup()


def move_forward():
    tom.pendown()
    tom.forward(10)


screen = Screen()
screen.listen()
screen.onkeypress(key='space', fun=move_forward)
screen.exitonclick()
