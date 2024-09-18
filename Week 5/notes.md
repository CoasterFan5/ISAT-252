# More loops & formatted print statements

Friday assessment:
- Nested loops
- While loops
- Formatted output

## When should be use loops?
- When we have a repeated pattern
  - We have some kind of data about all employees & we need to process them all the same way
- When there is some form of repetition 

## The while loop
- ```python
    while condition:
        # statements here will be executed while condition is true
- ```python
  while x > 3:
- Infinite loops are very easy to create with while loops
- Indentation is very important to be careful with when dealing with while loops
- Examples:
  - ```python
    count = 0
    while count < 9:
        print('The count is:', count)
        count += 1
    print("Good bye!")
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # Good bye!

## For or While?
- For loops are good for:
  - Iteration in which I want to count
  - Iteration where I want to go through all elements in a list
- While loops are good for:
  - until the user says to stop
  - Until all data is finished processing

## Else statement in loops:
- Python supports using an else statement associated with either a for or while loop
- Probably won't need it
- may be handy in more complex programs
- conflicts with break statements

## Loop Control Statements
- Change execution from normal sequence
- `break` - Terminate loop statement and transfer execution to the statement immediately following the loop
- `continue` - Skip this execution of the loop, and go back to the top
- `pass` - Used when a statement is required, but you don't want any command or code to execute
  - Probably never needed
  - Just a placeholder

## Nested Loops
- a loop inside a loop
- ```python
  for i in range(10):
    for j in range(10):
      statement(s) # executed 100 times
- You can do this with both for loops and while loops, or a mix of both
- No limit to the level of nesting
  - Eventually you will crash the system
  - ```python
    for i in range(1, 3):
      for j in range(1, 4):
        print(i, j)
    # 1 1
    # 1 2
    # 1 3
    # 2 1
    # 2 2
    # 2 3
  - This type of nesting is very prevent on the assessment Friday

## Formatted Printing
- Four kinds of printing
  - The plain odl fashioned way
  - Formatted printing
    - F-strings (Formatted string literals)
      - The newest
      - Only available in python 3.6+
      - ```python
        name = "Alice"
        age = 30
        print(f"My name is {name} and I am {age} years old.")
        # My name is Alice and I am 30 years old.
      - ```python
        for i in range(1, 6)
        print(f"{i:>3} {i**2:>3} {i**3:>3")
        # : starts the format specifier
        # > indicates right alignment
        # 3 specifies a field width of 3 characters
    - The `str.format()` method
      - The second oldest
    - The % Operator
      - Oldest of the three
      - Older code and examples use this
      - Clunky
