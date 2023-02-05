from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Gio's Snake Game")
screen.tracer(0) # turn animation off

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15: # food is 10x10
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.snake[1:]: # this is the way of calling all the segments, except by the head
        # if segment == snake.head:
        #     pass
        # el
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
screen.exitonclick()
