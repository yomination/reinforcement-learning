import random
from tkinter import *

gamma = 0.9
epsilon = 0.1
total_visits_table = {}

q_value_table = {}

valid_starting_positions = ("B2", "B3", "B4", "B5",
                            "C3", "C4", "C6",
                            "D3", "D6",
                            "E2", "E3", "E4", "E5", "E6",
                            )
intial_rewards_table = {
    "A1": -50, "A2": -50, "A3": -50, "A4": -50, "A5": -50, "A6": -50, "A7": -50,
    "B1": -50, "B2": 0, "B3": 0, "B4": 0, "B5": 0, "B6": "WALL", "B7": -50,
    "C1": -50, "C2": "WALL", "C3": 0, "C4": 0, "C5": "WALL", "C6": 0, "C7": -50,
    "D1": -50, "D2": "WALL", "D3": 0, "D4": 100, "D5": "WALL", "D6": 0, "D7": -50,
    "E1": -50, "E2": 0, "E3": 0, "E4": 0, "E5": 0, "E6": 0, "E7": -50,
    "F1": -50, "F2": -50, "F3": -50, "F4": -50, "F5": -50, "F6": -50, "F7": -50,
}

reward_for_move = {
    "NORTH": -3,
    "SOUTH": -1,
    "EAST": -2,
    "WEST": -2
}

directions = ("NORTH",
              "SOUTH",
              "EAST",
              "WEST")


def starting_position():
    return random.choice(valid_starting_positions)


def best_direction_to_move(position):
    best_direction = ""
    # Use max q for best direction, unless hit by randomness introduced by epsilon
    if (random.random() <= epsilon):
        best_direction = random.choice(directions)
        print("Random direction triggered! for Position: ", position,
              "Now heading ", best_direction)
        return best_direction

    max_q_value = get_max_q_value(position)

    list_of_directions_for_position = list(q_value_table.get(position).keys())
    list_of_q_values_for_position = list(q_value_table.get(position).values())
    index_of_max_q_value = list_of_q_values_for_position.index(max_q_value)

    best_direction = list_of_directions_for_position[index_of_max_q_value]

    return best_direction


def get_max_q_value(position):
    all_directions_at_position = q_value_table.get(position)

    # TODO itterate through directions
    q_values_all_directions = [
        all_directions_at_position.get(directions[0]),
        all_directions_at_position.get(directions[1]),
        all_directions_at_position.get(directions[2]),
        all_directions_at_position.get(directions[3])
    ]
    return max(q_values_all_directions)


def calculate_q_value(current_position, current_direction, future_position, future_direction):
    current_state_q = q_value_table.get(current_position).get(current_direction)
    how_many_times_this_direction = total_visits_table.get(current_position).get(current_direction)

    number_of_tries_ratio = 1 / (1 + how_many_times_this_direction)
    current_action_reward = reward_for_move.get(current_direction)

    max_future_q_value = get_max_q_value(future_position)

    gamma_probability = current_state_q + number_of_tries_ratio * \
                        (current_action_reward + gamma * \
                         max_future_q_value - current_state_q)
    return gamma_probability

Row1 = list(intial_rewards_table.values())[0:7]
Row2 = list(intial_rewards_table.values())[7:14]
Row3 = list(intial_rewards_table.values())[14:21]
Row4 = list(intial_rewards_table.values())[21:28]
Row5 = list(intial_rewards_table.values())[28:35]
Row6 = list(intial_rewards_table.values())[35:42]
#print(intial_rewards_table.get("A1"))

#print(Row1)
#print(Row2)
#print(Row3)
#print(Row4)
#print(Row5)
#print(Row6)


visual_maze = Tk()
visual_maze.title("Windy Maze")

mylabel1 = Label(visual_maze, text=directions[0], padx=20, pady=20)
mylabel2 = Label(visual_maze, text=Row1[1], padx=20, pady=20)
mylabel3 = Label(visual_maze, text=Row1[2], padx=20, pady=20)
mylabel4 = Label(visual_maze, text=Row1[3], padx=20, pady=20)
mylabel5 = Label(visual_maze, text=Row1[4], padx=20, pady=20)
mylabel6 = Label(visual_maze, text=Row1[5], padx=20, pady=20)
mylabel7 = Label(visual_maze, text=Row1[6], padx=20, pady=20)

mylabel8 = Label(visual_maze, text=Row2[0], padx=20, pady=20)
mylabel9 = Label(visual_maze, text=Row2[1], padx=20, pady=20)
mylabel10 = Label(visual_maze, text=Row2[2], padx=20, pady=20)
mylabel11 = Label(visual_maze, text=Row2[3], padx=20, pady=20)
mylabel12 = Label(visual_maze, text=Row2[4], padx=20, pady=20)
mylabel13 = Label(visual_maze, text=Row2[5], padx=20, pady=20)
mylabel14 = Label(visual_maze, text=Row2[6], padx=20, pady=20)

