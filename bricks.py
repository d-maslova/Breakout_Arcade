from turtle import Turtle
import random

COLORS = ["#D5D5D5", "#9D84B7", "#77D970", "#091353", "#753188"]


class Bricks:
    def __init__(self):
        self.bricks = []
        self.tile = Turtle()
        self.tile.penup()
        self.tile.shape("square")
        self.tile.shapesize(stretch_wid=1.5, stretch_len=3)
        self.tile.goto((-340, 250))
        self.tile.color("black", random.choice(COLORS))
        self.tile.pendown()
        self.bricks.append(self.tile)

        for tile in range(11):
            new_tile = Turtle(shape="square")
            new_tile.penup()
            new_tile.shapesize(stretch_wid=1.5, stretch_len=3)
            new_tile.color("black", random.choice(COLORS))
            new_tile.goto(x=self.bricks[-1].xcor()+61, y=self.bricks[-1].ycor())
            new_tile.stamp()
            self.bricks.append(new_tile)
        print(self.bricks)

    def destroy_brick(self, tile):
        self.bricks[tile].clearstamp(tile)
