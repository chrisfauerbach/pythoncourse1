"""
Error Handling — Exercises
============================

Practice problems to test your understanding of error handling.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Safe division
#
# Write a function `safe_divide(a, b)` that:
#   - Returns a / b if possible
#   - Returns None if b is zero (handle ZeroDivisionError)
#   - Prints a message when division by zero is caught
#
# Test it with: safe_divide(10, 3), safe_divide(10, 0), safe_divide(7, 2)
#
# Expected output:
#   10 / 3 = 3.3333333333333335
#   Cannot divide by zero! Returning None.
#   10 / 0 = None
#   7 / 2 = 3.5
#
# =============================================================================

def exercise_1():
    def safe_divide(a, b):
        # YOUR CODE HERE
        pass

    # Test cases
    for a, b in [(10, 3), (10, 0), (7, 2)]:
        result = safe_divide(a, b)
        print(f"  {a} / {b} = {result}")


# =============================================================================
# Exercise 2: Safe integer parser
#
# Write a function `safe_int(value, default=0)` that:
#   - Tries to convert `value` to an int and return it
#   - Returns `default` if the conversion fails (ValueError or TypeError)
#
# Test it with: safe_int("42"), safe_int("abc"), safe_int(None, -1),
#               safe_int("3.14"), safe_int("")
#
# Expected output:
#   safe_int('42') = 42
#   safe_int('abc') = 0
#   safe_int(None, -1) = -1
#   safe_int('3.14') = 0
#   safe_int('') = 0
#
# =============================================================================

def exercise_2():
    def safe_int(value, default=0):
        # YOUR CODE HERE
        pass

    # Test cases
    test_cases = [
        (("42",), {}),
        (("abc",), {}),
        ((None, -1), {}),
        (("3.14",), {}),
        (("",), {}),
    ]
    for args, kwargs in test_cases:
        result = safe_int(*args, **kwargs)
        if len(args) > 1:
            print(f"  safe_int({args[0]!r}, {args[1]!r}) = {result}")
        else:
            print(f"  safe_int({args[0]!r}) = {result}")


# =============================================================================
# Exercise 3: Graceful file reader
#
# Write a function `read_file(filepath)` that:
#   - Tries to open and read the file, returning its contents
#   - Returns None if the file doesn't exist (handle FileNotFoundError)
#   - Prints a friendly message (not a traceback!) on failure
#   - Uses a finally block to print "Read attempt finished." either way
#
# Test it with: read_file("nonexistent.txt")
# Then create a quick test: write a small string to a temp file and read it.
#
# Expected output:
#   File 'nonexistent.txt' not found.
#   Read attempt finished.
#   Contents: None
#   Read attempt finished.
#   Contents: Hello from the temp file!
#
# =============================================================================

def exercise_3():
    import tempfile
    import os

    def read_file(filepath):
        # YOUR CODE HERE
        pass

    # Test with nonexistent file
    contents = read_file("nonexistent.txt")
    print(f"  Contents: {contents}")

    # Test with a real file
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    tmp.write("Hello from the temp file!")
    tmp.close()
    try:
        contents = read_file(tmp.name)
        print(f"  Contents: {contents}")
    finally:
        os.unlink(tmp.name)


# =============================================================================
# Exercise 4: Custom ValidationError
#
# Create a custom exception class `ValidationError` that inherits from
# Exception and accepts a field name and a message.
#
# Then write a function `validate_user(name, age)` that:
#   - Raises ValidationError("name", "cannot be empty") if name is empty
#   - Raises ValidationError("age", "must be a positive number") if age <= 0
#   - Raises ValidationError("age", "must be an integer") if age is not an int
#   - Returns a dict {"name": name, "age": age} if valid
#
# Your ValidationError should have `field` and `message` attributes, and
# its str representation should be: "Validation failed on 'field': message"
#
# Test it with: ("Alice", 30), ("", 25), ("Bob", -5), ("Charlie", "old")
#
# Expected output:
#   validate_user('Alice', 30) = {'name': 'Alice', 'age': 30}
#   validate_user('', 25) raised: Validation failed on 'name': cannot be empty
#   validate_user('Bob', -5) raised: Validation failed on 'age': must be a positive number
#   validate_user('Charlie', 'old') raised: Validation failed on 'age': must be an integer
#
# =============================================================================

def exercise_4():
    # Define ValidationError HERE
    # YOUR CODE HERE

    def validate_user(name, age):
        # YOUR CODE HERE
        pass

    # Test cases
    test_cases = [("Alice", 30), ("", 25), ("Bob", -5), ("Charlie", "old")]
    for name, age in test_cases:
        try:
            result = validate_user(name, age)
            print(f"  validate_user({name!r}, {age!r}) = {result}")
        except Exception as e:
            print(f"  validate_user({name!r}, {age!r}) raised: {e}")


# =============================================================================
# Exercise 5: Retry pattern
#
# Write a function `retry(func, max_attempts=3)` that:
#   - Calls `func()` up to `max_attempts` times
#   - If func() succeeds, return the result immediately
#   - If func() raises an exception, print which attempt failed and try again
#   - If all attempts fail, re-raise the last exception
#
# Test it with a function that uses a counter to fail the first 2 times,
# then succeed. Then test with a function that always fails.
#
# Expected output:
#   Attempt 1 failed: Simulated failure 1
#   Attempt 2 failed: Simulated failure 2
#   Success on attempt 3: It worked!
#   ---
#   Attempt 1 failed: Always fails
#   Attempt 2 failed: Always fails
#   Attempt 3 failed: Always fails
#   All 3 attempts failed. Last error: Always fails
#
# =============================================================================

def exercise_5():
    def retry(func, max_attempts=3):
        # YOUR CODE HERE
        pass

    # Test 1: Succeeds on third try
    call_count = 0
    def flaky_function():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise RuntimeError(f"Simulated failure {call_count}")
        return "It worked!"

    result = retry(flaky_function, max_attempts=3)
    print(f"  Success on attempt {call_count}: {result}")

    # Test 2: Always fails
    print("  ---")
    def always_fails():
        raise RuntimeError("Always fails")

    try:
        retry(always_fails, max_attempts=3)
    except RuntimeError as e:
        print(f"  All 3 attempts failed. Last error: {e}")


# =============================================================================
# Exercise 6: Safe nested dictionary getter
#
# Write a function `safe_get(data, *keys, default=None)` that:
#   - Navigates into a nested dictionary using the sequence of keys
#   - Returns the value if all keys exist
#   - Returns `default` if any key is missing (KeyError) or if a
#     non-dict is encountered along the way (TypeError)
#
# Example: safe_get({"a": {"b": {"c": 42}}}, "a", "b", "c") returns 42
#          safe_get({"a": {"b": 1}}, "a", "b", "c") returns None
#
# Expected output:
#   safe_get(data, 'user', 'address', 'city') = Springfield
#   safe_get(data, 'user', 'address', 'zip') = N/A
#   safe_get(data, 'user', 'phone') = N/A
#   safe_get(data, 'user', 'name') = Alice
#   safe_get(data, 'user', 'name', 'first') = N/A
#   safe_get(data, 'missing') = N/A
#
# =============================================================================

def exercise_6():
    def safe_get(data, *keys, default=None):
        # YOUR CODE HERE
        pass

    # Test data — a nested dictionary
    data = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Springfield",
                "state": "IL"
            }
        }
    }

    # Test cases
    test_cases = [
        (("user", "address", "city"), {}),
        (("user", "address", "zip"), {"default": "N/A"}),
        (("user", "phone"), {"default": "N/A"}),
        (("user", "name"), {}),
        (("user", "name", "first"), {"default": "N/A"}),
        (("missing",), {"default": "N/A"}),
    ]

    for keys, kwargs in test_cases:
        result = safe_get(data, *keys, **kwargs)
        keys_str = ", ".join(f"'{k}'" for k in keys)
        print(f"  safe_get(data, {keys_str}) = {result}")


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    def safe_divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("  Cannot divide by zero! Returning None.")
            return None

    for a, b in [(10, 3), (10, 0), (7, 2)]:
        result = safe_divide(a, b)
        print(f"  {a} / {b} = {result}")


def solution_2():
    def safe_int(value, default=0):
        try:
            return int(value)
        except (ValueError, TypeError):
            return default

    test_cases = [
        (("42",), {}),
        (("abc",), {}),
        ((None, -1), {}),
        (("3.14",), {}),
        (("",), {}),
    ]
    for args, kwargs in test_cases:
        result = safe_int(*args, **kwargs)
        if len(args) > 1:
            print(f"  safe_int({args[0]!r}, {args[1]!r}) = {result}")
        else:
            print(f"  safe_int({args[0]!r}) = {result}")


def solution_3():
    import tempfile
    import os

    def read_file(filepath):
        try:
            with open(filepath) as f:
                return f.read()
        except FileNotFoundError:
            print(f"  File '{filepath}' not found.")
            return None
        finally:
            print("  Read attempt finished.")

    contents = read_file("nonexistent.txt")
    print(f"  Contents: {contents}")

    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    tmp.write("Hello from the temp file!")
    tmp.close()
    try:
        contents = read_file(tmp.name)
        print(f"  Contents: {contents}")
    finally:
        os.unlink(tmp.name)


def solution_4():
    class ValidationError(Exception):
        def __init__(self, field, message):
            self.field = field
            self.message = message
            super().__init__(f"Validation failed on '{field}': {message}")

    def validate_user(name, age):
        if not isinstance(age, int):
            raise ValidationError("age", "must be an integer")
        if not name:
            raise ValidationError("name", "cannot be empty")
        if age <= 0:
            raise ValidationError("age", "must be a positive number")
        return {"name": name, "age": age}

    test_cases = [("Alice", 30), ("", 25), ("Bob", -5), ("Charlie", "old")]
    for name, age in test_cases:
        try:
            result = validate_user(name, age)
            print(f"  validate_user({name!r}, {age!r}) = {result}")
        except ValidationError as e:
            print(f"  validate_user({name!r}, {age!r}) raised: {e}")


def solution_5():
    def retry(func, max_attempts=3):
        last_exception = None
        for attempt in range(1, max_attempts + 1):
            try:
                return func()
            except Exception as e:
                last_exception = e
                print(f"  Attempt {attempt} failed: {e}")
        raise last_exception

    call_count = 0
    def flaky_function():
        nonlocal call_count
        call_count += 1
        if call_count < 3:
            raise RuntimeError(f"Simulated failure {call_count}")
        return "It worked!"

    result = retry(flaky_function, max_attempts=3)
    print(f"  Success on attempt {call_count}: {result}")

    print("  ---")
    def always_fails():
        raise RuntimeError("Always fails")

    try:
        retry(always_fails, max_attempts=3)
    except RuntimeError as e:
        print(f"  All 3 attempts failed. Last error: {e}")


def solution_6():
    def safe_get(data, *keys, default=None):
        current = data
        for key in keys:
            try:
                current = current[key]
            except (KeyError, TypeError):
                return default
        return current

    data = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Springfield",
                "state": "IL"
            }
        }
    }

    test_cases = [
        (("user", "address", "city"), {}),
        (("user", "address", "zip"), {"default": "N/A"}),
        (("user", "phone"), {"default": "N/A"}),
        (("user", "name"), {}),
        (("user", "name", "first"), {"default": "N/A"}),
        (("missing",), {"default": "N/A"}),
    ]

    for keys, kwargs in test_cases:
        result = safe_get(data, *keys, **kwargs)
        keys_str = ", ".join(f"'{k}'" for k in keys)
        print(f"  safe_get(data, {keys_str}) = {result}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Safe division", exercise_1),
        ("Safe integer parser", exercise_2),
        ("Graceful file reader", exercise_3),
        ("Custom ValidationError", exercise_4),
        ("Retry pattern", exercise_5),
        ("Safe nested dict getter", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
