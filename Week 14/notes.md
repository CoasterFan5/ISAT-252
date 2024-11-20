# Dictionaries
If you want to look up information, and you know what you are looking for, it is very easy to find.

`key: value` pair, where like a real dictionary, the key is the word you are looking up and the value is the definition. 

## Why Dictionaries? 
- Fast data retrieval
  - They allow you to quickly access values using the keys
- Meaningful Associations
- Flexible Data Organization

## Parts of a dictionary
- Keys
  - Must be unique
  - Must be an immutable type
- Values
  - can be of any type
- Casing


```python

dict1 = dict()
dict1["a"] = "b"
dict1["b"] = "a"
print(dict1) # {'a': 'b', 'b': 'a'}

dictionary = {
    "a": "123",
    "b": "456",
    "c": "789"
}

print(dictionary["a"]) # 123

```




