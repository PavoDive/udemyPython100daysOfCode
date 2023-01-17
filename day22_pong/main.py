from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from random import choice
from scoreboard import Scoreboard

# Create the board with screen dimensions

screen = Screen()
screen.setup(width = 800, height = 600)

screen.bgcolor("black")
screen.title("Gio's PONG")
screen.tracer(0)

# create the rackets
# this could be a class


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
paddle_l.color("red")

ball = Ball()

score_l = Scoreboard((-175, 280))
score_r = Scoreboard((175, 280))
score_l.color("red")

screen.listen()

# there should be methods for movement upon key input
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")




# Create the scoreboard (similar to the other scoreboard?)
# this could be a class
# there should be a method por score keeping

# Create the medium field dashed line

# create superior and inferior walls


# create the "ball"
# this could be a class
# there should be a method for bouncing upon contact with the rackets or walls
# angle (.towards) is negative upon interaction


game_is_on = True

possible_steps = [-1, 1]
x_step = 10 * choice(possible_steps)
y_step = 10 * choice(possible_steps)

while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.speed("normal")
    ball.move(x_step, y_step)
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        y_step *= -1
    elif (ball.xcor() >= 330 and ball.distance(paddle_r) < 50) or (ball.xcor() <= -330 and ball.distance(paddle_l) < 50):
        x_step *= -1
        

    if ball.xcor() >= 380:
        score_l.increase_score()
        ball.home()
        x_step *= -1
    if ball.xcor() <= -380:
        score_r.increase_score()
        ball.home()
        x_step *= -1



screen.exitonclick()
