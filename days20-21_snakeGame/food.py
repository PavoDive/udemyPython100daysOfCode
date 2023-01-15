from turtle import Turtle
from random import randint

####### This is the first that came to my mind ########
# But I didn't use any of the inheritance things, that were
# supposed to be the core of this session. So I'm commenting it out
# and giving the inheritance thing a go.

# class Food:
#     def __init__(self):
#         self.create_food()

#     def create_food(self):
#         self.food = Turtle("circle")
#         self.food.color("blue")
#         self.food.penup()
#         self.food.setposition(x = random.randint(-300, 300), y = random.randint(-300, 300))
        
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len = .5, stretch_wid = .5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x = randint(-280, 280), y = randint(-280, 280))
        
