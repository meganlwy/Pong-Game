from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("yellow")
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.sleeptime = 0.1

    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx, newy)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.sleeptime *= (
            0.9  # each time the ball collide with the paddle, the speed will get faster
        )

    def restart(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.sleeptime = 0.1
