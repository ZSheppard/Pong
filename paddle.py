from turtle import Turtle
WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)


    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
