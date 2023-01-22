from turtle import Turtle

class Scoreboard(Turtle):
    """Documentation for Scoreboard

    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 245)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        score_string = f"Current Score: {self.score}/50"
        self.write(score_string, align = "center", font = ("Arial", 18, "bold"))

    def increase_score(self):
        self.score += 1
        self.refresh_score()
        
        
