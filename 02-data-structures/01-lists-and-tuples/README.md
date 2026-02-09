# Lists and Tuples

## Objective

Learn how to store, access, and manipulate ordered collections of data using Python's two core sequence types: lists (mutable) and tuples (immutable).

## Concepts Covered

- Creating lists (literal syntax, `list()` constructor)
- Indexing and negative indexing
- Slicing (same rules as strings)
- Modifying lists: `append()`, `insert()`, `extend()`, `remove()`, `pop()`, `clear()`
- Sorting: `sort()` vs `sorted()`, `reverse` parameter, `key` parameter
- Other useful operations: `len()`, `in`, `index()`, `count()`, `min()`, `max()`, `sum()`
- Nested lists (lists of lists, accessing nested elements)
- Copying lists: shallow copy gotchas
- Tuples — the immutable cousin
- When to use tuples vs lists
- Named tuples (brief intro)

## Prerequisites

- Variables and types
- Basic string operations (slicing will feel familiar)

## Lesson

### Creating Lists

A list is an ordered, mutable collection. You can put anything in a list — numbers, strings, other lists, a mix of everything. Use square brackets:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True, None]
empty = []
```

You can also use the `list()` constructor to convert other iterables into lists:

```python
letters = list("hello")          # ['h', 'e', 'l', 'l', 'o']
numbers = list(range(5))         # [0, 1, 2, 3, 4]
another_copy = list([1, 2, 3])   # [1, 2, 3] — works but pointless
```

### Indexing and Negative Indexing

Every item in a list has a position (index), starting at 0:

```python
fruits = ["apple", "banana", "cherry", "date"]
#          0         1         2         3

print(fruits[0])    # "apple"   — first item
print(fruits[2])    # "cherry"  — third item
```

Negative indexes count backwards from the end:

```python
print(fruits[-1])   # "date"   — last item
print(fruits[-2])   # "cherry" — second to last
```

This is super handy when you need the last element and don't know (or care) how long the list is.

### Slicing

Slicing extracts a portion of the list. The syntax is `list[start:stop:step]` — the same rules you learned with strings:

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:5]       # [2, 3, 4]       — index 2 up to (not including) 5
nums[:3]        # [0, 1, 2]       — from the beginning
nums[7:]        # [7, 8, 9]       — to the end
nums[::2]       # [0, 2, 4, 6, 8] — every other item
nums[::-1]      # [9, 8, 7, ...]  — reversed copy
```

Slicing always returns a **new list**. The original stays untouched.

### Modifying Lists

Lists are **mutable** — you can change them after creation. This is one of the biggest differences from strings and tuples.

#### Adding Items

```python
fruits = ["apple", "banana"]

fruits.append("cherry")            # Add to the end: ["apple", "banana", "cherry"]
fruits.insert(1, "blueberry")      # Insert at index 1: ["apple", "blueberry", "banana", "cherry"]
fruits.extend(["date", "elderberry"])  # Add multiple items to the end
```

**Common mistake:** `append()` adds one item. If you append a list, you get a nested list. Use `extend()` to merge lists.

```python
a = [1, 2]
a.append([3, 4])   # [1, 2, [3, 4]]  — probably not what you wanted
b = [1, 2]
b.extend([3, 4])   # [1, 2, 3, 4]    — this is probably what you wanted
```

#### Removing Items

```python
fruits = ["apple", "banana", "cherry", "banana"]

fruits.remove("banana")    # Removes the FIRST occurrence: ["apple", "cherry", "banana"]
popped = fruits.pop()      # Removes and returns the LAST item: "banana"
popped = fruits.pop(0)     # Removes and returns item at index 0: "apple"
fruits.clear()             # Removes everything: []
```

You can also reassign by index or delete by index:

```python
colors = ["red", "green", "blue"]
colors[1] = "yellow"       # ["red", "yellow", "blue"]
del colors[0]              # ["yellow", "blue"]
```

### Sorting

There are two ways to sort, and the difference matters:

#### `sort()` — sorts in place (modifies the original, returns None)

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

#### `sorted()` — returns a new sorted list (original unchanged)

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
ordered = sorted(numbers)
print(ordered)   # [1, 1, 2, 3, 4, 5, 6, 9]
print(numbers)   # [3, 1, 4, 1, 5, 9, 2, 6] — still the original order
```

#### Reverse and Key

Both `sort()` and `sorted()` accept `reverse` and `key` parameters:

```python
# Descending order
numbers.sort(reverse=True)     # [9, 6, 5, 4, 3, 2, 1, 1]

# Sort by a custom rule — key is a function applied to each element
words = ["banana", "pie", "strawberry", "fig"]
words.sort(key=len)            # ["pie", "fig", "banana", "strawberry"]

