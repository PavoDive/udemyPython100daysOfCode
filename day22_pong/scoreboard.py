from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.setposition(position[0], position[1])
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.score}", move = False, align = "center", font = ("Arial", 12, "bold"))
        
