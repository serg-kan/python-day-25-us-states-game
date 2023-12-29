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
# Scoreboard
# - somehow write to csv checked answers and save current record
# - read from csv and open game from current state

screen = turtle.Screen()
screen.title("U.S. States")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states_turtle = StatesTurtle()
scoreboard = Scoreboard()

states_data = pd.read_csv("50_states.csv")
answered_data = pd.read_csv("answered.csv")

curr_score = answered_data.shape[0]
for index, row in answered_data.iterrows():
    states_turtle.write_state((row['x'], row['y']), row['state'])

scoreboard.set_score(curr_score)

while scoreboard.score < 50:
    user_answer = screen.textinput(title=f"{scoreboard.score}/50 correct", prompt="What's another state's name?")
    state_curr = states_data[states_data["state"].str.lower() == user_answer.lower()]

    if not state_curr.empty:
        if not (answered_data["state"] == state_curr.iloc[0]["state"]).any():
            answered_data.loc[len(answered_data)] = {
                "state": state_curr.iloc[0]["state"],
                "x": state_curr.iloc[0]["x"],
                "y": state_curr.iloc[0]["y"],
            }
            scoreboard.update_score()

    answered_data.to_csv("answered.csv", index=False)





# user_answer = screen.textinput(title=f"{scoreboard.score}/50 correct", prompt="What's another state's name?")
# state_curr = states_data.index[states_data["state"].str.lower() == user_answer.lower()].tolist()
#
#
turtle.mainloop()