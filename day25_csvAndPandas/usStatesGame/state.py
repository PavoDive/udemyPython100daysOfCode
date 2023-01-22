from turtle import Turtle

class State(Turtle):
    """Documentation for State

    """
    def __init__(self, color, state_name, state_x, state_y):
        super().__init__()
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.color(color)
        self.setposition(state_x, state_y)
        self.write(state_name, move = False)
        
        
