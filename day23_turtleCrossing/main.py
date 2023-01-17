import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CARS_IN_BATCH = 20

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Gio's Turtle Crossing")
screen.tracer(0)
screen.listen()

player = Player()

def create_batch(number_of_cars):
    cars = []
    for i in range(number_of_cars):
        new_car = CarManager()
        cars.append(new_car)
    return cars

cars = create_batch(CARS_IN_BATCH)

scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    for car in cars:
        car.move()
        car.replace_car()
        if player.distance(car) < 20:
            scoreboard.gameover()
            game_is_on = False
 
    if player.is_finish():
        scoreboard.increase()
        player.restart()
        for car in cars:
            car.speed_increase()

screen.exitonclick()



    
