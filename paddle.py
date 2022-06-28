from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("#DCD7C9")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.goto(position)

    def go_right(self):
        self.setx(self.xcor()+12)

    def go_left(self):
        self.setx(self.xcor()-12)
