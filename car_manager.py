from turtle import Turtle
import random


COLORS = ["yellow", "blue", "red", "purple", "green", "orange"]
CAR_MOVE = 5
INCREASE_SPEED = 10

class Car_manager:

    def __init__(self):
        self.all_cars = []
        self.move = CAR_MOVE

    def create_car(self):
        random_move = random.randint(1, 6)
        if random_move == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_y = random.randint(-260, 260)
            new_car.goto(300, new_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.move)

    def increase_speed(self):
        self.move += INCREASE_SPEED