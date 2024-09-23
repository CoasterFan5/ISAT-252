# String functions and string methods
Tools we use to do things with strings

String functions and methods
- Length and count
- Case conversion
- Search and replace
- String logical check
- String splitting and joining

## Functions v.s. Methods
- Function:
  - ```python
    my_string = "Hello World!"
    length = len(my_string)
  - Functions are traditionally not part of an object
- Methods:
  - ```python
    my_string = "Hello, World!"
    shouting = my_string.upper()
  - Methods are part of an object

## Immutability
- Cant change the value
- Strings are immutable

## List of methods and functions

### Concatenation (`+`)
- Used to combine two or more strings
- ```python
  "a" + "b" # ab

### Length
- Function
- `len()` 
- Returns the length of the string

### Count
- Method
- Case sensitive
- Returns 0 when there is no match
- ```python
  text = "banana"
  print(text.count("a")) # 3
  
### Case conversion methods
- All of these return the value, do not mutate the original string since strings are immutable in this language
- `<typeof str>.lower()` - Returns string as lowercase
- `<typeof str>.upper()` - Returns string as uppercase 
- `<typeof str>.capitalize()` - Capitalize the first char of a string and the rest to lower
- `<typeof str>.title()` - Converts the first char of each word to uppercase and makes everything else lowercase
- `<typeof str>.swapcase()` - Swaps the case of each char
- Examples:
  - ```python
    mystring = "HELLO"
    mystring.lower()
    print(mystring) # HELLO
    
    my_string = "HELLO"
    my_string_lower = my_string.lower()
    print(my_string_lower) # hello
  - ```python
    user_input = input("Enter a, b, or c")
    if(user_input.lower() == "a"): # Allows a or A to be input
        print("a or A")

### Search and replace methods
- `find()`
  - Searches for a substring and returns the index of it's first occurrence. Returns -1 if not found
  - Example:
    - ```python
      text = "Hello, World!"
      index = text.find("World")
      index2 = text.find("Python")
      print(index) # 7
      print(index2) # -1
- `replace(old, new)`
  - Replace all occurrences of the substring `old` with `new`
  - Example:
    - ```python
      mystring = "Hello World"
      print(mystring.replace("World", "Python")) # Hello Python"
      print(mystring) # Hello World
    - ```python
      text = "apple apple apple apple apple apple"
      print(text.replace("apple", "orange", 5)) # orange orange orange orange orange apple
      print(text.replace("apple", "orange")) # orange orange orange orange orange orange

### Logical check methods
- these return booleans
- `<typeof str>.isdigit()` - Checks if all chars in string are digits
- `<typeof str>.isalpha()` - Checks if all chars in string are alphabetic
- `<typeof str>.isalnum()` - Checks if all chars in string are alphanumeric
- `<typeof str>.startswith(substring)` - Checks if string starts with specified substring
- `<typeof str>.endswith(substring)` - Checks if string ends with specified substring
- Examples:
  - ```python
    if("abc.123".endswith("123", "asdjh"))
-