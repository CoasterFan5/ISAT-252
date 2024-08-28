# Variables and simple inputs / outputs

## This week: 
- Variables
  - Storage in a computers memory
- Assignment
  - Assign things to variables
- Simple input
- Simple output
- Basic math functions
- Comments
  - Notes within code
- Assignments (see assignment folder):
  - Program that takes user input in Fahrenheit and convert to Celsius
  - Program that calculates age bsed on current year and year of birth, ignore months.

## Notes
- Conventions
  - Name program file `lastname(assignment#).py`
- The first computer
  - ENIAc is considered the first computer by many.
- What is a program?
  - A set of instructions a computer follows to perform a task
  - Like a recipie 
- Terms:
  - ***Algorithms***: Conceptual list of step-by-step procedures for solving problems or performing tasks
  - ***Code***: Written instructions in a programming language
  - ***Data***: Information a program processes 
- Languages
  - First done by connecting wires
  - Moved to hex, then assembler, now high level languages
  - Three important languages
    - ***Fortran*** (Formula Translator)
      - Made in 1956 by IBM
      - First high level language
      - Primary language for mathematics, science, and engineering. 
    - ***COBOL*** (Common Business Oriented Language)
      - 1959 by a committee
        - Headed by Grace Hopper
      - Dominated business data processing
      - Died out in the 90's
    - ***C***
      - Invented 1970's by Dennis Ritchie
      - Most languages have been built on concepts of C
- Downloading and installing python
  - I'm not taking notes on that. https://python.org
- IDLE
  - This course recommends using IDLE to write python. That's nice, but I get that Jetbrains student discount so Pycharm is where it's at.
  - VSCode is cool too.
  - You could also use something trendy like [Zed](https://zed.dev) (I think zed has good python support)
  - Basics of Python Programming
    - Variables
      - Boxes where we store info
      - Each box has a unique id (the name) and can hold specific data
      - Most languages allow you to declare variables and specify types
      - In Python, you just use a variable and pray the interpreter takes care of it
        - basic types
          - int - whole number
          - float - not so whole number
          - string - text
          - boolean - true/false
          - Examples:
            ```python
            age = 25 # int
            price = 19.99 # float
            name = "alice" # string
            is_student = False # boolean
            ```
    - **Rules and conventions**
      - Naming Rules
        - Variables are case sensitive
        - can contain letters, digits, and underscores
        - first char must be letter or an underscore
      - Naming Conventions
        - Use descriptive names
        - Separate words in variable names with underscores (snake_case)
        - Avoid using keywords for vars
        - Follow [PEP 8 style guide](https://peps.python.org/pep-0008/)
    - Simple Output
      - Most common is a `print("this is an out")`
      - Can also use basic escape stuff
      - Casting is weird, use methods like `str()`
    - Simple input
      - Use `input()`
      - Use casting methods `age = int(input("enter age"))`
    - Comments
      - Just a note
      - `print("hello world") # this is a comment`
        