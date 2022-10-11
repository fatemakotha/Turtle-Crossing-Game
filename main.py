import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, key="Up")
screen.onkey(player.go_down, key="Down")

cars = CarManager()




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()











