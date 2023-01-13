import turtle
from turtle import Turtle, Screen

timy = Turtle()
timy.shape("turtle")
timy.color("purple")

############## draw a square ##############
# def advance_turn_right(who, size):
#     who.forward(size)
#     who.right(90)
#
#
# def square(who, size):
#     for i in range(1, 5):
#         advance_turn_right(who, size)

# square(timy, 100)


########## draw a dashed line #############
# for i in range(20):
#     timy.pendown()
#     timy.forward(10)
#     timy.penup()
#     timy.forward(10)

########## daw triangle - decagon ##########
import random


#
# for i in range(3, 11):
#     angle = 360 / i
#     tup = (random.random(), random.random(), random.random())
#     timy.pencolor(tup)
#     for _ in range(i):
#         timy.forward(100)
#         timy.right(angle)

############# draw a random walk ###########

# from random import choice, random
#
# lengths = [8, 16, 24]
# angles = [-180, -90, 0, 90]
# timy.pensize(4)
#
# for i in range(200):
#     tup = (random(), random(), random())
#     timy.pencolor(tup)
#     timy.forward(choice(lengths))
#     timy.right(choice(angles))

############ draw a spirograph ################
# from random import random
# angle = 0
# timy.speed("fastest")
#
# for i in range(90):
#     tup = (random(), random(), random())
#     timy.pencolor(tup)
#     timy.circle(100)
#     timy.right(angle)
#     angle += 1


########### draw hirst dots ###########
from spotPainting import color_list
from random import choice

turtle.colormode(255)
timy.penup()
timy.hideturtle()

def make_line(who, dot_size, advance):
    who.dot(dot_size)
    who.penup()
    who.forward(advance)

def move_y_pos(who, increment):
    actual_position_y = who.position()[1]
    who.setposition(-200, actual_position_y + increment)

increment = 50
timy.setposition(-200, -200)

for y in range(10):
    for x in range(10):
        timy.pencolor(choice(color_list))
        make_line(timy, 20, 50)
    move_y_pos(timy, increment)






my_screen = Screen()
my_screen.exitonclick()
