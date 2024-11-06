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

def get_user_category(headers):
    cat_list = headers[1:]

    for i in range(len(cat_list)):
        print(f"{i + 1}) {cat_list[i]}")
    return get_valid_int("Select category number: ", lower_bound=1, upper_bound=len(cat_list))

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

def total_expenditure(headers, data):
    total_cost = 0
    for row in data:
        for i in range(1, len(row)):
            total_cost += float(row[i])
    print(f"Total expenditure across all categories is {format_energy_use_as_dollar_amount(total_cost)}")

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

def highest_in_category(headers, data):
    high = 0
    state_name = ""
    category_index = get_user_category(headers)
    for row in data:
        if float(row[category_index]) > high:
            high = float(row[category_index])
            state_name = row[0]

    print(f"\n{state_name} is the highest in {headers[category_index]} with {format_energy_use_as_dollar_amount(high)}")

def average_in_category(headers, data):
    category = get_user_category(headers)
    total = 0
    for row in data:
        total += float(row[category])
    average = total / len(data)
    print(f"Average spend on {headers[category]} is {format_energy_use_as_dollar_amount(average)}")

def export_summary(headers, data):
    csv_writer = csv.writer(open("energy_summary.csv", "w"))
    csv_writer.writerow(["state", "expenditure"])
    for row in data:
        total = 0
        for i in range(1, len(row)):
            total += float(row[i])
        csv_writer.writerow([row[0], format_energy_use_as_dollar_amount(total)])
    print("Summary saved as energy_summary.csv")

def exit_program(headers, data):
    exit()

def main():

    menu_options = [
        MenuOption("Count states", count_states),
        MenuOption("Total expenditure", total_expenditure),
        MenuOption("Highest expenditure state", highest_expenditure_state),
        MenuOption("Lowest expenditure state", lowest_expenditure_state),
        MenuOption("High state expenditure in category", highest_in_category),
        MenuOption("Average expenditure in category", average_in_category),
        MenuOption("Export summary", export_summary),
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

        print("-" * 15 + "\n")
        menu_options[choice - 1].func(headers, data)

if __name__ == "__main__":
    main()
