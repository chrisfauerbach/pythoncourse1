# Error Handling

## Objective

Learn how to handle errors gracefully in Python using `try`/`except`, understand the exception hierarchy, raise your own exceptions, and write code that doesn't crash when the unexpected happens.

## Concepts Covered

- Exceptions vs syntax errors
- `try`/`except` basics
- Catching specific exceptions (and why bare `except` is bad)
- Multiple `except` blocks
- Catching multiple exceptions in one block
- The `else` clause
- The `finally` clause
- Accessing the exception object with `as e`
- Raising exceptions with `raise`
- Creating custom exceptions
- Exception chaining with `raise ... from ...`
- Common built-in exceptions
- LBYL vs EAFP

## Prerequisites

- Functions
- Basic file I/O concepts
- Dictionaries

## Lesson

### Exceptions vs Syntax Errors

Python has two kinds of errors, and they're very different:

**Syntax errors** happen *before* your code runs. Python reads your file, sees something that isn't valid Python, and refuses to even start:

```python
# SyntaxError — Python can't parse this
print("hello"
```

**Exceptions** happen *while* your code is running. The syntax is fine, but something goes wrong at runtime:

```python
# This is valid Python, but it blows up when you run it
result = 10 / 0  # ZeroDivisionError
```

This lesson is all about exceptions — how to catch them, raise them, and handle them like a pro.

### try/except Basics

The `try`/`except` block is Python's way of saying "try this, and if it blows up, do this instead":

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

Python tries to run everything in the `try` block. If an exception is raised, it jumps immediately to the matching `except` block. If no exception happens, the `except` block is skipped entirely.

### Catching Specific Exceptions (and Why Bare `except` Is Bad)

You should always catch *specific* exception types. A bare `except:` with no exception type catches **everything** — including things you probably don't want to catch, like `KeyboardInterrupt` (when the user presses Ctrl+C) or `SystemExit`:

```python
# BAD — don't do this
try:
    result = int(user_input)
except:  # Catches EVERYTHING, even Ctrl+C!
    print("Something went wrong")

# GOOD — catch what you expect
try:
    result = int(user_input)
except ValueError:
    print("That's not a valid number")
```

The rule is simple: only catch exceptions you know how to handle. Let the rest bubble up so you can see them and fix the real problem.

### Multiple except Blocks

You can handle different exception types differently by stacking `except` blocks:

```python
try:
    value = my_dict[key]
    result = 10 / value
except KeyError:
    print(f"Key '{key}' not found in dictionary")
except ZeroDivisionError:
    print("Can't divide by zero")
```

Python checks them in order and runs the *first* one that matches. Once a match is found, the rest are skipped.

### Catching Multiple Exceptions in One Block

If you want to handle several exception types the same way, group them in a tuple:

```python
try:
    value = int(user_input)
    result = 100 / value
except (ValueError, ZeroDivisionError):
    print("Invalid input — need a non-zero integer")
```

Note the parentheses — they're required. Without them, you'd get a syntax error.

### The else Clause

The `else` block runs only if the `try` block completed *without* raising an exception. It's a great place to put code that should only execute on success:

```python
try:
    result = int(user_input)
except ValueError:
    print("Not a number!")
else:
    print(f"You entered: {result}")  # Only runs if conversion succeeded
```

Why not just put that code in the `try` block? Because `else` keeps your `try` block small and focused. You only wrap the code that might fail — the rest goes in `else`.

### The finally Clause

The `finally` block *always* runs, no matter what — whether the code succeeded, raised an exception, or even if you `return` from inside the `try`. It's the place for cleanup:

```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    # This runs no matter what — close the file if it was opened
    print("Cleanup complete")
```

The classic use case is closing files, releasing locks, or cleaning up resources. (Though for files, the `with` statement is usually better.)

### Accessing the Exception Object with `as e`

You can capture the exception object to get more details about what went wrong:

```python
try:
    result = int("not_a_number")
except ValueError as e:
    print(f"Error: {e}")   # Error: invalid literal for int() with base 10: 'not_a_number'
    print(f"Type: {type(e).__name__}")  # Type: ValueError
```

