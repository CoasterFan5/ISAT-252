# Example Framework
# IDK what this is even for tbh

class Example:
    def __init__(self, name, func):
        self.name = name
        self.func = func


def example_1():
    print("Example 1")

example_list = [
    Example("Example 1", example_1),
]

while True:
    for i in range(len(example_list)):
        print(f"{i}) {example_list[i].name}")
    int(input("Select example #: "))

