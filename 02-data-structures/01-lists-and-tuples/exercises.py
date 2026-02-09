"""
Lists and Tuples — Exercises
=============================

Practice problems to test your understanding of lists and tuples.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Second largest
#
# Write a function that takes a list of numbers and returns the second
# largest value. Do NOT just sort and grab index [-2] — that's too easy!
#
# Think about how to do it with a single pass through the list.
#
# Example:
#   find_second_largest([10, 5, 8, 20, 3])  =>  10
#   find_second_largest([1, 1, 1])           =>  1
#
# Hint: Track both the largest and second-largest as you go.
# =============================================================================

def exercise_1():
    nums = [10, 5, 8, 20, 3]
    # YOUR CODE HERE — find the second largest without sorting
    pass


# =============================================================================
# Exercise 2: Remove duplicates (preserving order)
#
# Given a list with duplicate values, create a new list that contains
# only the first occurrence of each value — keeping the original order.
#
# Example:
#   [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]  =>  [3, 1, 4, 5, 9, 2, 6]
#
# Hint: Use a helper structure to remember what you've already seen.
# =============================================================================

def exercise_2():
    items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    # YOUR CODE HERE — remove duplicates while preserving order
    pass


# =============================================================================
# Exercise 3: Merge and sort
#
# Given two already-sorted lists, merge them into a single sorted list.
# You CAN just concatenate and sort — that works. But for a challenge,
# try the "merge" approach: walk through both lists simultaneously,
# always picking the smaller of the two current items.
#
# Example:
#   merge_sorted([1, 4, 7, 9], [2, 3, 5, 8])  =>  [1, 2, 3, 4, 5, 7, 8, 9]
#
# =============================================================================

def exercise_3():
    list_a = [1, 4, 7, 9]
    list_b = [2, 3, 5, 8]
    # YOUR CODE HERE — merge two sorted lists into one sorted list
    pass


# =============================================================================
# Exercise 4: Transpose a matrix
#
# Given a 3x3 matrix (list of lists), transpose it — rows become columns
# and columns become rows.
#
# Example:
#   [[1, 2, 3],         [[1, 4, 7],
#    [4, 5, 6],    =>    [2, 5, 8],
#    [7, 8, 9]]          [3, 6, 9]]
#
# Hint: The element at [row][col] in the original goes to [col][row]
# in the transposed version.
# =============================================================================

def exercise_4():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    # YOUR CODE HERE — transpose the matrix and print both versions
    pass


# =============================================================================
# Exercise 5: Swap first and last using tuple unpacking
#
# Given a list, swap its first and last elements using tuple unpacking.
# Do it in a single line (not counting the print statements).
#
# Example:
#   [1, 2, 3, 4, 5]  =>  [5, 2, 3, 4, 1]
#
# Hint: You can assign to list indexes using unpacking:
#   a[0], a[-1] = a[-1], a[0]
# =============================================================================

def exercise_5():
    items = [1, 2, 3, 4, 5]
    print("Before:", items)
    # YOUR CODE HERE — swap first and last in one line
    print("After:", items)


# =============================================================================
# Exercise 6: Flatten a nested list
#
# Given a list of lists, flatten it into a single list containing
# all the elements.
#
# Example:
#   [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]  =>  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Try solving it two ways:
#   a) Using a regular for loop
#   b) Using extend()
#
# =============================================================================

def exercise_6():
    nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
    # YOUR CODE HERE — flatten the nested list
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    nums = [10, 5, 8, 20, 3]

    # Single pass — track largest and second largest
    largest = second = float("-inf")
    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second:
            second = n

    # Handle the edge case where all values are the same
    if second == float("-inf"):
        second = largest

    print(f"List: {nums}")
    print(f"Largest: {largest}, Second largest: {second}")


def solution_2():
    items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            seen.add(item)
            unique.append(item)
    print(f"Original:   {items}")
    print(f"Deduplicated: {unique}")


def solution_3():
    list_a = [1, 4, 7, 9]
    list_b = [2, 3, 5, 8]

    # The merge approach — walk through both simultaneously
    merged = []
    i, j = 0, 0
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            merged.append(list_a[i])
            i += 1
        else:
            merged.append(list_b[j])
            j += 1

    # One of the lists might have remaining items
    merged.extend(list_a[i:])
    merged.extend(list_b[j:])

    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Merged: {merged}")


def solution_4():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # Build the transposed matrix — element [row][col] goes to [col][row]
    transposed = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        transposed.append(new_row)

    print("Original:")
    for row in matrix:
        print(f"  {row}")
    print("Transposed:")
    for row in transposed:
        print(f"  {row}")


def solution_5():
    items = [1, 2, 3, 4, 5]
    print("Before:", items)
    items[0], items[-1] = items[-1], items[0]    # Tuple unpacking swap!
    print("After:", items)


def solution_6():
    nested = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]

    # Method a: regular for loop
    flat_a = []
    for sublist in nested:
        for item in sublist:
            flat_a.append(item)

    # Method b: using extend
    flat_b = []
    for sublist in nested:
        flat_b.extend(sublist)

    print(f"Nested:  {nested}")
    print(f"Flat (loop):   {flat_a}")
    print(f"Flat (extend): {flat_b}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Second largest", exercise_1),
        ("Remove duplicates (preserving order)", exercise_2),
        ("Merge and sort", exercise_3),
        ("Transpose a matrix", exercise_4),
        ("Swap first and last", exercise_5),
        ("Flatten a nested list", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
