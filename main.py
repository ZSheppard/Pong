#Pong Arcade Game
#Zachary Sheppard
#September 6, 2023

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

lEFT_PADDLE_STARTING_POSITION = (-350, 0)
RIGHT_PADDLE_STARTING_POSITION = (350, 0)

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_PADDLE_STARTING_POSITION)
l_paddle = Paddle(lEFT_PADDLE_STARTING_POSITION)
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

direction = random.choice([-1, 1])

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    elif ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect when R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()

    #Detect when L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()


screen.exitonclick()
