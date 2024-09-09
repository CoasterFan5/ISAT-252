import unittest
import Myers4



class MyTestCase(unittest.TestCase):
    def test1(self):
        expected_out = ("Total characters: 80\n"
                        "Upper case letters: 1\n"
                        "Lower case letters: 60\n"
                        "Vowels: 23\n"
                        "Consonants: 38\n"
                        "Non-alphabetic characters: 19\n"
                        "Word count: 17\n"
                        "Most common character:   (space)\n"
                        )
        self.assertEqual(Myers4.myers4("Ask not what your country can do for you – ask what you can do for your country."), expected_out)
    def test2(self):
        expected_out = ("Total characters: 100\n"
                        "Upper case letters: 1\n"
                        "Lower case letters: 75\n"
                        "Vowels: 30\n"
                        "Consonants: 46\n"
                        "Non-alphabetic characters: 24\n"
                        "Word count: 20\n"
                        "Most common character:   (space)\n")
        self.assertEqual(Myers4.myers4("You can't always get what you want, but if you try sometimes, you might find, you get what you need."), expected_out)