# Sort case-insensitively
names = ["alice", "Bob", "CHARLIE"]
sorted_names = sorted(names, key=str.lower)  # ["alice", "Bob", "CHARLIE"]
```

**A classic gotcha:** `sort()` returns `None`, not the sorted list. Don't do `x = my_list.sort()` — `x` will be `None`.

### Other Useful Operations

```python
nums = [3, 1, 4, 1, 5, 9]

len(nums)          # 6         — number of items
5 in nums          # True      — membership check
99 in nums         # False
nums.index(4)      # 2         — index of first occurrence (raises ValueError if not found)
nums.count(1)      # 2         — how many times 1 appears
min(nums)          # 1
max(nums)          # 9
sum(nums)          # 23
```

### Nested Lists

Lists can contain other lists. This is how you represent grids, tables, or matrices:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[0])       # [1, 2, 3]     — first row
print(matrix[0][1])    # 2             — first row, second column
print(matrix[2][2])    # 9             — third row, third column
```

You can go as deep as you need, but if you find yourself nesting more than two or three levels, it's usually a sign you should use a class or a different data structure.

### Copying Lists: Shallow Copy Gotchas

This is where beginners get bitten. Assigning a list to a new variable does **not** copy it — both variables point to the **same** list:

```python
a = [1, 2, 3]
b = a           # b is NOT a copy — it's the same list
b.append(4)
print(a)        # [1, 2, 3, 4]  — surprise! a changed too
```

To make a **shallow copy** (a new list with the same elements):

```python
a = [1, 2, 3]
b = a[:]          # Slice copy
c = a.copy()      # .copy() method
d = list(a)       # list() constructor
```

Now `b`, `c`, and `d` are independent copies. Changing one won't affect the others.

**But watch out with nested lists.** A shallow copy only copies the outer list. The inner lists are still shared:

```python
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0][0] = 99
print(original)  # [[99, 2], [3, 4]]  — the inner list changed!
```

For a truly independent copy of nested structures, use `copy.deepcopy()`:

```python
import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original)  # [[1, 2], [3, 4]]  — safe!
```

### Tuples — The Immutable Cousin

A tuple is like a list, but you **cannot change it** after creation. Use parentheses instead of square brackets:

```python
point = (3, 4)
rgb = (255, 128, 0)
single = (42,)      # Note the trailing comma — without it, (42) is just the number 42
empty = ()
```

You can also create tuples without parentheses (tuple packing):

```python
coordinates = 10, 20, 30   # This is a tuple: (10, 20, 30)
```

Indexing and slicing work exactly like lists:

```python
print(point[0])     # 3
print(rgb[-1])      # 0
print(rgb[1:])      # (128, 0)
```

But you **cannot** assign to an index:

```python
point[0] = 99       # TypeError: 'tuple' object does not support item assignment
```

#### Tuple Unpacking

One of the most useful features in Python. You can assign each element to a separate variable in one line:

```python
point = (3, 4)
x, y = point
print(x)  # 3
print(y)  # 4

# Works great with functions that return multiple values
def get_dimensions():
    return 1920, 1080

width, height = get_dimensions()
```

You can also use `*` to capture the rest:

```python
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

head, *middle, tail = [1, 2, 3, 4, 5]
print(head)    # 1
print(middle)  # [2, 3, 4]
print(tail)    # 5
```

### When to Use Tuples vs Lists

| Use a **list** when... | Use a **tuple** when... |
|---|---|
| The data will change (add/remove items) | The data is fixed and shouldn't change |
| Items are the same "kind" of thing (all names, all scores) | Items have different roles (x/y coordinates, name/age pairs) |
| Order might change (sorting, shuffling) | You need it as a dictionary key (tuples are hashable, lists aren't) |

A good rule of thumb: if the collection is a "group of things," use a list. If it's a "record with fields," use a tuple.

### Named Tuples (Brief Mention)

If you find yourself using tuples as records, `namedtuple` from the `collections` module gives you named fields:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x)    # 3
print(p.y)    # 4
print(p[0])   # 3  — regular indexing still works
```

This gives you the readability of a class with the simplicity of a tuple. We'll cover this more in a later lesson — just know it exists.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Lists are ordered, mutable sequences created with `[]` — use them when data will change
- Tuples are ordered, immutable sequences created with `()` — use them for fixed data
- Both support indexing, negative indexing, and slicing with `[start:stop:step]`
- `sort()` modifies in place (returns `None`); `sorted()` returns a new list
- Assigning a list to a new variable does **not** copy it — use `[:]`, `.copy()`, or `list()` for a shallow copy
- For nested lists, use `copy.deepcopy()` to avoid shared references
- Tuple unpacking (`x, y = point`) is one of Python's most useful features
- Use `namedtuple` when a tuple starts feeling like a record with named fields
