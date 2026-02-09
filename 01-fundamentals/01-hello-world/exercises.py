"""
Hello World — Exercises
========================

Practice problems to test your understanding of print().
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Introduce yourself
#
# Print three lines:
#   - Your name
#   - Your favorite programming language
#   - Why you're learning Python
#
# Example output:
#   Hi, I'm Alice!
#   My favorite language is JavaScript.
#   I'm learning Python because it's everywhere!
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Build a date
#
# Using a SINGLE print() call with the sep parameter, print today's date
# in the format: 2025-02-09
#
# Hint: print("2025", "02", "09", sep=???)
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: ASCII art
#
# Print this simple house using print() statements:
#
#     /\
#    /  \
#   /    \
#  |------|
#  |      |
#  |  []  |
#  |______|
#
# Hint: You might find it easier to use a multi-line string with triple quotes
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Loading bar
#
# Using print() with the end parameter, create output that looks like:
#   Loading: [#####] Complete!
#
# The catch: do it with THREE separate print() calls:
#   1. Print "Loading: ["
#   2. Print "#####"
#   3. Print "] Complete!"
#
# Hint: Use end="" to prevent print from adding a newline
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Receipt
#
# Print a simple receipt using \t (tab) for alignment:
#
#   ===== RECEIPT =====
#   Item        Price
#   Coffee      $4.50
#   Muffin      $3.25
#   Juice       $5.00
#   ===================
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    print("Hi, I'm Alice!")
    print("My favorite language is JavaScript.")
    print("I'm learning Python because it's everywhere!")


def solution_2():
    print("2025", "02", "09", sep="-")


def solution_3():
    print("""    /\\
   /  \\
  /    \\
 |------|
 |      |
 |  []  |
 |______|""")


def solution_4():
    print("Loading: [", end="")
    print("#####", end="")
    print("] Complete!")


def solution_5():
    print("===== RECEIPT =====")
    print("Item\t\tPrice")
    print("Coffee\t\t$4.50")
    print("Muffin\t\t$3.25")
    print("Juice\t\t$5.00")
    print("===================")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("EXERCISE 1: Introduce yourself")
    print("=" * 50)
    exercise_1()
    print()

    print("=" * 50)
    print("EXERCISE 2: Build a date")
    print("=" * 50)
    exercise_2()
    print()

    print("=" * 50)
    print("EXERCISE 3: ASCII art")
    print("=" * 50)
    exercise_3()
    print()

    print("=" * 50)
    print("EXERCISE 4: Loading bar")
    print("=" * 50)
    exercise_4()
    print()

    print("=" * 50)
    print("EXERCISE 5: Receipt")
    print("=" * 50)
    exercise_5()
    print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
    print("Uncomment the solution functions to check your work.")
