"""
Loops — Exercises
==================

Practice problems to test your understanding of loops.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Sum of numbers
#
# Write a function that returns the sum of all numbers from 1 to n (inclusive).
# Use a for loop and range().
#
# Example:
#   sum_to_n(5) should return 15   (1 + 2 + 3 + 4 + 5)
#   sum_to_n(10) should return 55
#
# Hint: Start a total at 0 and add each number in range(1, n+1)
# =============================================================================

def exercise_1():
    n = 10
    # YOUR CODE HERE — calculate the sum of 1 to n, then print it
    pass


# =============================================================================
# Exercise 2: Multiplication table
#
# Print a multiplication table for numbers 1 through 5.
# Use nested for loops.
#
# Expected output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25
#
# Hint: Use f-strings with a width like f"{value:4}" for alignment
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Count vowels in a string
#
# Given a string, count how many vowels (a, e, i, o, u) it contains.
# Make it case-insensitive (count both 'A' and 'a').
# Use a for loop and continue to skip non-vowels.
#
# Example:
#   "Hello World" should have 3 vowels (e, o, o)
#
# Hint: Convert each character to lowercase before checking
# =============================================================================

def exercise_3():
    text = "Python Programming Is Awesome"
    # YOUR CODE HERE — count the vowels and print the result
    pass


# =============================================================================
# Exercise 4: First prime above N
#
# Find and print the first prime number greater than n.
# A prime number is only divisible by 1 and itself.
#
# Use a while loop to check candidates, and a for loop with else to test
# if each candidate is prime.
#
# Example:
#   n = 10 → first prime above 10 is 11
#   n = 20 → first prime above 20 is 23
#
# Hint: For each candidate, try dividing by all numbers from 2 to candidate-1.
#       If none divide evenly, it's prime. The for/else pattern is perfect here.
# =============================================================================

def exercise_4():
    n = 50
    # YOUR CODE HERE — find and print the first prime above n
    pass


# =============================================================================
# Exercise 5: Number pyramid
#
# Print a number pyramid with n rows.
# For n = 5, the output should look like:
#
#         1
#        1 2
#       1 2 3
#      1 2 3 4
#     1 2 3 4 5
#
# Hint: Each row i has (n - i) leading spaces, then numbers 1 through i
# =============================================================================

def exercise_5():
    n = 5
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Fibonacci sequence
#
# Print the first n numbers in the Fibonacci sequence.
# The Fibonacci sequence starts with 0, 1, and each following number is
# the sum of the two before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Example for n = 10:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#
# Hint: Keep track of two variables (a and b), and on each step set
#       a, b = b, a + b  (remember multiple assignment from lesson 2?)
# =============================================================================

def exercise_6():
    n = 10
    # YOUR CODE HERE — print the first n Fibonacci numbers
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    n = 10
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum of 1 to {n} = {total}")


def solution_2():
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i * j:4}", end="")
        print()


def solution_3():
    text = "Python Programming Is Awesome"
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() not in vowels:
            continue
        count += 1
    print(f"'{text}' has {count} vowels")


def solution_4():
    n = 50
    candidate = n + 1
    while True:
        # Check if candidate is prime using for/else
        for i in range(2, candidate):
            if candidate % i == 0:
                break    # Not prime — divisible by i
        else:
            # Loop finished without break — candidate is prime!
            print(f"First prime above {n} is {candidate}")
            break    # Exit the while loop
        candidate += 1


def solution_5():
    n = 5
    for i in range(1, n + 1):
        # Print leading spaces, then numbers
        spaces = " " * (n - i)
        numbers = " ".join(str(x) for x in range(1, i + 1))
        print(spaces + numbers)


def solution_6():
    n = 10
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print(", ".join(str(x) for x in sequence))


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Sum of numbers", exercise_1),
        ("Multiplication table", exercise_2),
        ("Count vowels", exercise_3),
        ("First prime above N", exercise_4),
        ("Number pyramid", exercise_5),
        ("Fibonacci sequence", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
