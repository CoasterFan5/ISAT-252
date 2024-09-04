import unittest
import Myers3

class InputHelper:
    iterations = 0
    def __init__(self, input_list):
        self.input_list = input_list
    def get_input(self, s):
        output = self.input_list[self.iterations]
        self.iterations += 1
        return output


class MyTestCase(unittest.TestCase):
    def test_hyena(self):
        Myers3.input = InputHelper([0, 0, 0]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a hyena!")
    def test_red_wolf(self):
        Myers3.input = InputHelper([0, 0, 1]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a red wolf!")
    def test_other(self):
        Myers3.input = InputHelper([0, 1, 0]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a dodo!")
    def test_other1(self):
        Myers3.input = InputHelper([0, 1, 1]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a t-rex!")
    def test_other2(self):
        Myers3.input = InputHelper([1, 0, 0]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a koala!")
    def test_other3(self):
        Myers3.input = InputHelper([1, 0, 1]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a giraffe!")
    def test_other4(self):
        Myers3.input = InputHelper([1, 1, 0]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a chicken!")
    def test_other5(self):
        Myers3.input = InputHelper([1, 1, 1]).get_input
        output = Myers3.animal_guess()
        self.assertEqual(output, "I think your animal is a cow!")


if __name__ == '__main__':
    unittest.main()
