"""
Standard Input and Output — Example Code
==========================================

Run this file:
    python3 example.py

This file demonstrates input(), f-strings, format specifiers, stderr,
and all the different ways to get data in and display data out.

NOTE: Since input() is interactive and blocks the program waiting for
keyboard input, the input() examples in this file use HARDCODED values
to simulate what the user would type. Comments show what the real
interactive version would look like.
"""

# -----------------------------------------------------------------------------
# 1. The input() function — getting text from the user
# -----------------------------------------------------------------------------

# In a real program, you'd use:
#   name = input("What's your name? ")
# But we'll hardcode it so this file runs without waiting for input:

name = "Alice"   # Simulates the user typing "Alice"
print(f"What's your name? {name}")
print(f"Hello, {name}! Welcome to Python.")
print()

# -----------------------------------------------------------------------------
# 2. input() always returns a string — you must convert!
# -----------------------------------------------------------------------------

# In a real program:  age = input("How old are you? ")
age_str = "25"   # Simulates user typing "25"
print(f"How old are you? {age_str}")

# age_str is a STRING, not a number:
print(f"  type(age_str) = {type(age_str).__name__}")   # str

# Convert to int to do math:
age = int(age_str)
print(f"  type(age) = {type(age).__name__}")            # int
print(f"  Next year you'll be {age + 1}")
print()

# The one-liner pattern — wrap input() in int() or float():
# In a real program:  birth_year = int(input("Birth year: "))
birth_year = 1999
print(f"Birth year: {birth_year}")
current_year = 2026
print(f"  You are (or will be) {current_year - birth_year} this year")
print()

# Float conversion works the same way:
# In a real program:  price = float(input("Enter price: "))
price = 19.99
print(f"Enter price: {price}")
tax_rate = 0.08
total = price * (1 + tax_rate)
print(f"  With {tax_rate:.0%} tax: ${total:.2f}")
print()

# -----------------------------------------------------------------------------
# 3. f-strings — the best way to format output
# -----------------------------------------------------------------------------

print("--- f-strings Basics ---")

first_name = "Bob"
age = 42
print(f"My name is {first_name} and I'm {age} years old.")

# You can put ANY expression inside the braces
x = 7
print(f"{x} times {x} is {x * x}")
print(f"{x} divided by 3 is {x / 3}")
print(f"Is {x} even? {x % 2 == 0}")
print()

# Calling methods inside f-strings
greeting = "hello world"
print(f"Original:    {greeting}")
print(f"Upper:       {greeting.upper()}")
print(f"Title case:  {greeting.title()}")
print()

# -----------------------------------------------------------------------------
# 4. f-string format specifiers — the good stuff
# -----------------------------------------------------------------------------

print("--- Format Specifiers ---")

# Decimal places with .Nf
pi = 3.14159265358979
print(f"Pi (default):    {pi}")
print(f"Pi (2 decimals): {pi:.2f}")
print(f"Pi (4 decimals): {pi:.4f}")
print(f"Pi (0 decimals): {pi:.0f}")
print()

# Width and alignment
print("--- Alignment ---")
print(f"{'Left':<15}|")      # Left-aligned in 15 chars
print(f"{'Center':^15}|")    # Centered in 15 chars
print(f"{'Right':>15}|")     # Right-aligned in 15 chars
print()

# Practical example: a formatted table
print("--- Formatted Table ---")
print(f"{'Item':<20} {'Qty':>5} {'Price':>10}")
print(f"{'-' * 20} {'-' * 5} {'-' * 10}")
print(f"{'Widget':<20} {3:>5} {'$9.99':>10}")
print(f"{'Gizmo':<20} {12:>5} {'$24.50':>10}")
print(f"{'Thingamajig':<20} {1:>5} {'$199.00':>10}")
print()

# Number formatting
print("--- Number Formatting ---")
big = 1234567890
print(f"Plain:       {big}")
print(f"With commas: {big:,}")
print(f"Underscores: {big:_}")
print()

# Percentages
hit_rate = 0.8567
print(f"Hit rate: {hit_rate:.1%}")     # 85.7%
print(f"Hit rate: {hit_rate:.2%}")     # 85.67%
print()

# Combining width + decimal places — great for receipts
print("--- Combined Formatting ---")
items = [("Coffee", 4.50), ("Muffin", 3.25), ("Orange Juice", 5.00)]
print(f"{'Item':<20} {'Price':>8}")
print("-" * 30)
for item_name, item_price in items:
    print(f"{item_name:<20} ${item_price:>7.2f}")
total = sum(p for _, p in items)
print("-" * 30)
print(f"{'Total':<20} ${total:>7.2f}")
print()

# -----------------------------------------------------------------------------
# 5. Printing to stderr
# -----------------------------------------------------------------------------

import sys

print("--- stderr ---")
print("This is a normal message (stdout)")
print("WARNING: This is an error message (stderr)", file=sys.stderr)
print("Back to normal output (stdout)")
print()

# Why does this matter? Try running this in a terminal:
#   python3 example.py > output.txt
# The normal messages go into output.txt, but the error message
# still shows up on your screen. That's the whole point of stderr.

# -----------------------------------------------------------------------------
# 6. String concatenation vs f-strings
# -----------------------------------------------------------------------------

print("--- Concatenation vs f-strings ---")

city = "Portland"
temp = 72.6

# The old way — concatenation (clunky)
message_old = "It's " + str(temp) + " degrees in " + city + " today."
print("Concat:  ", message_old)

# The new way — f-string (clean!)
message_new = f"It's {temp} degrees in {city} today."
print("f-string:", message_new)

# Same output, but the f-string version is way easier to read and write.
# No str() conversion, no fiddly + operators, no missing spaces.
print()

# You can even do formatting inline:
print(f"Temperature: {temp:.1f}F")     # Can't do this with concatenation!
print()

# -----------------------------------------------------------------------------
# 7. Multi-line output with f-strings
# -----------------------------------------------------------------------------

print("--- Multi-line Output ---")

student = "Alice"
score = 95
grade = "A" if score >= 90 else "B" if score >= 80 else "C"

# Triple-quoted f-strings — super handy for blocks of text
report = f"""
=============================
  REPORT CARD
=============================
  Student:  {student}
  Score:    {score}/100
  Grade:    {grade}
  Status:   {'Passing' if score >= 60 else 'Failing'}
=============================
"""
print(report)

# You can also build strings across multiple lines with regular f-strings
line1 = f"Name: {student}"
line2 = f"Score: {score}%"
line3 = f"Grade: {grade}"
print(line1)
print(line2)
print(line3)
print()

# -----------------------------------------------------------------------------
# 8. A few more handy f-string tricks
# -----------------------------------------------------------------------------

print("--- Bonus Tricks ---")

# Debugging shortcut: add = after the variable name (Python 3.8+)
x = 42
y = "hello"
print(f"{x = }")      # x = 42
print(f"{y = }")      # y = 'hello'
print()

# Padding numbers with zeros
for i in range(1, 6):
    print(f"File_{i:03d}.txt")    # File_001.txt, File_002.txt, etc.
print()

# Repr vs str in f-strings
text = "hello\tworld"
print(f"str:  {text}")       # hello   world (tab is rendered)
print(f"repr: {text!r}")     # 'hello\tworld' (shows the escape character)
print()

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print("=" * 40)
print("  STDIN & STDOUT COMPLETE!")
print("=" * 40)
