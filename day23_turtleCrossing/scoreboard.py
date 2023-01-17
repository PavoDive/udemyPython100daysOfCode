from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("black")
        self.setposition(0, 220)
        self.score = 0
        self.show()


    def show(self):
        self.clear()
        self.write(f"Score: {self.score}", move = False, align = "center", font = FONT)

    def increase(self):
        self.score += 1
        self.show()

    def gameover(self):
        self.home()
        self.write("Game Over", move = False, align = "center", font = ("Arial", 20, "bold"))
