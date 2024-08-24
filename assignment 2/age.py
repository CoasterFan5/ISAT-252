import datetime

current_year = datetime.datetime.now().year
def birth_year_to_age(birth_year):
    return current_year - birth_year

# inputs and stuff
in_year = int(input("Enter a year: "))
print("Someone born in " + str(in_year) + " would be " + str(birth_year_to_age(in_year)))