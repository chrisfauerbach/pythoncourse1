"""
Lists and Tuples — Example Code
=================================

Run this file:
    python3 example.py

A complete tour of lists and tuples in Python. Every concept from the
README is demonstrated here with plenty of comments.
"""

import copy
from collections import namedtuple

# -----------------------------------------------------------------------------
# 1. Creating lists
# -----------------------------------------------------------------------------

# Literal syntax — the most common way
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed = [1, "hello", 3.14, True, None]   # Lists can hold any mix of types
empty = []

print("fruits:", fruits)
print("numbers:", numbers)
print("mixed:", mixed)
print("empty:", empty)

# list() constructor — converts other iterables into a list
letters = list("hello")         # Each character becomes an item
from_range = list(range(5))     # Generates [0, 1, 2, 3, 4]

print("letters:", letters)
print("from_range:", from_range)

# -----------------------------------------------------------------------------
# 2. Indexing and negative indexing
# -----------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#          0        1         2         3       4
#         -5       -4        -3        -2      -1

print("\n--- Indexing ---")
print("First item (index 0):", fruits[0])      # apple
print("Third item (index 2):", fruits[2])      # cherry
print("Last item (index -1):", fruits[-1])     # elderberry
print("Second to last (-2):", fruits[-2])      # date

# -----------------------------------------------------------------------------
# 3. Slicing — same [start:stop:step] syntax as strings
# -----------------------------------------------------------------------------

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("\n--- Slicing ---")
print("nums[2:5]:", nums[2:5])        # [2, 3, 4]
print("nums[:3]:", nums[:3])          # [0, 1, 2]
print("nums[7:]:", nums[7:])          # [7, 8, 9]
print("nums[::2]:", nums[::2])        # [0, 2, 4, 6, 8]  — every other item
print("nums[1::2]:", nums[1::2])      # [1, 3, 5, 7, 9]  — odd-indexed items
print("nums[::-1]:", nums[::-1])      # reversed copy

# Slicing returns a NEW list — the original is untouched
first_three = nums[:3]
first_three[0] = 999
print("Modified slice:", first_three)  # [999, 1, 2]
print("Original still:", nums)         # [0, 1, 2, 3, ...]

# -----------------------------------------------------------------------------
# 4. Modifying lists — adding items
# -----------------------------------------------------------------------------

print("\n--- Adding items ---")

shopping = ["milk", "eggs"]
print("Start:", shopping)

# append() — add one item to the end
shopping.append("bread")
print("After append('bread'):", shopping)

# insert() — add one item at a specific position
shopping.insert(1, "butter")
print("After insert(1, 'butter'):", shopping)

# extend() — add multiple items to the end
shopping.extend(["cheese", "yogurt"])
print("After extend(['cheese', 'yogurt']):", shopping)

# The append vs extend trap
trap_demo = [1, 2]
trap_demo.append([3, 4])       # Adds the list AS ONE ITEM (nested!)
print("\nappend([3,4]):", trap_demo)    # [1, 2, [3, 4]]

correct_demo = [1, 2]
correct_demo.extend([3, 4])   # Adds each item individually
print("extend([3,4]):", correct_demo)  # [1, 2, 3, 4]

# -----------------------------------------------------------------------------
# 5. Modifying lists — removing items
# -----------------------------------------------------------------------------

print("\n--- Removing items ---")

colors = ["red", "green", "blue", "green", "yellow"]
print("Start:", colors)

# remove() — removes the FIRST matching item
colors.remove("green")
print("After remove('green'):", colors)    # Only the first "green" is gone

# pop() — removes and returns an item by index (default: last item)
last = colors.pop()
print(f"pop() returned '{last}', list is now: {colors}")

first = colors.pop(0)
print(f"pop(0) returned '{first}', list is now: {colors}")

# del — remove by index without getting the value back
del colors[0]
print("After del colors[0]:", colors)

# clear() — remove everything
colors.clear()
print("After clear():", colors)

# Reassignment by index
letters = ["a", "b", "c"]
letters[1] = "B"
print("\nAfter letters[1] = 'B':", letters)   # ['a', 'B', 'c']

# -----------------------------------------------------------------------------
# 6. Sorting
# -----------------------------------------------------------------------------

print("\n--- Sorting ---")

# sort() — sorts the list IN PLACE, returns None
scores = [85, 92, 78, 95, 88, 72]
print("Original:", scores)
scores.sort()
print("After sort():", scores)

# sorted() — returns a NEW sorted list, original unchanged
scores = [85, 92, 78, 95, 88, 72]
ordered = sorted(scores)
print("\nsorted() result:", ordered)
print("Original after sorted():", scores)    # Unchanged!

# reverse parameter — descending order
scores.sort(reverse=True)
print("\nDescending sort:", scores)

# key parameter — sort by a custom rule
words = ["banana", "pie", "strawberry", "fig", "kiwi"]
words.sort(key=len)
print("Sorted by length:", words)

# Case-insensitive sorting with key
names = ["alice", "Bob", "CHARLIE", "dave"]
print("\nCase-insensitive sort:", sorted(names, key=str.lower))

# The classic gotcha: sort() returns None!
result = [3, 1, 2].sort()
print(f"\nlist.sort() returns: {result}")   # None — don't assign it!

# -----------------------------------------------------------------------------
# 7. Other useful operations
# -----------------------------------------------------------------------------

print("\n--- Useful operations ---")

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("len(nums):", len(nums))          # 9
print("5 in nums:", 5 in nums)          # True
print("99 in nums:", 99 in nums)        # False
print("nums.index(4):", nums.index(4))  # 2 (first occurrence)
print("nums.count(1):", nums.count(1))  # 2
print("min(nums):", min(nums))          # 1
print("max(nums):", max(nums))          # 9
print("sum(nums):", sum(nums))          # 36

