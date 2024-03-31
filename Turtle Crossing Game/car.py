from turtle import Turtle
class Car(Turtle):
    def __init__(self, position, color, delay):
        super().__init__()
        self.shape("square")
        self.turtlesize(1, 1.5)
        self.color(color)
        self.penup()
        self.goto(position)
        self.speed(delay)

    def move_left1(self, new):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)
        self.backward(new)

    def move_left2(self, new2):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)
        self.backward(new2)

    def move_left3(self, new3):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)
        self.backward(new3)

    def move_left4(self, new4):
        new_x = self.xcor()
        new_y = self.ycor()
        self.goto(new_x, new_y)
        self.backward(new4)
