from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(-100, -100)
        self.color("white")
        self.xmove = 10
        self.ymove = 10
        self.bounceCount = 0


    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)


    def bounce_y(self):
        self.ymove *= -1
        self.ymove *= 1.1

    def bounce_x(self):
        self.xmove *= -1
        self.xmove *= 1.1






