"""
Itertools -- Exercises
========================

Practice problems to test your understanding of itertools.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

from itertools import (
    chain, combinations, groupby, islice, cycle, accumulate, product
)


# =============================================================================
# Exercise 1: Flatten multiple lists
#
# You have three separate lists of numbers. Use chain() to combine them
# into a single flat list and print it.
#
# lists:
#   evens = [2, 4, 6, 8]
#   odds  = [1, 3, 5, 7]
#   primes = [2, 3, 5, 7, 11]
#
# Expected output:
#   Flattened: [2, 4, 6, 8, 1, 3, 5, 7, 2, 3, 5, 7, 11]
#
# =============================================================================

def exercise_1():
    evens = [2, 4, 6, 8]
    odds = [1, 3, 5, 7]
    primes = [2, 3, 5, 7, 11]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Team pairings
#
# You're organizing a round-robin tournament. Given a list of team names,
# use combinations() to generate every possible pairing (each pair plays
# once). Print each matchup.
#
# teams = ["Lions", "Tigers", "Bears", "Wolves"]
#
# Expected output:
#   Lions vs Tigers
#   Lions vs Bears
#   Lions vs Wolves
#   Tigers vs Bears
#   Tigers vs Wolves
#   Bears vs Wolves
#   Total matchups: 6
#
# =============================================================================

def exercise_2():
    teams = ["Lions", "Tigers", "Bears", "Wolves"]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Group students by grade
#
# You have a list of (name, grade) tuples. Use groupby() to group the
# students by their grade letter. Remember: the data must be sorted
# by the grouping key first!
#
# students = [
#     ("Alice", "B"), ("Bob", "A"), ("Carol", "A"),
#     ("Dave", "C"), ("Eve", "B"), ("Frank", "A"),
# ]
#
# Expected output:
#   Grade A: ['Bob', 'Carol', 'Frank']
#   Grade B: ['Alice', 'Eve']
#   Grade C: ['Dave']
#
# Hint: sort the students by grade first, then use groupby()
# =============================================================================

def exercise_3():
    students = [
        ("Alice", "B"), ("Bob", "A"), ("Carol", "A"),
        ("Dave", "C"), ("Eve", "B"), ("Frank", "A"),
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Round-robin scheduler
#
# You have 3 workers and a list of 10 tasks. Use islice() and cycle()
# to assign tasks in round-robin order (Worker 1 gets task 1, Worker 2
# gets task 2, Worker 3 gets task 3, Worker 1 gets task 4, and so on).
#
# workers = ["Alice", "Bob", "Carol"]
# tasks = ["Task-01", "Task-02", "Task-03", "Task-04", "Task-05",
#           "Task-06", "Task-07", "Task-08", "Task-09", "Task-10"]
#
# Expected output:
#   Alice  -> Task-01
#   Bob    -> Task-02
#   Carol  -> Task-03
#   Alice  -> Task-04
#   Bob    -> Task-05
#   Carol  -> Task-06
#   Alice  -> Task-07
#   Bob    -> Task-08
#   Carol  -> Task-09
#   Alice  -> Task-10
#
# Hint: cycle the workers, then zip (or islice) with the tasks
# =============================================================================

def exercise_4():
    workers = ["Alice", "Bob", "Carol"]
    tasks = ["Task-01", "Task-02", "Task-03", "Task-04", "Task-05",
             "Task-06", "Task-07", "Task-08", "Task-09", "Task-10"]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Running balance
#
# You have a starting balance and a list of transactions (positive for
# deposits, negative for withdrawals). Use accumulate() to calculate
# the running balance after each transaction, then find the minimum
# balance reached.
#
# starting_balance = 1000
# transactions = [200, -150, -300, 500, -80, -200, 100, -600]
#
# Expected output:
#   Starting balance: $1000
#   After each transaction: [1200, 1050, 750, 1250, 1170, 970, 1070, 470]
#   Minimum balance reached: $470
#
# Hint: Put the starting balance at the front of the transactions list,
#       then use accumulate(). You can skip the first element (it's just
#       the starting balance) or include it -- your call.
# =============================================================================

def exercise_5():
    starting_balance = 1000
    transactions = [200, -150, -300, 500, -80, -200, 100, -600]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: PIN code generator
#
# Use product() to generate all possible 3-digit PIN codes using the
# digits 0-9. Then answer these questions:
#
# 1. How many total PINs are possible?
# 2. Print the first 5 PINs as strings (e.g., "000", "001", "002", ...)
# 3. Print the last 5 PINs as strings (e.g., "995", "996", ...)
#
# Expected output:
#   Total 3-digit PINs: 1000
#   First 5: ['000', '001', '002', '003', '004']
#   Last 5:  ['995', '996', '997', '998', '999']
#
# Hint: product(range(10), repeat=3) gives you tuples of digits.
#       Use ''.join(str(d) for d in pin) to convert each tuple to a string.
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    evens = [2, 4, 6, 8]
    odds = [1, 3, 5, 7]
    primes = [2, 3, 5, 7, 11]

    flattened = list(chain(evens, odds, primes))
    print(f"Flattened: {flattened}")


def solution_2():
    teams = ["Lions", "Tigers", "Bears", "Wolves"]

    matchups = list(combinations(teams, 2))
    for team_a, team_b in matchups:
        print(f"  {team_a} vs {team_b}")
    print(f"  Total matchups: {len(matchups)}")


def solution_3():
    students = [
        ("Alice", "B"), ("Bob", "A"), ("Carol", "A"),
        ("Dave", "C"), ("Eve", "B"), ("Frank", "A"),
    ]

    # Sort by grade first -- groupby only groups CONSECUTIVE items
    sorted_students = sorted(students, key=lambda s: s[1])

    for grade, group in groupby(sorted_students, key=lambda s: s[1]):
        names = [name for name, _ in group]
        print(f"  Grade {grade}: {names}")


def solution_4():
    workers = ["Alice", "Bob", "Carol"]
    tasks = ["Task-01", "Task-02", "Task-03", "Task-04", "Task-05",
             "Task-06", "Task-07", "Task-08", "Task-09", "Task-10"]

    # cycle() the workers infinitely, islice() to match the number of tasks
    worker_rotation = islice(cycle(workers), len(tasks))

    for worker, task in zip(worker_rotation, tasks):
        print(f"  {worker:<6} -> {task}")


def solution_5():
    starting_balance = 1000
    transactions = [200, -150, -300, 500, -80, -200, 100, -600]

    # Put starting balance first, then accumulate the running total
    all_amounts = [starting_balance] + transactions
    running = list(accumulate(all_amounts))

    # running[0] is just the starting balance, running[1:] are after transactions
    print(f"  Starting balance: ${starting_balance}")
    print(f"  After each transaction: {running[1:]}")
    print(f"  Minimum balance reached: ${min(running[1:])}")


def solution_6():
    # Generate all 3-digit PINs using Cartesian product
    all_pins = ["".join(str(d) for d in pin) for pin in product(range(10), repeat=3)]

    print(f"  Total 3-digit PINs: {len(all_pins)}")
    print(f"  First 5: {all_pins[:5]}")
    print(f"  Last 5:  {all_pins[-5:]}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Flatten multiple lists", exercise_1),
        ("Team pairings", exercise_2),
        ("Group students by grade", exercise_3),
        ("Round-robin scheduler", exercise_4),
        ("Running balance", exercise_5),
        ("PIN code generator", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
