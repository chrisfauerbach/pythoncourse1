"""
unittest Basics — Exercises
============================

Practice writing unit tests! Each exercise gives you a function or class
to test, and your job is to write the test cases.

Try to solve each exercise before looking at the solutions at the bottom!

Run this file:
    python3 exercises.py
    python3 exercises.py -v    (verbose — see each test name)
"""

import unittest


# =============================================================================
# FUNCTIONS AND CLASSES TO TEST
# =============================================================================
# These are the "units" you'll be writing tests for. Read them carefully
# before writing your test cases — understand what they do, what they return,
# and what exceptions they raise.

# --- Calculator functions (Exercises 1 & 3) ---

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# --- String utilities (Exercise 2) ---

def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.
    Ignores case and spaces."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def capitalize_words(text):
    """Capitalize the first letter of each word in text.
    Raises TypeError if text is not a string."""
    if not isinstance(text, str):
        raise TypeError("Expected a string")
    return " ".join(word.capitalize() for word in text.split())


# --- Stack class (Exercise 5) ---

class Stack:
    """A simple last-in, first-out (LIFO) stack."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items on the stack."""
        return len(self._items)


# --- Edge-case function (Exercise 6) ---

def find_max(numbers):
    """Return the largest number in the list.
    Raises ValueError if the list is empty.
    Raises TypeError if numbers is None."""
    if numbers is None:
        raise TypeError("Input cannot be None")
    if len(numbers) == 0:
        raise ValueError("Cannot find max of an empty list")
    return max(numbers)


# =============================================================================
# Exercise 1: Test the calculator — add, subtract, multiply
# =============================================================================
#
# Write a test class called TestCalculatorBasics with test methods that verify:
#   - add(2, 3) returns 5
#   - add(-1, -1) returns -2
#   - add(0, 0) returns 0
#   - subtract(10, 4) returns 6
#   - subtract(3, 7) returns -4
#   - multiply(3, 4) returns 12
#   - multiply(5, 0) returns 0
#   - multiply(-2, -3) returns 6
#
# Use self.assertEqual for all of these.
# =============================================================================

class TestCalculatorBasics(unittest.TestCase):
    # YOUR CODE HERE — write test methods
    pass


# =============================================================================
# Exercise 2: Test string utilities
# =============================================================================
#
# Write a test class called TestStringUtilities with test methods that verify:
#   - is_palindrome("racecar") returns True
#   - is_palindrome("hello") returns False
#   - is_palindrome("A man a plan a canal Panama") returns True  (ignores case/spaces)
#   - is_palindrome("") returns True  (empty string is a palindrome)
#   - capitalize_words("hello world") returns "Hello World"
#   - capitalize_words("python is fun") returns "Python Is Fun"
#   - capitalize_words("") returns ""
#
# Use assertEqual, assertTrue, and assertFalse as appropriate.
# =============================================================================

class TestStringUtilities(unittest.TestCase):
    # YOUR CODE HERE — write test methods
    pass


# =============================================================================
# Exercise 3: Test for expected exceptions
# =============================================================================
#
# Write a test class called TestExceptions with test methods that verify:
#   - divide(10, 0) raises ValueError
#   - divide(10, 0) raises ValueError with "Cannot divide by zero" in the message
#   - capitalize_words(123) raises TypeError
#   - capitalize_words(None) raises TypeError
#
# Use self.assertRaises as a context manager (the "with" pattern).
# =============================================================================

class TestExceptions(unittest.TestCase):
    # YOUR CODE HERE — write test methods
    pass


# =============================================================================
# Exercise 4: Use setUp to prepare test data
# =============================================================================
#
# Write a test class called TestWithSetUp.
# In setUp, create a list of sample numbers: [10, 20, 30, 40, 50]
# Store it as self.numbers.
#
# Then write test methods that verify:
#   - The list has 5 elements
#   - The first element is 10
#   - The last element is 50
#   - 30 is in the list
#   - 99 is NOT in the list
#   - After appending 60, the list has 6 elements
#
# The key thing: each test should work with a FRESH copy of the list,
# so appending in one test doesn't affect another.
# =============================================================================

class TestWithSetUp(unittest.TestCase):
    # YOUR CODE HERE — write setUp and test methods
    pass


