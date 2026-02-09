"""
Generators — Exercises
=======================

Practice problems to test your understanding of generators.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Even numbers generator
#
# Write a generator function `evens_up_to(n)` that yields even numbers
# from 2 up to and including n.
#
# Example:
#   list(evens_up_to(10))  ->  [2, 4, 6, 8, 10]
#   list(evens_up_to(7))   ->  [2, 4, 6]
#   list(evens_up_to(1))   ->  []
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE — define evens_up_to(n)
    def evens_up_to(n):
        return
        yield  # makes this a generator function (remove when you add your code)

    # Test it
    print(f"  evens_up_to(10): {list(evens_up_to(10))}")
    print(f"  evens_up_to(7):  {list(evens_up_to(7))}")
    print(f"  evens_up_to(1):  {list(evens_up_to(1))}")


# =============================================================================
# Exercise 2: Fibonacci generator
#
# Write a generator function `fibonacci(limit)` that yields Fibonacci
# numbers less than `limit`.
#
# The Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Each number is the sum of the two before it.
#
# Example:
#   list(fibonacci(10))  ->  [0, 1, 1, 2, 3, 5, 8]
#   list(fibonacci(50))  ->  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE — define fibonacci(limit)
    def fibonacci(limit):
        return
        yield  # makes this a generator function (remove when you add your code)

    # Test it
    print(f"  fibonacci(10): {list(fibonacci(10))}")
    print(f"  fibonacci(50): {list(fibonacci(50))}")
    print(f"  fibonacci(1):  {list(fibonacci(1))}")


# =============================================================================
# Exercise 3: Simulated file reader
#
# Write a generator function `read_lines(data)` that takes a list of strings
# (simulating lines in a file) and yields each line stripped of whitespace,
# skipping any blank lines.
#
# Example:
#   data = ["  hello  ", "", "  world  ", "   ", "foo"]
#   list(read_lines(data))  ->  ["hello", "world", "foo"]
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE — define read_lines(data)
    def read_lines(data):
        return
        yield  # makes this a generator function (remove when you add your code)

    # Test it
    test_data = [
        "  Alice  ",
        "",
        "  Bob  ",
        "   ",
        "  Charlie  ",
        "",
        "  Diana  ",
    ]
    print(f"  read_lines: {list(read_lines(test_data))}")


# =============================================================================
# Exercise 4: Generator pipeline
#
# Build a 3-stage generator pipeline that processes a list of numbers:
#   Stage 1: read_numbers(data) — yields each number from the list
#   Stage 2: filter_positive(numbers) — yields only numbers > 0
#   Stage 3: double(numbers) — yields each number multiplied by 2
#
# Chain them together so that:
#   data = [-3, 5, -1, 8, 0, 2, -7, 10]
#   result -> [10, 16, 4, 20]
#
# (only positive numbers, doubled)
#
# =============================================================================

def exercise_4():
    data = [-3, 5, -1, 8, 0, 2, -7, 10]

    # YOUR CODE HERE — define read_numbers, filter_positive, double
    def read_numbers(data):
        return
        yield  # makes this a generator function (remove when you add your code)

    def filter_positive(numbers):
        return
        yield  # makes this a generator function (remove when you add your code)

    def double(numbers):
        return
        yield  # makes this a generator function (remove when you add your code)

    # Chain the pipeline
    pipeline = double(filter_positive(read_numbers(data)))
    result = list(pipeline)
    print(f"  Input:    {data}")
    print(f"  Pipeline: {result}")


# =============================================================================
# Exercise 5: Infinite ID generator
#
# Write a generator function `unique_ids(prefix)` that yields IDs forever:
#   "prefix-001", "prefix-002", "prefix-003", ...
#
# Use it to generate the first 5 IDs with prefix "ITEM".
#
# Expected output:
#   ITEM-001, ITEM-002, ITEM-003, ITEM-004, ITEM-005
#
# Hint: Use a while True loop. The caller decides when to stop.
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define unique_ids(prefix)
    def unique_ids(prefix):
        return
        yield  # makes this a generator function (remove when you add your code)

    # Take just 5 IDs from the infinite generator
    from itertools import islice
    gen = unique_ids("ITEM")
    ids = list(islice(gen, 5))
    print(f"  First 5 IDs: {ids}")


# =============================================================================
# Exercise 6: Flatten nested lists (any depth)
#
# Write a generator function `flatten(nested)` that takes an arbitrarily
# nested list and yields all the non-list values in order.
#
# Example:
#   list(flatten([1, [2, 3], [4, [5, 6]], 7]))  ->  [1, 2, 3, 4, 5, 6, 7]
#   list(flatten([[1, [2, [3, [4]]]], 5]))       ->  [1, 2, 3, 4, 5]
#
# Hint: Use recursion with yield from. If an item is a list, recurse.
#       Otherwise, yield the item.
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define flatten(nested)
    def flatten(nested):
        return
        yield  # makes this a generator function (remove when you add your code)

    # Test it
    test1 = [1, [2, 3], [4, [5, 6]], 7]
    test2 = [[1, [2, [3, [4]]]], 5]
    test3 = [[], [1], [[2]], [[[3]]]]

    print(f"  flatten({test1})")
    print(f"    -> {list(flatten(test1))}")
    print(f"  flatten({test2})")
    print(f"    -> {list(flatten(test2))}")
    print(f"  flatten({test3})")
    print(f"    -> {list(flatten(test3))}")


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    def evens_up_to(n):
        num = 2
        while num <= n:
            yield num
            num += 2

    print(f"  evens_up_to(10): {list(evens_up_to(10))}")
    print(f"  evens_up_to(7):  {list(evens_up_to(7))}")
    print(f"  evens_up_to(1):  {list(evens_up_to(1))}")


def solution_2():
    def fibonacci(limit):
        a, b = 0, 1
        while a < limit:
            yield a
            a, b = b, a + b

    print(f"  fibonacci(10): {list(fibonacci(10))}")
    print(f"  fibonacci(50): {list(fibonacci(50))}")
    print(f"  fibonacci(1):  {list(fibonacci(1))}")


def solution_3():
    def read_lines(data):
        for line in data:
            stripped = line.strip()
            if stripped:
                yield stripped

    test_data = [
        "  Alice  ",
        "",
        "  Bob  ",
        "   ",
        "  Charlie  ",
        "",
        "  Diana  ",
    ]
    print(f"  read_lines: {list(read_lines(test_data))}")


def solution_4():
    data = [-3, 5, -1, 8, 0, 2, -7, 10]

    def read_numbers(data):
        for num in data:
            yield num

    def filter_positive(numbers):
        for num in numbers:
            if num > 0:
                yield num

    def double(numbers):
        for num in numbers:
            yield num * 2

    pipeline = double(filter_positive(read_numbers(data)))
    result = list(pipeline)
    print(f"  Input:    {data}")
    print(f"  Pipeline: {result}")


def solution_5():
    def unique_ids(prefix):
        n = 1
        while True:
            yield f"{prefix}-{n:03d}"
            n += 1

    from itertools import islice
    gen = unique_ids("ITEM")
    ids = list(islice(gen, 5))
    print(f"  First 5 IDs: {ids}")


def solution_6():
    def flatten(nested):
        for item in nested:
            if isinstance(item, list):
                yield from flatten(item)
            else:
                yield item

    test1 = [1, [2, 3], [4, [5, 6]], 7]
    test2 = [[1, [2, [3, [4]]]], 5]
    test3 = [[], [1], [[2]], [[[3]]]]

    print(f"  flatten({test1})")
    print(f"    -> {list(flatten(test1))}")
    print(f"  flatten({test2})")
    print(f"    -> {list(flatten(test2))}")
    print(f"  flatten({test3})")
    print(f"    -> {list(flatten(test3))}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Even numbers generator", exercise_1),
        ("Fibonacci generator", exercise_2),
        ("Simulated file reader", exercise_3),
        ("Generator pipeline", exercise_4),
        ("Infinite ID generator", exercise_5),
        ("Flatten nested lists", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
