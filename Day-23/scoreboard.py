from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update()
        self.write(f"Level: {self.score}", align="Left", font=FONT)

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", align="Left", font=FONT)

    def reset(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="CENTER", font=FONT)
        # self.goto(0, -50)
        # self.write(f"Press space to play again", align="CENTER", font=("Courier", 14, "normal"))
        # self.score = 1



