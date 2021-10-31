from turtle import Turtle, update

STYLE = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(position)
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=STYLE)

    def addscore(self):
        self.score += 1
        self.updatescoreboard()