mylabel15 = Label(visual_maze, text=Row3[0], padx=20, pady=20)
mylabel16 = Label(visual_maze, text=Row3[1], padx=20, pady=20)
mylabel17 = Label(visual_maze, text=Row3[2], padx=20, pady=20)
mylabel18 = Label(visual_maze, text=Row3[3], padx=20, pady=20)
mylabel19 = Label(visual_maze, text=Row3[4], padx=20, pady=20)
mylabel20 = Label(visual_maze, text=Row3[5], padx=20, pady=20)
mylabel21 = Label(visual_maze, text=Row3[6], padx=20, pady=20)

mylabel22 = Label(visual_maze, text=Row4[0], padx=20, pady=20)
mylabel23 = Label(visual_maze, text=Row4[1], padx=20, pady=20)
mylabel24 = Label(visual_maze, text=Row4[2], padx=20, pady=20)
mylabel25 = Label(visual_maze, text=Row4[3], padx=20, pady=20)
mylabel26 = Label(visual_maze, text=Row4[4], padx=20, pady=20)
mylabel27 = Label(visual_maze, text=Row4[5], padx=20, pady=20)
mylabel28 = Label(visual_maze, text=Row4[6], padx=20, pady=20)

mylabel29 = Label(visual_maze, text=Row5[0], padx=20, pady=20)
mylabel30 = Label(visual_maze, text=Row5[1], padx=20, pady=20)
mylabel31 = Label(visual_maze, text=Row5[2], padx=20, pady=20)
mylabel32 = Label(visual_maze, text=Row5[3], padx=20, pady=20)
mylabel33 = Label(visual_maze, text=Row5[4], padx=20, pady=20)
mylabel34 = Label(visual_maze, text=Row5[5], padx=20, pady=20)
mylabel35 = Label(visual_maze, text=Row5[6], padx=20, pady=20)

mylabel36 = Label(visual_maze, text=Row6[0], padx=20, pady=20)
mylabel37 = Label(visual_maze, text=Row6[1], padx=20, pady=20)
mylabel38 = Label(visual_maze, text=Row6[2], padx=20, pady=20)
mylabel39 = Label(visual_maze, text=Row6[3], padx=20, pady=20)
mylabel40 = Label(visual_maze, text=Row6[4], padx=20, pady=20)
mylabel41 = Label(visual_maze, text=Row6[5], padx=20, pady=20)
mylabel42 = Label(visual_maze, text=Row6[6], padx=20, pady=20)

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=0, column=1)
mylabel3.grid(row=0, column=2)
mylabel4.grid(row=0, column=3)
mylabel5.grid(row=0, column=4)
mylabel6.grid(row=0, column=5)
mylabel7.grid(row=0, column=6)

mylabel8.grid(row=1, column=0)
mylabel9.grid(row=1, column=1)
mylabel10.grid(row=1, column=2)
mylabel11.grid(row=1, column=3)
mylabel12.grid(row=1, column=4)
mylabel13.grid(row=1, column=5)
mylabel14.grid(row=1, column=6)

mylabel15.grid(row=2, column=0)
mylabel16.grid(row=2, column=1)
mylabel17.grid(row=2, column=2)
mylabel18.grid(row=2, column=3)
mylabel19.grid(row=2, column=4)
mylabel20.grid(row=2, column=5)
mylabel21.grid(row=2, column=6)

mylabel22.grid(row=3, column=0)
mylabel23.grid(row=3, column=1)
mylabel24.grid(row=3, column=2)
mylabel25.grid(row=3, column=3)
mylabel26.grid(row=3, column=4)
mylabel27.grid(row=3, column=5)
mylabel28.grid(row=3, column=6)

mylabel29.grid(row=4, column=0)
mylabel30.grid(row=4, column=1)
mylabel31.grid(row=4, column=2)
mylabel32.grid(row=4, column=3)
mylabel33.grid(row=4, column=4)
mylabel34.grid(row=4, column=5)
mylabel35.grid(row=4, column=6)

mylabel36.grid(row=5, column=0)
mylabel37.grid(row=5, column=1)
mylabel38.grid(row=5, column=2)
mylabel39.grid(row=5, column=3)
mylabel40.grid(row=5, column=4)
mylabel41.grid(row=5, column=5)
mylabel42.grid(row=5, column=6)

visual_maze.mainloop()


