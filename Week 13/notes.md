# Tuples and sets

```python
my_tuple = ("a", "b", "c")

print(my_tuple[0]) # a
len(my_tuple) # 3

# editing and modifying tuples
new_list = list(my_tuple)
new_list[0] = "d"
new_tuple = tuple(new_list)
print(new_tuple) # a, b, c, d
# see example one

```

## Tuples
- Tuples are immutable
- Tuples allow access to elements using indexing
- Used for a list of seperate items
- idk I forgot to take half the notes tbh

## Sets
- Based on mathematical theory in an attempt to implement what math mathematicians talk about when they say sets. 
- A set is an unordered collection of unique elements
  - Uniqueness:
    - Unlike lists or tuples, sets automatically ensure that all elements are unique. 
    - If you try to add a duplicate element to a set, it will simply be ignored
- There is no indexing in sets
- Why are sets useful? 
  - Imagine a club where each member can only join once
    - Once you are a member, trying to join again does nothing
    - This is similar to how sets handle uniqueness
- Unordered Collection
  - Think a bag of marbles. When you reach into the bag, you don't know which marble you'll grab first
  - The marbles don't have a specific order, just like elements in a set.
  - You can't have duplicates, but python won't error if you try and add an element that already exists
- Efficient lookup
  - Sets are optimized for quickly checking if an element exists
- Set Methods

## Set methods
| method             | desc                                                   |
|--------------------|--------------------------------------------------------|
| add(element)       | Add a single element to the set                        |
| `update(iterable)` | add multiple elements to the set                       |
| `remove(elemenet)` | Remove an element (raises KeyError if not found)       |
| `discard(element)` | Remove an element if it exists (no error if not found) |
| `pop()`            | Remove and return an arbitrary element (that's fun)    |
| `clear()`          | Remove everything from a set                           | 

## Mathematical Set Operations
Returns a new set
- `union(other_set)` or `|`
  - Items in either set (all items)
- `intersection(other_set)` or `&`
  - Items in both sets
- `difference(other_set)` or `-`:
  - Elements in the first set but not in the second
- `symmetric_difference(other_set)` or `^`
  - Elements in either set, but not in both

```python
# Creating sets
my_set = {1, 2, 3}
print(my_set) # {1, 2, 3}

# or use the set constructor
new_set = set([1, 2, 3])
print(my_set) # {1, 2, 3}

empty_set = set()
print(empty_set) # {}

# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set) # {0, 1, 4, 9, 16

another_set = {0, 1, 2, 2, 2, 3}
print(another_set) # {0, 1, 2, 3}

# Mathematical Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a | set_b) # {1, 2, 3, 4, 5}
print(set_a & set_b) # {3}
print(set_a - set_b) # {1, 2}
print(set_a ^ set_b) # {1, 2, 4, 5}

another_one = {1, 2, 3, 4, 5}
print(3 in another_one) # True
print(10 in another_one) # False

```


## Data type and mutability
| Type         | Mutability | 
|--------------|------------|
| Strings      | Immutable  |
| Lists        | Mutable    | 
| Tuple        | Immutable  |
| Sets         | Mutable    |
| Dictionaries | Mutable    |


