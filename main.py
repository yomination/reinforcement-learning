import random

total_visits_table = {}

q_value_table = {}

reward_table = {
  "A1":-50,"A2":-50,"A3":-50,"A4":-50,"A5":-50,"A6":-50,"A7":-50,
  "B1":-50,"B2":0,"B3":0,"B4":0,"B5":0,"B6":"WALL","B7":-50,
  "C1":-50,"C2":"WALL","C3":0,"C4":0,"C5":"WALL","C6":0,"C7":-50,
  "D1":-50,"D2":"WALL","D3":0,"D4":100,"D5":"WALL","D6":0,"D7":-50,
  "E1":-50,"E2":0,"E3":0,"E4":0,"E5":0,"E6":0,"E7":-50,
  "F1":-50,"F2":-50,"F3":-50,"F4":-50,"F5":-50,"F6":-50,"F7":-50,
}

cost_to_move = {
    "NORTH":-3,
    "SOUTH":-1,
    "EAST":-2,
    "WEST":-2
}

reward_to_move = {
    "NORTH":3,
    "SOUTH":1,
    "EAST":2,
    "WEST":2
}

directions = ["NORTH",
              "SOUTH",
              "EAST",
              "WEST"]


def get_random_direction():
    return random.choice(directions)

  
if __name__ == "__main__":
    for x in range(1,10):
        print(x, get_random_direction())
