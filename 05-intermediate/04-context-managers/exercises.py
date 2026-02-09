"""
Context Managers — Exercises
=============================

Practice problems to test your understanding of context managers.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import time
import os
import sys
import io
import tempfile
from contextlib import contextmanager


# =============================================================================
# Exercise 1: Timer context manager (class-based)
#
# Write a class-based context manager called `Timer` that:
#   - Records the start time in __enter__
#   - Returns self so the caller can access it with `as`
#   - In __exit__, calculates elapsed time and stores it in self.elapsed
#   - Does NOT suppress exceptions
#
# Usage:
#   with Timer() as t:
#       sum(range(1_000_000))
#   print(f"Took {t.elapsed:.4f} seconds")
#
# Hint: Use time.perf_counter() for precise timing
# =============================================================================

def exercise_1():
    # YOUR CODE HERE — define the Timer class, then test it:
    # with Timer() as t:
    #     sum(range(1_000_000))
    # print(f"  Elapsed: {t.elapsed:.4f} seconds")
    pass


# =============================================================================
# Exercise 2: Temporary directory changer (class-based)
#
# Write a class-based context manager called `ChangeDir` that:
#   - Takes a target directory path in __init__
#   - In __enter__, saves the current directory and changes to the target
#   - In __exit__, changes back to the original directory
#   - Does NOT suppress exceptions
#
# Usage:
#   print(os.getcwd())          # /home/user/project
#   with ChangeDir("/tmp"):
#       print(os.getcwd())      # /tmp
#   print(os.getcwd())          # /home/user/project  (restored!)
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE — define ChangeDir, then test it:
    # original = os.getcwd()
    # with ChangeDir(tempfile.gettempdir()):
    #     print(f"  Inside:  {os.getcwd()}")
    # print(f"  After:   {os.getcwd()}")
    # print(f"  Restored? {os.getcwd() == original}")
    pass


# =============================================================================
# Exercise 3: Temp file creator (@contextmanager)
#
# Write a generator-based context manager called `temp_writer` that:
#   - Creates a temporary file with a given filename in the system temp dir
#   - Writes initial_content to the file (if provided)
#   - Yields the full file path
#   - Deletes the file when the block exits (even on exceptions!)
#
# Usage:
#   with temp_writer("test.txt", "Hello!") as path:
#       with open(path) as f:
#           print(f.read())   # Hello!
#   # file is now deleted
#
# Hint: Use try/finally around the yield
# =============================================================================

def exercise_3():
    # YOUR CODE HERE — define temp_writer, then test it:
    # with temp_writer("exercise3.txt", "Context managers are great!") as path:
    #     with open(path) as f:
    #         print(f"  Contents: {f.read()}")
    #     print(f"  File exists during block? {os.path.exists(path)}")
    # print(f"  File exists after block?  {os.path.exists(path)}")
    pass


# =============================================================================
# Exercise 4: Selective exception suppressor (class-based)
#
# Write a class-based context manager called `Suppress` that:
#   - Takes one or more exception types in __init__
#   - Suppresses those specific exceptions (returns True from __exit__)
#   - Stores the suppressed exception in self.exception (or None if clean)
#   - Lets all other exception types propagate normally
#
# Usage:
#   s = Suppress(ValueError, TypeError)
#   with s:
#       int("not a number")   # ValueError — suppressed!
#   print(s.exception)        # ValueError: invalid literal ...
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define Suppress, then test it:
    # s = Suppress(ValueError, TypeError)
    # with s:
    #     int("not_a_number")
    # print(f"  Suppressed: {s.exception}")
    # print(f"  Code continues normally!")
    #
    # # Also test that non-matching exceptions still propagate:
    # try:
    #     with Suppress(ValueError):
    #         raise KeyError("this should NOT be suppressed")
    # except KeyError:
    #     print("  KeyError correctly propagated!")
    pass


# =============================================================================
# Exercise 5: Output capturer (@contextmanager)
#
# Write a generator-based context manager called `capture_output` that:
#   - Redirects sys.stdout to an io.StringIO buffer
#   - Yields the buffer so the caller can inspect it
#   - Restores the original sys.stdout when done (even on exceptions!)
#
# Usage:
#   with capture_output() as output:
#       print("Hello")
#       print("World")
#   print(output.getvalue())  # "Hello\nWorld\n"
#
# Hint: Save sys.stdout, replace it, yield, restore in finally
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define capture_output, then test it:
    # with capture_output() as output:
    #     print("Captured line 1")
    #     print("Captured line 2")
    # # These print to the real stdout (it's been restored)
    # print(f"  Captured text:")
    # for line in output.getvalue().strip().split("\n"):
    #     print(f"    > {line}")
    pass


# =============================================================================
# Exercise 6: Transaction manager (@contextmanager)
#
# Write a generator-based context manager called `transaction` that:
#   - Takes a dictionary (representing a "database")
#   - Makes a snapshot (copy) of the dict before the block runs
#   - If the block completes successfully, keeps the changes (commit)
#   - If the block raises an exception, restores the snapshot (rollback)
#   - Re-raises the exception after rollback (don't suppress it)
#   - Prints "Committed" or "Rolled back" as appropriate
#
# Usage:
#   data = {"balance": 100}
#   with transaction(data):
#       data["balance"] -= 50     # success — committed
#   # data["balance"] is now 50
#
#   try:
#       with transaction(data):
#           data["balance"] -= 9999
#           raise RuntimeError("Insufficient funds")
#   except RuntimeError:
#       pass
#   # data["balance"] is back to 50 — rolled back!
#
# Hint: Use try/except around the yield. Restore the dict with .clear()
#       and .update() to modify it in-place (don't reassign the variable).
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define transaction, then test it:
    # data = {"balance": 100, "name": "Alice"}
    # print(f"  Start:    {data}")
    #
    # with transaction(data):
    #     data["balance"] -= 30
    # print(f"  After ok: {data}")
    #
    # try:
    #     with transaction(data):
    #         data["balance"] -= 9999
    #         raise RuntimeError("Insufficient funds!")
    # except RuntimeError:
    #     pass
    # print(f"  After err:{data}")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    class Timer:
        def __enter__(self):
            self.start = time.perf_counter()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.elapsed = time.perf_counter() - self.start
            return False

    with Timer() as t:
        sum(range(1_000_000))
    print(f"  Elapsed: {t.elapsed:.4f} seconds")


def solution_2():
    class ChangeDir:
        def __init__(self, target):
            self.target = target

        def __enter__(self):
            self.original = os.getcwd()
            os.chdir(self.target)
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            os.chdir(self.original)
            return False

    original = os.getcwd()
    with ChangeDir(tempfile.gettempdir()):
        print(f"  Inside:   {os.getcwd()}")
    print(f"  After:    {os.getcwd()}")
    print(f"  Restored? {os.getcwd() == original}")


def solution_3():
    @contextmanager
    def temp_writer(filename, initial_content=""):
        path = os.path.join(tempfile.gettempdir(), filename)
        with open(path, "w") as f:
            f.write(initial_content)
        try:
            yield path
        finally:
            if os.path.exists(path):
                os.remove(path)

    with temp_writer("exercise3.txt", "Context managers are great!") as path:
        with open(path) as f:
            print(f"  Contents: {f.read()}")
        print(f"  File exists during block? {os.path.exists(path)}")
    print(f"  File exists after block?  {os.path.exists(path)}")


def solution_4():
    class Suppress:
        def __init__(self, *exception_types):
            self.exception_types = exception_types
            self.exception = None

        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type and issubclass(exc_type, self.exception_types):
                self.exception = exc_val
                return True
            return False

    s = Suppress(ValueError, TypeError)
    with s:
        int("not_a_number")
    print(f"  Suppressed: {s.exception}")
    print(f"  Code continues normally!")

    # Non-matching exceptions still propagate
    try:
        with Suppress(ValueError):
            raise KeyError("this should NOT be suppressed")
    except KeyError:
        print("  KeyError correctly propagated!")


def solution_5():
    @contextmanager
    def capture_output():
        original_stdout = sys.stdout
        buffer = io.StringIO()
        sys.stdout = buffer
        try:
            yield buffer
        finally:
            sys.stdout = original_stdout

    with capture_output() as output:
        print("Captured line 1")
        print("Captured line 2")
    # These print to the real stdout (it's been restored)
    print(f"  Captured text:")
    for line in output.getvalue().strip().split("\n"):
        print(f"    > {line}")


def solution_6():
    @contextmanager
    def transaction(data):
        snapshot = dict(data)
        try:
            yield data
            print("  Committed")
        except Exception:
            data.clear()
            data.update(snapshot)
            print("  Rolled back")
            raise

    data = {"balance": 100, "name": "Alice"}
    print(f"  Start:     {data}")

    with transaction(data):
        data["balance"] -= 30
    print(f"  After ok:  {data}")

    try:
        with transaction(data):
            data["balance"] -= 9999
            raise RuntimeError("Insufficient funds!")
    except RuntimeError:
        pass
    print(f"  After err: {data}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Timer context manager", exercise_1),
        ("Temporary directory changer", exercise_2),
        ("Temp file creator", exercise_3),
        ("Selective exception suppressor", exercise_4),
        ("Output capturer", exercise_5),
        ("Transaction manager", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
