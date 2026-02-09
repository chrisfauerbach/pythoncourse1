"""
pytest Basics — Example Code
==============================

Run this file with pytest:
    pytest example.py -v

Or run it directly with Python to see a demo:
    python3 example.py

This file defines functions AND their tests side by side. In a real project
you'd typically put tests in a separate test_*.py file, but having everything
in one file makes it easier to learn.
"""

import sys

# We'll try to import pytest. If it's not installed, the file still works
# when run with `python3 example.py` — the demo mode doesn't need pytest.
try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False


# =============================================================================
# 1. Functions to test — just regular Python code
# =============================================================================

def add(a, b):
    """Add two numbers."""
    return a + b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def greet(name, greeting="Hello"):
    """Return a greeting string."""
    if not name:
        raise ValueError("Name cannot be empty")
    return f"{greeting}, {name}!"


# =============================================================================
# 2. Basic test functions — just use `assert`!
#
#    Notice: no classes, no inheritance, no self.assertEqual().
#    Just functions that start with `test_` and plain assert statements.
# =============================================================================

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(100, 0) == 100


def test_multiply():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(999, 0) == 0


def test_is_even_true():
    assert is_even(4)


def test_is_even_false():
    assert not is_even(7)


# =============================================================================
# 3. Testing with helpful failure messages
#
#    You can add a message after the assert — it shows up when the test fails.
#    This is optional but handy for debugging.
# =============================================================================

def test_add_with_message():
    result = add(10, 20)
    assert result == 30, f"Expected 30, but got {result}"


def test_celsius_to_fahrenheit_boiling():
    result = celsius_to_fahrenheit(100)
    assert result == 212, f"100C should be 212F, got {result}"


def test_celsius_to_fahrenheit_freezing():
    result = celsius_to_fahrenheit(0)
    assert result == 32, f"0C should be 32F, got {result}"


# =============================================================================
# 4. Testing exceptions with pytest.raises
#
#    When you EXPECT code to blow up, wrap it in `with pytest.raises(...)`.
#    The test passes if the expected exception is raised, fails if it isn't.
# =============================================================================

def test_divide_by_zero():
    """Test that dividing by zero raises ValueError."""
    if not PYTEST_AVAILABLE:
        return  # Skip when running without pytest
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_message():
    """Test that the error message is helpful."""
    if not PYTEST_AVAILABLE:
        return
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_greet_empty_name():
    """Test that empty name raises ValueError."""
    if not PYTEST_AVAILABLE:
        return
    with pytest.raises(ValueError, match="Name cannot be empty"):
        greet("")


# =============================================================================
# 5. Parametrize — one test function, many test cases
#
#    Instead of writing test_add_1, test_add_2, test_add_3... just list
#    all the input/output pairs and let pytest run them all.
# =============================================================================

if PYTEST_AVAILABLE:
    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (100, -50, 50),
        (0.1, 0.2, 0.30000000000000004),  # Floating point is fun!
    ])
    def test_add_parametrized(a, b, expected):
        assert add(a, b) == expected


    @pytest.mark.parametrize("celsius, fahrenheit", [
        (0, 32),
        (100, 212),
        (-40, -40),      # The temperature where C and F are equal!
        (37, 98.6),      # Body temperature
    ])
    def test_celsius_conversions(celsius, fahrenheit):
        assert celsius_to_fahrenheit(celsius) == fahrenheit


# =============================================================================
# 6. Fixtures — setup data for your tests
#
#    A fixture is a function decorated with @pytest.fixture that provides
#    data to test functions. The test "asks" for it by including the fixture
#    name as a parameter.
# =============================================================================

if PYTEST_AVAILABLE:
    @pytest.fixture
    def number_list():
        """Provides a fresh list of numbers for each test."""
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    @pytest.fixture
    def user_data():
        """Provides sample user data."""
        return {
            "name": "Alice",
            "age": 30,
            "email": "alice@example.com",
            "active": True,
        }


    def test_number_list_length(number_list):
        assert len(number_list) == 10


    def test_number_list_sum(number_list):
        assert sum(number_list) == 55


    def test_number_list_contains_evens(number_list):
        evens = [n for n in number_list if is_even(n)]
        assert len(evens) == 5


    def test_user_has_name(user_data):
        assert user_data["name"] == "Alice"


    def test_user_is_active(user_data):
        assert user_data["active"] is True


# =============================================================================
# 7. Fixture with teardown (yield)
#
#    Use `yield` instead of `return` when you need cleanup after the test.
#    Code before yield = setup. Code after yield = teardown.
# =============================================================================

if PYTEST_AVAILABLE:
    @pytest.fixture
    def greeting_list():
        """Provides a list and cleans up after."""
        # Setup
        data = ["hello", "hi", "hey"]

        yield data  # This is what the test receives

        # Teardown — runs after the test, even if it fails
        data.clear()  # Clean up


    def test_greeting_list_has_items(greeting_list):
        assert len(greeting_list) == 3
        assert "hello" in greeting_list


