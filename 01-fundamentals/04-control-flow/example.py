"""
Control Flow — Example Code
==============================

Run this file:
    python3 example.py

This file demonstrates how to make decisions in Python using if/elif/else,
comparison and logical operators, ternary expressions, and match/case.
"""

# -----------------------------------------------------------------------------
# 1. Basic if statement — checking a single condition
# -----------------------------------------------------------------------------

print("--- Basic if Statement ---")

temperature = 35

# The colon and indentation are required!
if temperature > 30:
    print(f"{temperature} degrees — It's hot outside!")

# If the condition is False, the block is simply skipped
if temperature < 0:
    print("It's freezing!")   # This won't print because 35 is not < 0

print()

# -----------------------------------------------------------------------------
# 2. Comparison operators — building conditions
# -----------------------------------------------------------------------------

print("--- Comparison Operators ---")

x = 10

print(f"x = {x}")
print(f"x == 10: {x == 10}")    # True  — equal to
print(f"x != 5:  {x != 5}")     # True  — not equal to
print(f"x > 5:   {x > 5}")      # True  — greater than
print(f"x < 20:  {x < 20}")     # True  — less than
print(f"x >= 10: {x >= 10}")    # True  — greater than or equal to
print(f"x <= 9:  {x <= 9}")     # False — less than or equal to
print()

# -----------------------------------------------------------------------------
# 3. if / elif / else — multiple branches
# -----------------------------------------------------------------------------

print("--- if / elif / else ---")

score = 85

# Python checks top to bottom. The FIRST True condition wins.
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"       # This one matches! Everything below is skipped.
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"       # Catch-all: only runs if nothing above matched

print(f"Score: {score} -> Grade: {grade}")
print()

# -----------------------------------------------------------------------------
# 4. Logical operators — combining conditions
# -----------------------------------------------------------------------------

print("--- Logical Operators ---")

age = 25
has_id = True
is_vip = False

# and — both conditions must be True
if age >= 21 and has_id:
    print("You can enter the bar")

# or — at least one condition must be True
if is_vip or age >= 21:
    print("You get in either way")

# not — flips True to False (and vice versa)
is_banned = False
if not is_banned:
    print("You're not on the ban list — welcome!")

# Combining multiple operators
if age >= 18 and has_id and not is_banned:
    print("All checks passed!")

# Storing conditions in variables for readability
is_adult = age >= 18
has_access = has_id and not is_banned
if is_adult and has_access:
    print("Clean and readable condition check!")

print()

# -----------------------------------------------------------------------------
# 5. Truthy and falsy values in conditions
# -----------------------------------------------------------------------------

print("--- Truthy and Falsy Values ---")

# These are all "falsy" — they act like False in a condition
falsy_values = [False, 0, 0.0, "", None]

for val in falsy_values:
    if not val:
        print(f"  {val!r:>10} is falsy")

print()

# Practical use: checking if a string has content
username = "Alice"
if username:
    print(f"Hello, {username}!")   # Runs because "Alice" is truthy

empty_name = ""
if not empty_name:
    print("No name provided!")     # Runs because "" is falsy

print()

# -----------------------------------------------------------------------------
# 6. Nested if statements
# -----------------------------------------------------------------------------

print("--- Nested if Statements ---")

has_ticket = True
age = 15

# You can nest ifs, but don't go too deep!
if has_ticket:
    if age >= 18:
        print("Welcome to the R-rated movie!")
    elif age >= 13:
        print("Welcome to the PG-13 movie!")
    else:
        print("Sorry, kid — G-rated movies only")
else:
    print("You need a ticket first!")

# The same logic flattened with and (often cleaner)
print("\nSame logic, flattened:")
if has_ticket and age >= 18:
    print("Welcome to the R-rated movie!")
elif has_ticket and age >= 13:
    print("Welcome to the PG-13 movie!")
elif has_ticket:
    print("Sorry, kid — G-rated movies only")
else:
    print("You need a ticket first!")

print()

# -----------------------------------------------------------------------------
# 7. Ternary expressions (conditional expressions)
# -----------------------------------------------------------------------------

print("--- Ternary Expressions ---")

age = 20

# The one-liner: value_if_true if condition else value_if_false
status = "adult" if age >= 18 else "minor"
print(f"Age {age} -> {status}")

# Great for quick assignments
temperature = 15
outfit = "t-shirt" if temperature > 25 else "jacket"
print(f"{temperature} degrees -> Wear a {outfit}")

# Works in print() too
number = 7
print(f"{number} is {'even' if number % 2 == 0 else 'odd'}")

# But don't chain them — use regular if/elif for complex logic
# Bad:  result = "A" if score >= 90 else "B" if score >= 80 else "C"
# Good: use if/elif/else (like section 3 above)

print()

# -----------------------------------------------------------------------------
# 8. match/case — structural pattern matching (Python 3.10+)
# -----------------------------------------------------------------------------

print("--- match/case (Python 3.10+) ---")

# Simple value matching — like a clean if/elif chain
command = "greet"

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "greet":
        print("Hello there!")
    case _:
        print(f"Unknown command: {command}")

# Matching with the OR pattern using |
day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday")
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend day!")
    case _:
        print(f"{day} is not a valid day")

# Matching with a guard clause (if condition)
status_code = 404

match status_code:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 404:
        print("Not Found")
    case code if code >= 500:
        print(f"Server Error ({code})")
    case _:
        print(f"Other status: {status_code}")

print()

# -----------------------------------------------------------------------------
# 9. Common pitfalls — things to watch out for
# -----------------------------------------------------------------------------

print("--- Common Pitfalls ---")

# Pitfall 1: = vs ==
x = 10
# if x = 10:      # SyntaxError! Use == for comparison
if x == 10:
    print("Pitfall 1: Use == for comparison, not =")

# Pitfall 2: The or trap
color = "green"
# WRONG: if color == "red" or "blue":    # "blue" is always truthy!
# RIGHT:
if color == "red" or color == "blue":
    print("Primary color")
else:
    print(f"Pitfall 2: '{color}' is not red or blue")

# EVEN BETTER — use 'in' with a tuple:
if color in ("red", "blue", "green"):
    print(f"Pitfall 2 (better): '{color}' is in the list!")

# Pitfall 3: Comparing with None — use 'is', not '=='
result = None
if result is None:
    print("Pitfall 3: Use 'is None' instead of '== None'")

print()

# -----------------------------------------------------------------------------
# 10. Putting it all together — a mini program
# -----------------------------------------------------------------------------

print("--- Putting It All Together ---")
print()

# A simple ticket pricing system
age = 25
is_student = True
day = "Tuesday"

print(f"Customer: age={age}, student={is_student}, day={day}")

# Determine base price
if age < 5:
    price = 0
    category = "Free (under 5)"
elif age < 13:
    price = 8
    category = "Child"
elif age >= 65:
    price = 10
    category = "Senior"
else:
    price = 15
    category = "Adult"

# Apply discounts
discount_reason = ""
if is_student and age >= 13:
    price *= 0.8    # 20% student discount
    discount_reason = "student discount"
if day == "Tuesday":
    price *= 0.5    # Half-price Tuesdays!
    discount_reason += (" + " if discount_reason else "") + "Tuesdays half-price"

print(f"Category: {category}")
print(f"Final price: ${price:.2f}")
if discount_reason:
    print(f"Discounts applied: {discount_reason}")

print()

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print("=" * 40)
print("  CONTROL FLOW COMPLETE!")
print("=" * 40)
