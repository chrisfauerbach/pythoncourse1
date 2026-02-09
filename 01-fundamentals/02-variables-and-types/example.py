"""
Variables and Types — Example Code
====================================

Run this file:
    python3 example.py

This file demonstrates how variables work in Python, the core data types,
arithmetic operations, and type conversion.
"""

# -----------------------------------------------------------------------------
# 1. Creating variables — just pick a name and use =
# -----------------------------------------------------------------------------

name = "Alice"
age = 30
height = 5.6
is_student = False
favorite_color = None    # No value yet

print("--- Creating Variables ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)
print("Favorite color:", favorite_color)
print()

# -----------------------------------------------------------------------------
# 2. Checking types with type()
# -----------------------------------------------------------------------------

print("--- Checking Types ---")
print(f"name = {name!r}, type = {type(name).__name__}")
print(f"age = {age!r}, type = {type(age).__name__}")
print(f"height = {height!r}, type = {type(height).__name__}")
print(f"is_student = {is_student!r}, type = {type(is_student).__name__}")
print(f"favorite_color = {favorite_color!r}, type = {type(favorite_color).__name__}")
print()

# Don't worry about the f"..." syntax — that's f-strings, coming in a later lesson.
# For now, just notice how type() tells you what each variable is.

# -----------------------------------------------------------------------------
# 3. Integer operations
# -----------------------------------------------------------------------------

print("--- Integer Arithmetic ---")
a = 17
b = 5

print(f"{a} + {b} = {a + b}")       # Addition: 22
print(f"{a} - {b} = {a - b}")       # Subtraction: 12
print(f"{a} * {b} = {a * b}")       # Multiplication: 85
print(f"{a} / {b} = {a / b}")       # Division: 3.4 (always a float!)
print(f"{a} // {b} = {a // b}")     # Floor division: 3
print(f"{a} % {b} = {a % b}")       # Modulo (remainder): 2
print(f"{a} ** {b} = {a ** b}")     # Power: 1419857
print()

# Big numbers — underscores are just for readability
world_population = 8_045_000_000
print(f"World population: {world_population}")
print()

# -----------------------------------------------------------------------------
# 4. Float quirks
# -----------------------------------------------------------------------------

print("--- Float Quirks ---")
print(f"0.1 + 0.2 = {0.1 + 0.2}")         # 0.30000000000000004
print(f"Rounded:    {round(0.1 + 0.2, 1)}")  # 0.3 (round() fixes it)
print()

# Division always returns a float
print(f"10 / 2 = {10 / 2}")     # 5.0 (not 5!)
print(f"10 // 2 = {10 // 2}")   # 5   (floor division gives an int)
print()

# -----------------------------------------------------------------------------
# 5. Strings — a few operations you can do right away
# -----------------------------------------------------------------------------

print("--- String Operations ---")
first = "Hello"
last = "World"

# Concatenation (joining strings)
combined = first + " " + last
print("Concatenation:", combined)

# Repetition
print("Repetition:", "ha" * 3)       # hahaha
print("Separator:", "-" * 30)

# Length
message = "Python is fun"
print(f"'{message}' has {len(message)} characters")
print()

# -----------------------------------------------------------------------------
# 6. Booleans — True and False
# -----------------------------------------------------------------------------

print("--- Booleans ---")
is_sunny = True
is_raining = False

print(f"Sunny: {is_sunny}")
print(f"Raining: {is_raining}")

# Booleans are actually integers under the hood!
print(f"True + True = {True + True}")     # 2
print(f"True * 10 = {True * 10}")         # 10
print(f"False + 5 = {False + 5}")         # 5

# Comparison operators return booleans
print(f"10 > 5: {10 > 5}")       # True
print(f"10 == 5: {10 == 5}")     # False (== checks equality)
print(f"10 != 5: {10 != 5}")     # True  (!= means "not equal")
print()

# -----------------------------------------------------------------------------
# 7. Type conversion (casting)
# -----------------------------------------------------------------------------

print("--- Type Conversion ---")

# String to int
user_input = "42"
number = int(user_input)
print(f"String '{user_input}' → int {number}, doubled = {number * 2}")

# String to float
price_text = "19.99"
price = float(price_text)
print(f"String '{price_text}' → float {price}")

# Number to string
count = 7
message = "There are " + str(count) + " days in a week"
print(message)

# Float to int (truncates, does NOT round!)
pi = 3.99
print(f"int({pi}) = {int(pi)}")   # 3 (chopped, not rounded)

# "Truthy" and "Falsy" conversions
print(f"bool(1) = {bool(1)}")       # True  (any non-zero number)
print(f"bool(0) = {bool(0)}")       # False
print(f"bool('hi') = {bool('hi')}") # True  (any non-empty string)
print(f"bool('') = {bool('')}")     # False (empty string)
print(f"bool(None) = {bool(None)}") # False
print()

# -----------------------------------------------------------------------------
# 8. Multiple assignment and swapping
# -----------------------------------------------------------------------------

print("--- Multiple Assignment ---")

# Assign multiple variables at once
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# Same value for multiple variables
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

# Swap without a temporary variable!
print(f"Before swap: x={x}, y={y}")
x, y = y, x
print(f"After swap:  x={x}, y={y}")
print()

# -----------------------------------------------------------------------------
# 9. Assignment shortcuts
# -----------------------------------------------------------------------------

print("--- Assignment Shortcuts ---")
score = 100
print(f"Start:    {score}")

score += 25     # score = score + 25
print(f"+= 25:   {score}")

score -= 10     # score = score - 10
print(f"-= 10:   {score}")

score *= 2      # score = score * 2
print(f"*= 2:    {score}")

score //= 3     # score = score // 3
print(f"//= 3:   {score}")

score %= 7      # score = score % 7
print(f"%= 7:    {score}")
print()

# -----------------------------------------------------------------------------
# 10. Dynamic typing — variables can change type
# -----------------------------------------------------------------------------

print("--- Dynamic Typing ---")
thing = 42
print(f"thing = {thing!r}, type = {type(thing).__name__}")

thing = "now I'm a string"
print(f"thing = {thing!r}, type = {type(thing).__name__}")

thing = True
print(f"thing = {thing!r}, type = {type(thing).__name__}")

thing = None
print(f"thing = {thing!r}, type = {type(thing).__name__}")
print()

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print("=" * 40)
print("  VARIABLES AND TYPES COMPLETE!")
print("=" * 40)
