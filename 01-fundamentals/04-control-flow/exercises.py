"""
Control Flow — Exercises
=========================

Practice problems to test your understanding of if/elif/else and control flow.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Grade calculator
#
# Given a numeric score (0-100), return the letter grade:
#   90-100 → "A"
#   80-89  → "B"
#   70-79  → "C"
#   60-69  → "D"
#   Below 60 → "F"
#
# Test with: 95, 82, 71, 60, 45
# Expected output:
#   Score 95 -> Grade A
#   Score 82 -> Grade B
#   Score 71 -> Grade C
#   Score 60 -> Grade D
#   Score 45 -> Grade F
# =============================================================================

def exercise_1():
    scores = [95, 82, 71, 60, 45]
    for score in scores:
        # YOUR CODE HERE — determine the grade for each score
        grade = "?"
        print(f"Score {score} -> Grade {grade}")


# =============================================================================
# Exercise 2: Leap year checker
#
# A year is a leap year if:
#   - It's divisible by 4
#   - BUT NOT by 100
#   - UNLESS it's also divisible by 400
#
# So: 2000 -> leap, 1900 -> not leap, 2024 -> leap, 2023 -> not leap
#
# Test with: 2000, 1900, 2024, 2023
# Expected output:
#   2000 is a leap year
#   1900 is NOT a leap year
#   2024 is a leap year
#   2023 is NOT a leap year
#
# Hint: Use % (modulo) to check divisibility. x % 4 == 0 means x is divisible by 4.
# =============================================================================

def exercise_2():
    years = [2000, 1900, 2024, 2023]
    for year in years:
        # YOUR CODE HERE — determine if each year is a leap year
        pass


# =============================================================================
# Exercise 3: FizzBuzz
#
# The classic coding challenge! For numbers 1 through 20:
#   - If the number is divisible by both 3 and 5, print "FizzBuzz"
#   - If the number is divisible by 3 only, print "Fizz"
#   - If the number is divisible by 5 only, print "Buzz"
#   - Otherwise, print the number
#
# Expected output (first 15):
#   1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...
#
# Hint: Check the "both" condition FIRST, then 3, then 5, then the number.
# =============================================================================

def exercise_3():
    for number in range(1, 21):
        # YOUR CODE HERE — apply the FizzBuzz rules
        pass


# =============================================================================
# Exercise 4: Ticket price calculator
#
# Calculate the ticket price based on age and time of day:
#   - Under 5:    Free ($0)
#   - Ages 5-12:  Child price ($8)
#   - Ages 13-64: Adult price ($15)
#   - 65 and up:  Senior price ($10)
#
# Then apply a discount:
#   - If it's a matinee (before 5 PM / hour < 17): 25% off the price
#
# Test with these (age, hour) pairs: (3, 14), (8, 20), (30, 10), (70, 18)
# Expected output:
#   Age 3, 2:00 PM -> $0.00 (Free)
#   Age 8, 8:00 PM -> $8.00 (Child)
#   Age 30, 10:00 AM -> $11.25 (Adult + matinee discount)
#   Age 70, 6:00 PM -> $10.00 (Senior)
# =============================================================================

def exercise_4():
    customers = [
        (3, 14),    # age 3, 2:00 PM
        (8, 20),    # age 8, 8:00 PM
        (30, 10),   # age 30, 10:00 AM
        (70, 18),   # age 70, 6:00 PM
    ]
    for age, hour in customers:
        # YOUR CODE HERE — calculate the ticket price
        pass


# =============================================================================
# Exercise 5: Simple login validator
#
# Check a username and password against stored credentials:
#   - Correct username: "admin"
#   - Correct password: "python123"
#
# Print one of these messages:
#   - Both correct:  "Login successful!"
#   - Wrong password: "Incorrect password."
#   - Wrong username: "User not found."
#   - Both wrong:    "User not found."  (don't reveal the username exists)
#
# Test with: ("admin", "python123"), ("admin", "wrong"), ("guest", "python123"), ("guest", "wrong")
# Expected output:
#   admin / python123 -> Login successful!
#   admin / wrong -> Incorrect password.
#   guest / python123 -> User not found.
#   guest / wrong -> User not found.
#
# Hint: Check the username FIRST, then check the password.
# =============================================================================

def exercise_5():
    correct_user = "admin"
    correct_pass = "python123"

    attempts = [
        ("admin", "python123"),
        ("admin", "wrong"),
        ("guest", "python123"),
        ("guest", "wrong"),
    ]
    for username, password in attempts:
        # YOUR CODE HERE — validate the login
        pass


# =============================================================================
# Exercise 6: Number classifier
#
# Given a number, classify it with ALL of the following:
#   - "positive", "negative", or "zero"
#   - "even" or "odd" (only if it's an integer — skip for floats)
#   - "small" (abs value < 10), "medium" (10-99), or "large" (100+)
#
# Use a ternary expression for at least one classification.
#
# Test with: 42, -7, 0, 150, -0.5
# Expected output:
#   42 -> positive, even, medium
#   -7 -> negative, odd, small
#   0 -> zero, even, small
#   150 -> positive, even, large
#   -0.5 -> negative, small
# =============================================================================

def exercise_6():
    numbers = [42, -7, 0, 150, -0.5]
    for num in numbers:
        # YOUR CODE HERE — classify each number
        pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    scores = [95, 82, 71, 60, 45]
    for score in scores:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"Score {score} -> Grade {grade}")


def solution_2():
    years = [2000, 1900, 2024, 2023]
    for year in years:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is NOT a leap year")


def solution_3():
    for number in range(1, 21):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
    print()   # Newline at the end


def solution_4():
    customers = [
        (3, 14),
        (8, 20),
        (30, 10),
        (70, 18),
    ]
    for age, hour in customers:
        # Determine base price and category
        if age < 5:
            price = 0
            category = "Free"
        elif age <= 12:
            price = 8
            category = "Child"
        elif age <= 64:
            price = 15
            category = "Adult"
        else:
            price = 10
            category = "Senior"

        # Apply matinee discount
        label = category
        if hour < 17 and price > 0:
            price *= 0.75
            label += " + matinee discount"

        # Format time for display
        period = "AM" if hour < 12 else "PM"
        display_hour = hour if hour <= 12 else hour - 12
        print(f"Age {age}, {display_hour}:00 {period} -> ${price:.2f} ({label})")


def solution_5():
    correct_user = "admin"
    correct_pass = "python123"

    attempts = [
        ("admin", "python123"),
        ("admin", "wrong"),
        ("guest", "python123"),
        ("guest", "wrong"),
    ]
    for username, password in attempts:
        if username == correct_user:
            if password == correct_pass:
                result = "Login successful!"
            else:
                result = "Incorrect password."
        else:
            result = "User not found."
        print(f"{username} / {password} -> {result}")


def solution_6():
    numbers = [42, -7, 0, 150, -0.5]
    for num in numbers:
        # Positive, negative, or zero (using ternary)
        sign = "positive" if num > 0 else "negative" if num < 0 else "zero"

        # Even or odd — only for integers
        parity = ""
        if isinstance(num, int):
            parity = ", even" if num % 2 == 0 else ", odd"

        # Size classification
        abs_val = abs(num)
        if abs_val >= 100:
            size = "large"
        elif abs_val >= 10:
            size = "medium"
        else:
            size = "small"

        print(f"{num} -> {sign}{parity}, {size}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Grade calculator", exercise_1),
        ("Leap year checker", exercise_2),
        ("FizzBuzz", exercise_3),
        ("Ticket price calculator", exercise_4),
        ("Simple login validator", exercise_5),
        ("Number classifier", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
