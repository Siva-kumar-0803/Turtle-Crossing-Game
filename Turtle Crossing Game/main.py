from turtle import Screen
from create_turtle import Turtles
from car import Car
from scoreboard import Scoreboard
import time
import random

new = random.randint(10, 20)
new2 = random.randint(10, 20)
new3 = random.randint(10, 20)
new4 = random.randint(10, 20)

screen = Screen()
screen.tracer(0)

turtle = Turtles((0, -180))
car = Car((250, -120), "yellow", 1)
car2 = Car((250, -60), "blue", 1)
car3 = Car((250, 0), "green", 1)
car4 = Car((250, 60), "red", 1)
sc = Scoreboard()

screen.setup(500, 400)
screen.title("Turtle Crossing Game")


def is_collision(car, t):
    distance = car.distance(t)
    if distance < 20:
        return True
    else:
        return False


game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    screen.listen()

    car.move_left1(new)
    car2.move_left2(new2)
    car3.move_left3(new3)
    car4.move_left4(new4)

    if turtle.ycor() == 120:
        sc.count()

    if (is_collision(car=car, t=turtle) or is_collision(car=car2, t=turtle) or is_collision(car=car3, t=turtle) or
            is_collision(car=car4, t=turtle)):
        game_over = True
        sc.finish()

    if turtle.ycor() < 120:
        screen.onkey(turtle.move_up, "Up")
    else:
        turtle.goto(0, -180)

    if car.xcor() < -230:
        car.goto(250, -120)
    if car2.xcor() < -230:
        car2.goto(250, -60)
    if car3.xcor() < -230:
        car3.goto(250, 0)
    if car4.xcor() < -230:
        car4.goto(250, 60)
screen.exitonclick()
