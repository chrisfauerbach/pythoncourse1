"""
unittest Basics — Example Code
================================

Run this file:
    python3 example.py
    python3 -m unittest example -v

This file defines some simple functions and classes, then writes test classes
for them. It's meant to show you the full workflow: code + tests in one place.

In real projects you'd put tests in a separate file (like test_calculator.py),
but keeping everything together here makes it easier to learn.
"""

import unittest

# =============================================================================
# 1. Functions to test — a simple calculator
# =============================================================================

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


# =============================================================================
# 2. A class to test — a simple BankAccount
# =============================================================================

class BankAccount:
    """A simple bank account with deposit, withdraw, and balance."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}'s account: ${self.balance:.2f}"


# =============================================================================
# 3. Test class: testing the calculator functions
# =============================================================================
# Each test method checks one specific behavior. Keep tests focused and small.

class TestCalculator(unittest.TestCase):
    """Tests for our calculator functions."""

    # --- Addition tests ---

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 5), 4)

    def test_add_floats(self):
        # assertAlmostEqual is great for floating-point comparisons
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    # --- Subtraction tests ---

    def test_subtract_positive(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 7), -4)

    # --- Multiplication tests ---

    def test_multiply_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(100, 0), 0)

    # --- Division tests ---

    def test_divide_evenly(self):
        self.assertEqual(divide(10, 2), 5.0)

    def test_divide_with_remainder(self):
        self.assertAlmostEqual(divide(7, 3), 2.3333333)

    def test_divide_by_zero_raises_error(self):
        # Use assertRaises as a context manager — the cleanest pattern
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_divide_by_zero_error_message(self):
        # You can also check the error message
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


# =============================================================================
# 4. Test class with setUp and tearDown
# =============================================================================
# setUp runs before EACH test method. Every test starts with a fresh account.

class TestBankAccount(unittest.TestCase):
    """Tests for the BankAccount class, demonstrating setUp/tearDown."""

    def setUp(self):
        """Create a fresh account before every test."""
        self.account = BankAccount("Alice", balance=100)

    def tearDown(self):
        """Clean up after every test (not strictly needed here, but shown
        for demonstration purposes)."""
        self.account = None

    # --- Basic behavior ---

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    def test_owner_name(self):
        self.assertEqual(self.account.owner, "Alice")

    # --- Deposits ---

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)

    def test_deposit_negative_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10)

    def test_deposit_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # --- Withdrawals ---

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_withdraw_entire_balance(self):
        self.account.withdraw(100)
        self.assertEqual(self.account.balance, 0)

    def test_withdraw_too_much_raises_error(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    # --- String representation ---

    def test_str(self):
        self.assertEqual(str(self.account), "Alice's account: $100.00")


# =============================================================================
# 5. Demonstrating setUpClass and tearDownClass
# =============================================================================
# These run once for the entire class, not once per test.

class TestWithClassSetup(unittest.TestCase):
    """Shows setUpClass/tearDownClass — runs once, not per-test."""

    @classmethod
    def setUpClass(cls):
        """Runs ONCE before any tests in this class."""
        # Imagine this is an expensive operation like loading a config file
        cls.config = {"app_name": "TestApp", "version": "1.0", "debug": True}

    @classmethod
    def tearDownClass(cls):
        """Runs ONCE after all tests in this class are done."""
        cls.config = None

    def test_config_has_app_name(self):
        self.assertEqual(self.config["app_name"], "TestApp")

    def test_config_has_version(self):
        self.assertIn("version", self.config)

    def test_config_debug_is_true(self):
        self.assertTrue(self.config["debug"])


# =============================================================================
# 6. Demonstrating various assertion methods
# =============================================================================

class TestAssertionShowcase(unittest.TestCase):
    """A tour of the most common assertion methods."""

    def test_assertEqual(self):
        self.assertEqual(3 + 3, 6)

    def test_assertNotEqual(self):
        self.assertNotEqual("hello", "goodbye")

    def test_assertTrue(self):
        self.assertTrue(10 > 5)

    def test_assertFalse(self):
        self.assertFalse(10 < 5)

    def test_assertIs(self):
        # assertIs checks identity (same object), not just equality
        a = [1, 2, 3]
        b = a  # b points to the SAME list
        self.assertIs(a, b)

    def test_assertIsNone(self):
        result = None
        self.assertIsNone(result)

    def test_assertIn(self):
        self.assertIn("py", "python")
        self.assertIn(42, [10, 20, 42, 80])

    def test_assertAlmostEqual(self):
        # Perfect for floating-point math where exact equality fails
        self.assertAlmostEqual(0.1 + 0.2, 0.3)

    def test_assertRaises(self):
        with self.assertRaises(TypeError):
            len(42)  # Can't get the length of an integer


# =============================================================================
# 7. Demonstrating skip decorators
# =============================================================================

class TestSkipExamples(unittest.TestCase):
    """Shows how to skip tests that shouldn't run."""

    @unittest.skip("Demonstrating unconditional skip")
    def test_skipped(self):
        self.fail("This should never run")

    @unittest.skipIf(True, "Skipped because condition is True")
    def test_skip_if(self):
        self.fail("This should never run either")

    @unittest.skipUnless(True, "Only runs when condition is True")
    def test_skip_unless_true(self):
        # This one WILL run because the condition is True
        self.assertTrue(True)


# =============================================================================
# Run all the tests!
# =============================================================================
# The unittest.main() call discovers all TestCase classes in this file and
# runs every method that starts with test_.
#
# Try running in verbose mode to see each test individually:
#     python3 example.py -v

if __name__ == "__main__":
    unittest.main()
