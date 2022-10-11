from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(COLORS[random.randint(0, 7)])
        self.shapesize(stretch_wid=1, stretch_len=2)

    def move_left(self):
        new_x = self.xcor() - 5
        self.goto(x=new_x, y=self.ycor())
