import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


def game(carRate, game_is_on):
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        car_manager.move()

        if carRate >= 6:
            car_manager.spawn()
            carRate = 0

        if player1.ycor() >= 300:
            player1.reset()
            scoreboard.score += 1
            scoreboard.update()
            car_manager.speed += 5

        for i in car_manager.cars:
            if player1.distance(i) <= 20:
                player1.reset()
                car_manager.speed = 5
                scoreboard.reset()
                game_is_on = False

        carRate += 1


player1 = Player()

player1.setheading(90)

scoreboard = Scoreboard()

car_manager = CarManager()


screen.listen()
screen.onkey(player1.move, "w")

game(6, True)

screen.exitonclick()
