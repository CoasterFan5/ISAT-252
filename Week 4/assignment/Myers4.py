# Author: Dylan Myers
# Description: Count certain metrics for strings
# Tests: tests.py


vowel_list: list[str] = ['a', 'e', 'i', 'o', 'u']

def myers4(user_input):

    char_dict: dict[str, int] = {}

    total_chars: int = len(user_input)
    upper_case_letters: int = 0
    lower_case_letters: int = 0
    vowels: int = 0
    consonants: int = 0
    non_alpha: int = 0


    word_count: int = 0

    # we love word counts
    for word in user_input.split(" "):
        for letter in word:
            if letter.isalpha():
                word_count += 1
                break

    most_common_char_count = 0
    most_common_char = ""
    is_most_common_char_space = False

    for this_char in user_input:
        if this_char.isalpha():

            if this_char.islower():
                lower_case_letters += 1
            elif this_char.isupper():
                upper_case_letters += 1

            if this_char.lower() in vowel_list:
                vowels += 1
            else:
                consonants += 1

        else:
            non_alpha += 1

        if char_dict.get(this_char):
            char_dict[this_char] += 1
        else:
            char_dict[this_char] = 1

        # most common char logic
        if char_dict[this_char] > most_common_char_count:
            most_common_char_count = char_dict[this_char]
            most_common_char = this_char


    if most_common_char == " ":
        is_most_common_char_space = True

    user_output = ""
    user_output += "Total characters: " + str(total_chars) + "\n"
    user_output += "Upper case letters: " + str(upper_case_letters) + "\n"
    user_output += "Lower case letters: " + str(lower_case_letters) + "\n"
    user_output += "Vowels: " + str(vowels) + "\n"
    user_output += "Consonants: " + str(consonants) + "\n"
    user_output += "Non-alphabetic characters: " + str(non_alpha) + "\n"
    user_output += "Word count: " + str(word_count) + "\n"
    if is_most_common_char_space:
        user_output += "Most common character: " + str(most_common_char) + " (space)\n"
    else:
        user_output += "Most common character: " + str(most_common_char) + "\n"

    return user_output



if __name__ == '__main__':
    print(myers4(input("Enter a line of text: ")))
