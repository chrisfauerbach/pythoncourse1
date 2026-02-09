"""
Context Managers — Example Code
=================================

Run this file:
    python3 example.py

Everything you need to know about context managers — the `with` statement,
class-based and generator-based approaches, contextlib utilities, and more.
"""

import os
import time
import io
import tempfile
import threading
from contextlib import contextmanager, suppress, redirect_stdout, closing
from decimal import Decimal, localcontext

# -----------------------------------------------------------------------------
# 1. The problem context managers solve
# -----------------------------------------------------------------------------

print("=" * 60)
print("1. THE PROBLEM CONTEXT MANAGERS SOLVE")
print("=" * 60)

# The OLD way — manually managing cleanup with try/finally
tmp_path = os.path.join(tempfile.gettempdir(), "cm_example.txt")

f = open(tmp_path, "w")
try:
    f.write("Written the old way\n")
finally:
    f.close()  # you have to remember this!

print(f"File closed (old way)? {f.closed}")  # True

# The BETTER way — with statement handles cleanup automatically
with open(tmp_path, "w") as f:
    f.write("Written the clean way\n")
# f.close() happens automatically — even if an exception occurred above

print(f"File closed (with)?    {f.closed}")  # True
print()

# -----------------------------------------------------------------------------
# 2. Built-in context managers
# -----------------------------------------------------------------------------

print("=" * 60)
print("2. BUILT-IN CONTEXT MANAGERS")
print("=" * 60)

# File I/O — the one you'll use most often
with open(tmp_path, "w") as f:
    f.write("Hello from a context manager!\n")

with open(tmp_path, "r") as f:
    print(f"File contents: {f.read().strip()}")

# Temporary directory — auto-deleted when the block exits
with tempfile.TemporaryDirectory() as tmpdir:
    temp_file = os.path.join(tmpdir, "temp.txt")
    with open(temp_file, "w") as f:
        f.write("This file will vanish")
    print(f"Temp dir exists during block: {os.path.exists(tmpdir)}")

print(f"Temp dir exists after block:  {os.path.exists(tmpdir)}")

# Decimal precision — temporarily change precision
with localcontext() as ctx:
    ctx.prec = 42
    result = Decimal(1) / Decimal(7)
    print(f"1/7 with 42 digits: {result}")

# Threading lock — auto-acquired and auto-released
lock = threading.Lock()
with lock:
    print("Lock acquired — critical section running")
# lock is released here

print()

# -----------------------------------------------------------------------------
# 3. Class-based context managers (__enter__ / __exit__)
# -----------------------------------------------------------------------------

print("=" * 60)
print("3. CLASS-BASED CONTEXT MANAGERS")
print("=" * 60)

# A Timer that measures how long a block takes to run
class Timer:
    """A simple timer context manager."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self  # this is what gets assigned to the `as` variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"  Timer: {self.elapsed:.6f} seconds")
        return False  # don't suppress exceptions

# Using it
with Timer() as t:
    total = sum(range(1_000_000))
print(f"  Sum result: {total}")

# You can also access the timer after the block
print(f"  Stored elapsed: {t.elapsed:.6f} seconds")

print()

# A context manager that temporarily changes the working directory
class ChangeDirectory:
    """Temporarily change the current working directory."""

    def __init__(self, new_path):
        self.new_path = new_path

    def __enter__(self):
        self.original_path = os.getcwd()
        os.chdir(self.new_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_path)
        return False

original_dir = os.getcwd()
with ChangeDirectory(tempfile.gettempdir()):
    print(f"  Inside block: {os.getcwd()}")
print(f"  After block:  {os.getcwd()}")
assert os.getcwd() == original_dir, "Directory wasn't restored!"
print("  Directory restored correctly!")

print()

# -----------------------------------------------------------------------------
# 4. The __exit__ parameters — exception handling
# -----------------------------------------------------------------------------

print("=" * 60)
print("4. THE __exit__ PARAMETERS")
print("=" * 60)

class VerboseExit:
    """Shows what __exit__ receives in different scenarios."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("  __exit__ called: no exception (clean exit)")
        else:
            print(f"  __exit__ called: {exc_type.__name__}: {exc_val}")
        return False  # let exceptions propagate

