from turtle import Turtle


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, state_name, state_cord):
        self.goto(state_cord)
        self.write(state_name, align="center")

    def game_over(self):
        self.home()
        self.write("You win!", align="center", font=("Courier", 20, "bold"))

