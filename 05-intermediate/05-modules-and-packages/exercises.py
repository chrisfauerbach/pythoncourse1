"""
Modules and Packages — Exercises
=================================

Practice problems to test your understanding of modules, imports, and the
standard library. Try to solve each exercise before looking at the solutions!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Math module basics
#
# Import the math module and use it to:
#   1. Calculate the square root of 625
#   2. Calculate 2 raised to the power of 10 (use math.pow)
#   3. Calculate the factorial of 7 (use math.factorial)
#
# Print each result with a label, like:
#   sqrt(625)    = 25.0
#   2^10         = 1024.0
#   7!           = 5040
#
# Hint: Use "from math import ..." to import just what you need.
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Dice roller
#
# Use the random module to simulate rolling two six-sided dice 10 times.
# For each roll, print the two dice values and their sum, like:
#   Roll 1: [3, 5] -> sum = 8
#   Roll 2: [1, 6] -> sum = 7
#   ...
#
# After all 10 rolls, print how many times the sum was 7 or higher.
#
# Hint: random.randint(1, 6) gives a random number from 1 to 6.
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Module explorer
#
# Pick the 'os.path' module and do the following:
#   1. Import it
#   2. Use dir() to get all public names (filter out ones starting with '_')
#   3. Print how many public functions/attributes it has
#   4. Print the first 10 public names sorted alphabetically
#   5. Use os.path.join to build a path: home -> documents -> notes.txt
#   6. Use os.path.splitext to split "report.final.pdf" into name and extension
#
# Expected output (something like):
#   os.path has 22 public names
#   First 10: ['abspath', 'basename', 'commonpath', ...]
#   Joined path: home/documents/notes.txt
#   splitext('report.final.pdf') = ('report.final', '.pdf')
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: The __name__ guard
#
# Write a function called `is_leap_year(year)` that returns True if a year is
# a leap year, False otherwise.
#
# Leap year rules:
#   - Divisible by 4 -> leap year
#   - UNLESS divisible by 100 -> NOT a leap year
#   - UNLESS divisible by 400 -> leap year
#
# Then write an if __name__ == "__main__" style test by printing results
# for these years: 2000, 1900, 2024, 2023
#
# Expected output:
#   2000: True  (divisible by 400)
#   1900: False (divisible by 100 but not 400)
#   2024: True  (divisible by 4)
#   2023: False (not divisible by 4)
#
# Note: Since this exercise runs inside a function, you can't literally use
# if __name__ == "__main__" here — just print the test results directly.
# The point is to practice writing a reusable function with test output.
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define is_leap_year() inside this function, then test it
    pass


# =============================================================================
# Exercise 5: Word frequency with collections.Counter
#
# Use collections.Counter to find the 5 most common words in this text:
#
#   text = "the quick brown fox jumps over the lazy dog the fox the dog
#           the quick fox jumps high over the brown lazy dog and the fox"
#
# Steps:
#   1. Split the text into a list of words (use .split())
#   2. Create a Counter from the word list
#   3. Print the total number of unique words
#   4. Print the 5 most common words and their counts using .most_common(5)
#   5. Print how many times "fox" appears
#
# Expected output (something like):
#   Unique words: 11
#   Top 5 words: [('the', 7), ('fox', 4), ('dog', 3), ...]
#   'fox' appears 4 times
#
# =============================================================================

def exercise_5():
    text = ("the quick brown fox jumps over the lazy dog the fox the dog "
            "the quick fox jumps high over the brown lazy dog and the fox")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Multi-module mini project
#
# Combine pathlib, json, and datetime to build a small "activity log" system:
#
#   1. Create a list of 3 log entries, each a dictionary with:
#      - "timestamp": current time as an ISO format string
#                     (use datetime.datetime.now().isoformat())
#      - "action": a string like "login", "upload", "logout"
#      - "user": a username string
#
#   2. Convert the list to a formatted JSON string (indent=2)
#
#   3. Use pathlib to create a Path object for "/tmp/activity_log.json"
#
#   4. Write the JSON string to that file using path.write_text()
#
#   5. Read it back using path.read_text() and parse it with json.loads()
#
#   6. Print each entry from the parsed data like:
#        [2025-02-09T14:30:00] user=alice action=login
#
#   7. Print the file size using path.stat().st_size
#
# This exercise shows how modules work together in real-world code!
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    from math import sqrt, pow, factorial

    print(f"  sqrt(625)    = {sqrt(625)}")
    print(f"  2^10         = {pow(2, 10)}")
    print(f"  7!           = {factorial(7)}")


def solution_2():
    import random

    lucky_count = 0
    for roll_num in range(1, 11):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        print(f"  Roll {roll_num:>2}: [{die1}, {die2}] -> sum = {total}")
        if total >= 7:
            lucky_count += 1

    print(f"  Sum was 7 or higher: {lucky_count} out of 10 rolls")


def solution_3():
    import os.path

    public_names = sorted(name for name in dir(os.path) if not name.startswith("_"))
    print(f"  os.path has {len(public_names)} public names")
    print(f"  First 10: {public_names[:10]}")

    joined = os.path.join("home", "documents", "notes.txt")
    print(f"  Joined path: {joined}")

    name, ext = os.path.splitext("report.final.pdf")
    print(f"  splitext('report.final.pdf') = ('{name}', '{ext}')")


def solution_4():
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    test_years = [
        (2000, "divisible by 400"),
        (1900, "divisible by 100 but not 400"),
        (2024, "divisible by 4"),
        (2023, "not divisible by 4"),
    ]
    for year, reason in test_years:
        result = is_leap_year(year)
        print(f"  {year}: {str(result):<5} ({reason})")


def solution_5():
    from collections import Counter

    text = ("the quick brown fox jumps over the lazy dog the fox the dog "
            "the quick fox jumps high over the brown lazy dog and the fox")

    words = text.split()
    word_counts = Counter(words)

    print(f"  Unique words: {len(word_counts)}")
    print(f"  Top 5 words:  {word_counts.most_common(5)}")
    print(f"  'fox' appears {word_counts['fox']} times")


def solution_6():
    import json
    import datetime
    from pathlib import Path

    # 1. Create log entries
    log_entries = [
        {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": "login",
            "user": "alice",
        },
        {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": "upload",
            "user": "bob",
        },
        {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": "logout",
            "user": "alice",
        },
    ]

    # 2. Convert to JSON
    json_string = json.dumps(log_entries, indent=2)

    # 3. Create a Path object
    log_path = Path("/tmp/activity_log.json")

    # 4. Write to file
    log_path.write_text(json_string)
    print(f"  Wrote log to: {log_path}")

    # 5. Read it back and parse
    raw_text = log_path.read_text()
    parsed_entries = json.loads(raw_text)

    # 6. Print each entry
    for entry in parsed_entries:
        ts = entry["timestamp"]
        print(f"  [{ts}] user={entry['user']} action={entry['action']}")

    # 7. Print file size
    file_size = log_path.stat().st_size
    print(f"  File size: {file_size} bytes")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Math module basics", exercise_1),
        ("Dice roller", exercise_2),
        ("Module explorer", exercise_3),
        ("The __name__ guard", exercise_4),
        ("Word frequency with Counter", exercise_5),
        ("Multi-module mini project", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
