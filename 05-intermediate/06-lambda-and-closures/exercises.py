"""
Lambda and Closures — Exercises
=================================

Practice problems to test your understanding of lambdas and closures.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Sort by score
#
# You have a list of (name, score) tuples. Sort them by the score
# (second element) in descending order using sorted() with a lambda.
#
# Expected output:
#   [('Charlie', 92), ('Alice', 88), ('Diana', 81), ('Bob', 75)]
#
# =============================================================================

def exercise_1():
    students = [("Alice", 88), ("Bob", 75), ("Charlie", 92), ("Diana", 81)]
    # YOUR CODE HERE — sort students by score, highest first
    # sorted_students = sorted(...)
    # print(sorted_students)
    pass


# =============================================================================
# Exercise 2: Fahrenheit to Celsius
#
# Use map() with a lambda to convert a list of Fahrenheit temperatures
# to Celsius. Formula: C = (F - 32) * 5/9
# Round each result to 1 decimal place.
#
# Expected output:
#   [0.0, 22.2, 37.0, 100.0]
#
# =============================================================================

def exercise_2():
    temps_f = [32, 72, 98.6, 212]
    # YOUR CODE HERE — use map() and lambda to convert
    # temps_c = list(map(...))
    # print(temps_c)
    pass


# =============================================================================
# Exercise 3: Filter even numbers
#
# Use filter() with a lambda to keep only the even numbers from the list.
#
# Expected output:
#   [2, 4, 6, 8, 10]
#
# =============================================================================

def exercise_3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # YOUR CODE HERE — use filter() and lambda to get evens
    # evens = list(filter(...))
    # print(evens)
    pass


# =============================================================================
# Exercise 4: Make a multiplier
#
# Write a function called make_multiplier that takes a number and returns
# a new function. The returned function should multiply its argument by
# that number.
#
# Example usage:
#   triple = make_multiplier(3)
#   print(triple(10))  # 30
#   print(triple(7))   # 21
#
# Expected output:
#   triple(10) = 30
#   triple(7)  = 21
#   double(10) = 20
#   double(7)  = 14
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define make_multiplier as a closure
    # def make_multiplier(factor):
    #     ...
    #
    # triple = make_multiplier(3)
    # double = make_multiplier(2)
    # print(f"triple(10) = {triple(10)}")
    # print(f"triple(7)  = {triple(7)}")
    # print(f"double(10) = {double(10)}")
    # print(f"double(7)  = {double(7)}")
    pass


# =============================================================================
# Exercise 5: Closure-based counter
#
# Write a function called make_counter that returns TWO functions:
#   - increment(): adds 1 to the count and returns the new count
#   - get_count(): returns the current count without changing it
#
# The counter should start at 0.
#
# Expected output:
#   increment() -> 1
#   increment() -> 2
#   increment() -> 3
#   get_count() -> 3
#   increment() -> 4
#   get_count() -> 4
#
# Hint: You'll need the nonlocal keyword.
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define make_counter
    # def make_counter():
    #     ...
    #
    # inc, get = make_counter()
    # print(f"increment() -> {inc()}")
    # print(f"increment() -> {inc()}")
    # print(f"increment() -> {inc()}")
    # print(f"get_count() -> {get()}")
    # print(f"increment() -> {inc()}")
    # print(f"get_count() -> {get()}")
    pass


# =============================================================================
# Exercise 6: Range checker factory
#
# Write a function called make_range_checker that takes a min and max value
# and returns a function that checks whether a number falls within that range
# (inclusive on both ends).
#
# Example usage:
#   is_valid_age = make_range_checker(0, 150)
#   is_valid_age(25)   # True
#   is_valid_age(-5)   # False
#   is_valid_age(200)  # False
#
# Expected output:
#   is_valid_age(25)  = True
#   is_valid_age(-5)  = False
#   is_valid_age(200) = False
#   is_percentage(50) = True
#   is_percentage(0)  = True
#   is_percentage(101)= False
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define make_range_checker
    # def make_range_checker(min_val, max_val):
    #     ...
    #
    # is_valid_age = make_range_checker(0, 150)
    # print(f"is_valid_age(25)  = {is_valid_age(25)}")
    # print(f"is_valid_age(-5)  = {is_valid_age(-5)}")
    # print(f"is_valid_age(200) = {is_valid_age(200)}")
    #
    # is_percentage = make_range_checker(0, 100)
    # print(f"is_percentage(50) = {is_percentage(50)}")
    # print(f"is_percentage(0)  = {is_percentage(0)}")
    # print(f"is_percentage(101)= {is_percentage(101)}")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    students = [("Alice", 88), ("Bob", 75), ("Charlie", 92), ("Diana", 81)]
    sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
    print(sorted_students)


def solution_2():
    temps_f = [32, 72, 98.6, 212]
    temps_c = list(map(lambda f: round((f - 32) * 5 / 9, 1), temps_f))
    print(temps_c)


def solution_3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)


def solution_4():
    def make_multiplier(factor):
        def multiply(x):
            return x * factor
        return multiply

    triple = make_multiplier(3)
    double = make_multiplier(2)
    print(f"triple(10) = {triple(10)}")
    print(f"triple(7)  = {triple(7)}")
    print(f"double(10) = {double(10)}")
    print(f"double(7)  = {double(7)}")


def solution_5():
    def make_counter():
        count = 0

        def increment():
            nonlocal count
            count += 1
            return count

        def get_count():
            return count

        return increment, get_count

    inc, get = make_counter()
    print(f"increment() -> {inc()}")
    print(f"increment() -> {inc()}")
    print(f"increment() -> {inc()}")
    print(f"get_count() -> {get()}")
    print(f"increment() -> {inc()}")
    print(f"get_count() -> {get()}")


def solution_6():
    def make_range_checker(min_val, max_val):
        def check(value):
            return min_val <= value <= max_val
        return check

    is_valid_age = make_range_checker(0, 150)
    print(f"is_valid_age(25)  = {is_valid_age(25)}")
    print(f"is_valid_age(-5)  = {is_valid_age(-5)}")
    print(f"is_valid_age(200) = {is_valid_age(200)}")

    is_percentage = make_range_checker(0, 100)
    print(f"is_percentage(50) = {is_percentage(50)}")
    print(f"is_percentage(0)  = {is_percentage(0)}")
    print(f"is_percentage(101)= {is_percentage(101)}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Sort by score", exercise_1),
        ("Fahrenheit to Celsius", exercise_2),
        ("Filter even numbers", exercise_3),
        ("Make a multiplier", exercise_4),
        ("Closure-based counter", exercise_5),
        ("Range checker factory", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
