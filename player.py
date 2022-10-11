from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(x=0, y=-280)
        self.left(90)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 10)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 10)