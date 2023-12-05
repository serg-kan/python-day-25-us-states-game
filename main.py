import turtle
import pandas as pd
from states_turtle import StatesTurtle
from scoreboard import Scoreboard

# Algorithm #
# 1. setup screen and turtle
# 2. get a user input
# 3. compare it with data
#     3.1. read csv file
#     3.2. find user input in data
#     3.3. if there is a match, get coordinates
# 4. handle answer
#     4.1. print state name on the map
# 5. make it work in a loop
# 6. refactor, if needed

screen = turtle.Screen()
screen.title("U.S. States")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_turtle = StatesTurtle()
scoreboard = Scoreboard()

states_data = pd.read_csv("50_states.csv")

while scoreboard.score < 50:
    user_answer = screen.textinput(title=f"{scoreboard.score}/50 correct", prompt="What's another state's name?")

    # read data
    state_curr = states_data[states_data["state"].str.lower() == user_answer.lower()]

    if not state_curr.empty:
        state_coordinates = (state_curr.iloc[0][1], state_curr.iloc[0][2])
        states_turtle.write_state(coordinates=state_coordinates, text=state_curr.iloc[0][0])
        scoreboard.update_score()

turtle.mainloop()