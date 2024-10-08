import unittest
import datetime
from Myers2B import birth_year_to_age
from Myers2A import fahrenheit_to_celsius

current_year = datetime.datetime.now().year
class MyTestCase(unittest.TestCase):
    def test_age(self):
        self.assertEqual(birth_year_to_age(1997), 27 + (current_year - 2024))
        self.assertEqual(birth_year_to_age(2005), 19 + (current_year - 2024))
        self.assertEqual(birth_year_to_age(2001), 23 + (current_year - 2024))
    def test_temp(self):
        self.assertEqual(fahrenheit_to_celsius(67), 19.44)
        self.assertEqual(fahrenheit_to_celsius(74), 23.33)
        self.assertEqual(fahrenheit_to_celsius(96), 35.56)


if __name__ == '__main__':
    unittest.main()
