import pandas

states_df = pandas.read_csv("50_states.csv")
STATES_LIST = states_df.state.to_list()


def get_state_cord(answer_state):
    answer_row = states_df[states_df.state == answer_state]
    ans_cord = (int(answer_row.x), int(answer_row.y))
    return ans_cord


def remaining_states_csv(remaining_states):
    pandas.DataFrame(remaining_states).to_csv("remaining_states.csv")

