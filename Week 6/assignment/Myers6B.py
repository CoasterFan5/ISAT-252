# Assignment 6b
# The same as assignment 6a, but avoiding string functions and methods

class CustomStringFunctionHelper:
    desc: str = ""


    def __init__(self, desc, func):
        self.desc = desc
        self.func = func

class CustomString:
    custom_string: str = ""
    lower_case_char_set = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_case_char_set = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alpha_char_set = lower_case_char_set + upper_case_char_set
    number_char_set = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    alpha_num_char_set = alpha_char_set + number_char_set
    clean_char_set = alpha_num_char_set + [" "]

    def __init__(self, custom_string):
        self.custom_string = custom_string

    def remove_all_spaces(self):
        temp_string = ""
        for letter in self.custom_string:
            if not (letter == " "):
                temp_string += letter
        self.custom_string = temp_string

    def replace_all_non_alphabetic(self):
        temp_string = ""
        for letter in self.custom_string:
            if letter in self.alpha_char_set:
                temp_string += letter
        self.custom_string = temp_string

    def make_alphanumeric(self):
        temp_string = ""
        for letter in self.custom_string:
            if letter in self.alpha_num_char_set:
                temp_string += letter
        self.custom_string = temp_string

    def clean_string(self):
        temp_string = ""
        for letter in self.custom_string:
            if letter in self.clean_char_set:
                temp_string += letter
        self.custom_string = temp_string

    def replace_all_of_one_with_another(self):
        print("Notice, this function is case sensitive")
        find = input("Enter character or substring to replace: ")
        replace_with = input("Enter what you would like to replace " + find + " with: ")

        temp_string = ""

        # calculate the length of finding string
        find_length = 0
        for letter in find:
            find_length += 1

        # calculate length of custom string
        str_length = 0
        for letter in self.custom_string:
            str_length += 1

        i = 0
        while i < str_length - find_length + 1:
            # use a second for loop to create a substring
            sub_str = ""
            for j in range(find_length):
                sub_str += self.custom_string[j + i]
            if sub_str == find:
                print(f"increasing i ({i}) by {find_length}")
                i += find_length
                temp_string += replace_with
            else:
                temp_string += self.custom_string[i]
                i += 1
        else:
            print(i)
            print(self.custom_string[i:])
            temp_string += self.custom_string[i:]



        self.custom_string = temp_string

    def make_string_lowercase(self):
        temp_string = ""
        iterator = 0
        for letter in self.custom_string:
            iterator_2 = 0
            for upper_letter in self.upper_case_char_set:
                if letter == upper_letter:
                    temp_string += self.lower_case_char_set[iterator_2]
                    break
                iterator_2 += 1
            else:
                temp_string += letter

        iterator += 1

        self.custom_string = temp_string

    def make_string_uppercase(self):
        temp_string = ""
        iterator = 0
        for letter in self.custom_string:
            iterator_2 = 0
            for lower_letter in self.lower_case_char_set:
                if letter == lower_letter:
                    temp_string += self.upper_case_char_set[iterator_2]
                    break
                iterator_2 += 1
            else:
                temp_string += letter

        iterator += 1

        self.custom_string = temp_string

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