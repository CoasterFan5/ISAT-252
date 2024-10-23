from datetime import date

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

valid_locations = [
    "Cedar Creek near Winchester, VA",
    "Passage Creek near Buckton, VA",
    "North Fork Shenandoah River near Strasburg, VA",
    "South Fork Shenandoah River at Front Royal, VA",
    "Mill Creek near Luray, VA",
    "Smith Creek at Rainbow Hill Farm, VA",
    "Linville Creek at Broadway, VA",
    "Mossy Creek near Bridgewater, VA",
    "North River near Stokesville, VA",
    "Beaver Creek near Ottobine, VA",
    "Back Creek near Swope, VA",
    "South River near Greenville, VA",
]

def get_valid_location(prompt: str):
    while True:
        user_input = input(prompt)
        if len(user_input) == 0:
            print("That's an empty string")
            continue
        if user_input == 'help':
            for location in valid_locations:
                print(location)
            continue
        # Attempt to match user_input to a valid location
        found_locations = []
        for valid_location in valid_locations:
            if user_input.lower() in valid_location.lower():
                found_locations.append(valid_location)
        if len(found_locations) == 0:
            print("Invalid location, to see a list of valid locations, type 'help'")
            continue
        if len(found_locations) > 1:
            print("Query matched multiple locations. to see a list of valid locations, type 'help'")
            continue
        return found_locations[0]

def get_valid_date(prompt: str, lower_bound: date=None, upper_bound=date.today()):
    while True:
        user_input = input(prompt)
        if len(user_input) == 0:
            print("That's an empty string")
            continue
        user_input_list = user_input.split("-")
        if len(user_input_list) != 3:
            print("Invalid date format, use MM-DD-YYYY")
            continue
        month = int(user_input_list[0])
        day = int(user_input_list[1])
        year = int(user_input_list[2])

        try:
            new_date = date(year, month, day)
            if lower_bound is not None and new_date < lower_bound:
                print(f"That date is too early, must be after {lower_bound.strftime('%m/%d/%Y')}")
                continue
            if upper_bound is not None and new_date > upper_bound:
                print(f"That date is too late, must be before {upper_bound.strftime('%m/%d/%Y')}")
                continue
            return new_date
        except ValueError:
            print("Invalid date format, use MM-DD-YYYY")
            continue

def get_valid_float(prompt: str, lower_bound=None, upper_bound=None):
    while True:
        user_input = input(prompt)
        if len(user_input) == 0:
            print("You have to enter a number")
            continue

        try:
            user_input = float(user_input)
            if lower_bound is not None and user_input < lower_bound:
                print(f"That number is too low, must be greater than", lower_bound)
                continue
            if upper_bound is not None and user_input > upper_bound:
                print(f"That number is too high, must be less than or equal to", upper_bound)
                continue
            return user_input
        except ValueError:
            print("That's not a number.")
# endregion


# region Program Specific Functionality

class WaterData:

    location = ""
    sample_date: date = None
    water_temp: float = None
    water_ph: float = None
    water_turbidity: float = None
    dissolved_oxygen: float = None

    def __init__(self, location: str, sample_date: date, water_temp: float, water_ph: float, water_turbidity: float, dissolved_oxygen: float):
        self.location = location
        self.sample_date = sample_date
        self.water_temp = water_temp
        self.water_ph = water_ph
        self.water_turbidity = water_turbidity
        self.dissolved_oxygen = dissolved_oxygen

    def to_string(self):
        return f"Location: {self.location}, date: {self.sample_date.strftime('%b %d, %Y')}, Water temp: {self.water_temp}, Water turbidity: {self.water_ph}, Dissolved oxygen: {self.water_turbidity}"

def add_data():
    print("Adding water data.")
    location = get_valid_location("Enter location: ")
    sample_date = get_valid_date("Enter sample date (MM-DD-YYYY): ", lower_bound=date(1960, 1, 1))
    water_temp = get_valid_float("Enter water temperature (C): ", lower_bound=0, upper_bound=100)
    ph = get_valid_float("Enter PH: ", lower_bound=0, upper_bound=14)
    turbidity = get_valid_float("Enter turbidity (NTU): ", lower_bound=0)
    dissolved_oxygen = get_valid_float("Enter dissolved oxygen : ", lower_bound=0)
    print("")
    print("Date Recorded")
    print("")

# endregion

#region Inputs

class SelectionOption:
    def __init__(self, name, func):
        self.name = name
        self.func = func


def main():

    def quit_program():
        exit()

    options = [
        SelectionOption("Add Data", add_data),
        SelectionOption("Quit", quit_program)
    ]

    print("Water Quality Data Collection Interface")
    while True:
        print("Select option:")
        for i in range(len(options)):
            print(f"{i + 1}) {options[i].name}")
        selected_option = get_valid_int("Select Option: ", lower_bound=1, upper_bound=len(options))
        print("")
        options[selected_option - 1].func()

# endregion

if __name__ == '__main__':
    main()