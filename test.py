import unittest
import main

class MainTests(unittest.TestCase):

    def test_random_direction_matches_a_defined_direction(self):
        message = "Verify a randomily generated direction is a valid one"
        expected_directions_list = main.directions
        expected_directions_string = "".join(expected_directions_list)
        random_direction = main.get_random_direction()

        self.assertIn(random_direction, expected_directions_string, message)

        
    def test_ramdomily_entering_room_is_valid_room(self):
        message = "Initial random entry into 'maze' is a valid room"
        list_of_valid_rooms_string = "".join(main.valid_starting_positions)
        starting_position = main.starting_position()

        self.assertIn(starting_position, list_of_valid_rooms_string, message)


    def test_get_max_q_value(self):
        position_in_maze = "B2"
        main.q_value_table = {"B2_NORTH":5,
                              "B2_SOUTH":1,
                              "B2_EAST":1,
                              "B2_WEST":1,
        }
        expected_max_q_value = 5
        actual_max_q_value = main.get_max_q_value(position_in_maze)

        self.assertEqual(expected_max_q_value, actual_max_q_value)

    def test_calculated_q_value(self):
        current_position = "B2"
        current_direction = "EAST"
        future_position = "B3"
        future_direction = "SOUTH"
        main.total_visits_table = {"B2_EAST":9}
        main.q_value_table = {"B2_EAST":5,"B3_NORTH":2,"B3_EAST":2,"B3_SOUTH":50,"B3_WEST":2}
        
        explected_q_value = 4.8
        actual_q_value = main.calculate_q_value(current_position,
        current_direction, future_position, future_direction)

        self.assertEqual(explected_q_value, actual_q_value)

if __name__ == '__main__':
    unittest.main()
