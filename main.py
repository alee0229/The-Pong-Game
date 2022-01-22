import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("THE PONG GAME")
screen.tracer(0)


ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = ScoreBoard()


screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 350:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.restart()
        scoreboard.r_point()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
screen.exitonclick()
