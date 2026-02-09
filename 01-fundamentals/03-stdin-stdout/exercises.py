"""
Standard Input and Output — Exercises
=======================================

Practice problems to test your understanding of input(), f-strings, and
output formatting.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

NOTE: Since input() is interactive and would block this file from running,
all exercises use HARDCODED values that simulate what input() would return.
Comments show what the real interactive version would look like.
"""


# =============================================================================
# Exercise 1: Greeting
#
# Simulate asking the user for their name and favorite color.
# Print a greeting like:
#   Hello, Alice! I hear your favorite color is blue.
#
# Use an f-string for the output.
#
# In a real program you'd use:
#   name = input("What's your name? ")
#   color = input("What's your favorite color? ")
# =============================================================================

def exercise_1():
    name = "Alice"       # Simulates: name = input("What's your name? ")
    color = "blue"       # Simulates: color = input("What's your favorite color? ")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Age calculator
#
# Simulate asking the user for their birth year.
# Calculate and print their age (or the age they will turn) in 2026.
#
# Expected output:
#   You were born in 1995.
#   You are (or will turn) 31 in 2026.
#
# Remember: input() returns a string, so you'd need int() in real code.
# In a real program: birth_year = int(input("What year were you born? "))
# =============================================================================

def exercise_2():
    birth_year = 1995    # Simulates: birth_year = int(input("What year were you born? "))
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Mad libs
#
# Simulate asking the user for a noun, a verb, an adjective, and a place.
# Build a silly sentence using an f-string:
#   The [adjective] [noun] decided to [verb] all the way to [place].
#
# Example output:
#   The sparkly dinosaur decided to moonwalk all the way to Antarctica.
#
# In a real program:
#   noun = input("Give me a noun: ")
#   verb = input("Give me a verb: ")
#   adjective = input("Give me an adjective: ")
#   place = input("Give me a place: ")
# =============================================================================

def exercise_3():
    noun = "dinosaur"         # Simulates: noun = input("Give me a noun: ")
    verb = "moonwalk"         # Simulates: verb = input("Give me a verb: ")
    adjective = "sparkly"     # Simulates: adjective = input("Give me an adjective: ")
    place = "Antarctica"      # Simulates: place = input("Give me a place: ")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Receipt formatter
#
# Given the items and prices below, print a formatted receipt like this:
#
#   ==============================
#          PYTHON CAFE
#   ==============================
#   Espresso              $  3.50
#   Avocado Toast         $ 12.99
#   Sparkling Water       $  2.75
#   Blueberry Muffin      $  4.25
#   ------------------------------
#   Subtotal              $ 23.49
#   Tax (8%)              $  1.88
#   Total                 $ 25.37
#   ==============================
#
# Hints:
#   - Use f-strings with :<20 for left-aligned item names
#   - Use f-strings with :>6.2f for right-aligned prices
#   - Calculate subtotal, tax (8%), and total
# =============================================================================

def exercise_4():
    items = [
        ("Espresso", 3.50),
        ("Avocado Toast", 12.99),
        ("Sparkling Water", 2.75),
        ("Blueberry Muffin", 4.25),
    ]
    tax_rate = 0.08
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Temperature converter
#
# Simulate asking the user for a temperature in Fahrenheit.
# Convert it to Celsius using: C = (F - 32) * 5/9
# Print the result formatted to 1 decimal place:
#   98.6°F = 37.0°C
#
# Then convert 100°C to Fahrenheit using: F = C * 9/5 + 32
# Print:
#   100.0°C = 212.0°F
#
# In a real program: temp_f = float(input("Enter temperature in °F: "))
# =============================================================================

def exercise_5():
    temp_f = 98.6    # Simulates: temp_f = float(input("Enter temp in °F: "))
    temp_c = 100.0   # Simulates: temp_c = float(input("Enter temp in °C: "))
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Student report card (putting it all together)
#
# Given the student data below, print a formatted report card using a
# triple-quoted f-string. It should look like:
#
#   ================================
#     REPORT CARD — Spring 2026
#   ================================
#     Student: Maria Rodriguez
#     ID:      STU-004271
#   --------------------------------
#     Math         92    A
#     Science      87    B+
#     English      95    A
#     History      78    C+
#   --------------------------------
#     Average:   88.0
#     Status:    PASSING
#   ================================
#
# Hints:
#   - Calculate the average of the four scores
#   - Status is "PASSING" if average >= 60, otherwise "FAILING"
#   - Use alignment format specifiers to line things up
# =============================================================================

def exercise_6():
    student_name = "Maria Rodriguez"
    student_id = "STU-004271"
    semester = "Spring 2026"
    grades = [
        ("Math", 92, "A"),
        ("Science", 87, "B+"),
        ("English", 95, "A"),
        ("History", 78, "C+"),
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    name = "Alice"
    color = "blue"
    print(f"Hello, {name}! I hear your favorite color is {color}.")


def solution_2():
    birth_year = 1995
    current_year = 2026
    age = current_year - birth_year
    print(f"You were born in {birth_year}.")
    print(f"You are (or will turn) {age} in {current_year}.")


def solution_3():
    noun = "dinosaur"
    verb = "moonwalk"
    adjective = "sparkly"
    place = "Antarctica"
    print(f"The {adjective} {noun} decided to {verb} all the way to {place}.")


def solution_4():
    items = [
        ("Espresso", 3.50),
        ("Avocado Toast", 12.99),
        ("Sparkling Water", 2.75),
        ("Blueberry Muffin", 4.25),
    ]
    tax_rate = 0.08

    print("=" * 30)
    print(f"{'PYTHON CAFE':^30}")
    print("=" * 30)
    for item_name, item_price in items:
        print(f"{item_name:<22} ${item_price:>6.2f}")
    print("-" * 30)

    subtotal = sum(price for _, price in items)
    tax = subtotal * tax_rate
    total = subtotal + tax

    print(f"{'Subtotal':<22} ${subtotal:>6.2f}")
    print(f"{'Tax (8%)':<22} ${tax:>6.2f}")
    print(f"{'Total':<22} ${total:>6.2f}")
    print("=" * 30)


def solution_5():
    temp_f = 98.6
    temp_c_result = (temp_f - 32) * 5 / 9
    print(f"{temp_f:.1f}\u00b0F = {temp_c_result:.1f}\u00b0C")

    temp_c = 100.0
    temp_f_result = temp_c * 9 / 5 + 32
    print(f"{temp_c:.1f}\u00b0C = {temp_f_result:.1f}\u00b0F")


def solution_6():
    student_name = "Maria Rodriguez"
    student_id = "STU-004271"
    semester = "Spring 2026"
    grades = [
        ("Math", 92, "A"),
        ("Science", 87, "B+"),
        ("English", 95, "A"),
        ("History", 78, "C+"),
    ]

    average = sum(score for _, score, _ in grades) / len(grades)
    status = "PASSING" if average >= 60 else "FAILING"

    print("=" * 32)
    print(f"  REPORT CARD \u2014 {semester}")
    print("=" * 32)
    print(f"  Student: {student_name}")
    print(f"  ID:      {student_id}")
    print("-" * 32)
    for subject, score, letter in grades:
        print(f"  {subject:<14} {score:>3}    {letter}")
    print("-" * 32)
    print(f"  Average: {average:>6.1f}")
    print(f"  Status:  {status}")
    print("=" * 32)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Greeting", exercise_1),
        ("Age calculator", exercise_2),
        ("Mad libs", exercise_3),
        ("Receipt formatter", exercise_4),
        ("Temperature converter", exercise_5),
        ("Student report card", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
