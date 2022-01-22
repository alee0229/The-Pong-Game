from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.speed("fastest")
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            new_x = self.xcor()
            new_y = self.ycor() + 50
            self.goto(new_x, new_y)

    def down(self):
        if self.ycor() > -250:
            new_x = self.xcor()
            new_y = self.ycor() - 50
            self.goto(new_x, new_y)
