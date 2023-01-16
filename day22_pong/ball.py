from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()


    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self, x_step, y_step):
        self.goto(self.xcor() + x_step, self.ycor() + y_step)


