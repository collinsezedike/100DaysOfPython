from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
for i in range(10):
    timmy.forward(30)
    timmy.circle(30)
    timmy.left(60)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.bgcolor('black')
my_screen.exitonclick()
