from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()

        self.score = 0

    def update_score(self):
        self.score += 1

    def set_score(self, score):
        self.score = score
