from turtle import Turtle
FONT = ("TIMES NEW ROMAN", 20, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.time = 0.5
        self.color("Black")
        self.penup()
        self.goto(-200, 160)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def count(self):
        self.score += 1
        self.time -= 0.1
        self.clear()
        self.update_score()

    def finish(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

    def inc_speed(self):
        self.time -= 0.1
