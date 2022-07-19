import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Player instance
player = Player()

# Car instance
cars_m = CarManager()

# Scoreboard
scoreboard = Scoreboard()

# Key registration
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_level()
    if random.randint(1, 5) == 1:
        cars_m.generate_car()
    cars_m.move()

    # Detect collision with cars_m
    for car in cars_m.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # If player finish, go to the starting location, increase the level and difficulty / car speed
    if player.finish():
        player.go_to_start()
        scoreboard.increase_level()
        cars_m.increase_speed()

screen.exitonclick()
