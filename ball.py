from turtle import Turtle


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("#FF9F29")
        self.goto(position)
        self.movex = 10
        self.movey = 10
        self.ball_speed = 0.5

    def move(self):
        new_x = self.xcor() + self.movex
        new_y = self.ycor() + self.movey
        self.goto(new_x, new_y)

    def x_bounce(self):
        self.movex *= -1

    def y_bounce(self):
        self.movey *= -1

    def reset_ball(self):
        self.goto((0, -249))
