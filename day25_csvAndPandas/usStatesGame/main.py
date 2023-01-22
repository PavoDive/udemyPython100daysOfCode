import turtle
import pandas
from state import State
from scoreboard import Scoreboard

states = pandas.read_csv("50_states.csv").reset_index()

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# I we wanted to get the coordinates:
# def get_mouse_click_coordinates(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coordinates)

scoreboard = Scoreboard()


def fill_non_guessed(guessed_states, states):
    for state_name in list(states.state[~states.state.isin(guessed_states)].values):
        new_state = states[states.state == state_name]
        text_on_map = State("red", state_name, new_state.x.item(), new_state.y.item())


correct_states = []
game_is_on = True
answer_state = ""

while game_is_on:
    if answer_state in correct_states:
        next
    elif answer_state in states.state.values:
        new_state = states[states.state == answer_state]
        correct_states.append(answer_state)
        text_on_map = State("black", new_state.state.item(), new_state.x.item(), new_state.y.item())
        scoreboard.increase_score()
    elif answer_state.lower() == "give up":
        game_is_on = False
        fill_non_guessed(correct_states, states)
        break

    if len(correct_states) == 50:
        game_is_on = False

    answer_state = screen.textinput(title = "Guess the state", prompt = "What's the state name? Or 'Give up'").title()
                            




# this is an alternative to screen.exitonclick() to avoid it extiting
turtle.mainloop()

