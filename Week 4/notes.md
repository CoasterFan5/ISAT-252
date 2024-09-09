# Loops and strings
Most simple iteration:
- For loop
  - Generally the best loop if you know how many times you want it to run
  - Remember we start at 0
  - ```python
    for i in range(10):
        print(i)
    
    # Result:
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
  - Note: using `i` in a loop is tradition. 
  - Range Params
    - defaults to starting at 0 and incrementing by 1
    - `range(10)` - stars at 0, goes up to 10, increment by 1
    - `range(2, 30)` - starts at 2 and goes up to 30
    - `range(2, 30, 3)` - starts at 2, goes up to 30, increment by 3

## Strings in Python
- Easy to handle strings
- Create by enclosing something in quotes
- Stings as simple as assigning a value to a variable:
- ```python
    var1 = 'Hello World!'
    var2 = "Python Programming"
- Strings are stored as a sequence
- ```python
  this_string = "Killer Rabbit"
  this_string[0] # K
  this_string[7] # R
- ```python
  var1 = "Hello World!"
  var2 = "Python Programming"
  print("var1[0]:", var1[0])
  print("var2[7]:", var2[7])
  print("var2[1:5]:", var2[1:5])
  print("Var1[1:]:", var1[1:])
  print("Var2[:5]:", var2[:5])
  # See examples.py to run this
- Python is not inclusive with ends, so `var2[:5]` will print position 0, 1, 2, 3, and 4, making `Pytho`.
- But its also inclusive when using starting at. `var1[1:]` will print `ello World!`
- More examples:
  - ```python
    word = 'banana'
    slice_1 = word[3]
    slice_2 word[2:4] # na
    slice_3 = word[:3] # ban
    slice_4 = word[3:] # ana
- Useful string methods
  - ```python
    word = 'banana'
    x = len(banana)
    print(x) # 6
    
    A = "Apple"
    B = "Banana"
    C = "Cantaloupe"
    print(len(A), len(B), len(C)) # 5 6 10
    print(len(A) + len(B) + len(C)) # 21
  - You can do the following to easily loop through a string:
    - ```python
      word = "hello"
      for letter in word:
        print(letter)
      
      # Result:
      # h
      # e
      # l
      # l
      # o