"""
Functions — Example Code
==========================

Run this file:
    python3 example.py

This file demonstrates how to define and use functions in Python —
parameters, return values, defaults, *args, **kwargs, scope, and more.
"""

import math

# -----------------------------------------------------------------------------
# 1. Defining a basic function
# -----------------------------------------------------------------------------

print("--- 1. Basic Functions ---")


def greet():
    """A simple function with no parameters and no return value."""
    print("Hello there!")


# Call it twice to show reuse
greet()
greet()
print()

# -----------------------------------------------------------------------------
# 2. Parameters and arguments
# -----------------------------------------------------------------------------

print("--- 2. Parameters and Arguments ---")


def greet_person(name):
    """Greet someone by name."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")


# Multiple parameters
def introduce(name, age, city):
    """Introduce someone with their details."""
    print(f"I'm {name}, {age} years old, from {city}.")


introduce("Alice", 30, "Seattle")
introduce("Bob", 25, "Austin")
print()

# -----------------------------------------------------------------------------
# 3. Return values
# -----------------------------------------------------------------------------

print("--- 3. Return Values ---")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


result = add(3, 5)
print(f"add(3, 5) = {result}")
print(f"multiply(4, 7) = {multiply(4, 7)}")

# You can use returned values directly in expressions
total = add(10, 20) + multiply(3, 4)
print(f"add(10, 20) + multiply(3, 4) = {total}")


# Functions without a return statement return None
def say_hi():
    """Just prints — doesn't return anything."""
    print("Hi!")


result = say_hi()
print(f"say_hi() returned: {result}")   # None
print()

# -----------------------------------------------------------------------------
# 4. Default parameter values
# -----------------------------------------------------------------------------

print("--- 4. Default Parameters ---")


def power(base, exponent=2):
    """Raise base to the given exponent. Defaults to squaring."""
    return base ** exponent


print(f"power(5) = {power(5)}")         # 25 (exponent defaults to 2)
print(f"power(5, 3) = {power(5, 3)}")   # 125
print(f"power(2, 10) = {power(2, 10)}") # 1024


def make_greeting(name, greeting="Hello", punctuation="!"):
    """Build a greeting string with customizable parts."""
    return f"{greeting}, {name}{punctuation}"


print(make_greeting("Alice"))                          # Hello, Alice!
print(make_greeting("Bob", greeting="Hey"))            # Hey, Bob!
print(make_greeting("Charlie", punctuation="..."))     # Hello, Charlie...
print(make_greeting("Diana", "Howdy", "!!"))           # Howdy, Diana!!
print()

# -----------------------------------------------------------------------------
# 5. Keyword arguments vs positional arguments
# -----------------------------------------------------------------------------

print("--- 5. Keyword vs Positional Arguments ---")


def describe_pet(name, animal, age):
    """Describe a pet with their details."""
    print(f"  {name} is a {animal}, age {age}")


# Positional — order matters
print("Positional:")
describe_pet("Buddy", "dog", 5)

# Keyword — order doesn't matter
print("Keyword:")
describe_pet(animal="cat", age=3, name="Whiskers")

# Mix — positional first, then keyword
print("Mixed:")
describe_pet("Goldie", animal="fish", age=2)
print()

# -----------------------------------------------------------------------------
# 6. *args — variable positional arguments
# -----------------------------------------------------------------------------

print("--- 6. *args ---")


def total(*numbers):
    """Sum up any number of values."""
    print(f"  Received: {numbers} (type: {type(numbers).__name__})")
    return sum(numbers)


print(f"total(1, 2, 3) = {total(1, 2, 3)}")
print(f"total(10, 20, 30, 40) = {total(10, 20, 30, 40)}")
print(f"total(5) = {total(5)}")
print(f"total() = {total()}")


# Practical example: a flexible average function
def average(*values):
    """Calculate the average of any number of values."""
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)


print(f"average(90, 85, 92, 88) = {average(90, 85, 92, 88)}")
print()

# -----------------------------------------------------------------------------
# 7. **kwargs — variable keyword arguments
# -----------------------------------------------------------------------------

print("--- 7. **kwargs ---")


def build_profile(**info):
    """Print key-value pairs from keyword arguments."""
    print(f"  Received: {info} (type: {type(info).__name__})")
    for key, value in info.items():
        print(f"    {key}: {value}")


build_profile(name="Alice", age=30, city="Seattle")
print()
build_profile(language="Python", level="beginner", goal="web development")
print()

