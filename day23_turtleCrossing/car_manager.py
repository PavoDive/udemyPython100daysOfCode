from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANES = list(range(-260, 270, 10))

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.advance = STARTING_MOVE_DISTANCE
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.penup()
        self.setheading(180)
        self.create_car()



    def create_car(self):
        self.setposition(randint(20, 1500), choice(LANES))


    def replace_car(self):
        if self.xcor() < -350:
            self.goto(randint(330, 350), choice(LANES))
        # for i in range(amount):
        #     new_car = self.create_car()
        #     self.batch.append(new_car)
        # return self.batch
     
    # def position_car(self):
    #     self.setposition(320, randint(-270, 270))


    def move(self):
        self.goto(self.xcor() - self.advance, self.ycor())

        
    def speed_increase(self):
        self.advance += MOVE_INCREMENT


        
