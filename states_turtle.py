from turtle import Turtle

class StatesTurtle(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()

    def write_state(self, coordinates, text):
        self.goto(coordinates)
        self.write(text)

