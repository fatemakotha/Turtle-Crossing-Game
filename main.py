import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Turtle()
tim.color("black")
tim.shape("turtle")
tim.penup()
tim.goto(x=0, y=-280)
tim.left(90)




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()










