"""
pytest Basics — Exercises
==========================

Practice writing pytest-style tests! Each exercise gives you a function (or class)
to test, and asks you to write test functions for it.

Run this file with pytest for the real experience:
    pytest exercises.py -v

Or run it directly with Python to check the solutions:
    python3 exercises.py

Try to solve each exercise before looking at the solutions at the bottom!
"""

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False


# =============================================================================
# FUNCTIONS AND CLASSES TO TEST
#
# These are the "production code" that your tests will verify.
# Don't modify these — just write tests for them!
# =============================================================================

def absolute_value(n):
    """Return the absolute value of a number."""
    if n < 0:
        return -n
    return n


def maximum(a, b):
    """Return the larger of two numbers."""
    if a >= b:
        return a
    return b


def factorial(n):
    """Return the factorial of n. Raises ValueError for negative numbers."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32


class ShoppingCart:
    """A simple shopping cart that holds items and calculates totals."""

    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity=1):
        """Add an item to the cart. Price must be positive."""
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.items.append({
            "name": name,
            "price": price,
            "quantity": quantity,
        })

    def remove_item(self, name):
        """Remove an item by name. Raises ValueError if not found."""
        for i, item in enumerate(self.items):
            if item["name"] == name:
                self.items.pop(i)
                return
        raise ValueError(f"Item '{name}' not found in cart")

    def get_total(self):
        """Calculate the total price of all items."""
        return sum(item["price"] * item["quantity"] for item in self.items)

    def item_count(self):
        """Return the total number of items (counting quantities)."""
        return sum(item["quantity"] for item in self.items)

    def is_empty(self):
        """Return True if the cart has no items."""
        return len(self.items) == 0

    def apply_discount(self, percent):
        """Apply a percentage discount to all items. Must be 0-100."""
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")
        factor = 1 - percent / 100
        for item in self.items:
            item["price"] = round(item["price"] * factor, 2)


def validate_password(password):
    """
    Validate a password. Returns True if valid, raises ValueError if not.

    Rules:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*()_+-=)
    """
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one digit")
    special_chars = "!@#$%^&*()_+-="
    if not any(c in special_chars for c in password):
        raise ValueError("Password must contain at least one special character")
    return True


# =============================================================================
# Exercise 1: Simple assert-based tests for math utilities
#
# Write test functions for absolute_value() and maximum().
# You should test:
#   - absolute_value with positive, negative, and zero
#   - maximum with different orderings, equal values, and negatives
#
# Remember: test function names must start with test_
# =============================================================================

def exercise_1_test_absolute_value():
    # YOUR CODE HERE — write assert statements to test absolute_value()
    # Example: assert absolute_value(5) == 5
    pass


def exercise_1_test_maximum():
    # YOUR CODE HERE — write assert statements to test maximum()
    pass


# =============================================================================
# Exercise 2: Parametrized tests for temperature converter
#
# Write a parametrized test for fahrenheit_to_celsius() using these known
# conversion pairs:
#   32F  =  0C
#   212F = 100C
#   -40F = -40C
#   98.6F = 37C
#   0F   = -17.78C (approximately — use round() to 2 decimal places)
#
# Also write a parametrized test for celsius_to_fahrenheit() to verify
# the reverse conversion.
#
# Hint: Use @pytest.mark.parametrize("param1, param2", [(val1, val2), ...])
# =============================================================================

# YOUR CODE HERE — write parametrized test functions
# def test_fahrenheit_to_celsius(...)
# def test_celsius_to_fahrenheit(...)


# =============================================================================
# Exercise 3: Testing exceptions with pytest.raises
#
# Write tests that verify:
#   - factorial(-1) raises ValueError
#   - factorial(-5) raises ValueError with a message containing "negative"
#   - ShoppingCart.add_item() with price=0 raises ValueError
#   - ShoppingCart.add_item() with negative quantity raises ValueError
#   - ShoppingCart.remove_item() for a non-existent item raises ValueError
#
# Hint: Use `with pytest.raises(ValueError):` or
#       `with pytest.raises(ValueError, match="some text"):`
# =============================================================================

# YOUR CODE HERE — write test functions for exception cases


# =============================================================================
# Exercise 4: Write a fixture for test data setup
#
# Write a pytest fixture called `sample_numbers` that returns this dict:
#   {"positive": [1, 5, 10, 100], "negative": [-1, -5, -10], "zero": [0]}
#
# Then write three test functions that use the fixture:
#   - test_all_positives_are_positive: check absolute_value(n) == n for positives
#   - test_all_negatives_flip: check absolute_value(n) == -n for negatives
#   - test_zero_is_zero: check absolute_value(0) == 0
#
# Hint: Define the fixture with @pytest.fixture, then use its name as a
#       parameter in your test functions.
# =============================================================================

# YOUR CODE HERE — write the fixture and test functions


# =============================================================================
# Exercise 5: Write tests for ShoppingCart
#
# Write a fixture called `cart` that returns a new ShoppingCart().
# Then write tests for:
#   - A new cart is empty (is_empty() returns True)
#   - Adding an item makes it non-empty
#   - get_total() returns correct total for one item
#   - get_total() returns correct total for multiple items with quantities
#   - item_count() returns the sum of all quantities
#   - remove_item() actually removes the item
#   - apply_discount() reduces prices correctly (e.g., 10% off $100 = $90)
#
# Hint: Build up the cart inside each test, using the fixture for a fresh start.
# =============================================================================

# YOUR CODE HERE — write the fixture and test functions


# =============================================================================
# Exercise 6: Comprehensive tests for password validator
#
# This is the big one! Write thorough tests for validate_password():
#
#   a) Test that a valid password returns True
#   b) Use @pytest.mark.parametrize to test EACH failure case with an
#      appropriate error message:
#      - Too short (less than 8 chars)
#      - Missing uppercase
#      - Missing lowercase
#      - Missing digit
#      - Missing special character
#   c) Write a parametrized test with several valid passwords to make sure
#      they all pass
#   d) Write a parametrized test with several INVALID passwords, each paired
#      with the expected error message substring
#
# Hint: For testing that an exception message matches, use:
#       with pytest.raises(ValueError, match="expected text"):
# =============================================================================

# YOUR CODE HERE — write comprehensive test functions


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1: Simple assert-based tests
# -----------------------------------------------------------------------------

def solution_1_test_absolute_value():
    # Positive numbers stay the same
    assert absolute_value(5) == 5
    assert absolute_value(100) == 100

    # Negative numbers become positive
    assert absolute_value(-3) == 3
    assert absolute_value(-99) == 99

    # Zero stays zero
    assert absolute_value(0) == 0


def solution_1_test_maximum():
    # First is bigger
    assert maximum(10, 5) == 10

    # Second is bigger
    assert maximum(3, 7) == 7

    # Equal values
    assert maximum(4, 4) == 4

    # Negative numbers
    assert maximum(-1, -5) == -1

    # Mixed positive and negative
    assert maximum(-10, 10) == 10


# -----------------------------------------------------------------------------
# Solution 2: Parametrized temperature tests
# -----------------------------------------------------------------------------

if PYTEST_AVAILABLE:
    @pytest.mark.parametrize("fahrenheit, celsius", [
        (32, 0),
        (212, 100),
        (-40, -40),
        (98.6, 37),
        (0, -17.78),
    ])
    def solution_2_test_f_to_c(fahrenheit, celsius):
        result = round(fahrenheit_to_celsius(fahrenheit), 2)
        assert result == celsius, f"{fahrenheit}F should be {celsius}C, got {result}C"

    @pytest.mark.parametrize("celsius, fahrenheit", [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
    ])
    def solution_2_test_c_to_f(celsius, fahrenheit):
        result = celsius_to_fahrenheit(celsius)
        assert result == fahrenheit, f"{celsius}C should be {fahrenheit}F, got {result}F"


# -----------------------------------------------------------------------------
# Solution 3: Testing exceptions
# -----------------------------------------------------------------------------

def solution_3_test_factorial_negative():
    if not PYTEST_AVAILABLE:
        return
    with pytest.raises(ValueError):
        factorial(-1)


def solution_3_test_factorial_negative_message():
    if not PYTEST_AVAILABLE:
        return
    with pytest.raises(ValueError, match="negative"):
        factorial(-5)


def solution_3_test_cart_zero_price():
    if not PYTEST_AVAILABLE:
        return
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Price must be positive"):
        cart.add_item("Free thing", 0)


def solution_3_test_cart_negative_quantity():
    if not PYTEST_AVAILABLE:
        return
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="Quantity must be positive"):
        cart.add_item("Widget", 9.99, quantity=-1)


def solution_3_test_cart_remove_missing():
    if not PYTEST_AVAILABLE:
        return
    cart = ShoppingCart()
    with pytest.raises(ValueError, match="not found"):
        cart.remove_item("nonexistent")


# -----------------------------------------------------------------------------
# Solution 4: Fixture for test data
# -----------------------------------------------------------------------------

if PYTEST_AVAILABLE:
    @pytest.fixture
    def sample_numbers():
        return {
            "positive": [1, 5, 10, 100],
            "negative": [-1, -5, -10],
            "zero": [0],
        }

    def solution_4_test_positives(sample_numbers):
        for n in sample_numbers["positive"]:
            assert absolute_value(n) == n, f"absolute_value({n}) should be {n}"

    def solution_4_test_negatives(sample_numbers):
        for n in sample_numbers["negative"]:
            assert absolute_value(n) == -n, f"absolute_value({n}) should be {-n}"

    def solution_4_test_zero(sample_numbers):
        for n in sample_numbers["zero"]:
            assert absolute_value(n) == 0


# -----------------------------------------------------------------------------
# Solution 5: ShoppingCart tests with fixture
# -----------------------------------------------------------------------------

if PYTEST_AVAILABLE:
    @pytest.fixture
    def cart():
        """Provides a fresh empty ShoppingCart for each test."""
        return ShoppingCart()

    def solution_5_test_new_cart_is_empty(cart):
        assert cart.is_empty()

    def solution_5_test_add_item_not_empty(cart):
        cart.add_item("Apple", 1.50)
        assert not cart.is_empty()

    def solution_5_test_total_one_item(cart):
        cart.add_item("Book", 12.99)
        assert cart.get_total() == 12.99

    def solution_5_test_total_multiple_items(cart):
        cart.add_item("Shirt", 25.00, quantity=2)
        cart.add_item("Hat", 15.00, quantity=1)
        # 25.00 * 2 + 15.00 * 1 = 65.00
        assert cart.get_total() == 65.00

    def solution_5_test_item_count(cart):
        cart.add_item("Apple", 1.00, quantity=3)
        cart.add_item("Banana", 0.50, quantity=5)
        assert cart.item_count() == 8

    def solution_5_test_remove_item(cart):
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.remove_item("Apple")
        assert cart.item_count() == 1
        assert cart.get_total() == 0.75

    def solution_5_test_apply_discount(cart):
        cart.add_item("Laptop", 100.00)
        cart.apply_discount(10)  # 10% off
        assert cart.get_total() == 90.00


# -----------------------------------------------------------------------------
# Solution 6: Comprehensive password validator tests
# -----------------------------------------------------------------------------

def solution_6_test_valid_password():
    assert validate_password("MyP@ss1!") is True


if PYTEST_AVAILABLE:
    @pytest.mark.parametrize("password, error_match", [
        ("Sh0r!",                "at least 8 characters"),
        ("alllowercase1!",       "uppercase letter"),
        ("ALLUPPERCASE1!",       "lowercase letter"),
        ("NoDigitsHere!",        "at least one digit"),
        ("NoSpecial1a",          "special character"),
    ])
    def solution_6_test_invalid_passwords(password, error_match):
        with pytest.raises(ValueError, match=error_match):
            validate_password(password)

    @pytest.mark.parametrize("password", [
        "MyP@ssw0rd",
        "Str0ng!Pass",
        "H3llo_World",
        "C0mpl3x!ty",
        "Ab1!efgh",
    ])
    def solution_6_test_various_valid_passwords(password):
        assert validate_password(password) is True

    @pytest.mark.parametrize("password, error_match", [
        ("",            "at least 8 characters"),
        ("Ab1!",        "at least 8 characters"),
        ("abcdefg1!",   "uppercase letter"),
        ("ABCDEFG1!",   "lowercase letter"),
        ("Abcdefgh!",   "at least one digit"),
        ("Abcdefg1",    "special character"),
    ])
    def solution_6_test_each_rule_fails(password, error_match):
        with pytest.raises(ValueError, match=error_match):
            validate_password(password)


# =============================================================================
# Run it! — Demo mode for running with python3 exercises.py
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  pytest Basics — Exercises (Solution Check)")
    print("=" * 60)
    print()
    print("Tip: For the full pytest experience, run:")
    print("    pytest exercises.py -v")
    print()
    if not PYTEST_AVAILABLE:
        print("(pytest is not installed — install it with: pip install pytest)")
        print()
    print("-" * 60)
    print()

    solutions = [
        ("Exercise 1: Math utility tests", [
            ("absolute_value tests", solution_1_test_absolute_value),
            ("maximum tests", solution_1_test_maximum),
        ]),
        ("Exercise 2: Parametrized temperature tests", [
            ("fahrenheit_to_celsius", lambda: [
                (lambda f, c: (
                    round(fahrenheit_to_celsius(f), 2) == c
                    or print(f"  FAILED: {f}F should be {c}C")
                ))(f, c)
                for f, c in [(32, 0), (212, 100), (-40, -40), (98.6, 37), (0, -17.78)]
            ]),
            ("celsius_to_fahrenheit", lambda: [
                (lambda c, f: (
                    celsius_to_fahrenheit(c) == f
                    or print(f"  FAILED: {c}C should be {f}F")
                ))(c, f)
                for c, f in [(0, 32), (100, 212), (-40, -40), (37, 98.6)]
            ]),
        ]),
        ("Exercise 3: Exception testing", [
            ("factorial(-1) raises ValueError", solution_3_test_factorial_negative),
            ("factorial(-5) message check", solution_3_test_factorial_negative_message),
            ("cart zero price", solution_3_test_cart_zero_price),
            ("cart negative quantity", solution_3_test_cart_negative_quantity),
            ("cart remove missing item", solution_3_test_cart_remove_missing),
        ]),
        ("Exercise 5: ShoppingCart tests", [
            ("cart operations", lambda: None),  # Fixture-based — run with pytest
        ]),
        ("Exercise 6: Password validator", [
            ("valid password", solution_6_test_valid_password),
        ]),
    ]

    passed = 0
    failed = 0

    for exercise_title, tests in solutions:
        print(f"  {exercise_title}")
        print(f"  {'-' * len(exercise_title)}")
        for test_name, test_func in tests:
            try:
                test_func()
                print(f"    {test_name}  ...PASSED")
                passed += 1
            except Exception as e:
                print(f"    {test_name}  ...FAILED ({e})")
                failed += 1
        print()

    print("-" * 60)
    print(f"Solutions checked: {passed} passed, {failed} failed")
    print()

    if failed == 0:
        print("All solution checks passed!")
    else:
        print("Some solutions had issues — check the output above.")

    print()
    print("Note: Exercises 2, 4, 5, and 6 use pytest features (parametrize,")
    print("fixtures) that work best when run with pytest directly:")
    print("    pytest exercises.py -v -k solution")
