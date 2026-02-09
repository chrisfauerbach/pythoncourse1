# Mocking

## Objective

Learn how to isolate your code from external dependencies during testing using Python's built-in `unittest.mock` library. By the end of this lesson, you'll be able to replace API calls, file reads, database queries, and other side effects with controlled mock objects — so your tests are fast, reliable, and focused on *your* code.

## Concepts Covered

- What mocking is and why you need it
- `unittest.mock` — Python's built-in mocking library
- `Mock` objects — creating and using them
- Mock attributes and return values (`.return_value`, `.side_effect`)
- Asserting calls: `.assert_called_once()`, `.assert_called_with()`, `.call_count`
- `@patch` decorator — replacing real objects during tests
- `patch` as a context manager
- Where to patch (patch where it's *used*, not where it's *defined*)
- `MagicMock` vs `Mock`
- Mocking common things: API calls, file operations, `datetime.now`
- `side_effect` for multiple return values or raising exceptions
- The `spec` parameter — making mocks match real interfaces

## Prerequisites

- Comfortable with functions, classes, and imports
- Basic understanding of `unittest` (TestCase, assertions, running tests)
- Familiarity with how Python imports work

## Lesson

### What Is Mocking and Why Do You Need It?

Imagine you wrote a function that fetches weather data from an API, parses it, and returns a nice summary. You want to test it. But every time you run your test, it makes a real HTTP request. That means:

- Your tests are **slow** (network round-trip every time)
- Your tests are **flaky** (API is down? Test fails. Rate limited? Test fails.)
- Your tests are **unpredictable** (the weather changes! Your assertions break.)
- You might be **charged money** (paid APIs, cloud services)

Mocking solves all of this. Instead of calling the real API, you replace it with a fake object that instantly returns whatever data you tell it to. Your test now only checks *your* logic — not whether the internet is working.

```python
# Without mocking — fragile, slow, unpredictable
def test_weather_summary():
    result = get_weather_summary("London")  # Makes a REAL API call!
    assert "London" in result               # Fails if API is down

# With mocking — fast, reliable, controlled
def test_weather_summary(mock_api):
    mock_api.return_value = {"temp": 20, "condition": "Sunny"}
    result = get_weather_summary("London")  # Calls the MOCK, not the API
    assert result == "London: 20C and Sunny"
```

The rule of thumb: **mock the things you don't own** — APIs, databases, file systems, the current time, email servers, etc.

### unittest.mock — Python's Built-in Mocking Library

Python ships with a powerful mocking library. No need to install anything:

```python
from unittest.mock import Mock, MagicMock, patch
```

That's your toolkit. Let's go through each piece.

### Mock Objects — Creating and Using Mock()

A `Mock` object is a chameleon. It accepts any attribute access, any method call, any argument — and records everything that happened to it.

```python
from unittest.mock import Mock

mock = Mock()

# You can call it like a function
mock(1, 2, 3)

# You can access any attribute
mock.some_attribute

# You can chain calls endlessly
mock.foo.bar.baz()

# None of this raises an error — Mock accepts EVERYTHING
```

This is the key insight: a Mock says "yes" to everything, while quietly recording what happened. You can then check those recordings in your assertions.

### Mock Attributes and Return Values

#### .return_value — Control What the Mock Returns

```python
mock = Mock()
mock.return_value = 42

result = mock()  # Returns 42
print(result)    # 42
```

You can also set return values on methods:

```python
mock = Mock()
mock.calculate.return_value = 100

result = mock.calculate(5, 20)  # Returns 100
```

#### .side_effect — Do Something When Called

`side_effect` is more powerful. It can:

**Raise an exception:**
```python
mock = Mock()
mock.side_effect = ConnectionError("Server is down")

mock()  # Raises ConnectionError!
```

**Return different values on each call:**
```python
mock = Mock()
mock.side_effect = [1, 2, 3]

mock()  # Returns 1
mock()  # Returns 2
mock()  # Returns 3
```

**Run a custom function:**
```python
mock = Mock()
mock.side_effect = lambda x: x * 2

mock(5)   # Returns 10
mock(21)  # Returns 42
```

### Asserting Calls — Did the Mock Get Used Correctly?

Mocks remember how they were called. You can assert on that:

```python
mock = Mock()
mock("hello", count=3)

# Was it called at all?
mock.assert_called()           # Passes

# Was it called exactly once?
mock.assert_called_once()      # Passes

# Was it called with these exact arguments?
mock.assert_called_with("hello", count=3)      # Passes
mock.assert_called_once_with("hello", count=3) # Passes

# How many times was it called?
print(mock.call_count)  # 1

# What were all the calls?
print(mock.call_args_list)  # [call('hello', count=3)]
```

If an assertion fails, you get a clear error message telling you what was expected vs. what actually happened.

### @patch Decorator — Replacing Real Objects During Tests

This is where it all comes together. `@patch` temporarily replaces a real object with a Mock during a test, and automatically restores it afterward.

```python
import unittest
from unittest.mock import patch

# Your production code
def get_user_greeting(user_id):
    user = fetch_user_from_database(user_id)  # We want to mock THIS
    return f"Hello, {user['name']}!"

# Your test
class TestGreeting(unittest.TestCase):

    @patch("mymodule.fetch_user_from_database")
    def test_greeting(self, mock_fetch):
        mock_fetch.return_value = {"name": "Alice"}

        result = get_user_greeting(42)

        self.assertEqual(result, "Hello, Alice!")
        mock_fetch.assert_called_once_with(42)
```

The `@patch` decorator injects the mock as an extra argument to your test method. When the test finishes, the real function is automatically restored.

