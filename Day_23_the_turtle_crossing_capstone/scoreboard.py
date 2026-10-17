from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(-250, 270)
        self.write(f"Level: {self.score}",align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_level(self):
        self.score += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))