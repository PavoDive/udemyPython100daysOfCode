from turtle import Turtle

# WIDTH = 20
# LENGTH = 100
# X_POS = 350
# Y_POS = 0
MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.goto(position[0], position[1])


        
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT)

        
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT)

