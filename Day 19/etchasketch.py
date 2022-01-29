from turtle import Turtle, Screen

tom = Turtle()

screen = Screen()
screen.listen()

def move_forward():
    tom.pendown()
    tom.forward(10)
    
    
def move_backward():
    tom.pendown()
    tom.backward(10)
    
    
def turn_clockwise():
    tom.pendown()
    tom.right(10)
    
    
def turn_counterclockwise():
    tom.pendown()
    tom.left(10)
    

def clear_screen():
    tom.penup()
    tom.clear()
    tom.setposition(0,0)
    tom.setheading(0)
    
    
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='d', fun=turn_clockwise)
screen.onkeypress(key='a', fun=turn_counterclockwise)
screen.onkeypress(key='c', fun=clear_screen)
# screen.onkey()
screen.exitonclick()
