from turtle import Turtle
from turtle import Screen
import time
import random
from random import choice

# this is the ball
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

# this is the paddle
MOVEMENT = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 4)
        self.goto(position[0], position[1])

    def left(self):
        self.goto(self.xcor() - MOVEMENT, self.ycor())

        
    def right(self):
        self.goto(self.xcor() + MOVEMENT, self.ycor())

# this is the scoreboard
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

    def increase_score(self, amount):
        self.score += amount
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.score}", move = False, align = "center", font = ("Arial", 12, "bold"))

class Brick(Turtle):
    def __init__(self, position, brick_type):
        super().__init__()
        self.brick_type = brick_type
        self.create_brick(position)

    def create_brick(self, position):
        self.shape("square")
        self.color(self.brick_type)
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 4)
        self.goto(position[0], position[1])

    def kill_brick(self):
        self.goto(-1000,-1000)

############################################################
#                     GAME STARTS HERE                     #
############################################################

# Create the board with screen dimensions

screen = Screen()
screen.setup(width = 800, height = 600)

screen.bgcolor("black")
screen.title("Gio's BREAKOUT")
screen.tracer(0)

# create the paddles

paddle = Paddle((0, -290))

ball = Ball()

score = Scoreboard((0, 280))
score.color("red")

lives = Scoreboard((370, -280))
lives.color("green")
lives.increase_score(6)

screen.listen()

# there should be methods for movement upon key input
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

# create the bricks
x_pos = [-360., -280., -200., -120.,  -40.,   40.,  120.,  200.,  280., 360.]
red_bricks = []
for i in range(10):
    red_bricks.append(Brick((x_pos[i], 260), "red"))

orange_bricks = []
for i in range(10):
    orange_bricks.append(Brick((x_pos[i], 230), "orange"))

yellow_bricks = []
for i in range(10):
    yellow_bricks.append(Brick((x_pos[i], 200), "yellow"))

green_bricks = []
for i in range(10):
    green_bricks.append(Brick((x_pos[i], 170), "green"))


game_is_on = True

possible_steps = [-1, 1]
x_step = 10 * choice(possible_steps)
y_step = 10 * choice(possible_steps)

while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.speed("normal")
    ball.move(x_step, y_step)
    if (ball.ycor() >= 290) or (ball.distance(paddle) < 40):#ball.ycor() >= 290 or ball.ycor() <= -290:
        y_step *= -1
    elif abs(ball.xcor()) >= 390: #(ball.xcor() >= 330 and ball.distance(paddle) < 50) or (ball.xcor() <= -330 and ball.distance(paddle) < 50):
        x_step *= -1

    for i in red_bricks:
        if ball.distance(i) < 40:
            score.increase_score(7)
            y_step *= -1
            i.kill_brick()

    for i in orange_bricks:
        if ball.distance(i) < 40:
            score.increase_score(5)
            y_step *= -1
            i.kill_brick()

    for i in yellow_bricks:
        if ball.distance(i) < 40:
            score.increase_score(1)
            y_step *= -1
            i.kill_brick()

    for i in green_bricks:
        if ball.distance(i) < 40:
            score.increase_score(3)
            y_step *= -1
            i.kill_brick()

    if ball.ycor() <= -290:
        lives.increase_score(-1)
        ball.home()
        if lives.score == 0:
            game_is_on = False
        
screen.exitonclick()

