import time
from snake import Snake
from food import Food
from score import Score
from turtle import Screen, Turtle

screen = Screen()
screen.setup(592, 592)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

orochi = Snake()
apple = Food()
scoreboard = Score()

with open('data.txt', mode='r') as file:
    scoreboard.highScore = int(file.read())


screen.listen()
screen.onkey(orochi.up, "Up")
screen.onkey(orochi.down, "Down")
screen.onkey(orochi.left, "Left")
screen.onkey(orochi.right, "Right")

screen.update()

game = True
while game:
    screen.update()
    time.sleep(0.1)
    orochi.move()

    # Colisão com a frutinha
    if orochi.segment[0].distance(apple) < 15:
        scoreboard.count()
        apple.refresh()
        orochi.grown()

    # Colisão com a parede
    if orochi.segment[0].xcor() >= 300 or orochi.segment[0].xcor() <= -300 or orochi.segment[0].ycor() >= 300 or \
            orochi.segment[0].ycor() <= -300:
        scoreboard.reset()
        orochi.reset()

    # Colisão com a cauda
    for segment in orochi.segment[1:]:
        # if segment == orochi.segment[0]:
        #     pass
        if orochi.segment[0].distance(segment) < 10:
            scoreboard.reset()
            orochi.reset()

screen.exitonclick()
