import turtle
from turtle import Turtle, Screen
import random


colors = ["red","orange","yellow","green","blue","purple",]

is_race_on = False
screen = Screen()
screen.setup(520,400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
all_turtles = []

y = -100
for t in colors:
    new_T = Turtle(shape="turtle")
    new_T.color(t)
    new_T.penup()
    new_T.goto(-250, y)
    y += 30
    all_turtles.append(new_T)


if user_bet:
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            winner = t.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

        dist = random.randint(0,10)
        t.forward(dist)

screen.exitonclick()