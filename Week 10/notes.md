# Error handling and input verification

- Anticipate Errors
  - Understand where things can go wrong
  - Prevent program from crashing
- Validate input
  - Ensure proper input is put in
  - Make sure input is what you are expecting
- Graceful Failure
  - Program does not just crash
- Exceptions
  - Python's `try` and `except` blcoks make handling exceptions and errors possible.
- Prevention is better than Cure:

## Errors in Python
- Syntax errors
  - Typos
  - Bad capitalization
  - etc.
- Logic Errors
  - Program produces incorrect results but does not error
- Runtime errors
  - Program errors in the runtime
  - Normally from bad inputs

## Handle Exceptions
```python
try:
    print("trying")
    # One or my python statements
except ValueError: # if ValueError 1 occurs, run  code in block
    print("valueError")
else: # if no exceptions, execute this block
    print("else")
finally:# Always execute this, no matter what
    print("Done!")
# See examples for a full example
```

## Examples of data validation
When asking a persons name, we need to ensure the input is valid, readable, and fits the expected format. A common validation method involves checking that:
- The input isn't empty
- The input consists of allowed characters
  - Accent marks are not alphanumeric
  - This is an important consideration
- The input is not excessively long or short. 

See `examples.py` for an example of input validation.