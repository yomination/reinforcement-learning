import random


gamma = 0.1

total_visits_table = {}

q_value_table = {}

valid_starting_positions = ("B2","B3","B4","B5",
                            "C3","C4","C6",
                            "D3","D6",
                            "E2","E3","E4","E5","E6",
                            )
intial_rewards_table = {
  "A1":-50,"A2":-50,"A3":-50,"A4":-50,"A5":-50,"A6":-50,"A7":-50,
  "B1":-50,"B2":0,"B3":0,"B4":0,"B5":0,"B6":"WALL","B7":-50,
  "C1":-50,"C2":"WALL","C3":0,"C4":0,"C5":"WALL","C6":0,"C7":-50,
  "D1":-50,"D2":"WALL","D3":0,"D4":100,"D5":"WALL","D6":0,"D7":-50,
  "E1":-50,"E2":0,"E3":0,"E4":0,"E5":0,"E6":0,"E7":-50,
  "F1":-50,"F2":-50,"F3":-50,"F4":-50,"F5":-50,"F6":-50,"F7":-50,
}

reward_for_move = {
    "NORTH":-3,
    "SOUTH":-1,
    "EAST":-2,
    "WEST":-2
}

directions = ("NORTH",
              "SOUTH",
              "EAST",
              "WEST")


def starting_position():
    return random.choice(valid_starting_positions)

  
def get_random_direction():
    return random.choice(directions)

def get_max_q_value(position):

    q_values_all_directions = [
        q_value_table.get(position+"_"+directions[0]),
        q_value_table.get(position+"_"+directions[1]),
        q_value_table.get(position+"_"+directions[2]),
        q_value_table.get(position+"_"+directions[3])
    ]
    return max(q_values_all_directions)

def calculate_q_value(current_position, current_direction, future_position, future_direction):
    current_point = current_position+"_"+current_direction
    future_point = future_position+"_"+future_direction

    current_state_q = q_value_table.get(current_point)
    
    number_of_tries_ratio = 1 / (1 + total_visits_table.get(current_point))
    current_action_reward = reward_for_move.get(current_direction)

    max_q_value = get_max_q_value(future_position)

    gamma_probability = current_state_q + number_of_tries_ratio * \
         ( current_action_reward + gamma * \
         max_q_value - current_state_q )
    return gamma_probability

if __name__ == "__main__":
    print("Hello")