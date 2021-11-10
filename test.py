import unittest
import main

class MainTests(unittest.TestCase):

    def test_random_direction_matches_a_defined_direction(self):
        message = "Verify a randomily generated direction is a valid one"
        expected_directions_list = main.directions
        expected_directions_string = "".join(expected_directions_list)
        random_direction = main.get_random_direction()

        self.assertIn(random_direction, expected_directions_string, message)

if __name__ == '__main__':
    unittest.main()