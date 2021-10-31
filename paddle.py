from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def goup(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def godown(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)
