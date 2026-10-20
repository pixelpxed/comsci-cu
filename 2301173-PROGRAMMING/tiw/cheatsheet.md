**เมธวัจน์ โรจน์นิเวทย์ (6934455123)** — Programming Lab Exam 1 (2301173)

```python
# Print auto ends with `\n` unless specified
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

```python
# Sorted
sorted(iterable, key=key, reverse=reverse)
# Example
sorted(scores, key = lambda x:x[1], reverse=True)  # Lambda method

def get_second_value(score_tuple):
  return score_tuple[1]
sorted(scores, key=get_second_value, reverse=True) # Function method
```

```python
# File Opening
file_raw = open("file_name.txt")            # Can specifiy only file name if in directory
file_raw = open("D:\\myfiles\welcome.txt")  # Full path if not in directory
file_contents = file_raw.read().split()     # Read contents as string
file_contents = file_raw.readline()         # Read one line, call again to read another
file_contents = file_raw.readlines()        # Gets all the lines
file_raw.close()

# Additional methods using `with`
with open("demofile.txt") as f:
  print(f.read())

# raw, append, write, create, textmode, binarymode
open(file, mode=["r" | "a" | "w" | "x" | "t" | "b"])
```

```python
# Utilities
int(), str(), float()
string.strip(), max(), min(), sum(), len()
round(value, decimal_places)
```

```python
# String Selection
string = "Something123"
print(string)       # Something123
print(string[2])    # m
print(string[-2])   # 2
print(string[:2])   # So
print(string[4:])   # thing123
print(string[-2:])  # 23
print(string[:-4])  # Somethin
print(string[2:5])  # met
```

```python
for item in array / for i in range(n) / while (True)
if else elif
```

```python
# Lists
# Adding, editing a value to list.
lists[0] = 8       # Editing a value in a position
lists.append(6)    # Adding the value to last in list
lists.insert(2, 7) # Adding the value inside the specific position
lists.remove(5)    # Removes the first-matching value inside list
```

```python
# Tuples
tuples = (12, 13)
print(tuples[1], tuples[0])

# Because tuples are strict, unlike lists you'll have to build the whole () again.
tuples = (14, tuples[1])
print(tuples)
```

```python
# Dictionaries
dictionary = {
  "key1": "value1",
  "key2": "value2"
}
dictionary["key1"], dictionary.keys(), list(dictionary.keys()), list(dictionary.items())
dictionary["key2"] = "value4"     # Edits a value
dictionary["something"] = "that"  # Adds a new value
```

```python
# Good to know math modules
import math
math.sqrt(), math.log(), math.ceil(), math.floor()

"string".isalpha() # Is all alphabets or not (True, False)
```