You can stack multiple `@patch` decorators — they inject arguments bottom-up:

```python
@patch("mymodule.send_email")       # Becomes mock_email (2nd mock arg)
@patch("mymodule.fetch_user")       # Becomes mock_fetch (1st mock arg)
def test_something(self, mock_fetch, mock_email):
    # mock_fetch replaces fetch_user
    # mock_email replaces send_email
    pass
```

### patch as a Context Manager

Don't want to use decorators? Use `with`:

```python
def test_something(self):
    with patch("mymodule.fetch_user") as mock_fetch:
        mock_fetch.return_value = {"name": "Bob"}
        result = get_user_greeting(1)
        self.assertEqual(result, "Hello, Bob!")

    # Outside the `with` block, the real function is restored
```

This is handy when you only need the mock for part of your test, or when you're not inside a `TestCase` class.

### Where to Patch — The Most Common Gotcha

This trips up everyone at first. You patch where something is **used**, not where it's **defined**.

```python
# utils.py
def get_timestamp():
    return datetime.now().isoformat()

# report.py
from utils import get_timestamp   # <-- get_timestamp is now IN report's namespace

def generate_report():
    return f"Report generated at {get_timestamp()}"
```

```python
# test_report.py

# WRONG — this patches the original, but report.py already imported its own copy
@patch("utils.get_timestamp")

# RIGHT — patch where it's USED (in the report module)
@patch("report.get_timestamp")
```

When you do `from utils import get_timestamp`, the `report` module gets its own reference to that function. Patching the original in `utils` doesn't affect report's copy. You have to patch `report.get_timestamp` instead.

### MagicMock vs Mock

`MagicMock` is a subclass of `Mock` that comes with pre-built support for Python's magic methods (`__len__`, `__iter__`, `__getitem__`, etc.):

```python
from unittest.mock import Mock, MagicMock

# Regular Mock — magic methods don't work by default
mock = Mock()
# len(mock)  # TypeError!

# MagicMock — magic methods work out of the box
magic = MagicMock()
magic.__len__.return_value = 5
print(len(magic))  # 5

magic.__getitem__.return_value = "hello"
print(magic[0])    # "hello"

magic.__iter__.return_value = iter([1, 2, 3])
print(list(magic))  # [1, 2, 3]
```

In practice: `@patch` uses `MagicMock` by default, so you usually don't need to think about this. Use plain `Mock()` when you're creating standalone mocks manually and don't need magic method support.

### Mocking Common Things

#### API Calls (with requests)

```python
@patch("mymodule.requests.get")
def test_api_call(self, mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temp": 22}

    result = fetch_weather("London")
    self.assertEqual(result["temp"], 22)
```

#### File Operations (builtins.open)

```python
from unittest.mock import mock_open

@patch("builtins.open", mock_open(read_data="name=Alice\nage=30"))
def test_read_config(self):
    result = read_config("settings.txt")
    self.assertEqual(result["name"], "Alice")
```

#### datetime.now()

```python
from datetime import datetime

@patch("mymodule.datetime")
def test_time_dependent(self, mock_dt):
    mock_dt.now.return_value = datetime(2025, 12, 25, 10, 0, 0)

    result = get_greeting()
    self.assertEqual(result, "Good morning!")
```

### side_effect — Advanced Patterns

#### Simulate a Retry Scenario

```python
mock_api = Mock()
mock_api.side_effect = [
    ConnectionError("timeout"),   # First call fails
    ConnectionError("timeout"),   # Second call fails
    {"status": "ok"},             # Third call succeeds
]

# If your code has retry logic, this tests it perfectly
```

#### Validate Arguments Dynamically

```python
def check_positive(n):
    if n < 0:
        raise ValueError("Must be positive")
    return n * 2

mock = Mock(side_effect=check_positive)
mock(5)   # Returns 10
mock(-1)  # Raises ValueError
```

### The spec Parameter — Making Mocks Match Real Interfaces

Plain mocks accept any attribute. That's a problem — you might have a typo in your test and never catch it:

```python
mock = Mock()
mock.send_emial("test")  # Typo! But Mock doesn't complain...
mock.send_emial.assert_called_once()  # "Test passes" but it's testing nothing useful
```

Use `spec` to make the mock match a real class's interface:

```python
class EmailSender:
    def send_email(self, to, subject, body):
        pass

mock = Mock(spec=EmailSender)
mock.send_email("a@b.com", "Hi", "Hello")  # Works fine
mock.send_emial("a@b.com", "Hi", "Hello")  # AttributeError! Catches the typo.
```

You can also use `spec` with `@patch`:

```python
@patch("mymodule.EmailSender", spec=EmailSender)
def test_something(self, MockEmailSender):
    pass
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates all the mocking techniques above — tested against realistic code with external dependencies.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding. You'll mock API calls, file reads, time functions, and more.

## Key Takeaways

- **Mocking replaces external dependencies** with fake objects you control — making tests fast, reliable, and isolated
- Use `Mock()` for general-purpose mocks; `MagicMock()` when you need magic method support
- `.return_value` controls what a mock returns; `.side_effect` lets you raise exceptions, return sequences, or run custom logic
- `@patch` temporarily replaces real objects during a test and auto-restores them when done
- **Patch where it's used, not where it's defined** — this is the most common mistake
- Use `mock_open` for faking file operations
- Use `spec` to make mocks match real interfaces and catch typos
- Assert on calls with `.assert_called_once()`, `.assert_called_with()`, and `.call_count`
- Only mock what you need — over-mocking makes tests brittle and hard to understand
