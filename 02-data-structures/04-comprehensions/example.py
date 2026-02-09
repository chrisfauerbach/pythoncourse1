"""
Comprehensions — Example Code
===============================

Run this file:
    python3 example.py

Comprehensions let you build lists, dicts, and sets in a single expressive
line. This file walks through every type with practical examples.
"""

# -----------------------------------------------------------------------------
# 1. Basic list comprehension — transform every item
# -----------------------------------------------------------------------------

# The old way: build a list with a loop
squares_loop = []
for n in range(6):
    squares_loop.append(n ** 2)

# The comprehension way: same result, one line
squares_comp = [n ** 2 for n in range(6)]

print("1. Basic list comprehension")
print(f"   Squares (loop): {squares_loop}")
print(f"   Squares (comp): {squares_comp}")
print()

# A few more examples
names = ["alice", "bob", "carol"]
shouting = [name.upper() for name in names]
lengths = [len(name) for name in names]
print(f"   Names uppercased: {shouting}")
print(f"   Name lengths:     {lengths}")
print()

# -----------------------------------------------------------------------------
# 2. Filtering with if — keep only items that pass a condition
# -----------------------------------------------------------------------------

# Only even numbers from 0-9
evens = [n for n in range(10) if n % 2 == 0]

# Only words longer than 3 characters
words = ["hi", "hello", "hey", "howdy", "yo"]
long_words = [w for w in words if len(w) > 3]

# Only positive numbers from a mixed list
numbers = [-5, 3, -1, 7, -2, 8, 0]
positives = [n for n in numbers if n > 0]

print("2. Filtering with if")
print(f"   Even numbers:  {evens}")
print(f"   Long words:    {long_words}")
print(f"   Positives:     {positives}")
print()

# -----------------------------------------------------------------------------
# 3. Transforming with if/else — include everything, but modify based on condition
# -----------------------------------------------------------------------------

# Label numbers as even or odd
labels = ["even" if n % 2 == 0 else "odd" for n in range(6)]

# Clamp values to a range (keep between 0 and 10)
raw = [-3, 5, 12, 7, -1, 10, 15]
clamped = [max(0, min(10, x)) for x in raw]

# Replace negatives with zero
cleaned = [n if n >= 0 else 0 for n in numbers]

print("3. Transforming with if/else")
print(f"   Labels:  {labels}")
print(f"   Raw:     {raw}")
print(f"   Clamped: {clamped}")
print(f"   Cleaned (negatives -> 0): {cleaned}")
print()

# -----------------------------------------------------------------------------
# 4. Nested comprehensions — working with nested data
# -----------------------------------------------------------------------------

# Flatten a matrix (list of lists) into a single list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
flat = [num for row in matrix for num in row]

print("4. Nested comprehensions")
print(f"   Matrix:    {matrix}")
print(f"   Flattened: {flat}")

# Transpose a matrix (swap rows and columns)
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"   Transposed: {transposed}")

# All combinations of two lists (like a cross product)
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combos = [(c, s) for c in colors for s in sizes]
print(f"   Combos:    {combos}")
print()

# -----------------------------------------------------------------------------
# 5. Dictionary comprehensions — build dicts in one line
# -----------------------------------------------------------------------------

# Map each word to its length
fruits = ["apple", "banana", "cherry", "date"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}

# Square lookup table: number -> its square
square_table = {n: n ** 2 for n in range(1, 6)}

# Filter a dict: only passing scores
scores = {"Alice": 92, "Bob": 67, "Carol": 85, "Dave": 43}
passing = {name: score for name, score in scores.items() if score >= 70}

# Invert a dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

print("5. Dictionary comprehensions")
print(f"   Fruit lengths: {fruit_lengths}")
print(f"   Square table:  {square_table}")
print(f"   All scores:    {scores}")
print(f"   Passing only:  {passing}")
print(f"   Original dict: {original}")
print(f"   Inverted dict: {inverted}")
print()

# -----------------------------------------------------------------------------
# 6. Set comprehensions — build sets (duplicates removed automatically)
# -----------------------------------------------------------------------------

# Unique first letters from a list of words
animals = ["ant", "ape", "bear", "bat", "cat", "cobra", "deer"]
first_letters = {animal[0] for animal in animals}

# Unique word lengths
sentence = "the quick brown fox jumps over the lazy dog"
unique_lengths = {len(word) for word in sentence.split()}

print("6. Set comprehensions")
print(f"   Animals: {animals}")
print(f"   Unique first letters: {sorted(first_letters)}")
print(f"   Unique word lengths:  {sorted(unique_lengths)}")
print()

# -----------------------------------------------------------------------------
# 7. Generator expressions — lazy comprehensions
# -----------------------------------------------------------------------------

# A generator expression looks like a list comprehension but uses parentheses
# It doesn't build the whole list in memory — it produces values one at a time

# Sum of squares using a generator (no intermediate list created)
sum_of_squares = sum(n ** 2 for n in range(1, 11))

# Check if any number is negative
numbers = [3, 7, -2, 5, 1]
has_negative = any(n < 0 for n in numbers)
all_positive = all(n > 0 for n in numbers)

# Find the longest word
words = ["python", "is", "absolutely", "fantastic"]
longest = max(words, key=lambda w: len(w))

print("7. Generator expressions")
print(f"   Sum of squares 1-10: {sum_of_squares}")
print(f"   Numbers: {numbers}")
print(f"   Has a negative?  {has_negative}")
print(f"   All positive?    {all_positive}")
print(f"   Longest word in {words}: '{longest}'")
print()

# -----------------------------------------------------------------------------
# 8. Side-by-side: loop vs. comprehension
# -----------------------------------------------------------------------------

print("8. Loop vs. comprehension — same results, different style")
print()

# Example A: Convert temperatures
temps_f = [32, 68, 100, 212]

# Loop version
temps_c_loop = []
for f in temps_f:
    temps_c_loop.append(round((f - 32) * 5 / 9, 1))

# Comprehension version
temps_c_comp = [round((f - 32) * 5 / 9, 1) for f in temps_f]

print(f"   Fahrenheit: {temps_f}")
print(f"   Celsius (loop): {temps_c_loop}")
print(f"   Celsius (comp): {temps_c_comp}")
print()

# Example B: Build a lookup dict from two lists
keys = ["name", "age", "city"]
values = ["Alice", 30, "Portland"]

# Loop version
lookup_loop = {}
for k, v in zip(keys, values):
    lookup_loop[k] = v

# Comprehension version
lookup_comp = {k: v for k, v in zip(keys, values)}

print(f"   Keys:   {keys}")
print(f"   Values: {values}")
print(f"   Dict (loop): {lookup_loop}")
print(f"   Dict (comp): {lookup_comp}")
print()

# -----------------------------------------------------------------------------
# 9. When NOT to use comprehensions
# -----------------------------------------------------------------------------

print("9. When NOT to use comprehensions")
print()
print("   DON'T use comprehensions for side effects:")
print("     Bad:  [print(x) for x in items]")
print("     Good: for x in items: print(x)")
print()
print("   DON'T sacrifice readability:")
print("     If it doesn't fit on one line, use a loop.")
print("     Future-you will thank present-you.")
print()

# -----------------------------------------------------------------------------
# 10. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 50)
print("   COMPREHENSIONS COMPLETE!")
print("=" * 50)
print()
print("You now know list, dict, set, and generator comprehensions.")
print("Try the exercises in exercises.py to practice!")
