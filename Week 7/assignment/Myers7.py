import random

secret_word_list = [
    "apple",
    "orange",
    "encyclopedia",
    "dictionary",
    "pear",
    "pair",
    "word"
]


def get_user_input(guessed: [str]):
    while True:
        try:
            user_input = input("Guess a letter: ").lower()
            if len(user_input) > 1:
                print("Invalid input, too many characters")
            elif not user_input.isalpha():
                print("That's not a letter")
            elif user_input in guessed:
                print("Already guessed")
            else:
                return user_input
        except ValueError:
            print("Invalid input")


def get_new_word():
    return random.choice(secret_word_list)


def update_display(guesses_left: int, secret_word: str, guessed: [str]):
    print(secret_word_revealer(secret_word, guessed))
    print("Guesses remaining: " + str(guesses_left))


def is_game_over(guesses_remaining: int, secret_word: str, guessed: [str]):
    if guesses_remaining == 0:
        print("Game over")
        return True
    elif secret_word == secret_word_revealer(secret_word, guessed):
        print("Congratulations, you won!")
        return True
    return False

def secret_word_revealer(secret_word: str, guessed: [str]):
    temp = ""
    for letter in secret_word:
        if letter in guessed:
            temp += letter
        else:
            temp += "*"
    return temp


def __main__():
    guessed: [str] = []
    guesses_left = 6
    secret_word = get_new_word()

    game_run = True
    while game_run:
        user_input = get_user_input(guessed)
        guessed.append(user_input)
        if user_input not in secret_word:
            guesses_left -= 1
            print("That is not correct!")
        else:
            print("Correct!")
        update_display(guesses_left, secret_word, guessed)
        if is_game_over(guesses_left, secret_word, guessed):
            game_run = False



if __name__ == "__main__":
    __main__()
