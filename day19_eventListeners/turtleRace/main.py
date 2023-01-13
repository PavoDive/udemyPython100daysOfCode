from turtle import Turtle, Screen
from random import random

screen = Screen()
screen.setup(width = 500, height = 400)

race_is_on = False

user_bet = screen.textinput(title = "Make yor bet", prompt = "Which turtle will win the race? Enter the color: (red/blue/green/yellow/purple/magenta)").lower()

colors = ["red", "blue", "green", "yellow", "purple", "magenta"]

initial_x = -220
initial_y = -160
y_increment = 60

all_turtles = []

for color in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(initial_x, initial_y)
    initial_y += y_increment
    new_turtle.color(color)
    
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} is the Winning Turtle")
                break
            else:
                print(f"You lost! The {winning_turtle} is the Winning Turtle")
                break
        turtle_movement = 10 * random()
        turtle.forward(turtle_movement)


screen.exitonclick()
                       
