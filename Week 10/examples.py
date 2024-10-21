# Example Framework
# IDK what this is even for tbh

class Example:
    def __init__(self, name, func):
        self.name = name
        self.func = func


def example_1():
    try:
        int(input("Enter whatever: "))
        # One or my python statements
    except ValueError:  # if ValueError 1 occurs, run  code in block
        print("valueError")
    else:  # if no exceptions, execute this block
        print("else")
    finally:  # Always execute this, no matter what
        print("Done!")

def example_2():
    my_string = "Apple"
    for x in range(10):
        try:
            print(my_string[x])
        except IndexError:
            print("x")

def example_3():
    # Input validation error
    try:
        age = int(input("Enter your age: "))
        print(f"Half age is {age/2}")
    except ValueError:
        print("Not a valid int!")


example_list = [
    Example("Exception Example", example_1),
    Example("Exception Example 2", example_2),
    Example("Input Validation", example_3),
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

