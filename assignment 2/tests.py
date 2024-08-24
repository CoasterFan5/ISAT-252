import unittest
import datetime
from age import birth_year_to_age
from temp import fahrenheit_to_celsius

current_year = datetime.datetime.now().year
class MyTestCase(unittest.TestCase):
    def test_age(self):
        self.assertEqual(birth_year_to_age(1997), 27 + (current_year - 2024))
        self.assertEqual(birth_year_to_age(2005), 19 + (current_year - 2024))
        self.assertEqual(birth_year_to_age(2001), 23 + (current_year - 2024))
    def test_temp(self):
        self.assertEqual(-18 < fahrenheit_to_celsius(1) < -17, True)
        self.assertEqual(21 < fahrenheit_to_celsius(71) < 22, True)


if __name__ == '__main__':
    unittest.main()
