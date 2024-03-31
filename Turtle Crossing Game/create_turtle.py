from turtle import Turtle
class Turtles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.color("purple")
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