The `as e` part gives you a variable (you can name it anything — `e`, `err`, `exc` are all common) that holds the actual exception instance. You can print it, log it, inspect its attributes, or re-raise it.

### Raising Exceptions with raise

You can raise exceptions yourself using the `raise` keyword:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return age
```

This is how you tell callers of your function "hey, you gave me something I can't work with." The caller can then catch it with `try`/`except`.

You can also re-raise the current exception inside an `except` block using bare `raise`:

```python
try:
    risky_operation()
except ValueError:
    print("Logging this error...")
    raise  # Re-raises the same exception so it keeps propagating
```

### Creating Custom Exceptions

For your own libraries and applications, you can define custom exception classes. Just inherit from `Exception` (or a more specific built-in exception):

```python
class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ${amount:.2f} — balance is ${balance:.2f}")
```

Custom exceptions make your error handling more readable and let callers catch *your* specific errors without accidentally catching unrelated ones.

### Exception Chaining with `raise ... from ...`

When you catch one exception and raise a different one, you can link them together so the context isn't lost:

```python
try:
    value = config_dict["timeout"]
except KeyError as e:
    raise ApplicationError("Missing required config: 'timeout'") from e
```

The `from e` part attaches the original `KeyError` as the "cause" of the new `ApplicationError`. When Python prints the traceback, it shows both — so you get a friendly message *and* the original context.

You can also use `raise ... from None` to suppress the chained context entirely, which is useful when the original exception is just noise.

### Common Built-in Exceptions

Here are the ones you'll run into most often:

| Exception | When It Happens |
|---|---|
| `ValueError` | Right type, wrong value — e.g., `int("abc")` |
| `TypeError` | Wrong type — e.g., `"hello" + 5` |
| `KeyError` | Dictionary key doesn't exist — e.g., `d["nope"]` |
| `IndexError` | List index out of range — e.g., `[1,2,3][10]` |
| `FileNotFoundError` | File doesn't exist — e.g., `open("nope.txt")` |
| `AttributeError` | Object doesn't have that attribute — e.g., `"hello".append("x")` |
| `ZeroDivisionError` | Division by zero — e.g., `1 / 0` |
| `NameError` | Variable doesn't exist — e.g., using `x` before defining it |
| `ImportError` | Module can't be imported — e.g., `import nonexistent_module` |
| `StopIteration` | Iterator is exhausted — usually handled by `for` loops automatically |
| `RuntimeError` | Generic error that doesn't fit other categories |
| `OSError` | OS-level error — file permissions, disk full, etc. |

All exceptions inherit from `BaseException`. Most inherit from `Exception`, which is why you should inherit from `Exception` for custom exceptions (not `BaseException`).

### LBYL vs EAFP

Two philosophies for dealing with things that might go wrong:

**LBYL — Look Before You Leap**: Check whether something will work before trying it.

```python
# LBYL style
if key in my_dict:
    value = my_dict[key]
else:
    value = "default"
```

**EAFP — Easier to Ask Forgiveness than Permission**: Just try it, and handle the error if it happens.

```python
# EAFP style
try:
    value = my_dict[key]
except KeyError:
    value = "default"
```

Python strongly favors the EAFP style. It's considered more "Pythonic" for a few reasons:

- It avoids race conditions (the thing you checked might change between the check and the action)
- It's often faster when the error is rare (no overhead from the check in the happy path)
- It keeps the "normal" code path front and center

That said, use your judgment. For simple checks like `if x is not None`, LBYL is perfectly fine and more readable.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Use `try`/`except` to catch exceptions — always catch *specific* types, never bare `except`
- `else` runs when no exception occurred; `finally` always runs (great for cleanup)
- Use `as e` to access details about the exception
- Raise exceptions with `raise` to signal errors in your own code
- Create custom exceptions by inheriting from `Exception`
- Use `raise ... from ...` to chain exceptions and preserve context
- Python prefers EAFP (try it and handle errors) over LBYL (check first)
- Only catch exceptions you know how to handle — let the rest propagate
