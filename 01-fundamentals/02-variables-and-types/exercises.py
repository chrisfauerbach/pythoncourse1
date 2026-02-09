"""
Variables and Types — Exercises
================================

Practice problems to test your understanding of variables and types.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Temperature converter
#
# Create a variable `temp_fahrenheit` set to 98.6
# Convert it to Celsius using the formula: C = (F - 32) * 5/9
# Store the result in `temp_celsius`
# Print both values like:
#   98.6°F is 37.0°C
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Type detective
#
# For each of the following values, print the value AND its type.
# Values: 42, 3.14, "hello", True, None
#
# Expected output format:
#   42 is a <class 'int'>
#   3.14 is a <class 'float'>
#   hello is a <class 'str'>
#   True is a <class 'bool'>
#   None is a <class 'NoneType'>
#
# Hint: Use type() to get the type
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Swap challenge
#
# Given three variables a=1, b=2, c=3, rotate their values so that:
#   a=2, b=3, c=1
#
# Do this in a SINGLE line using multiple assignment.
# Print the values before and after.
#
# =============================================================================

def exercise_3():
    a, b, c = 1, 2, 3
    print(f"Before: a={a}, b={b}, c={c}")
    # YOUR CODE HERE — rotate the values in one line
    print(f"After:  a={a}, b={b}, c={c}")


# =============================================================================
# Exercise 4: String to number math
#
# You have these two strings representing prices:
#   price1 = "24.99"
#   price2 = "13.50"
#
# Convert them to floats, add them together, and print:
#   Total: $38.49
#
# Bonus: also calculate and print a 20% tip on the total
# =============================================================================

def exercise_4():
    price1 = "24.99"
    price2 = "13.50"
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Integer division and remainder
#
# You have 157 minutes. Using // and %, calculate:
#   - How many full hours is that?
#   - How many minutes are left over?
#
# Print it like:
#   157 minutes = 2 hours and 37 minutes
#
# =============================================================================

def exercise_5():
    total_minutes = 157
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Truthy and falsy
#
# Without running the code first, predict what bool() returns for each value.
# Then uncomment the print statements to check your predictions.
#
# Values: 0, 1, -1, "", "False", 0.0, None, 42
# =============================================================================

def exercise_6():
    values = [0, 1, -1, "", "False", 0.0, None, 42]
    # Uncomment the lines below to check your predictions:
    # for val in values:
    #     print(f"bool({val!r:>10}) = {bool(val)}")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    temp_fahrenheit = 98.6
    temp_celsius = (temp_fahrenheit - 32) * 5 / 9
    print(f"{temp_fahrenheit}\u00b0F is {temp_celsius:.1f}\u00b0C")


def solution_2():
    values = [42, 3.14, "hello", True, None]
    for val in values:
        print(f"{val} is a {type(val)}")


def solution_3():
    a, b, c = 1, 2, 3
    print(f"Before: a={a}, b={b}, c={c}")
    a, b, c = b, c, a
    print(f"After:  a={a}, b={b}, c={c}")


def solution_4():
    price1 = "24.99"
    price2 = "13.50"
    total = float(price1) + float(price2)
    print(f"Total: ${total:.2f}")
    tip = total * 0.20
    print(f"Tip (20%): ${tip:.2f}")


def solution_5():
    total_minutes = 157
    hours = total_minutes // 60
    remaining = total_minutes % 60
    print(f"{total_minutes} minutes = {hours} hours and {remaining} minutes")


def solution_6():
    values = [0, 1, -1, "", "False", 0.0, None, 42]
    for val in values:
        print(f"bool({val!r:>10}) = {bool(val)}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Temperature converter", exercise_1),
        ("Type detective", exercise_2),
        ("Swap challenge", exercise_3),
        ("String to number math", exercise_4),
        ("Integer division and remainder", exercise_5),
        ("Truthy and falsy", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
