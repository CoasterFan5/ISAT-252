# Conditionals, 

This week:
- Programming Assignment
  - Focused on "if" statements
- Practice Questions
  - Focused on "if" statements
- Friday Assignment
  - Focus on "if" statements
  - Note readings (privacy)

## Boolean Logic and IF Statement:
- Based on the work of George Boole
- In python, you can use parentheses around condition logic, but it's not actually required
- If statements: 
    ```python
    x = 3
    if x == 1:
        print("X is one")
- Examples:
  - `if x == 3:`
  - `if x < y:`
  - `if (x > 5 and y < 7):`
  - `if my_flag:`
    - A flag is a boolean variable
    - Only two possible values, True or False
    - shorthand for `if my_flag == true:`
- `=` is not the same as `==`
  - `=` is for assignment
  - `==` is for truth checks
  - ```python
    stat = 1 == 2 # stat will be False
    if(stat):
        print("stat is True!")
  - ```python
    stat = 1
    if(stat = 2): # will print 2 since stat = 2 is an assignment, which evaluates to true
        print("stat is 2") 
  - Almost every programming follows this convention of one equals sign for assignment and one for conditionals
## Not Equals
- In older versions of Python (Version 2.x and older), the not equals was this:
  - <>
  - ```python
    if x <> 0:
- In Python 3.x this has been updated:
  - !=
  - ```python
    if x != 0:
    
## Examples of simple conditions
- `a < b` if a is less than b
- `x + y > 10.5` is the result of x + y greater than 10.5?
- `abs(z) < 0.001` if applying the absolute value of z less than 0.001
- `a` is a not zero?
- `x + y < z + s` if x plus y is less than z plus s
- `a < b and b < c` Is a less than b and b less than c? 
  - This is a bad way of doing this in modern python
  - `a < b < c` is a thing here
  - See examples.py for this in action
- `not (b == c or b == 5.5)` be is not equal to c and b is not equal to 5.5
- Exercises in case needed, determine if the following conditions are true or false
  - ```python
    a = 5.5
    b = 1.5
    k = -3
    # evaluate the following
    a < 10 + k
    a + b >= 6.5
    not (a == 3 * b)
    -k <= k + 6
    a < 10 and a > 5
    abs(k) > 3 or k < b - a
    # answers
    # True, True, True, True, True, False
- Parentheses are not recommended if they are redundant
- Boolean operation priorities
  - Not has first priority
  - And has second
  - Or has last priority
  - **Parentheses can help with clarity here**

## Challenge:
- Write a program in Python that calculates the letter grade for a student 
- Where g represents a grade
  - g >= 90 (A)
  - 80 <= g < 90 (B)
  - 70 <= g < 80 (C)
  - 60 <= g < 70 (D)
  - g < 60 (E)
    