# =============================================================================
# 8. Markers — skip, xfail, and custom tags
# =============================================================================

if PYTEST_AVAILABLE:
    @pytest.mark.skip(reason="Demonstrating how skip works")
    def test_skipped_example():
        """This test is always skipped."""
        assert False  # Would fail, but it never runs


    @pytest.mark.skipif(
        sys.platform == "win32",
        reason="This example only runs on Unix-like systems"
    )
    def test_platform_specific():
        """Skipped on Windows, runs elsewhere."""
        assert True


    @pytest.mark.xfail(reason="Demonstrating expected failure")
    def test_expected_failure():
        """This test is expected to fail — reported as xfail, not FAILED."""
        assert 1 == 2  # Intentionally wrong


# =============================================================================
# 9. Testing string operations — a more realistic example
# =============================================================================

def format_name(first, last):
    """Format a full name from first and last names."""
    return f"{first.strip().title()} {last.strip().title()}"


def test_format_name_basic():
    assert format_name("alice", "smith") == "Alice Smith"


def test_format_name_already_capitalized():
    assert format_name("Bob", "Jones") == "Bob Jones"


def test_format_name_with_spaces():
    assert format_name("  charlie  ", "  brown  ") == "Charlie Brown"


def test_format_name_all_caps():
    assert format_name("DIANA", "PRINCE") == "Diana Prince"


# =============================================================================
# 10. Demo mode — when running with `python3 example.py`
#
#     This lets you see the concepts in action even without pytest installed.
#     In a real project, you'd just run `pytest` and skip this section.
# =============================================================================

def demo_basic_tests():
    """Run basic tests manually and show results."""
    print("Testing add():")
    assert add(2, 3) == 5
    print(f"  add(2, 3) = {add(2, 3)}  ...PASSED")

    assert add(-1, -1) == -2
    print(f"  add(-1, -1) = {add(-1, -1)}  ...PASSED")

    assert add(100, 0) == 100
    print(f"  add(100, 0) = {add(100, 0)}  ...PASSED")

    print()
    print("Testing multiply():")
    assert multiply(3, 4) == 12
    print(f"  multiply(3, 4) = {multiply(3, 4)}  ...PASSED")

    assert multiply(999, 0) == 0
    print(f"  multiply(999, 0) = {multiply(999, 0)}  ...PASSED")


def demo_exception_testing():
    """Show how exception testing works — manually."""
    print("Testing divide() exceptions:")

    try:
        divide(10, 0)
        print("  FAILED — should have raised ValueError")
    except ValueError as e:
        print(f"  divide(10, 0) raised ValueError: '{e}'  ...PASSED")

    print()
    print("Testing greet() exceptions:")

    try:
        greet("")
        print("  FAILED — should have raised ValueError")
    except ValueError as e:
        print(f"  greet('') raised ValueError: '{e}'  ...PASSED")


def demo_parametrize_concept():
    """Show how parametrize works — manually looping through cases."""
    print("Parametrized celsius_to_fahrenheit() tests:")
    test_cases = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6),
    ]
    for celsius, expected_f in test_cases:
        result = celsius_to_fahrenheit(celsius)
        status = "PASSED" if result == expected_f else "FAILED"
        print(f"  celsius_to_fahrenheit({celsius}) = {result} (expected {expected_f})  ...{status}")


def demo_fixtures_concept():
    """Show how fixtures work — manually creating and using test data."""
    print("Fixture concept — fresh data for each test:")

    # This is what a fixture does behind the scenes
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert len(number_list) == 10
    print(f"  len(number_list) == 10  ...PASSED")

    # Each test gets a FRESH copy
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Fresh!
    assert sum(number_list) == 55
    print(f"  sum(number_list) == 55  ...PASSED")


def demo_format_name():
    """Test the format_name function."""
    print("Testing format_name():")

    test_cases = [
        (("alice", "smith"), "Alice Smith"),
        (("Bob", "Jones"), "Bob Jones"),
        (("  charlie  ", "  brown  "), "Charlie Brown"),
        (("DIANA", "PRINCE"), "Diana Prince"),
    ]
    for (first, last), expected in test_cases:
        result = format_name(first, last)
        status = "PASSED" if result == expected else "FAILED"
        print(f"  format_name({first!r}, {last!r}) = {result!r}  ...{status}")


if __name__ == "__main__":
    print("=" * 60)
    print("  pytest Basics — Demo Mode")
    print("=" * 60)
    print()
    print("Tip: For the full pytest experience, run:")
    print("    pytest example.py -v")
    print()
    if not PYTEST_AVAILABLE:
        print("(pytest is not installed — install it with: pip install pytest)")
        print()
    print("-" * 60)
    print()

    demo_basic_tests()
    print()

    demo_exception_testing()
    print()

    demo_parametrize_concept()
    print()

    demo_fixtures_concept()
    print()

    demo_format_name()
    print()

    print("-" * 60)
    print("All demo tests passed!")
    print()
    print("Next step: Run this file with pytest to see the real thing:")
    print("    pytest example.py -v")