# =============================================================================
# Exercise 5: Test the Stack class
# =============================================================================
#
# Write a test class called TestStack.
# Use setUp to create a fresh Stack before each test.
#
# Write test methods that verify:
#   - A new stack is empty (is_empty returns True)
#   - A new stack has size 0
#   - After pushing "a", is_empty returns False
#   - After pushing "a" then "b", peek returns "b" (last pushed)
#   - After pushing "a" then "b", pop returns "b"
#   - After pushing "a" then "b" then popping, size is 1
#   - Popping from an empty stack raises IndexError
#   - Peeking at an empty stack raises IndexError
# =============================================================================

class TestStack(unittest.TestCase):
    # YOUR CODE HERE — write setUp and test methods
    pass


# =============================================================================
# Exercise 6: Test edge cases for find_max
# =============================================================================
#
# Write a test class called TestFindMax with test methods that verify:
#   - find_max([1, 2, 3]) returns 3
#   - find_max([-5, -2, -10]) returns -2  (works with negatives)
#   - find_max([42]) returns 42  (single element)
#   - find_max([7, 7, 7]) returns 7  (all same)
#   - find_max([]) raises ValueError
#   - find_max(None) raises TypeError
#   - find_max([1, -1, 0, 100, -100]) returns 100  (mixed pos/neg)
#
# This exercise is about thinking of boundary conditions and edge cases.
# =============================================================================

class TestFindMax(unittest.TestCase):
    # YOUR CODE HERE — write test methods
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================


class Solution1_TestCalculatorBasics(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zeros(self):
        self.assertEqual(add(0, 0), 0)

    def test_subtract_positive_result(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)

    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_two_negatives(self):
        self.assertEqual(multiply(-2, -3), 6)


class Solution2_TestStringUtilities(unittest.TestCase):
    def test_palindrome_racecar(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_not_palindrome_hello(self):
        self.assertFalse(is_palindrome("hello"))

    def test_palindrome_ignores_case_and_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_capitalize_hello_world(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_capitalize_python_is_fun(self):
        self.assertEqual(capitalize_words("python is fun"), "Python Is Fun")

    def test_capitalize_empty_string(self):
        self.assertEqual(capitalize_words(""), "")


class Solution3_TestExceptions(unittest.TestCase):
    def test_divide_by_zero_raises(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_message(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_capitalize_int_raises(self):
        with self.assertRaises(TypeError):
            capitalize_words(123)

    def test_capitalize_none_raises(self):
        with self.assertRaises(TypeError):
            capitalize_words(None)


class Solution4_TestWithSetUp(unittest.TestCase):
    def setUp(self):
        self.numbers = [10, 20, 30, 40, 50]

    def test_length(self):
        self.assertEqual(len(self.numbers), 5)

    def test_first_element(self):
        self.assertEqual(self.numbers[0], 10)

    def test_last_element(self):
        self.assertEqual(self.numbers[-1], 50)

    def test_contains_30(self):
        self.assertIn(30, self.numbers)

    def test_does_not_contain_99(self):
        self.assertNotIn(99, self.numbers)

    def test_append_increases_length(self):
        self.numbers.append(60)
        self.assertEqual(len(self.numbers), 6)


class Solution5_TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_new_stack_size_zero(self):
        self.assertEqual(self.stack.size(), 0)

    def test_push_makes_non_empty(self):
        self.stack.push("a")
        self.assertFalse(self.stack.is_empty())

    def test_peek_returns_last_pushed(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.peek(), "b")

    def test_pop_returns_last_pushed(self):
        self.stack.push("a")
        self.stack.push("b")
        self.assertEqual(self.stack.pop(), "b")

    def test_pop_decreases_size(self):
        self.stack.push("a")
        self.stack.push("b")
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_empty_raises(self):
        with self.assertRaises(IndexError):
            self.stack.peek()


class Solution6_TestFindMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_max([1, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(find_max([-5, -2, -10]), -2)

    def test_single_element(self):
        self.assertEqual(find_max([42]), 42)

    def test_all_same(self):
        self.assertEqual(find_max([7, 7, 7]), 7)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            find_max([])

    def test_none_raises(self):
        with self.assertRaises(TypeError):
            find_max(None)

    def test_mixed_positive_negative(self):
        self.assertEqual(find_max([1, -1, 0, 100, -100]), 100)


# =============================================================================
# Run it!
# =============================================================================
# This runs all TestCase classes in the file. The exercise stubs (with just
# "pass") will be discovered but won't run any actual tests until you fill
# them in. The solution classes WILL run and should all pass.
#
# Try: python3 exercises.py -v

if __name__ == "__main__":
    unittest.main()
