# Lists

Several ways to create a new list

Simplest way is an assignment statement
```python
listOfNumbers = [10, 20, 30, 40]
```

```python
cheeses = ['Cheddar', 'edam', 'Gouda', 'Havarti', 'Gruyere']
```

Lists are "unique"???? to Python (idk man im just writing things down)

We can access items in a list using its index
```python
l = ['a', 'b', 'c', 'd']
print(l[0]) # a
print(l[2]) # c
```

Many things can be done a lot easier with a list

**Lists are mutable** (can be changed)

## Lists within lists
Called a nested list

Tricky to deal with, but makes python interesting
```python
l = [[1, 2, 3], [4, 5, 6], [[6, 7, 8], [9, 10, 11]]]
```
Lots of utilities we can use

```python
cheeses = ['Cheddar', 'edam', 'Gouda', 'Havarti', 'Gruyere']
print(cheeses) # ['Cheddar', 'edam', 'Gouda', 'Havarti', 'Gruyere']
```

## Iterate through a list

```python
colors = ['red', 'yellow', 'green']
for color in colors:
    print(color)
print(f"There are {len(colors)} colors in the list")
# red
# yellow
# green
# There are 3 colors in the list
```

## How we can use lists

```python
# Note, this example is better suited for a dictionary
employeeName = ['Smith', 'Jones', 'Whitney']
salaries = [50_000, 75_000, 100_000]

def get_employee_salary(name: str):
    sal = -1
    for i in range(len(employeeName)):
        if employeeName[i] == name:
            sal = salaries[i]
    return sal

get_employee_salary('Smith') # 50_000
get_employee_salary('Bob') # - 1
```

## List methods
### Append
Add item to the end of a list
```python
l = [0, 1, 2, 3]
print(l) # [0, 1, 2, 3, 4]
l.append(5)
print(l) # [0, 1, 2, 3, 4]
```
### extend
adds a list to the end of a list
```python
aList = [0, 1, 2, 3, 4]
bList = [5, 6, 7]

aList.extend(bList)
print(aList) # [0, 1, 2, 3, 4, 5, 6, 7]
```
### insert
Insert item at index
```python
aList = [1, 2, 3]
aList.insert(1, 7)
print(aList) # [1, 7, 2, 3]
```

### remove
remove a specific item from a list
```python
aList = [1, 2, 3, 4]
aList.remove(2)
print(aList) # [1, 3, 4]
```

### pop
remove the last element of a list
```python
aList = [0, 1, 2, 3]
aList.pop()
print(aList) # [0, 1, 2]
```

### del
```python
aList = [0, 1, 2, 3]
del aList[1]
print(aList) # [0, 2, 3]
```

### clear
```python
aList = [0, 1, 2, 3]
aList.clear()
print(aList) # []
```

## All the list methods
| Method                   | Desc                                   | 
|--------------------------|----------------------------------------|
| `list.append(obj)`       | Append obj to the end of the list      |
| `list.count(obj)`        | How many times does this item exist?   |
| `list.extend(iterable)`  | Add a list to the end of the list      |
| `list.index(obj)`        | Get the index of the first object      |
| `list.insert(index, obj` | Insert obj at index                    |
| `list.pop(obj=list[-1)`  | remove last item from list or last obj |
| `list.remove(obj)`       | Remove first obj from list             |
| `list.reverse()`         | reverse the list                       |
| `list.sort(func)`        | sort the list given the func           |




