import turtle
from states import *
from writer import Writer

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.setup(width=730, height=496)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


def end_game():
    not_guessed_states = []
    for state in STATES_LIST:
        if state in correct_guesses:
            pass
        else:
            not_guessed_states.append(state)
            writer.color("red")
            writer.write_state(state_name=state, state_cord=get_state_cord(state))
    return not_guessed_states


writer = Writer()
correct_guesses = set()

num_states = len(STATES_LIST)

game_on = True
while game_on:

    num_correct = len(correct_guesses)

    # when user has guessed all the states
    if num_correct == num_states:
        game_on = False
        writer.game_over()
    else:
        user_answer = screen.textinput(title=f"{num_correct}/{num_states} States Correct",
                                       prompt="What's another state?").title().strip()
        if user_answer in STATES_LIST:
            writer.write_state(state_name=user_answer, state_cord=get_state_cord(user_answer))
            correct_guesses.add(user_answer)
        # end game prematurely
        if user_answer == "Exit":
            game_on = False
            remaining_states = end_game()
            remaining_states_csv(remaining_states)

screen.exitonclick()

