from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_level = 1
        self.hideturtle()
        self.penup()

    def update_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.starting_level}", align="center", font=FONT)

    def increase_level(self):
        self.starting_level += 1

    def game_over(self):
        self.home()
        self.write("Game Over.", align="center", font=FONT)
