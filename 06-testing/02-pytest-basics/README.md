# pytest Basics

## Objective

Learn pytest — the testing framework that most Python developers actually use. You'll write tests with plain functions and `assert` statements, use fixtures for setup, parametrize tests to cover multiple cases, and understand the options that make pytest a joy to work with.

## Concepts Covered

- What pytest is and why it's the community standard
- Installing pytest
- Writing tests with plain functions and `assert`
- Running pytest from the command line
- Fixtures for setup and teardown
- Fixture scopes
- Parametrize — one test, many inputs
- Testing exceptions with `pytest.raises`
- Markers (`skip`, `xfail`, custom)
- `conftest.py` for shared fixtures
- Useful command-line options
- pytest vs unittest comparison

## Prerequisites

- Basic Python (functions, classes, exceptions)
- Helpful but not required: the unittest lesson (01-unittest-basics)

## Lesson

### What is pytest and Why Use It?

pytest is a testing framework for Python that makes writing tests feel natural. While Python ships with `unittest` in the standard library, pytest has become the community standard because it's simpler, more powerful, and honestly more fun to use.

The key insight: **you don't need classes, special methods, or a special API**. Just write functions that start with `test_` and use plain `assert` statements. That's it.

Why the community chose pytest over unittest:

- **Less boilerplate** — no classes or inheritance required
- **Plain assert** — no memorizing `assertEqual`, `assertTrue`, `assertIn`, etc.
- **Better failure output** — pytest shows you exactly what went wrong
- **Fixtures** — way more flexible than `setUp()`/`tearDown()`
- **Parametrize** — run the same test with different data in one decorator
- **Huge plugin ecosystem** — 1000+ plugins for every need imaginable

### Installing pytest

pytest doesn't come with Python — you need to install it:

```bash
pip install pytest
```

Verify it's installed:

```bash
pytest --version
```

### Writing Your First Test

Here's the simplest possible test:

```python
def test_addition():
    assert 1 + 1 == 2
```

That's a complete, runnable test. No imports needed (for this simple case), no classes, no `self.assertEqual()`. Just a function whose name starts with `test_` and a plain `assert` statement.

Let's test an actual function:

```python
def square(n):
    return n * n

def test_square_positive():
    assert square(3) == 9

def test_square_zero():
    assert square(0) == 0

def test_square_negative():
    assert square(-4) == 16
```

Save that in a file called `test_math.py`, run `pytest`, and you're done.

### The `assert` Statement — No Special Methods Needed

This is one of pytest's best features. You don't need to memorize different assertion methods. You just use `assert`:

```python
# Equality
assert result == 42

# Truthiness
assert is_valid

# Membership
assert "alice" in user_list

# Comparisons
assert len(items) > 0
assert response.status_code == 200

# With a message (shown on failure)
assert result == 42, f"Expected 42 but got {result}"
```

When a test fails, pytest uses introspection to give you a detailed breakdown of *what* was compared and *why* it failed. You get way more information than a basic `AssertionError` — pytest rewrites the assert to show you the actual values on both sides.

### Running pytest

pytest discovers tests automatically. It looks for files named `test_*.py` or `*_test.py`, and within those files, it runs functions named `test_*` and methods named `test_*` inside classes named `Test*`.

```bash
# Run all tests in the current directory (and subdirectories)
pytest

# Verbose mode — see each test name and its result
pytest -v

# Run a specific file
pytest test_math.py

# Run a specific test function in a file
pytest test_math.py::test_square_positive

# Run a specific method inside a test class
pytest test_math.py::TestCalculator::test_add
```

### Fixtures — Setup and Teardown the pytest Way

In unittest, you use `setUp()` and `tearDown()` methods. In pytest, you use **fixtures** — and they're much more flexible.

A fixture is a function decorated with `@pytest.fixture` that provides data or resources to your tests:

```python
import pytest

@pytest.fixture
def sample_list():
    """Provides a fresh list for each test."""
    return [1, 2, 3, 4, 5]

def test_list_length(sample_list):
    assert len(sample_list) == 5

def test_list_sum(sample_list):
    assert sum(sample_list) == 15
```

Here's the magic: your test function *asks* for the fixture by including it as a parameter. pytest sees the parameter name, finds a fixture with the same name, calls it, and injects the return value. Each test gets a fresh copy.

#### Fixtures with Teardown (yield)

Need cleanup after a test? Use `yield` instead of `return`. Code after `yield` runs after the test completes:

```python
import pytest

@pytest.fixture
def temp_file():
    # Setup — runs before the test
    f = open("test_output.txt", "w")
    f.write("test data")
    f.close()

    yield "test_output.txt"  # This value gets passed to the test

    # Teardown — runs after the test, even if it fails
    import os
    os.remove("test_output.txt")
```

#### Fixtures That Use Other Fixtures

Fixtures can depend on other fixtures — pytest handles the chain automatically:

```python
@pytest.fixture
def database_connection():
    conn = create_connection()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database_connection):
    database_connection.execute("CREATE TABLE users ...")
    yield database_connection
    database_connection.execute("DROP TABLE users")
```

### Fixture Scopes

By default, a fixture runs once per test function. You can change this with the `scope` parameter:

```python
@pytest.fixture(scope="function")   # Default — fresh for each test
def fresh_data():
    return {"count": 0}

@pytest.fixture(scope="class")      # Once per test class
def shared_resource():
    return ExpensiveResource()

@pytest.fixture(scope="module")     # Once per test file
def db_connection():
    conn = connect_to_db()
    yield conn
    conn.close()

@pytest.fixture(scope="session")    # Once for the ENTIRE test run
def app_config():
    return load_config("test_config.yaml")
```