# Normal exit — all three params are None
print("Normal exit:")
with VerboseExit():
    x = 42

# Exception exit — params contain the exception info
print("Exception exit:")
try:
    with VerboseExit():
        raise ValueError("something went wrong")
except ValueError:
    print("  (exception propagated normally)")

print()

# Suppressing exceptions by returning True
class SafeDivision:
    """Suppresses ZeroDivisionError, lets everything else through."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("  Caught division by zero — suppressing!")
            return True  # suppress the exception
        return False      # let other exceptions propagate

print("Suppressing ZeroDivisionError:")
with SafeDivision():
    result = 1 / 0  # this would normally crash
print("  Code continues after the with block!")

print()

# -----------------------------------------------------------------------------
# 5. Generator-based context managers with @contextmanager
# -----------------------------------------------------------------------------

print("=" * 60)
print("5. GENERATOR-BASED CONTEXT MANAGERS (@contextmanager)")
print("=" * 60)

# Same Timer concept, but much less code
@contextmanager
def timer(label="Block"):
    start = time.perf_counter()
    yield  # the with block runs here
    elapsed = time.perf_counter() - start
    print(f"  {label}: {elapsed:.6f} seconds")

with timer("Sum operation"):
    total = sum(range(500_000))

print()

# Yielding a value — it becomes the `as` variable
@contextmanager
def temp_file(content=""):
    """Create a temporary file with optional content, delete it when done."""
    path = os.path.join(tempfile.gettempdir(), "cm_temp_example.txt")
    with open(path, "w") as f:
        f.write(content)
    try:
        yield path  # the caller gets the path
    finally:
        os.remove(path)  # cleanup runs no matter what
        print(f"  Temp file removed: {os.path.basename(path)}")

with temp_file("Hello, temporary world!") as path:
    with open(path) as f:
        print(f"  Read from temp file: {f.read()}")
# file is auto-deleted here

print()

# Handling exceptions with try/finally in a generator CM
@contextmanager
def managed_resource(name):
    """Demonstrates proper cleanup even on exceptions."""
    print(f"  Acquiring: {name}")
    resource = {"name": name, "status": "open"}
    try:
        yield resource
    except Exception as e:
        print(f"  Exception in block: {e}")
        resource["status"] = "error"
        raise  # re-raise so the caller still sees the exception
    finally:
        print(f"  Releasing: {name} (status: {resource['status']})")

# Normal usage
with managed_resource("database") as res:
    res["status"] = "in-use"
    print(f"  Using resource: {res}")

print()

# Usage with an exception
try:
    with managed_resource("network") as res:
        raise ConnectionError("lost connection")
except ConnectionError:
    print("  Handled the ConnectionError outside the block")

print()

# -----------------------------------------------------------------------------
# 6. contextlib utilities
# -----------------------------------------------------------------------------

print("=" * 60)
print("6. CONTEXTLIB UTILITIES")
print("=" * 60)

# suppress() — cleanly ignore specific exceptions
print("suppress():")
with suppress(FileNotFoundError):
    os.remove("/tmp/this_file_definitely_does_not_exist_12345.txt")
print("  No crash, even though the file didn't exist")

with suppress(KeyError, IndexError):
    d = {"a": 1}
    _ = d["missing_key"]  # KeyError — suppressed
print("  KeyError suppressed cleanly")

print()

# redirect_stdout() — capture what print() produces
print("redirect_stdout():")
buffer = io.StringIO()
with redirect_stdout(buffer):
    print("This goes to the buffer, not your screen")
    print("So does this")

captured = buffer.getvalue()
print(f"  Captured {len(captured)} characters:")
for line in captured.strip().split("\n"):
    print(f"    > {line}")

print()

# closing() — ensure .close() is called on objects that aren't CMs
class LegacyResource:
    """An old-style object with .close() but no __enter__/__exit__."""
    def __init__(self):
        self.is_open = True
    def close(self):
        self.is_open = False
        print("  LegacyResource.close() was called")

print("closing():")
with closing(LegacyResource()) as resource:
    print(f"  Resource open? {resource.is_open}")
print(f"  Resource open? {resource.is_open}")

print()

# -----------------------------------------------------------------------------
# 7. Nested context managers
# -----------------------------------------------------------------------------

print("=" * 60)
print("7. NESTED CONTEXT MANAGERS")
print("=" * 60)

# Method 1: Nested with statements
path1 = os.path.join(tempfile.gettempdir(), "cm_input.txt")
path2 = os.path.join(tempfile.gettempdir(), "cm_output.txt")

# Create the input file first
with open(path1, "w") as f:
    f.write("Data to be copied")

# Nested — works in all Python versions
with open(path1, "r") as infile:
    with open(path2, "w") as outfile:
        outfile.write(infile.read())
        print("  Method 1 (nested): copied file contents")

# Method 2: Comma-separated — cleaner
with open(path1, "r") as infile, open(path2, "w") as outfile:
    outfile.write(infile.read())
    print("  Method 2 (comma):  copied file contents")

# Method 3: Parenthesized (Python 3.10+) — best for many CMs
with (
    open(path1, "r") as infile,
    open(path2, "w") as outfile,
):
    outfile.write(infile.read())
    print("  Method 3 (parens): copied file contents")

# Clean up
os.remove(path1)
os.remove(path2)

print()

# -----------------------------------------------------------------------------
# 8. Async context managers (quick preview)
# -----------------------------------------------------------------------------

print("=" * 60)
print("8. ASYNC CONTEXT MANAGERS (PREVIEW)")
print("=" * 60)

# We'll just show the structure — running async code requires asyncio.run()
print("""  Async context managers follow the same pattern:

  class AsyncResource:
      async def __aenter__(self):
          await self.connect()
          return self

      async def __aexit__(self, exc_type, exc_val, exc_tb):
          await self.disconnect()

  # Used with `async with`:
  async with AsyncResource() as resource:
      await resource.do_something()

  # Or use @asynccontextmanager from contextlib:
  from contextlib import asynccontextmanager

  @asynccontextmanager
  async def async_timer():
      start = time.perf_counter()
      yield
      print(f"Elapsed: {time.perf_counter() - start:.4f}s")
