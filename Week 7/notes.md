# Modular programming and functions
## Functions
- Block of organized, reusable code that is used to perform an action
- Better modularity for your application and allows reusing code
- Python gives many built-in functions like `print()`
- Python allows you to create your own functions which are defined as **user-defined functions**

## Benefits of user-defined functions
- Modularity
- re-usability
- Protect data from being disturbed by the disturbed that occur in a function
- Collaboration

## Defining a function
- You must define functions using specific rules
  - Use the keyword `def` followed by a name and parentheses
  - Optional: Arguments (also called parameters) inside the parentheses
  - Variables declared inside a function are scoped locally, and can't be accessed outside the function
  - ```python
    def myFunction(x, y, z):
      # code goes here
- The first statement of a function can be an optional statement, the documentation string of the function or docstring
- The statement `return <expression>` exits a function, optionally passing back some data
- A function that returns a value of called a "fruitful function"

## Tips
- Don't rely on global variables. Most functions should operated based on params
- Use different variable names inside function
- Make all of the inputs and outputs of a function obvious

## Variable length arguments
- use `*argList` to get a list of args
- ```python
  def addItems(*argList):
    total = 0
    for x in argList:
        total += x
    return total