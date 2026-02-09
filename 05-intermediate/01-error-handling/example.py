"""
Error Handling — Example Code
================================

Run this file:
    python3 example.py

Learn how to catch, raise, and handle exceptions in Python. This file walks
through every concept in the lesson with practical, runnable examples.
"""

# -----------------------------------------------------------------------------
# 1. Exceptions vs syntax errors
# -----------------------------------------------------------------------------

# Syntax errors are caught before your code runs — you can't catch them with
# try/except. Here's what an exception looks like at runtime:

print("--- 1. Exceptions at runtime ---")

# This would crash the program if we didn't catch it:
# result = 10 / 0  # ZeroDivisionError!

# Instead, let's see a few exceptions in action (safely):
print("10 / 0 would raise: ZeroDivisionError")
print("int('abc') would raise: ValueError")
print("{}['nope'] would raise: KeyError")
print()

# -----------------------------------------------------------------------------
# 2. try/except basics
# -----------------------------------------------------------------------------

print("--- 2. try/except basics ---")

# Try something risky — if it fails, handle it gracefully
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught a ZeroDivisionError — can't divide by zero!")

# If no exception occurs, the except block is simply skipped
try:
    result = 10 / 2
except ZeroDivisionError:
    print("This won't print — no error occurred")

print(f"10 / 2 = {result}")
print()

# -----------------------------------------------------------------------------
# 3. Catching specific exceptions (and why bare except is bad)
# -----------------------------------------------------------------------------

print("--- 3. Why bare except is bad ---")

# BAD EXAMPLE — bare except catches everything, even Ctrl+C and SystemExit.
# Don't do this in real code:
#
# try:
#     result = int("oops")
# except:
#     print("Something went wrong")  # Too vague! What went wrong?

# GOOD — catch the specific exception you expect:
user_input = "not_a_number"
try:
    result = int(user_input)
except ValueError:
    print(f"ValueError caught: '{user_input}' is not a valid integer")

print()

# -----------------------------------------------------------------------------
# 4. Multiple except blocks
# -----------------------------------------------------------------------------

print("--- 4. Multiple except blocks ---")

# Different exceptions can be handled differently
test_cases = [
    ({"a": 1, "b": 0}, "b"),  # Will cause ZeroDivisionError
    ({"a": 1, "b": 2}, "c"),  # Will cause KeyError
    ({"a": 1, "b": 2}, "b"),  # Will succeed
]

for data, key in test_cases:
    try:
        value = data[key]
        result = 10 / value
    except KeyError:
        print(f"  KeyError: key '{key}' not found in {data}")
    except ZeroDivisionError:
        print(f"  ZeroDivisionError: data['{key}'] is zero, can't divide")
    else:
        print(f"  Success: 10 / data['{key}'] = {result}")

print()

# -----------------------------------------------------------------------------
# 5. Catching multiple exceptions in one block
# -----------------------------------------------------------------------------

print("--- 5. Multiple exceptions in one block ---")

# When you want to handle several exception types the same way,
# group them in a tuple:
inputs = ["42", "zero", "0"]

for inp in inputs:
    try:
        value = int(inp)
        result = 100 / value
    except (ValueError, ZeroDivisionError) as e:
        print(f"  Bad input '{inp}': {type(e).__name__} — {e}")
    else:
        print(f"  100 / {value} = {result}")

print()

# -----------------------------------------------------------------------------
# 6. The else clause — runs only on success
# -----------------------------------------------------------------------------

print("--- 6. The else clause ---")

# else runs ONLY if the try block completes without an exception.
# It keeps your try block small — only wrap the risky part.

numbers = ["10", "abc", "7"]

for num_str in numbers:
    try:
        number = int(num_str)
    except ValueError:
        print(f"  '{num_str}' is not a valid number — skipping")
    else:
        # This only runs if int() succeeded
        doubled = number * 2
        print(f"  '{num_str}' -> {number} -> doubled = {doubled}")

print()

# -----------------------------------------------------------------------------
# 7. The finally clause — always runs
# -----------------------------------------------------------------------------

print("--- 7. The finally clause ---")

# finally runs no matter what — success, failure, even if you return.
# Great for cleanup tasks.

def read_first_line(filename):
    """Try to read the first line of a file."""
    f = None
    try:
        f = open(filename)
        return f.readline().strip()
    except FileNotFoundError:
        return "(file not found)"
    finally:
        if f is not None:
            f.close()
            print(f"  (closed file handle for '{filename}')")

# This will fail gracefully
result = read_first_line("nonexistent_file.txt")
print(f"  Result: {result}")

print()

# -----------------------------------------------------------------------------
# 8. Accessing the exception object with `as e`
# -----------------------------------------------------------------------------

print("--- 8. Accessing the exception object ---")

try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError as e:
    print(f"  Exception type: {type(e).__name__}")
    print(f"  Exception message: {e}")
    print(f"  Exception args: {e.args}")

# Works with any exception type
try:
    result = int("hello")
except ValueError as e:
    print(f"  Caught ValueError: {e}")

print()

# -----------------------------------------------------------------------------
# 9. Raising exceptions with raise
# -----------------------------------------------------------------------------

print("--- 9. Raising exceptions ---")

def set_age(age):
    """Set a person's age with validation."""
    if not isinstance(age, (int, float)):
        raise TypeError(f"Age must be a number, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative, got {age}")
    if age > 150:
        raise ValueError(f"Age {age} seems unrealistic")
    return int(age)

