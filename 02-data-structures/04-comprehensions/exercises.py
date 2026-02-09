"""
Comprehensions — Exercises
===========================

Practice problems to test your understanding of comprehensions.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Squares of even numbers
#
# Using a single list comprehension, create a list of the squares of all
# EVEN numbers from 1 to 20 (inclusive).
#
# Expected result:
#   [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
#
# Hint: You need both a filter (if) and a transformation (** 2)
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Flatten a matrix
#
# Given this matrix (list of lists), use a nested comprehension to flatten
# it into a single list.
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#
# Expected result:
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#
# Hint: You need two 'for' clauses — outer for rows, inner for items
# =============================================================================

def exercise_2():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Word lengths dictionary
#
# Given this sentence, create a dictionary that maps each UNIQUE word
# (lowercased) to its length.
#
# sentence = "the quick brown fox jumps over the lazy fox"
#
# Expected result (order may vary):
#   {'the': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumps': 5,
#    'over': 4, 'lazy': 4}
#
# Hint: Use .split() to get words, then a dict comprehension.
#       Duplicate words will naturally be handled — the last one wins.
# =============================================================================

def exercise_3():
    sentence = "the quick brown fox jumps over the lazy fox"
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Unique vowels
#
# Given a string, use a set comprehension to extract all unique vowels
# that appear in it (lowercase only).
#
# text = "Comprehensions Are Absolutely Awesome"
#
# Expected result (order may vary):
#   {'o', 'e', 'i', 'a', 'u'}
#
# Hint: Convert the text to lowercase first, then check each character
#       against a string of vowels like "aeiou"
# =============================================================================

def exercise_4():
    text = "Comprehensions Are Absolutely Awesome"
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Invert a dictionary
#
# Given a dictionary mapping country codes to country names, use a dict
# comprehension to create the inverse mapping (name -> code).
#
# codes = {"US": "United States", "GB": "United Kingdom",
#          "FR": "France", "DE": "Germany", "JP": "Japan"}
#
# Expected result:
#   {"United States": "US", "United Kingdom": "GB", "France": "FR",
#    "Germany": "DE", "Japan": "JP"}
#
# Hint: Use .items() and swap the key and value
# =============================================================================

def exercise_5():
    codes = {"US": "United States", "GB": "United Kingdom",
             "FR": "France", "DE": "Germany", "JP": "Japan"}
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: FizzBuzz comprehension (the ultimate challenge!)
#
# Create a list for numbers 1 through 20 where:
#   - If the number is divisible by both 3 and 5, use "FizzBuzz"
#   - If the number is divisible by 3 only, use "Fizz"
#   - If the number is divisible by 5 only, use "Buzz"
#   - Otherwise, use the number itself (as a string)
#
# Do it in a SINGLE list comprehension.
#
# Expected result:
#   ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz',
#    '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz']
#
# Hint: You can chain if/else expressions:
#       a if cond1 else b if cond2 else c if cond3 else d
#       Check divisible-by-15 FIRST (before 3 or 5 individually)
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    result = [n ** 2 for n in range(1, 21) if n % 2 == 0]
    print(f"   {result}")


def solution_2():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    flat = [num for row in matrix for num in row]
    print(f"   {flat}")


def solution_3():
    sentence = "the quick brown fox jumps over the lazy fox"
    word_lengths = {word: len(word) for word in sentence.split()}
    print(f"   {word_lengths}")


def solution_4():
    text = "Comprehensions Are Absolutely Awesome"
    vowels = {ch for ch in text.lower() if ch in "aeiou"}
    print(f"   {vowels}")


def solution_5():
    codes = {"US": "United States", "GB": "United Kingdom",
             "FR": "France", "DE": "Germany", "JP": "Japan"}
    inverted = {name: code for code, name in codes.items()}
    print(f"   {inverted}")


def solution_6():
    fizzbuzz = [
        "FizzBuzz" if n % 15 == 0
        else "Fizz" if n % 3 == 0
        else "Buzz" if n % 5 == 0
        else str(n)
        for n in range(1, 21)
    ]
    print(f"   {fizzbuzz}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Squares of even numbers", exercise_1),
        ("Flatten a matrix", exercise_2),
        ("Word lengths dictionary", exercise_3),
        ("Unique vowels", exercise_4),
        ("Invert a dictionary", exercise_5),
        ("FizzBuzz comprehension", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
