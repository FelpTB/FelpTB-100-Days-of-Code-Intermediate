from turtle import Turtle

FONT = ("Roboto", 14, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.goto(0, 260)
        self.pencolor("blue")
        self.penup()
        self.hideturtle()
        self.att()

    def att(self):
        self.goto(0, 260)
        self.clear()
        self.write(f"Score = {self.score} HighScore = {self.highScore}", True, "center", FONT)

    def count(self):
        self.goto(0, 260)
        self.score += 1
        self.att()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
        with open('data.txt', mode='w') as file:
            file.write(str(self.highScore))
        self.score = 0
        self.att()


    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", True, "center", FONT)


