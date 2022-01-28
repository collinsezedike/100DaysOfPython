from turtle import Turtle, Screen

thomas = Turtle()
# thomas.pensize(15)
thomas.speed('fastest')

screen = Screen()
screen.colormode(255)
# screen.bgcolor((200, 200, 200))


# draw a square
# for _ in range(4):
#     thomas.forward(100)
#     thomas.left(90)

# draw a dashed line
# for _ in range(15):
#     thomas.forward(10)
#     thomas.penup()
#     thomas.forward(10)
#     thomas.pendown()

# draw multiple shapes
## a list of the sides
# shapes = []
# for num in range(3,11):
#     shapes.append(num)


## randomly generate color
def colour_picker():
    '''Returns a randomly generated colour'''
    from random import randint
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colour = (r, g, b)
    return colour


# for side in shapes:
#     thomas.color(colour_picker())
#     for _ in range(side):
#         thomas.forward(100)
#         thomas.right(360//side)

# a random walk
# import random
# dist = 30
# angle = 90

# def choose_path():
#     coin = random.randint(0,2)
#     if coin == 0:
#         thomas.left(angle)
#         thomas.forward(dist)
#     elif coin == 1:
#         thomas.right(angle)
#         thomas.forward(dist)
#     else:
#         thomas.forward(dist)


# for _ in range(300):
#     thomas.color(colour_picker())
#     choose_path()

# make a spirograph
gap_size = 5

for _ in range(360//gap_size):
    thomas.color(colour_picker())
    thomas.circle(100)
    thomas.left(gap_size)


screen.exitonclick()
