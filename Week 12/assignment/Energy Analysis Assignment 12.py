import csv

# region Input Validation Functions
def get_valid_int(prompt: str, lower_bound=None, upper_bound=None):
    while True:
        try:
            user_input = int(input(prompt))
            if lower_bound is not None and user_input < lower_bound:
                print(f"Number too low, must be greater than", lower_bound)
                continue
            if upper_bound is not None and user_input > upper_bound:
                print("Number too high, must be less than or equal to", upper_bound)
                continue
            return user_input
        except ValueError:
            print("That's not a valid int.")

# endregion

def format_energy_use_as_dollar_amount(energy_use):
    return f"${round(energy_use * pow(10, 9), 2):,.0f}"

class MenuOption:
    def __init__(self, name, func):
        self.name = name
        self.func = func

def read_csv(filename):
    with open(filename, "r") as file_object:
        data = list(csv.reader(file_object, dialect="excel"))
        return data

def count_states(headers, data):
    state_list = []
    for row in data:
        state_list.append(row[0].strip().lower())
    number_of_states = len(set(state_list))
    print(f"There are {number_of_states} states.")

    pass

def total_expenditure(headers, data):
    total_cost = 0
    for row in data:
        for i in range(1, len(row)):
            total_cost += float(row[i])
    print(f"Total expenditure across all categories is {format_energy_use_as_dollar_amount(total_cost)}")
    pass

def highest_expenditure_state(headers, data):
    highest_expenditure_total = 0
    highest_expenditure_name = ""
    for row in data:
        total = 0
        for i in range(1, len(row)):
            total += float(row[i])
        if total > highest_expenditure_total:
            highest_expenditure_total = total
            highest_expenditure_name = row[0]
    print(f"Highest expenditure state is {highest_expenditure_name} with {format_energy_use_as_dollar_amount(highest_expenditure_total)}")

def lowest_expenditure_state(headers, data):
    lowest_expenditure_total = 1000000
    lowest_expenditure_name = ""
    for row in data:
        total = 0
        for i in range(1, len(row)):
            total += float(row[i])
        if total < lowest_expenditure_total:
            lowest_expenditure_total = total
            lowest_expenditure_name = row[0]
    print(
        f"Lowest expenditure state is {lowest_expenditure_name} with {format_energy_use_as_dollar_amount(lowest_expenditure_total)}")
    pass

def highest_in_category(data, category_index):
    # TODO: Implement this function to find the state with highest expenditure in a category
    pass

def average_in_category(data, category_index):
    # TODO: Implement this function to calculate the average expenditure in a category
    pass

def export_summary(data, filename):
    # TODO: Implement this function to export a summary to a new CSV file
    pass

def exit_program(headers, data):
    exit()

def main():

    menu_options = [
        MenuOption("Count states", count_states),
        MenuOption("Total expenditure", total_expenditure),
        MenuOption("Highest expenditure state", highest_expenditure_state),
        MenuOption("Lowest expenditure state", lowest_expenditure_state),
        MenuOption("Exit", exit_program),

    ]

    filename = "energy_data.csv" # Make sure this matches the name of your CSV file
    raw_data = read_csv(filename)
    headers = raw_data[0]
    data = raw_data[1:]
    
    while True:
        print("-" * 15)
        print("Energy Consumption Analysus")
        for i in range(len(menu_options)):
            print(f"{i + 1}) {menu_options[i].name}")
        
        choice = get_valid_int("Enter option number: ", 1, len(menu_options))

        print("-" * 15)
        print("\n")
        menu_options[choice - 1].func(headers, data)
        print("\n")

if __name__ == "__main__":
    main()
