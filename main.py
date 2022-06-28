from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time

# # SCREEN SETUP # #
screen = Screen()
screen.setup(width=800,
             height=600)
screen.bgcolor("#2C3639")
screen.title("Breakout")
screen.tracer(0)

# # GAME OBJECTS # #
paddle = Paddle((0, -270))
ball = Ball((0, -249))
brick = Bricks()


# # USER ACTION # #
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")

game_on = True
while game_on:
    time.sleep(0.09)
    screen.update()
    ball.move()

    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.x_bounce()
    elif ball.ycor() > 283:
        ball.y_bounce()

    if ball.distance(paddle) < 33:
        ball.y_bounce()

    for tile in brick.bricks:
        if ball.distance(tile) < 42:
            ball.y_bounce()
            tile.hideturtle()


print(paddle.turtlesize)
screen.exitonclick()