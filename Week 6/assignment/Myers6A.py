# This is going to be insane ngl

class CustomStringFunctionHelper:
    desc: str = ""
    def __init__(self, desc, func):
        self.desc = desc
        self.func = func

class CustomString:
    custom_string: str = ""

    def __init__(self, custom_string):
        self.custom_string = custom_string

    def remove_all_spaces(self):
        self.custom_string = self.custom_string.replace(" ", "")

    def replace_all_non_alphabetic(self):
        temp_string = ""
        for letter in self.custom_string:
            if letter.isalpha():
                temp_string += letter
        self.custom_string = temp_string

    def make_alphanumeric(self):
        temp_string = ""
        for letter in self.custom_string:
            if letter.isalnum():
                temp_string += letter
        self.custom_string = temp_string

    def clean_string(self):
        temp_string = ""
        for letter in self.custom_string:
            if letter.isalnum() or letter.isspace():
                temp_string += letter
        self.custom_string = temp_string

    def replace_all_of_one_with_another(self):
        print("Notice, this function is case sensitive")
        find = input("Enter character or substring to replace: ")
        replace_with = input("Enter what you would like to replace " + find + " with: ")
        self.custom_string = self.custom_string.replace(find, replace_with)

    def make_string_lowercase(self):
        self.custom_string = self.custom_string.lower()

    def make_string_uppercase(self):
        self.custom_string = self.custom_string.upper()

    def reverse_string(self):
        self.custom_string = self.custom_string[::-1]

    function_list = [
        CustomStringFunctionHelper("Remove all spaces", remove_all_spaces),
        CustomStringFunctionHelper("Replace all non-alphabetic characters", replace_all_non_alphabetic),
        CustomStringFunctionHelper("Make string alphanumeric", make_alphanumeric),
        CustomStringFunctionHelper("Remove all but numbers, letters, and spaces", clean_string),
        CustomStringFunctionHelper("Replace one string with another", replace_all_of_one_with_another),
        CustomStringFunctionHelper("Make string lowercase", make_string_lowercase),
        CustomStringFunctionHelper("Make string uppercase", make_string_uppercase),
        CustomStringFunctionHelper("Reverse string", reverse_string),
    ]

    def prompt_user_input(self):

        run_program = True
        while run_program:
            # Generate a list of options based on the function list
            print("Select an option:")
            for i in range(len(self.function_list)):
                print(str(i + 1) + ")", self.function_list[i].desc)

            # handle the userinput with error checking
            selected_option = 1
            has_entered_valid_option = False
            while not has_entered_valid_option:
                try:
                    selected_option = int(input("Enter option number: "))
                    if 0 < selected_option <= len(self.function_list):
                        has_entered_valid_option = True
                    else:
                        print(selected_option, "is not a valid option")
                except ValueError:
                    print("Please enter a valid option")

            # call the appropriate function from function_list
            self.function_list[selected_option - 1].func(self)
            print()
            print("New string: " + self.custom_string)
            print()
            continue_option = "0"
            while continue_option == "0":
                print("Please select an option below:")
                print("1) Quit program")
                print("2) Run again with the new string")
                print("3) Input new string and run again")
                continue_option = input("Enter option number: ")
                if continue_option not in "123":
                    print()
                    print("Please enter a valid option")
                    print()
                    continue_option = "0"
            if continue_option == "1":
                exit()
            if continue_option == "2":
                continue
            if continue_option == "3":
                break



while True:
    string_thing = CustomString(input("Enter a string: "))
    string_thing.prompt_user_input()