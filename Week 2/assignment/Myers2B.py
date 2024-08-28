# Age Calculator
# based on the birth year, calculates a users age, ignoring months and days.

import datetime

current_year = datetime.datetime.now().year
def birth_year_to_age(birth_year):
    return current_year - birth_year

# inputs and stuff
if __name__ == '__main__':
    in_year = int(input("Enter your birth year: "))
    print("That makes you", str(birth_year_to_age(in_year)), "years old! ")