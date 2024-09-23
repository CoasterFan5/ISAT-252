import math


def create_multiplication_table(columns: int, column_start: int, rows: int, rows_start: int):

    # 2 chars of spacing
    space_amount = math.floor(math.log10((columns + column_start) * (rows + rows_start)) + 4)
    alignment = "^"

    # Headers
    print(f'{"":{alignment}{space_amount}}|', end=" ")
    for column_number in range(column_start, column_start + columns):
        print(f'{column_number:{alignment}{space_amount}}', end=' ')
    print()
    for column_number in range(column_start, column_start + columns + 1):
        print(f'{"":-{alignment}{space_amount}}', end=" ")
    print()


    for row_number in range(rows_start, rows_start + rows):
        print(f'{row_number:{alignment}{space_amount}}|', end=' ')
        for column_number in range(column_start, column_start + columns):
            print(f'{(column_number * row_number):{alignment}{space_amount}}', end=' ')
        print()

if __name__ == "__main__":

    print("Let's make a multiplication table!")
    do_try = True
    while do_try:
        try:
            create_multiplication_table(
                int(input("How many columns would you like? ")),
                int(input("Where should the columns start? ")),
                int(input("How many rows would you like? ")),
                int(input("Where should the rows start? "))
            )
            do_prompt_try_again = True
            while do_prompt_try_again:
                try:
                    yn_input = input("Would you like to continue? [y/n]: ").lower()
                    if yn_input == "n":
                        do_try = False
                        do_prompt_try_again = False
                    elif yn_input == "y":
                        do_prompt_try_again = False
                    else:
                        raise ValueError
                except ValueError:
                    print("Bad input, please try again!")
        except ValueError:
            print("Bad input, try again!")



