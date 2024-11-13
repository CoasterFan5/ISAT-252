# Example Framework
# IDK what this is even for tbh

class Example:
    def __init__(self, name, func):
        self.name = name
        self.func = func


def example_1():
    my_tuple = ("a", "b", "c")
    print(my_tuple[0])  # a
    print(len(my_tuple)) # 3

def example_2():
    my_tuple = ("a", "b", "c")
    new_list=  list(my_tuple)
    new_list.append("d")
    new_tuple = tuple(new_list)
    print(new_tuple)

def example_3():
    my_tuple = 1, 2, 3, 4
    print(my_tuple)

    # this is different
    a, b, c, d = my_tuple
    print(a, b, c, d)


example_list = [
    Example("Tuple Basics", example_1),
    Example("Modfy a tuple", example_2),
    Example("Alternate declaration of a tuple", example_3),
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

