import csv

# region inputs
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

def get_valid_float(prompt: str, lower_bound=None, upper_bound=None):
    while True:
        try:
            user_input = float(input(prompt))
            if lower_bound is not None and user_input < lower_bound:
                print(f"Number too low, must be greater than", lower_bound)
                continue
            if upper_bound is not None and user_input > upper_bound:
                print("Number too high, must be less than or equal to", upper_bound)
                continue
            return user_input
        except ValueError:
            print("That's not a valid float.")
# endregion

class MenuOption:
    def __init__(self, desc: str, func):
        self.desc = desc
        self.func = func

def get_csv_data():

    product_info = dict()

    with open("manufacturing_data.csv") as file_object:
        csv_reader = csv.reader(file_object)
        next(csv_reader)
        for row in csv_reader:
            product_data = tuple(row[1:])
            product_info[row[0]] = product_data
        return product_info

def retrieve_product_information(csv_data):
    key_test = input("Enter product number: ")
    try:
        product = csv_data[key_test]
        print(f"Product Info: {product}")
    except KeyError:
        print("Item not found")

def calculate_average_production_time(csv_data):
    sum = 0
    total_entries = len(csv_data)
    for key in csv_data:
        sum += float(csv_data[key][2])

    print(f"Average production time for completed batches: {(sum / total_entries):.2f}")

def defect_rates(csv_data):
    threshold = get_valid_float("Enter defect rate threshold (e.g. 0.02): ")
    found_machines = set()
    for key in csv_data:
        if float(csv_data[key][3]) > threshold:
            found_machines.add(csv_data[key][0])
    pretty_print = ", ".join(found_machines)
    print(f"Machines {pretty_print} have a defect rate > {threshold}")

def total_material_cost(csv_data):
    total = 0
    for key in csv_data:
        total += float(csv_data[key][5])
    print(f"Total material cost: ${total:.2f}")

def calculate_efficiency_rating(csv_data):

    worse_value = 1000000000000
    worse_key = ""
    best_value = 0
    best_key = ""

    for(key, value) in csv_data.items():
        eff_rating = (float(value[4]) / float(value[2])) * (1 - float(value[3]))
        if eff_rating < worse_value:
            worse_value = eff_rating
            worse_key = key
        if eff_rating > best_value:
            best_value = eff_rating
            best_key = key
        print(f"Efficiency rating for product id: {key} is {eff_rating:.2f}")
    print("")
    print(f"Best batch is product id {best_key} with efficiency rating {best_value:.2f}")
    print(f"Worst batch is product id {worse_key} with efficiency rating {worse_value:.2f}")


def exit_program(csv_data):
    print("Bye bye!")
    exit(0)

menu_options = [
    MenuOption("Retrieve Product Information", retrieve_product_information),
    MenuOption("Calculate Average Production Time", calculate_average_production_time),
    MenuOption("Find machines with a defect rate above a threshold", defect_rates),
    MenuOption("Calculate Total Material Cost", total_material_cost),
    MenuOption("Calculate Efficiency Rating", calculate_efficiency_rating),
    MenuOption("Exit", exit_program)
]

def main():
    csv_data = get_csv_data()

    while True:
        print("")
        for i in range(len(menu_options)):
            print(f"{i + 1}. {menu_options[i].desc}")
        option_number = get_valid_int("Enter Option Number: ", lower_bound=1, upper_bound=len(menu_options))
        print("")
        menu_options[option_number - 1].func(csv_data)

if __name__ == "__main__":
    main()