# Test with valid and invalid ages
test_ages = [25, -5, 200, "old"]

for age in test_ages:
    try:
        result = set_age(age)
        print(f"  set_age({age!r}) = {result}")
    except (ValueError, TypeError) as e:
        print(f"  set_age({age!r}) raised {type(e).__name__}: {e}")

# Re-raising an exception (bare raise)
print()
print("  Re-raising example:")
try:
    try:
        int("oops")
    except ValueError:
        print("  Caught ValueError, logging and re-raising...")
        raise  # Re-raises the same exception
except ValueError as e:
    print(f"  Caught it again at the outer level: {e}")

print()

# -----------------------------------------------------------------------------
# 10. Creating custom exceptions
# -----------------------------------------------------------------------------

print("--- 10. Custom exceptions ---")

# Simple custom exception — just a new name
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the account balance."""
    pass

# Custom exception with extra data
class WithdrawalError(Exception):
    """Raised when a withdrawal fails."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.deficit = amount - balance
        super().__init__(
            f"Cannot withdraw ${amount:.2f} — "
            f"balance is ${balance:.2f} "
            f"(short by ${self.deficit:.2f})"
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise WithdrawalError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(100.00)

# Successful withdrawal
try:
    remaining = account.withdraw(30.00)
    print(f"  Withdrew $30.00 — remaining: ${remaining:.2f}")
except WithdrawalError as e:
    print(f"  {e}")

# Failed withdrawal
try:
    remaining = account.withdraw(500.00)
    print(f"  Withdrew $500.00 — remaining: ${remaining:.2f}")
except WithdrawalError as e:
    print(f"  {e}")
    print(f"  (Short by: ${e.deficit:.2f})")

print()

# -----------------------------------------------------------------------------
# 11. Exception chaining with raise ... from ...
# -----------------------------------------------------------------------------

print("--- 11. Exception chaining ---")

class ConfigError(Exception):
    """Raised when configuration is invalid or missing."""
    pass

def get_timeout(config):
    """Get the timeout value from a config dict."""
    try:
        return int(config["timeout"])
    except KeyError as e:
        # Chain the original KeyError as the "cause"
        raise ConfigError("Missing required config key: 'timeout'") from e
    except ValueError as e:
        raise ConfigError(f"Invalid timeout value: {config['timeout']!r}") from e

# Test with missing key
try:
    get_timeout({"retries": 3})
except ConfigError as e:
    print(f"  ConfigError: {e}")
    print(f"  Original cause: {type(e.__cause__).__name__}: {e.__cause__}")

# Test with invalid value
try:
    get_timeout({"timeout": "slow"})
except ConfigError as e:
    print(f"  ConfigError: {e}")
    print(f"  Original cause: {type(e.__cause__).__name__}: {e.__cause__}")

print()

# -----------------------------------------------------------------------------
# 12. Common built-in exceptions — a quick tour
# -----------------------------------------------------------------------------

print("--- 12. Common built-in exceptions ---")

# Let's trigger each one safely and show what they look like
common_errors = [
    ("ValueError",        lambda: int("abc")),
    ("TypeError",         lambda: "hello" + 5),
    ("KeyError",          lambda: {}["missing"]),
    ("IndexError",        lambda: [1, 2, 3][10]),
    ("AttributeError",    lambda: "hello".append("x")),
    ("ZeroDivisionError", lambda: 1 / 0),
    ("FileNotFoundError", lambda: open("this_file_does_not_exist_12345.txt")),
]

for name, trigger in common_errors:
    try:
        trigger()
    except Exception as e:
        print(f"  {type(e).__name__:>22}: {e}")

print()

# -----------------------------------------------------------------------------
# 13. LBYL vs EAFP
# -----------------------------------------------------------------------------

print("--- 13. LBYL vs EAFP ---")

data = {"name": "Alice", "age": 30}

# LBYL — Look Before You Leap
# Check first, then act
print("  LBYL style:")
key = "email"
if key in data:
    print(f"    {key} = {data[key]}")
else:
    print(f"    '{key}' not found — using default")

# EAFP — Easier to Ask Forgiveness than Permission
# Just try it, handle the error if it happens
print("  EAFP style:")
try:
    print(f"    email = {data['email']}")
except KeyError:
    print(f"    'email' not found — using default")

# Both approaches work. Python generally prefers EAFP because:
# 1. It avoids race conditions (no gap between check and action)
# 2. It's faster when errors are rare (no check overhead)
# 3. The "happy path" reads clearly

print()

# -----------------------------------------------------------------------------
# 14. The full try/except/else/finally — all together
# -----------------------------------------------------------------------------

print("--- 14. Full try/except/else/finally ---")

def safe_divide(a, b):
    """Demonstrates all four clauses working together."""
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  except: Can't divide {a} by zero")
        return None
    except TypeError as e:
        print(f"  except: Wrong types — {e}")
        return None
    else:
        print(f"  else: {a} / {b} = {result}")
        return result
    finally:
        print(f"  finally: safe_divide({a!r}, {b!r}) finished")

safe_divide(10, 3)
print()
safe_divide(10, 0)
print()
safe_divide("10", 3)

print()

# -----------------------------------------------------------------------------
# 15. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 50)
print("   ERROR HANDLING COMPLETE!")
print("=" * 50)
print()
print("You now know how to catch, raise, and create exceptions.")
print("Try the exercises in exercises.py to practice!")
