# Example Framework
# IDK what this is even for tbh

class Example:
    def __init__(self, name, func):
        self.name = name
        self.func = func

basic_dict = {
    "key1": "abc",
    "key2": "def",
    "key3": "ghi",
}

def example_1():
    print(basic_dict)

def example_2():
    key = input("Enter a key: ")
    try:
        print(basic_dict[key])
    except KeyError:
        print("Key not found")

def example_3():
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    basic_dict[key] = value

def example_4():
    for key in basic_dict:
        print(f"{key}: {basic_dict[key]}")

def example_5():
    try:
        key = input("Enter a key: ")
        del basic_dict[key]
    except KeyError:
        print("Key not found")

example_list = [
    Example("Print dictionary", example_1),
    Example("Print specific entry", example_2),
    Example("Set key to value", example_3),
    Example("Print all items nicely", example_4),
    Example("Delete an item", example_5),
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

