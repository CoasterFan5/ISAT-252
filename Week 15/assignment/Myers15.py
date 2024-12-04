from datetime import date
import requests

# constants

API_KEY="" # Hardcoded
# get key: https://www.exchangerate-api.com
# For historic data, you will need a pro plan

BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}"

# region input helpers

def get_valid_currency_name(prompt, currency_list):
    while True:
        currency_name = input(prompt).upper()
        if currency_name in currency_list:
            return currency_name
        print("Invalid currency name, try again.")

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

# endregion

class MenuOption:
    def __init__(self, name, func):
        self.name = name
        self.func = func

def get_currency_conversion():
    # Fetch from API
    response = requests.get(f"{BASE_URL}/latest/USD")
    data = response.json()
    currencies = data["conversion_rates"]

    # User Input
    from_currency = get_valid_currency_name("Convert from (enter like USD): ", currencies)
    to_currency = get_valid_currency_name("Convert to (enter like EUR): ", currencies)
    amt = get_valid_float(f"Enter amount of {from_currency}: ")

    # do the conversions
    usd_amount = amt / float(currencies[from_currency])
    to_amount = usd_amount * float(currencies[to_currency])
    print(f"{amt:.2f} {from_currency} is equal to {to_amount:.2f} {to_currency}")

def historic_currency_rates():

    # grab current rates so we can validate currency name
    current_response = requests.get(f"{BASE_URL}/latest/USD")
    current_data = current_response.json()
    current_currencies = current_data["conversion_rates"]

    # user input
    currency_date = get_valid_date("Enter a date to view exchange rates: ", lower_bound=date(2021, 1, 1), upper_bound=date.today())
    currency_name = get_valid_currency_name("Enter from  currency (like EUR): ", current_currencies)

    ## get the historic rates
    print(f"Loading data for {currency_date.strftime('%Y/%m/%d')}")
    historic_response =requests.get(f"{BASE_URL}/history/{currency_name}/{currency_date.strftime('%Y/%m/%d')}")
    historic_data = historic_response.json()

    if historic_data['result'] == 'error' and historic_data['error-type'] == "plan-upgrade-required":
        print("You need a premium API key for this function. Sorry.")
        return

    to_currency_name = get_valid_currency_name("Enter a currency to convert to (like USD): ", current_currencies)

    rates = historic_data['conversion_rates']
    print(f"1 {currency_name} on {currency_date.strftime('%Y/%m/%d')} is equal to {float(rates[to_currency_name]):.2f} {to_currency_name}")

def main():

    # menu
    while True:
        menu_list = [
            MenuOption("Convert Currencies", get_currency_conversion),
            MenuOption("Historic Currency", historic_currency_rates),
            MenuOption("Quit", exit),
        ]
        print("Currency Convertor")
        print("What would you like to do?")
        for i in range(len(menu_list)):
            print(f"{i+1}. {menu_list[i].name}")
        option_number = get_valid_int("Enter menu option: ", lower_bound=1, upper_bound=len(menu_list)) - 1
        print("")
        menu_list[option_number].func()
        print("")


if __name__ == "__main__":
    main()
