from turtle import Turtle, Screen
colours = [(25, 108, 164), (194, 38, 81), (236, 160, 53), (234, 214, 87), (222, 136, 175), (143, 107, 56), (103, 195, 218), (206, 166, 29), (213, 73, 92), (20, 57, 132), (143, 28, 71), (238, 88, 48), (118, 191, 140), (4, 185, 174), (141, 208, 227), (105, 107, 198), (5, 160, 87), (98, 51, 36), (21, 158, 209), (231, 165, 183), (88, 43, 29), (28, 41, 86), (30, 86, 90), (231, 174, 162), (156, 210, 190), (174, 185, 220), (243, 206, 6), (102, 15, 49), (29, 91, 88), (92, 59, 34)]

tom = Turtle()

screen = Screen()
screen.colormode(255)


def colour_picker():
    """Returns a randomly chosen colour from thw colours list"""
    import random
    return random.choice(colours)


def paint_dots():
    """Draws 10 dots"""
    for _ in range(0, 10):
        tom.dot(20, colour_picker())
        tom.penup()
        tom.forward(50)


def change_position():
    """Moves the turtle to the start of a new line"""
    global y_axis
    y_axis += 50
    tom.setposition(x_axis, y_axis)


# this is to make provide enough room for thw painting
tom.penup()
tom.hideturtle()
tom.sety(-220.00)
tom.setx(-230.00)

y_axis = tom.ycor()
x_axis = tom.xcor()

for _ in range(10):
    paint_dots()
    change_position()

screen.exitonclick()
