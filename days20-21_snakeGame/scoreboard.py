from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.shape("circle")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.setposition(x = 0, y = 280)
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move = False, align = "center", font = ("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move = False, align = "center", font = ("Arial", 10, "bold"))
