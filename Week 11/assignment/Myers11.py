def main():
    # Load the files in
    words_list: list[str] = []
    long_string: str = ""
    try:
        with open("FiveLetterWords.txt") as file_object:
            words_list = file_object.read().splitlines()
        with open("RandomText.txt") as file_object:
            long_string = file_object.read()
    except FileNotFoundError:
        print("File not found, exiting program")
        exit(0)

    print(f"Loaded {len(words_list)} words")
    print(f"Loaded {len(long_string)} characters")

    ## find the words
    found_word_count = 0

    for word in words_list:
        last_index = -1
        while True:
            i = long_string.find(word, last_index + 1)
            if i == -1:
                break
            last_index = i
            found_word_count += 1
            print(f"Found {word} at position {i}")


    print(f"Done! Found {found_word_count} words")

if __name__ == "__main__":
    main()