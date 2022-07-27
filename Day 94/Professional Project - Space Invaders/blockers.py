from turtle import Turtle 


class Block(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.color("#00ff00")
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)


class Blockers:

    def __init__(self, position):
        self.blocks = []
        start_xcor = position[0]
        for _ in range(6):
            for _ in range(3):
                for _ in range(5):
                    new_block = Block()
                    new_block.goto(position)
                    self.blocks.append(new_block)
                    position = (position[0]+25, position[1])
                position = (position[0]+40, position[1])
            position = (start_xcor, position[1]-20)

    def refresh(self, position):
        for block in self.blocks:
            block.goto(1000, -1000)
        self.blocks.clear()
        self.__init__(position)