""")

# -----------------------------------------------------------------------------
# 9. Practical use case — a database-style transaction
# -----------------------------------------------------------------------------

print("=" * 60)
print("9. PRACTICAL USE CASE — TRANSACTION MANAGER")
print("=" * 60)

class FakeDatabase:
    """A simple fake database to demonstrate transactions."""
    def __init__(self):
        self.data = {}
        self._backup = None

    def set(self, key, value):
        self.data[key] = value

    def snapshot(self):
        self._backup = dict(self.data)

    def commit(self):
        self._backup = None
        print("  Transaction committed")

    def rollback(self):
        self.data = self._backup
        self._backup = None
        print("  Transaction rolled back")

@contextmanager
def transaction(db):
    """Context manager for database-style transactions."""
    db.snapshot()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise

# Successful transaction
db = FakeDatabase()
db.set("name", "Alice")

with transaction(db):
    db.set("age", 30)
    db.set("city", "Portland")
print(f"  After success: {db.data}")

# Failed transaction — changes are rolled back
try:
    with transaction(db):
        db.set("city", "New York")
        db.set("age", 31)
        raise RuntimeError("Something went wrong!")
except RuntimeError:
    pass
print(f"  After failure: {db.data}")
# city is still "Portland", not "New York"

print()

# -----------------------------------------------------------------------------
# 10. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 60)
print("  CONTEXT MANAGERS COMPLETE!")
print("=" * 60)
print()
print("You've seen:")
print("  - The with statement and why it matters")
print("  - Class-based CMs with __enter__ / __exit__")
print("  - Generator-based CMs with @contextmanager")
print("  - contextlib utilities (suppress, redirect_stdout, closing)")
print("  - Nested context managers")
print("  - Async CMs (preview)")
print("  - Real-world patterns (timers, temp files, transactions)")
print()
print("Now try the exercises in exercises.py!")

# Clean up our temp file
if os.path.exists(tmp_path):
    os.remove(tmp_path)
