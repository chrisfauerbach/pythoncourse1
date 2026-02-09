"""
Functions — Exercises
======================

Practice problems to test your understanding of functions.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import math


# =============================================================================
# Exercise 1: Area of a circle
#
# Write a function called `area_of_circle` that takes a radius (a number)
# and returns the area of a circle.
#
# Formula: area = pi * radius^2
# Use math.pi for the value of pi.
#
# Examples:
#   area_of_circle(5)   -> 78.53981633974483
#   area_of_circle(1)   -> 3.141592653589793
#   area_of_circle(10)  -> 314.1592653589793
# =============================================================================

def exercise_1():
    # YOUR CODE HERE — define area_of_circle, then test it:
    # print(f"Radius 5:  {area_of_circle(5):.2f}")
    # print(f"Radius 1:  {area_of_circle(1):.2f}")
    # print(f"Radius 10: {area_of_circle(10):.2f}")
    pass


# =============================================================================
# Exercise 2: Palindrome checker
#
# Write a function called `is_palindrome` that takes a string and returns
# True if it reads the same forwards and backwards, False otherwise.
#
# Make it case-insensitive (treat "Racecar" the same as "racecar").
# Ignore spaces too (so "taco cat" counts as a palindrome).
#
# Examples:
#   is_palindrome("racecar")    -> True
#   is_palindrome("hello")      -> False
#   is_palindrome("Madam")      -> True
#   is_palindrome("taco cat")   -> True
# =============================================================================

def exercise_2():
    # YOUR CODE HERE — define is_palindrome, then test it:
    # print(f"'racecar':  {is_palindrome('racecar')}")
    # print(f"'hello':    {is_palindrome('hello')}")
    # print(f"'Madam':    {is_palindrome('Madam')}")
    # print(f"'taco cat': {is_palindrome('taco cat')}")
    pass


# =============================================================================
# Exercise 3: Power function with default parameter
#
# Write a function called `power` that takes a base and an optional exponent.
# If no exponent is provided, it should default to 2 (squaring).
#
# Examples:
#   power(5)       -> 25    (5 squared)
#   power(3, 3)    -> 27    (3 cubed)
#   power(2, 10)   -> 1024
#   power(7, 1)    -> 7
# =============================================================================

def exercise_3():
    # YOUR CODE HERE — define power, then test it:
    # print(f"power(5):      {power(5)}")
    # print(f"power(3, 3):   {power(3, 3)}")
    # print(f"power(2, 10):  {power(2, 10)}")
    # print(f"power(7, 1):   {power(7, 1)}")
    pass


# =============================================================================
# Exercise 4: Average with *args
#
# Write a function called `average` that accepts any number of numeric
# arguments using *args and returns their average.
#
# If no arguments are passed, return 0.0.
#
# Examples:
#   average(10, 20, 30)     -> 20.0
#   average(100)            -> 100.0
#   average(90, 85, 92, 88) -> 88.75
#   average()               -> 0.0
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define average, then test it:
    # print(f"average(10, 20, 30):     {average(10, 20, 30)}")
    # print(f"average(100):            {average(100)}")
    # print(f"average(90, 85, 92, 88): {average(90, 85, 92, 88)}")
    # print(f"average():               {average()}")
    pass


# =============================================================================
# Exercise 5: Greeting builder with **kwargs
#
# Write a function called `build_greeting` that accepts a required `name`
# parameter and any number of keyword arguments (**kwargs).
#
# It should return a greeting string that includes the name and lists
# all the extra info on separate lines.
#
# Example:
#   build_greeting("Alice", role="Engineer", city="Seattle")
#
# Should return:
#   "Hello, Alice!\n  role: Engineer\n  city: Seattle"
#
# When printed, that looks like:
#   Hello, Alice!
#     role: Engineer
#     city: Seattle
#
# If no kwargs are passed, just return "Hello, {name}!"
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define build_greeting, then test it:
    # print(build_greeting("Alice", role="Engineer", city="Seattle"))
    # print()
    # print(build_greeting("Bob"))
    # print()
    # print(build_greeting("Charlie", language="Python", level="beginner", goal="web dev"))
    pass


# =============================================================================
# Exercise 6: Temperature converter
#
# Write a function called `convert_temp` that takes a temperature value
# and a direction string.
#
# Parameters:
#   - temp: the temperature to convert (a number)
#   - direction: "F_to_C" or "C_to_F" (default: "F_to_C")
#
# Formulas:
#   Fahrenheit to Celsius: C = (F - 32) * 5 / 9
#   Celsius to Fahrenheit: F = C * 9 / 5 + 32
#
# Examples:
#   convert_temp(212)              -> 100.0  (boiling point, F to C)
#   convert_temp(32)               -> 0.0    (freezing point, F to C)
#   convert_temp(100, "C_to_F")   -> 212.0
#   convert_temp(0, "C_to_F")     -> 32.0
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define convert_temp, then test it:
    # print(f"212F -> C: {convert_temp(212):.1f}")
    # print(f"32F  -> C: {convert_temp(32):.1f}")
    # print(f"100C -> F: {convert_temp(100, 'C_to_F'):.1f}")
    # print(f"0C   -> F: {convert_temp(0, 'C_to_F'):.1f}")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    def area_of_circle(radius):
        """Calculate the area of a circle given its radius."""
        return math.pi * radius ** 2

    print(f"Radius 5:  {area_of_circle(5):.2f}")
    print(f"Radius 1:  {area_of_circle(1):.2f}")
    print(f"Radius 10: {area_of_circle(10):.2f}")


def solution_2():
    def is_palindrome(text):
        """Check if a string is a palindrome (case-insensitive, ignoring spaces)."""
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]

    print(f"'racecar':  {is_palindrome('racecar')}")
    print(f"'hello':    {is_palindrome('hello')}")
    print(f"'Madam':    {is_palindrome('Madam')}")
    print(f"'taco cat': {is_palindrome('taco cat')}")


def solution_3():
    def power(base, exponent=2):
        """Raise base to the given exponent. Defaults to squaring."""
        return base ** exponent

    print(f"power(5):      {power(5)}")
    print(f"power(3, 3):   {power(3, 3)}")
    print(f"power(2, 10):  {power(2, 10)}")
    print(f"power(7, 1):   {power(7, 1)}")


def solution_4():
    def average(*values):
        """Return the average of any number of values. Returns 0.0 if none given."""
        if len(values) == 0:
            return 0.0
        return sum(values) / len(values)

    print(f"average(10, 20, 30):     {average(10, 20, 30)}")
    print(f"average(100):            {average(100)}")
    print(f"average(90, 85, 92, 88): {average(90, 85, 92, 88)}")
    print(f"average():               {average()}")


def solution_5():
    def build_greeting(name, **kwargs):
        """Build a greeting string with optional extra info."""
        greeting = f"Hello, {name}!"
        for key, value in kwargs.items():
            greeting += f"\n  {key}: {value}"
        return greeting

    print(build_greeting("Alice", role="Engineer", city="Seattle"))
    print()
    print(build_greeting("Bob"))
    print()
    print(build_greeting("Charlie", language="Python", level="beginner", goal="web dev"))


def solution_6():
    def convert_temp(temp, direction="F_to_C"):
        """
        Convert a temperature between Fahrenheit and Celsius.

        Args:
            temp: The temperature value to convert.
            direction: "F_to_C" or "C_to_F" (default: "F_to_C").

        Returns:
            The converted temperature as a float.
        """
        if direction == "F_to_C":
            return (temp - 32) * 5 / 9
        return temp * 9 / 5 + 32

    print(f"212F -> C: {convert_temp(212):.1f}")
    print(f"32F  -> C: {convert_temp(32):.1f}")
    print(f"100C -> F: {convert_temp(100, 'C_to_F'):.1f}")
    print(f"0C   -> F: {convert_temp(0, 'C_to_F'):.1f}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Area of a circle", exercise_1),
        ("Palindrome checker", exercise_2),
        ("Power function with default", exercise_3),
        ("Average with *args", exercise_4),
        ("Greeting builder with **kwargs", exercise_5),
        ("Temperature converter", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
