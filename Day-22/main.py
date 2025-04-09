import time
from turtle import Screen, Turtle
from player import Player
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Player()
player2 = Player()
player2.goto(-350, 0)

ball = Ball()
ball.setheading(45)


scoreBoard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(player1.up, "Up")
screen.onkey(player1.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")
game = True
while game:
    screen.update()
    time.sleep(0.1)
    ball.move()

    #colisão nas paredes
    if ball.ycor() >= 300 or ball.ycor() <= -300:
        ball.bounce_y()

    #colisão na direita
    if ball.distance(player1) < 60 and ball.xcor() > 340:
        ball.bounce_x()

    #colisão na esquerda
    if ball.distance(player2) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    #ponto na direita
    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.bounce_x()
        scoreBoard.l_score += 1
        scoreBoard.update()

    #ponto na esquerda
    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.bounce_x()
        scoreBoard.r_score += 1
        scoreBoard.update()



screen.exitonclick()