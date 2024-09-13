# Problem 2:
# return each letter of the word in input on a new line

def main(input: str):
    out = ""
    for letter in input:
        out += letter + "\n"
    return out
test(main)