# -----------------------------------------------------------------------------
# 8. Nested lists
# -----------------------------------------------------------------------------

print("\n--- Nested lists ---")

# A 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Full matrix:", matrix)
print("First row:", matrix[0])           # [1, 2, 3]
print("Element [0][1]:", matrix[0][1])   # 2  (row 0, column 1)
print("Element [2][2]:", matrix[2][2])   # 9  (row 2, column 2)

# Iterating over a matrix
print("\nMatrix printed row by row:")
for row in matrix:
    print("  ", row)

# -----------------------------------------------------------------------------
# 9. Copying lists — shallow copy gotchas
# -----------------------------------------------------------------------------

print("\n--- Copying lists ---")

# The assignment trap — NOT a copy!
a = [1, 2, 3]
b = a                   # b points to the SAME list as a
b.append(4)
print("a after modifying b:", a)   # [1, 2, 3, 4] — oops!

# Three ways to make a shallow copy
original = [10, 20, 30]
copy1 = original[:]        # Slice copy
copy2 = original.copy()    # .copy() method
copy3 = list(original)     # list() constructor

copy1.append(40)
print("\nOriginal:", original)     # [10, 20, 30] — safe!
print("copy1:", copy1)            # [10, 20, 30, 40]

# Shallow copy gotcha with nested lists
print("\n--- Shallow vs deep copy ---")
original = [[1, 2], [3, 4]]

shallow = original.copy()
shallow[0][0] = 99                 # Modifies the inner list!
print("Original after shallow copy mutation:", original)  # [[99, 2], [3, 4]]

# Deep copy — fully independent
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99                    # Only affects the deep copy
print("Original after deep copy mutation:", original)     # [[1, 2], [3, 4]]
print("Deep copy:", deep)                                  # [[99, 2], [3, 4]]

# -----------------------------------------------------------------------------
# 10. Tuples — the immutable cousin
# -----------------------------------------------------------------------------

print("\n--- Tuples ---")

# Creating tuples
point = (3, 4)
rgb = (255, 128, 0)
single = (42,)          # Trailing comma is required for single-item tuples!
empty_tuple = ()
packed = 10, 20, 30     # Parentheses are optional (tuple packing)

print("point:", point)
print("rgb:", rgb)
print("single:", single)
print("type(single):", type(single))       # <class 'tuple'>
print("type((42)):", type((42)))           # <class 'int'> — no comma = not a tuple!
print("packed:", packed)

# Indexing and slicing — same as lists
print("\npoint[0]:", point[0])
print("rgb[-1]:", rgb[-1])
print("rgb[1:]:", rgb[1:])

# Tuples are immutable — you CANNOT change them
# Uncomment the line below to see the error:
# point[0] = 99   # TypeError: 'tuple' object does not support item assignment

# But you CAN do this — create a new tuple from the old one
new_point = (99,) + point[1:]
print("New point from old:", new_point)    # (99, 4)

# -----------------------------------------------------------------------------
# 11. Tuple unpacking
# -----------------------------------------------------------------------------

print("\n--- Tuple unpacking ---")

# Basic unpacking
point = (3, 4)
x, y = point
print(f"x={x}, y={y}")

# Unpacking in a loop — super common pattern
students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
for name, score in students:
    print(f"  {name}: {score}")

# Star unpacking — capture the rest
first, *rest = [1, 2, 3, 4, 5]
print(f"\nfirst={first}, rest={rest}")

head, *middle, tail = [1, 2, 3, 4, 5]
print(f"head={head}, middle={middle}, tail={tail}")

# The classic swap trick using unpacking
a, b = 1, 2
a, b = b, a
print(f"\nAfter swap: a={a}, b={b}")       # a=2, b=1

# -----------------------------------------------------------------------------
# 12. When to use tuples vs lists
# -----------------------------------------------------------------------------

print("\n--- Tuples vs lists in practice ---")

# Tuple as a record (fixed structure, different roles)
person = ("Alice", 30, "alice@example.com")
name, age, email = person
print(f"{name} is {age} years old")

# List as a collection (variable length, same kind of thing)
scores = [95, 87, 92, 88, 78]
scores.append(91)
print(f"Average score: {sum(scores) / len(scores):.1f}")

# Tuples can be dictionary keys (lists cannot!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London",
}
print(f"Location at (40.7128, -74.0060): {locations[(40.7128, -74.0060)]}")

# -----------------------------------------------------------------------------
# 13. Named tuples — readable tuples with named fields
# -----------------------------------------------------------------------------

print("\n--- Named tuples ---")

Point = namedtuple("Point", ["x", "y"])
Color = namedtuple("Color", ["red", "green", "blue"])

p = Point(3, 4)
c = Color(255, 128, 0)

print(f"Point: ({p.x}, {p.y})")           # Access by name
print(f"Point[0]: {p[0]}")                # Index still works
print(f"Color: rgb({c.red}, {c.green}, {c.blue})")

# Named tuples are still immutable
# p.x = 10  # AttributeError

# But you can create a new one with _replace()
p2 = p._replace(x=10)
print(f"New point after _replace: ({p2.x}, {p2.y})")

# -----------------------------------------------------------------------------
# 14. Putting it all together
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("  LISTS AND TUPLES COMPLETE!")
print("=" * 50)
print()
print("You've seen how to create, access, modify, sort, copy, and unpack")
print("both lists and tuples. Try the exercises to practice these skills!")
