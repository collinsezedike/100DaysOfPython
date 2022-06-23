from turtle import Turtle 


class NewBlock(Turtle):
    def __init__(self, color):
        super().__init__()
        self.penup()
        # self.shapesize(stretch_len=3.5, stretch_wid=2)
        self.shape("square")
        self.color(color)


class Blocks:
    def __init__(self):
        self.blocks = []
        self.block_color = ""
        self.first_block_xcor = -230
        self.first_block_ycor = 0

    def add_new_block(self):
        for _ in range(14):
            new_block = NewBlock(self.block_color)
            self.blocks.append(new_block)

    def goto_position(self):
        for block in self.blocks:
            block.goto(self.first_block_xcor, self.first_block_ycor)
            self.first_block_xcor += 35


class RedBlocks(Blocks):
    def __init__(self):
        super().__init__()
        self.block_color = "red"
        self.first_block_ycor = 280
        self.add_new_block()
        self.goto_position()


class OrangeBlocks(Blocks):
    def __init__(self):
        super().__init__()
        self.block_color = "orange"
        self.first_block_ycor = 250
        self.add_new_block()
        self.goto_position()


class YellowBlocks(Blocks):
    def __init__(self):
        super().__init__()
        self.block_color = "yellow"
        self.first_block_ycor = 220
        self.add_new_block()
        self.goto_position()
