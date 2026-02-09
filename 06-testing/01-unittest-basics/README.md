# unittest Basics

## Objective

Learn how to write and run unit tests in Python using the built-in `unittest` module. By the end of this lesson you'll be able to test your own functions and classes with confidence.

## Concepts Covered

- Why testing matters
- What unit tests are
- The `unittest` module and `TestCase` class
- Writing test methods and common assertions
- `setUp` / `tearDown` and `setUpClass` / `tearDownClass`
- Running tests and test discovery
- Testing for exceptions with `assertRaises`
- Skipping tests with decorators
- Organizing test files

## Prerequisites

- Functions and classes
- Exceptions and error handling
- Basic familiarity with running Python from the command line

## Lesson

### Why Testing Matters

Imagine you've just written a function that calculates shipping costs. It works perfectly — today. Next week you refactor the pricing logic and accidentally break it. Without tests, you won't know until a customer complains. With tests, you know in seconds.

Testing gives you three super-powers:

- **Confidence** — you know your code does what you think it does.
- **Refactoring safety** — change the internals, run the tests, and sleep well at night.
- **Living documentation** — tests show exactly how your code is supposed to behave. They're examples that never go stale.

### What Unit Tests Are

A *unit test* tests one small piece of code — a single function, a single method, a single behavior — in isolation. You're not testing your entire application at once; you're testing individual **units**.

```python
# The "unit" we want to test
def add(a, b):
    return a + b

# A unit test for that function
def test_add():
    assert add(2, 3) == 5
```

That's the basic idea. Give the function a known input, check that you get the expected output.

### The unittest Module

Python ships with a full-featured testing framework called `unittest`. You don't need to install anything — it's built right in.

```python
import unittest
```

The core idea: you create a **test class** that inherits from `unittest.TestCase`, and you write **test methods** inside it. Each method tests one thing.

### Writing Your First Test Class

```python
import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)
```

A few things to notice:

- The class inherits from `unittest.TestCase`. That's what makes it a test class.
- Every test method **must start with `test_`**. If it doesn't, unittest won't run it. This trips up everyone at least once.
- Inside each method, you use `self.assert...()` methods instead of plain `assert` statements. These give you much better error messages when something fails.

### Common Assertions

`unittest.TestCase` comes packed with assertion methods. Here are the ones you'll use most often:

| Method | Checks that |
|--------|------------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` (same object) |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(Error)` | the code raises `Error` |
| `assertAlmostEqual(a, b)` | `round(a - b, 7) == 0` (great for floats) |

```python
class TestAssertions(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(1 + 1, 2)

    def test_not_equal(self):
        self.assertNotEqual("hello", "world")

    def test_true(self):
        self.assertTrue(10 > 5)

    def test_false(self):
        self.assertFalse(10 < 5)

    def test_is_none(self):
        result = None
        self.assertIsNone(result)

    def test_in(self):
        self.assertIn("a", "abc")
        self.assertIn(3, [1, 2, 3])

    def test_almost_equal(self):
        # Floating point math: 0.1 + 0.2 != 0.3 exactly
        self.assertAlmostEqual(0.1 + 0.2, 0.3)
```

### setUp and tearDown

Often you need the same setup before every test — creating objects, preparing data, opening connections. That's what `setUp` and `tearDown` are for.

`setUp()` runs **before each test method**. `tearDown()` runs **after each test method**, even if the test fails.

```python
class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """Runs before EVERY test method."""
        self.cart = []
        self.cart.append("apple")

    def tearDown(self):
        """Runs after EVERY test method."""
        self.cart.clear()

    def test_cart_starts_with_one_item(self):
        self.assertEqual(len(self.cart), 1)

    def test_add_item(self):
        self.cart.append("banana")
        self.assertEqual(len(self.cart), 2)
        self.assertIn("banana", self.cart)
```

Each test gets its own fresh `self.cart` — they never interfere with each other.

### setUpClass and tearDownClass

Sometimes setup is expensive (opening a database connection, loading a big file) and you only want to do it once for the entire class, not before every single test.

