from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clock():
    tim.right(15)


def move_counterclock():
    tim.left(15)


def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counterclock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=reset)

screen.exitonclick()