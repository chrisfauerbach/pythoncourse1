"""
NumPy Basics — Exercises
=========================

Practice problems to test your understanding of NumPy fundamentals.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import sys

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Run: pip install numpy")
    sys.exit(0)


# =============================================================================
# Exercise 1: Array creation and inspection
#
# Create the following arrays and print each one along with its shape and dtype:
#   a) A 1D array of the integers 10, 20, 30, 40, 50
#   b) A 2x3 array of all zeros (floats)
#   c) An array of 7 evenly spaced numbers from 0 to 1 (use linspace)
#   d) An array of even numbers from 2 to 20 inclusive (use arange)
#
# For each array, print it, then print its .shape, .dtype, and .size
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Element-wise operations
#
# Given these two arrays:
#   prices = np.array([19.99, 35.50, 12.75, 89.00, 45.25])
#   quantities = np.array([2, 1, 5, 1, 3])
#
# Calculate and print:
#   a) The total cost for each item (price * quantity)
#   b) The overall total (sum of all item costs)
#   c) A 15% discount applied to each price (multiply by 0.85)
#   d) The savings per item (original price minus discounted price)
#
# =============================================================================

def exercise_2():
    prices = np.array([19.99, 35.50, 12.75, 89.00, 45.25])
    quantities = np.array([2, 1, 5, 1, 3])
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Boolean indexing
#
# Given this array of temperatures (in Fahrenheit):
#   temps = np.array([72, 85, 91, 68, 77, 103, 55, 88, 95, 61])
#
# Use boolean indexing to find and print:
#   a) All temperatures above 80
#   b) All temperatures below 70
#   c) All temperatures between 70 and 90 (inclusive)
#   d) How many days were above 90 (hint: sum the boolean mask)
#
# =============================================================================

def exercise_3():
    temps = np.array([72, 85, 91, 68, 77, 103, 55, 88, 95, 61])
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Statistics on a dataset
#
# You have monthly sales data for 3 stores over 4 months:
#
#   sales = np.array([[120, 150, 130, 160],   # Store A
#                     [200, 180, 210, 190],   # Store B
#                     [ 90, 110, 100, 120]])  # Store C
#
# Calculate and print:
#   a) Total sales for each store (sum across columns, axis=1)
#   b) Average monthly sales across all stores (mean down rows, axis=0)
#   c) The best month for each store (use np.max with axis=1)
#   d) The overall mean, standard deviation, min, and max of all sales
#
# =============================================================================

def exercise_4():
    sales = np.array([[120, 150, 130, 160],
                      [200, 180, 210, 190],
                      [ 90, 110, 100, 120]])
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Reshape and transpose
#
# Start with: a = np.arange(1, 25)  (numbers 1 through 24)
#
#   a) Reshape it into a 4x6 matrix and print it
#   b) Transpose the matrix and print its new shape
#   c) Reshape the original array into a 2x3x4 (3D) array and print it
#   d) Flatten the 3D array back to 1D and verify it matches the original
#
# =============================================================================

def exercise_5():
    a = np.arange(1, 25)
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Dice simulation
#
# Simulate rolling two dice 10,000 times and analyze the results.
#
#   a) Use np.random.randint to generate 10,000 rolls of die 1 (values 1-6)
#      and 10,000 rolls of die 2 (values 1-6)
#   b) Calculate the sum of both dice for each roll
#   c) Print the average sum (should be close to 7.0)
#   d) Count how many times the sum was exactly 7
#      (hint: use np.sum on a boolean mask)
#   e) Count how many times the sum was 2 ("snake eyes")
#   f) Count how many times the sum was 12 ("boxcars")
#
# Set np.random.seed(42) at the start for reproducible results.
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    # a) 1D array of integers
    a = np.array([10, 20, 30, 40, 50])
    print(f"a) {a}  shape={a.shape}, dtype={a.dtype}, size={a.size}")

    # b) 2x3 zeros
    b = np.zeros((2, 3))
    print(f"b)\n{b}")
    print(f"   shape={b.shape}, dtype={b.dtype}, size={b.size}")

    # c) 7 evenly spaced from 0 to 1
    c = np.linspace(0, 1, 7)
    print(f"c) {c}  shape={c.shape}, dtype={c.dtype}, size={c.size}")

    # d) Even numbers from 2 to 20 inclusive
    d = np.arange(2, 21, 2)
    print(f"d) {d}  shape={d.shape}, dtype={d.dtype}, size={d.size}")


def solution_2():
    prices = np.array([19.99, 35.50, 12.75, 89.00, 45.25])
    quantities = np.array([2, 1, 5, 1, 3])

    # a) Total cost per item
    item_totals = prices * quantities
    print(f"a) Item totals: {item_totals}")

    # b) Overall total
    overall = np.sum(item_totals)
    print(f"b) Overall total: ${overall:.2f}")

    # c) 15% discount on each price
    discounted = prices * 0.85
    print(f"c) Discounted prices: {discounted}")

    # d) Savings per item
    savings = prices - discounted
    print(f"d) Savings per item: {savings}")


def solution_3():
    temps = np.array([72, 85, 91, 68, 77, 103, 55, 88, 95, 61])

    # a) Above 80
    print(f"a) Above 80: {temps[temps > 80]}")

    # b) Below 70
    print(f"b) Below 70: {temps[temps < 70]}")

    # c) Between 70 and 90 inclusive
    between = temps[(temps >= 70) & (temps <= 90)]
    print(f"c) 70-90:    {between}")

    # d) Count of days above 90
    hot_days = np.sum(temps > 90)
    print(f"d) Days above 90: {hot_days}")


def solution_4():
    sales = np.array([[120, 150, 130, 160],
                      [200, 180, 210, 190],
                      [ 90, 110, 100, 120]])
    stores = ["Store A", "Store B", "Store C"]
    months = ["Month 1", "Month 2", "Month 3", "Month 4"]

    # a) Total sales per store
    store_totals = np.sum(sales, axis=1)
    print("a) Total sales per store:")
    for name, total in zip(stores, store_totals):
        print(f"   {name}: {total}")

    # b) Average monthly sales across stores
    monthly_avg = np.mean(sales, axis=0)
    print("b) Average monthly sales across stores:")
    for month, avg in zip(months, monthly_avg):
        print(f"   {month}: {avg:.1f}")

    # c) Best month for each store
    best = np.max(sales, axis=1)
    print("c) Best month sales per store:")
    for name, b in zip(stores, best):
        print(f"   {name}: {b}")

    # d) Overall statistics
    print(f"d) Overall mean: {np.mean(sales):.1f}")
    print(f"   Overall std:  {np.std(sales):.1f}")
    print(f"   Overall min:  {np.min(sales)}")
    print(f"   Overall max:  {np.max(sales)}")


def solution_5():
    a = np.arange(1, 25)
    print(f"Original: {a}")

    # a) Reshape to 4x6
    b = a.reshape(4, 6)
    print(f"a) 4x6 matrix:")
    print(b)

    # b) Transpose
    t = b.T
    print(f"b) Transposed shape: {t.shape}")
    print(t)

    # c) Reshape to 2x3x4 (3D)
    c = a.reshape(2, 3, 4)
    print(f"c) 3D array (2x3x4):")
    print(c)

    # d) Flatten and verify
    flat = c.flatten()
    print(f"d) Flattened: {flat}")
    print(f"   Matches original? {np.array_equal(flat, a)}")


def solution_6():
    np.random.seed(42)

    # a) Roll two dice 10,000 times each
    die1 = np.random.randint(1, 7, 10000)
    die2 = np.random.randint(1, 7, 10000)

    # b) Sum of both dice
    totals = die1 + die2

    # c) Average sum
    print(f"c) Average sum: {np.mean(totals):.3f} (expected ~7.0)")

    # d) Count of sevens
    sevens = np.sum(totals == 7)
    print(f"d) Sevens: {sevens} ({sevens / 100:.1f}%)")

    # e) Snake eyes (sum = 2)
    snake_eyes = np.sum(totals == 2)
    print(f"e) Snake eyes (2): {snake_eyes} ({snake_eyes / 100:.1f}%)")

    # f) Boxcars (sum = 12)
    boxcars = np.sum(totals == 12)
    print(f"f) Boxcars (12): {boxcars} ({boxcars / 100:.1f}%)")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Array creation and inspection", exercise_1),
        ("Element-wise operations", exercise_2),
        ("Boolean indexing", exercise_3),
        ("Statistics on a dataset", exercise_4),
        ("Reshape and transpose", exercise_5),
        ("Dice simulation", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
