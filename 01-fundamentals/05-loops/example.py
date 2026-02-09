"""
Loops — Example Code
======================

Run this file:
    python3 example.py

This file demonstrates for loops, while loops, range(), break, continue,
loop else clauses, nested loops, enumerate(), and zip().
"""

# -----------------------------------------------------------------------------
# 1. For loops — iterating over sequences
# -----------------------------------------------------------------------------

print("--- For Loops ---")

# Looping over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  I like {fruit}")

print()

# Looping over a string — one character at a time
word = "Python"
print(f"Letters in '{word}':")
for char in word:
    print(f"  {char}")

print()

# Looping over a tuple
print("Primary colors:")
for color in ("red", "green", "blue"):
    print(f"  {color}")

print()

# -----------------------------------------------------------------------------
# 2. The range() function
# -----------------------------------------------------------------------------

print("--- range() Function ---")

# range(n) — generates 0, 1, 2, ..., n-1
print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()  # New line

# range(start, stop) — generates start, start+1, ..., stop-1
print("range(2, 7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step) — count by step
print("range(0, 20, 3):", end=" ")
for i in range(0, 20, 3):
    print(i, end=" ")
print()

# Counting backwards with a negative step
print("range(5, 0, -1):", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

print()

# -----------------------------------------------------------------------------
# 3. While loops — repeat while a condition is true
# -----------------------------------------------------------------------------

print("--- While Loops ---")

# A simple countdown
count = 5
while count > 0:
    print(f"  {count}...")
    count -= 1
print("  Liftoff!")

print()

# Using while when you don't know the number of iterations
# Find the first power of 2 greater than 1000
power = 1
while power <= 1000:
    power *= 2
print(f"First power of 2 above 1000: {power}")

print()

# -----------------------------------------------------------------------------
# 4. Break — exit a loop early
# -----------------------------------------------------------------------------

print("--- Break ---")

# Stop searching once we find what we want
numbers = [4, 7, 2, 9, 1, 5, 8]
target = 9
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"  Checking {num}... not it")

print()

# Break in a while loop
print("While loop with break:")
total = 0
while True:    # This would loop forever without the break!
    total += 1
    if total >= 5:
        print(f"  Reached {total}, breaking out!")
        break

print()

# -----------------------------------------------------------------------------
# 5. Continue — skip to the next iteration
# -----------------------------------------------------------------------------

print("--- Continue ---")

# Print only odd numbers
print("Odd numbers from 1-10:", end=" ")
for i in range(1, 11):
    if i % 2 == 0:    # Even number? Skip it
        continue
    print(i, end=" ")
print()

# Skip blank strings in a list
items = ["hello", "", "world", "", "python"]
print("Non-empty items:")
for item in items:
    if item == "":
        continue
    print(f"  {item}")

print()

# -----------------------------------------------------------------------------
# 6. Else clause on loops — runs if no break happened
# -----------------------------------------------------------------------------

print("--- Loop Else Clause ---")

# Searching for an item — else means "not found"
print("Looking for an even number in [1, 3, 5, 7]:")
for num in [1, 3, 5, 7]:
    if num % 2 == 0:
        print(f"  Found even number: {num}")
        break
else:
    print("  No even numbers found!")   # This runs — no break happened

print()

# Now with a list that DOES have an even number
print("Looking for an even number in [1, 3, 4, 7]:")
for num in [1, 3, 4, 7]:
    if num % 2 == 0:
        print(f"  Found even number: {num}")
        break
else:
    print("  No even numbers found!")   # This does NOT run — break happened

print()

# while/else works the same way
print("While/else example:")
attempts = 0
while attempts < 3:
    attempts += 1
    print(f"  Attempt {attempts}")
else:
    print("  All attempts completed (no break)")

print()

# -----------------------------------------------------------------------------
# 7. Nested loops
# -----------------------------------------------------------------------------

print("--- Nested Loops ---")

# A coordinate grid
print("3x3 grid:")
for row in range(3):
    for col in range(3):
        print(f"  ({row},{col})", end="")
    print()    # New line after each row

print()

# Multiplication table (3x3)
print("Mini multiplication table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}x{j}={i*j}", end="")
    print()

print()

# -----------------------------------------------------------------------------
# 8. enumerate() — getting index and value
# -----------------------------------------------------------------------------

print("--- enumerate() ---")

# Without enumerate (the manual way — don't do this)
print("The manual way (avoid this):")
colors = ["red", "green", "blue", "yellow"]
index = 0
for color in colors:
    print(f"  {index}: {color}")
    index += 1

print()

# With enumerate (the Python way!)
print("With enumerate (much better):")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

print()

# Starting from 1 instead of 0
print("Starting from 1:")
for rank, color in enumerate(colors, start=1):
    print(f"  #{rank}: {color}")

print()

# -----------------------------------------------------------------------------
# 9. zip() — iterating over multiple sequences in parallel
# -----------------------------------------------------------------------------

print("--- zip() ---")

names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
cities = ["NYC", "London", "Tokyo"]

# Zip two lists
print("Names and ages:")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")

print()

# Zip three lists
print("Names, ages, and cities:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, age {age}, lives in {city}")

print()

# Zip with different lengths — stops at the shortest
print("Different lengths (stops at shortest):")
letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3]
for letter, number in zip(letters, numbers):
    print(f"  {letter} -> {number}")

print()

# -----------------------------------------------------------------------------
# 10. Common pitfalls
# -----------------------------------------------------------------------------

print("--- Common Pitfalls ---")

# Off-by-one with range
print("Want 1 through 5? Use range(1, 6), NOT range(1, 5):")
print("  range(1, 6):", list(range(1, 6)))    # [1, 2, 3, 4, 5]
print("  range(1, 5):", list(range(1, 5)))    # [1, 2, 3, 4] — missing 5!

print()

# Infinite loop protection — always have a way out
print("Safe while loop with a safety counter:")
safety = 0
value = 100
while value != 1 and safety < 20:
    if value % 2 == 0:
        value = value // 2
    else:
        value = value * 3 + 1
    safety += 1
    print(f"  Step {safety}: {value}")
print(f"  Finished in {safety} steps")

print()

# -----------------------------------------------------------------------------
# 11. Putting it all together — a practical example
# -----------------------------------------------------------------------------

print("--- Putting It All Together ---")
print()

# Grade report using enumerate and zip
students = ["Alice", "Bob", "Charlie", "Diana"]
midterm = [88, 72, 95, 64]
final = [92, 85, 91, 78]

print("Grade Report")
print("-" * 40)
for i, (name, mid, fin) in enumerate(zip(students, midterm, final), start=1):
    average = (mid + fin) / 2
    # Use a loop with break to determine the letter grade
    for threshold, letter in [(90, "A"), (80, "B"), (70, "C"), (60, "D")]:
        if average >= threshold:
            grade = letter
            break
    else:
        grade = "F"
    print(f"  {i}. {name}: midterm={mid}, final={fin}, avg={average:.1f}, grade={grade}")

print()

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print("=" * 40)
print("  LOOPS COMPLETE!")
print("=" * 40)
