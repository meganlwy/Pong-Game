from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()


screen.listen()
screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "x")

r_score = Score((200, 200))
l_score = Score((-200, 200))

gameon = True
while gameon:
    time.sleep(ball.sleeptime)  # get each while loop to sleep a little bit
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:  # bounce when hit the wall
        ball.bounce_y()
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):  # bounce when hit the paddles
        ball.bounce_x()
    if ball.xcor() > 380:  # left player +1
        ball.restart()
        l_score.addscore()
    elif ball.xcor() < -380:  # right player +1
        ball.restart()
        r_score.addscore()

screen.exitonclick()
