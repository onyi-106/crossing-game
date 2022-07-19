import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_y = random.randint(-280, 240)
        car = Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.goto(280, random_y)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
