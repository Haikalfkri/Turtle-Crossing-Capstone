from turtle import Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
car_manager = Car_manager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

is_in_game = True
while is_in_game:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_move()

    # Detect Collision with top
    if player.is_in_line():
        player.position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    # Detect Collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            is_in_game = False


screen.exitonclick()