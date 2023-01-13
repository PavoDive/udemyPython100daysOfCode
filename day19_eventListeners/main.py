from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)

def turn_counter_clockwise():
    tim.left(10)

def reset_screen():
    tim.reset()
    
# w = forward
# s = backward
# a = counter-clockwise
# d = clockwise

screen.listen()

screen.onkey(fun = move_forward, key= "w")
screen.onkey(fun = move_backward, key = "s")
screen.onkey(fun = turn_clockwise, key = "d")
screen.onkey(fun = turn_counter_clockwise, key = "a")
screen.onkey(fun = reset_screen, key = "c")

screen.exitonclick()
