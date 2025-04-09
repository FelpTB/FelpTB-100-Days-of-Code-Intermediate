from turtle import Turtle

MV_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_s()

    def create_s(self):
        for i in range(3):
            t = Turtle()
            t.penup()
            t.shape("square")
            t.color("white")
            t.goto(i * -20, 0)
            self.segment.append(t)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            newx = self.segment[seg - 1].xcor()
            newy = self.segment[seg - 1].ycor()
            self.segment[seg].goto(newx, newy)
        self.segment[0].forward(MV_DISTANCE)

    def grown(self):
        t = Turtle()
        t.penup()
        t.shape("square")
        t.color("white")
        newx = self.segment[len(self.segment) - 1].xcor()
        newy = self.segment[len(self.segment) - 1].ycor()
        t.goto(newx, newy)
        self.segment.append(t)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)


    def reset(self):
        for seg in self.segment:
            seg.goto(10000, 10000)
        self.segment.clear()
        self.create_s()