```python
class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Runs ONCE before all tests in this class."""
        print("Opening database connection...")
        cls.connection = "fake_db_connection"

    @classmethod
    def tearDownClass(cls):
        """Runs ONCE after all tests in this class."""
        print("Closing database connection...")
        cls.connection = None

    def test_connection_exists(self):
        self.assertIsNotNone(self.connection)
```

Note that `setUpClass` and `tearDownClass` are **class methods** — they take `cls` instead of `self` and need the `@classmethod` decorator.

### Running Tests

There are a few ways to run your tests:

**1. The `if __name__` pattern (most common for single files):**

```python
if __name__ == "__main__":
    unittest.main()
```

Then run: `python3 test_my_code.py`

**2. Using the unittest module directly:**

```bash
python3 -m unittest test_my_code
```

**3. Verbose mode — see each test's name and status:**

```bash
python3 -m unittest test_my_code -v
```

Output looks like:

```
test_positive_numbers (test_my_code.TestMultiply) ... ok
test_multiply_by_zero (test_my_code.TestMultiply) ... ok
test_negative_numbers (test_my_code.TestMultiply) ... ok
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

### Test Discovery

When your project has lots of test files, you don't want to run them one by one. Test discovery finds and runs all tests automatically:

```bash
python3 -m unittest discover
```

By default it looks for files matching `test*.py` in the current directory. You can customize this:

```bash
# Look in a specific directory
python3 -m unittest discover -s tests

# Match a different pattern
python3 -m unittest discover -p "*_test.py"
```

### Organizing Tests

A common project layout:

```
my_project/
    my_module.py
    tests/
        __init__.py
        test_my_module.py
```

Naming conventions that matter:

- Test files start with `test_` (e.g., `test_calculator.py`)
- Test classes start with `Test` (e.g., `TestCalculator`)
- Test methods start with `test_` (e.g., `test_add_positive_numbers`)

These aren't just style choices — `test_` prefixes on methods are **required** by unittest, and `test_` prefixes on files are required for test discovery to find them.

### assertRaises as a Context Manager

When you want to verify that code raises a specific exception, use `assertRaises` as a context manager. This is the cleanest way to test error handling:

```python
class TestDivision(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = 10 / 0

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            int("not_a_number")
```

The test passes if the expected exception is raised inside the `with` block. If no exception is raised (or a different one is raised), the test fails.

You can also inspect the exception message:

```python
def test_error_message(self):
    with self.assertRaises(ValueError) as context:
        int("abc")
    self.assertIn("invalid literal", str(context.exception))
```

### Skipping Tests

Sometimes a test shouldn't run — maybe it's for a feature you haven't built yet, or it only works on a certain OS.

```python
class TestFeatures(unittest.TestCase):
    @unittest.skip("Not implemented yet")
    def test_future_feature(self):
        pass  # This test won't run

    @unittest.skipIf(2 + 2 == 4, "Skipping because math works")
    def test_conditional_skip(self):
        pass  # This won't run either

    @unittest.skipUnless(False, "Only runs when condition is True")
    def test_skip_unless(self):
        pass  # This won't run because the condition is False
```

Skipped tests show up as `s` in the output, so you always know they exist — they don't silently disappear.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates all of the above. Run it with:

```bash
python3 example.py
# or
python3 -m unittest example -v
```

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding. You'll be writing test cases for provided functions and classes.

## Key Takeaways

- Unit tests verify that individual pieces of code work correctly in isolation
- Python's `unittest` module is built-in — no installation needed
- Test classes inherit from `unittest.TestCase`; test methods must start with `test_`
- Use specific assertions (`assertEqual`, `assertRaises`, etc.) for clear failure messages
- `setUp` / `tearDown` run before/after **each** test; `setUpClass` / `tearDownClass` run once per class
- Run tests with `python3 -m unittest` or the `unittest.main()` pattern
- Test discovery (`python3 -m unittest discover`) finds all `test*.py` files automatically
- Use `assertRaises` as a context manager to cleanly test exception handling
- Writing tests early saves you from painful debugging later