# -----------------------------------------------------------------------------
# 8. Combining everything in one function signature
# -----------------------------------------------------------------------------

print("--- 8. Combined Signature ---")


def flexible(required, *args, option="default", **kwargs):
    """Show how all parameter types work together."""
    print(f"  required: {required}")
    print(f"  args:     {args}")
    print(f"  option:   {option}")
    print(f"  kwargs:   {kwargs}")


flexible("hello", 1, 2, 3, option="custom", color="blue", size=10)
print()

# -----------------------------------------------------------------------------
# 9. Docstrings
# -----------------------------------------------------------------------------

print("--- 9. Docstrings ---")


def area_of_circle(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle.

    Returns:
        The area as a float.
    """
    return math.pi * radius ** 2


# You can access the docstring programmatically
print(f"area_of_circle(5) = {area_of_circle(5):.2f}")
print(f"Docstring: {area_of_circle.__doc__.strip().splitlines()[0]}")
print()

# -----------------------------------------------------------------------------
# 10. Scope — local vs global variables
# -----------------------------------------------------------------------------

print("--- 10. Scope ---")

# This is a global variable
global_message = "I'm global!"


def scope_demo():
    """Demonstrate local vs global scope."""
    local_message = "I'm local!"       # Only exists inside this function
    print(f"  Inside function — global: {global_message}")
    print(f"  Inside function — local:  {local_message}")


scope_demo()
print(f"  Outside function — global: {global_message}")
# print(local_message)  # This would cause a NameError!


# Shadowing — a local variable can have the same name as a global one
color = "blue"


def change_color():
    """The local 'color' shadows the global one — doesn't change it."""
    color = "red"               # This creates a NEW local variable
    print(f"  Inside function: color = {color}")


change_color()
print(f"  Outside function: color = {color}")  # Still "blue"!
print()

# -----------------------------------------------------------------------------
# 11. Functions as first-class objects
# -----------------------------------------------------------------------------

print("--- 11. Functions as First-Class Objects ---")


def shout(text):
    """Convert text to uppercase with an exclamation mark."""
    return text.upper() + "!"


def whisper(text):
    """Convert text to lowercase with ellipsis."""
    return text.lower() + "..."


def apply(func, message):
    """Apply a function to a message and return the result."""
    return func(message)


print(f"apply(shout, 'hello') = {apply(shout, 'hello')}")
print(f"apply(whisper, 'HELLO') = {apply(whisper, 'HELLO')}")

# Store functions in a list and loop through them
formatters = [shout, whisper, str.title, str.swapcase]
for func in formatters:
    print(f"  {func.__name__}('Hello World') = {func('Hello World')}")
print()

# -----------------------------------------------------------------------------
# 12. Type hints
# -----------------------------------------------------------------------------

print("--- 12. Type Hints ---")


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate Body Mass Index."""
    return weight_kg / (height_m ** 2)


def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0


def repeat_string(text: str, times: int = 2) -> str:
    """Repeat a string a given number of times."""
    return text * times


bmi = calculate_bmi(70.0, 1.75)
print(f"BMI for 70kg, 1.75m: {bmi:.1f}")
print(f"is_even(4) = {is_even(4)}")
print(f"is_even(7) = {is_even(7)}")
print(f"repeat_string('ha', 3) = {repeat_string('ha', 3)}")
print()

# -----------------------------------------------------------------------------
# 13. Putting it all together — a practical example
# -----------------------------------------------------------------------------

print("--- 13. Practical Example: Grade Calculator ---")


def letter_grade(score: float) -> str:
    """Convert a numerical score (0-100) to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def class_summary(*scores: float) -> None:
    """Print a summary of class scores with grades."""
    if not scores:
        print("  No scores provided.")
        return

    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print(f"  Students:  {len(scores)}")
    print(f"  Average:   {avg:.1f} ({letter_grade(avg)})")
    print(f"  Highest:   {highest:.0f} ({letter_grade(highest)})")
    print(f"  Lowest:    {lowest:.0f} ({letter_grade(lowest)})")
    print()

    # Print each student's grade
    for i, score in enumerate(scores, 1):
        print(f"  Student {i}: {score:6.1f} -> {letter_grade(score)}")


class_summary(92, 85, 78, 95, 61, 88, 73, 99)
print()

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print("=" * 40)
print("  FUNCTIONS COMPLETE!")
print("=" * 40)
