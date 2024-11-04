# Example Framework
# IDK what this is even for tbh

import csv

class Example:
    def __init__(self, name, func):
        self.name = name
        self.func = func


def example_1():
    try:
        with open("file.csv", "r") as file_object:
            data_reader = csv.reader(file_object)
            for row in data_reader:
                print(row)
        # One or my python statements
    except FileNotFoundError:  # if ValueError 1 occurs, run  code in block
        print("File not found")

def example_2():
    try:
        with open("file.csv", "r") as file_object:
            reader = csv.reader(file_object)
            data = list(reader)
            print(data)
    except FileNotFoundError:
        print("File not found")

def example_3():
    try:
        data = [
            ['name', 'age', 'city'],
            ['David', '31', 'Boston'],
            ['Eva', '29', 'Miami'],
            ['tim', '60', 'Seattle']
        ]

        with open('./new_data.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
    except Exception as e:
        print("Something went wrong")

def example_4():
    try:
        with open('city_data.csv', 'r') as file_object:
            reader = csv.reader(file_object)
            data = list(reader)

        header = data[0] + ['Population Density']
        city_data = data[1:]


        with open('new_city_data.csv', 'w') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            for row in city_data:
                csv_writer.writerow(row + [int(row[1]) / float(row[2])])
    except Exception:
        print("Something went wrong")

example_list = [
    Example("Print each row", example_1),
    Example("Use list(reader) to get all data at once", example_2),
    Example("Write to a file with csv writer", example_3),
    Example("Add a column to a csv file", example_4),
]



def get_valid_int(prompt: str, lower_bound=0, upper_bound=None):
    while True:
        try:
            user_int = int(input(prompt))
            if lower_bound is not None and user_int < lower_bound:
                print("Not within lower bound")
            elif upper_bound is not None and user_int > upper_bound:
                print("Not within upper bound")
            else:
                return user_int
        except ValueError:
            print("Not a valid int, try again.")


while True:
    for i in range(len(example_list)):
        print(f"{i + 1}) {example_list[i].name}")
    selected_example = get_valid_int("Enter option number:", 1, len(example_list))
    print("Running example...")
    print("")
    example_list[selected_example - 1].func()
    print("")
