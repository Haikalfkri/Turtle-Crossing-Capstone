from turtle import Turtle

PLAYER_POSITION = (0, -280)
PLAYER_MOVE = 10
LINE_Y = 290

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.position()
        self.setheading(90)

    def go_up(self):
        self.forward(PLAYER_MOVE)

    def position(self):
        self.goto(PLAYER_POSITION)

    def is_in_line(self):
        if self.ycor() > LINE_Y:
            return True
        else:
            return False