Use higher scopes for expensive resources (database connections, API clients). But be careful — tests that share state can lead to subtle, hard-to-debug failures.

### Parametrize — Run the Same Test with Different Data

Instead of writing five nearly identical test functions, use `@pytest.mark.parametrize`:

```python
import pytest

@pytest.mark.parametrize("input_val, expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (0, 0),
    (-3, 9),
])
def test_square(input_val, expected):
    assert square(input_val) == expected
```

This creates **five separate tests**, each with its own name and pass/fail status. In verbose mode you'll see:

```
test_math.py::test_square[1-1] PASSED
test_math.py::test_square[2-4] PASSED
test_math.py::test_square[3-9] PASSED
test_math.py::test_square[0-0] PASSED
test_math.py::test_square[-3-9] PASSED
```

You can parametrize with any number of arguments:

```python
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Testing Exceptions with `pytest.raises`

When you *expect* code to raise an exception, use `pytest.raises` as a context manager:

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# You can also check the exception message
def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)

# Or capture the exception for further inspection
def test_divide_by_zero_details():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert "zero" in str(exc_info.value)
```

### Markers

Markers let you tag tests with metadata. pytest comes with several built-in markers, and you can create your own.

#### `@pytest.mark.skip` — Skip a test entirely

```python
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    assert some_new_function() == 42
```

#### `@pytest.mark.skipif` — Skip conditionally

```python
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Unix only")
def test_unix_permissions():
    ...
```

#### `@pytest.mark.xfail` — Expected failure

```python
@pytest.mark.xfail(reason="Known bug — issue #123")
def test_known_broken():
    assert broken_function() == "correct"
```

If the test fails, it's reported as `xfail` (expected failure). If it unexpectedly *passes*, it's reported as `xpass` — handy for knowing when a bug gets fixed.

#### Custom Markers

You can invent your own markers to categorize tests:

```python
@pytest.mark.slow
def test_heavy_computation():
    ...

@pytest.mark.integration
def test_database_query():
    ...
```

Then run only tests with (or without) specific markers:

```bash
pytest -m slow
pytest -m "not slow"
pytest -m "slow or integration"
```

Register custom markers in `pyproject.toml` or `pytest.ini` to avoid warnings.

### `conftest.py` — Shared Fixtures Across Files

When multiple test files need the same fixtures, put them in a file called `conftest.py`. pytest discovers it automatically — no import needed.

```
tests/
    conftest.py          # Fixtures available to ALL test files below
    test_users.py
    test_orders.py
    api/
        conftest.py      # Additional fixtures just for api/ tests
        test_endpoints.py
```

```python
# conftest.py
import pytest

@pytest.fixture
def sample_user():
    return {"name": "Alice", "email": "alice@example.com"}

@pytest.fixture
def auth_token():
    return "test-token-12345"
```

Now every test file in that directory (and subdirectories) can use `sample_user` and `auth_token` as parameters without importing anything. This is one of pytest's most powerful features for keeping test code DRY.

### Useful pytest Options

Here are the command-line options you'll reach for most often:

```bash
# Verbose — show each test name and result
pytest -v

# Stop on first failure — great for debugging
pytest -x

# Stop after N failures
pytest --maxfail=3

# Filter by keyword expression (matches test names)
pytest -k "square"                    # Run tests with "square" in the name
pytest -k "square and not negative"   # Combine with logic

# Short traceback — less noise on failures
pytest --tb=short

# Show print() output (normally captured/hidden)
pytest -s

# Show local variables in tracebacks
pytest -l

# Run only tests that failed last time
pytest --lf

# Run last-failed tests first, then the rest
pytest --ff

# Quiet mode — just the summary
pytest -q
```

You can combine them:

```bash
pytest -v -x --tb=short -k "not slow"
```

### pytest vs unittest — Quick Comparison

| Feature | unittest | pytest |
|---|---|---|
| Test structure | Classes inheriting `TestCase` | Plain functions |
| Assertions | `self.assertEqual(a, b)` | `assert a == b` |
| Setup/Teardown | `setUp()` / `tearDown()` methods | Fixtures (way more flexible) |
| Parametrize | No built-in support | `@pytest.mark.parametrize` |
| Test discovery | Needs test runner config | Automatic |
| Output on failure | Basic | Rich, detailed diffs |
| Plugins | Limited | Huge ecosystem (1000+ plugins) |
| Compatibility | -- | Runs unittest tests too! |

One important note: **pytest can run unittest-style tests**. So if you have existing unittest tests, you can switch to pytest as your test runner immediately and migrate gradually.

## Code Example

Check out [`example.py`](example.py) for a complete working example showing tests you can run with `pytest example.py -v` or `python3 example.py`.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- pytest is the community standard — simpler and more powerful than unittest
- Write test functions (not classes) with names starting with `test_`
- Use plain `assert` statements — pytest gives you detailed failure output for free
- Fixtures replace setUp/tearDown and are far more flexible (dependency injection, scopes, yield for cleanup)
- `@pytest.mark.parametrize` eliminates repetitive test functions — one test, many inputs
- `pytest.raises` is the clean way to test that exceptions are raised
- `conftest.py` shares fixtures across test files without imports
- pytest can run your existing unittest tests — migration is painless
- The `-v`, `-x`, `-k`, and `--tb=short` flags will become second nature
