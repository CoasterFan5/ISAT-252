# Files

Main topics for the day:
- opening files
- reading files
- writing files

## What is a file?
- A file is a piece of data stored in a file format
- Files have extensions like:
  - .doc
  - .py
  - .txt
- In this course, we will be using plain text ascii files, which commonly have the .txt extension

## Using files in Python
- Before opening a file in python, you must open it
- Use `open()` to open a file (takes 1 required param, 2 optionals)
- File name should be a string, should represent the actual filename recognized by the operating system
- Examples of opening a file (the basic way)
  - ```python
    fo = open("DataFile.txt")
  - ```python
    the_file = input("What is the name of the file: ")
    fo = open(the_file)
- A better way to open files!
  - Use `with` and `as` 
  - ```python
    with open("file.txt") as file_object:
        # do things with a file
    # file is now closed
  - This auto handles file closing, which is very nice.
- 6 Different file modes, but we will probably only use three
  - `r` is read
  - `r+` is read but you can also write
  - `w` is write
  - `w+` is write but you can also read
  - `a` is append
  - `a+` is append but you can also read
  - If you don't specify a mode, read is the default. 
- When you look for a file with open, it has to be there or else your program crashes.
- 

## Why to close files?
- File locking
- Resource management

## How does python file files?
Default location: 
- When you open a file in Python without providing a specific path, Python looks in the same directory where your python script `.py` is stored.

## Use basic file routing
- `./` is the current directory
- `../` goes back a directory
- `./<name>/` goes to that directory
- `../../apps/web/file.txt` would go back two directories, enter the apps directory, then enter the web directory, then find file.txt

## Directories in python
`mkdir()` method
```python
import os
os.mkdir("test")
```

## Reading from files (4 Approaches)
1) Reading the entire file at once into a string
   - Go to the store once ever, and get a truck worth of stuff
   - Reduce travel overhead
   - You need a ton of storage
   - **Advantages**
     - Easy access
     - Simple code
     - Fast processing
   - **Disadvantages**
     - Memory intensive
     - Slower initial load
   - Doing it now;
   - ```python
     <file object>.read()
     # ex
     with open('file.txt', 'r) as file:
        long_str = file.read()
2) Read the entire contents of the file into a list
   - Same advantages and disadvantages as the first
   - ```python
     <file object>.read()
     # ex
     with open('file.txt', 'r) as file:
        long_str = file.readline()
3) Read a file one line at atime
   - Go to the store once a week
   - you have to travel very often
   - You don't need a ton of storage
   - **advantages**
     - Faster startup
     - Don't need a ton of memory
   - **disadvantages**
     - More time wasted reading file
   - ex:
     - ```python
       <file object>.readline()
       with open (`file.txt`, 'r') as file:
        line = file.readline()
4) Read a file one character at a time
   - Go to the store for each item
   - Travel very often
   - Need very little storage
   - **advantages**
     - Very memory efficient
     - Lots of control
   - **disadvantages**
     - Very slow if you have a large file
   - ex
     - ```python
       <file object>.read(number)
       str = ""
       for i in range(10):
        str = str + fo.read(i)

## Writing to files (Also has four approaches)
1) Write one large string at once
   - **Advantages**
     - Efficient
     - Simple code
   - **Disadvantages**
     - Memory intensive
     - No flexibility
   - ex
     - ```python
       <file object>.write()
2) Write a list
   - **Advantages**
        - Structured Output
        - Efficient
   - **Disadvantages**
     - Memory usage
     - Does not handle new lines for you :/
   - ex
      - ```python
        <file object>.writelines(lines)
      - ```python
        # handle new lines
        with open('out.txt', 'w') as my_file
            for list_item in big_list:
                my_file.write(list_item + "\n") # add new lines
3) Write one string at a time (on seperate lines)
   - **Advantages**
     - Idk
   - **Disadvantages**
     - Idk
   - ex:
     - ```python
       <file object>.write('str', '\n')
4) Write one char at a time
   - **Advantages**
     - Precise control
     - Memory efficient
   - **Disadvantages**
     - Very inefficient
     - Complex code
   - ex: 
     - ```python
       <file object>.write('a')
5) **Personal Notes**
   - What is even going on here
   - Apparently you just use write for everything???
   - This language is awful and I hate it here

## Important issues
- strings are not numeric data (lol)
- error handling is important (lmfao)
- Things are not always formatted the way you want
  - Use `.strip()` to get rid of leading and trailing whitespace



