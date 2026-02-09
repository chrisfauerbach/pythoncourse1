# Context Managers

## Objective

Understand context managers and the `with` statement — Python's elegant way to guarantee cleanup happens, no matter what.

## Concepts Covered

- The `with` statement and why it exists
- Guaranteed cleanup, even when exceptions occur
- Built-in context managers (`open()`, `threading.Lock`, etc.)
- Writing class-based context managers (`__enter__` / `__exit__`)
- The `__exit__` parameters and suppressing exceptions
- Generator-based context managers with `@contextmanager`
- `contextlib` utilities: `suppress()`, `redirect_stdout()`, `closing()`
- Nested context managers
- Async context managers (brief intro)
- Practical use cases

## Prerequisites

- Functions and classes
- Exception handling (`try` / `except` / `finally`)
- Decorators (helpful but not required)

## Lesson

### What's a Context Manager?

A context manager is any object that knows how to **set something up** and **tear it down**. You use it with the `with` statement:

```python
with open("data.txt", "r") as f:
    contents = f.read()
# f is automatically closed here, even if an error happened inside the block
```

That's the core idea. The `with` statement guarantees that cleanup code runs — closing files, releasing locks, restoring state — no matter how the block exits. Even if an exception is raised. Even if you `return` out of a function.

### Why They Matter

Without context managers, you'd write this:

```python
f = open("data.txt", "r")
try:
    contents = f.read()
finally:
    f.close()
```

That works, but it's verbose and easy to forget. The `with` version is shorter, safer, and impossible to mess up. Context managers turn "remember to clean up" into "cleanup is automatic."

### Built-in Context Managers

Python is full of context managers. Here are some you'll see constantly:

```python
# Files — the most common one
with open("output.txt", "w") as f:
    f.write("hello")

# Threading locks — automatically acquired and released
import threading
lock = threading.Lock()
with lock:
    # critical section — only one thread at a time
    shared_data += 1

# Decimal precision — temporarily change decimal context
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec = 50
    print(Decimal(1) / Decimal(7))  # 50 digits of precision

# Temporary directories
import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
    print(tmpdir)  # a real path on disk
# directory is deleted when the block exits
```

### Writing Class-Based Context Managers

Any class can be a context manager. Just implement two methods:

- `__enter__(self)` — runs at the start of the `with` block. Whatever this returns gets assigned to the `as` variable.
- `__exit__(self, exc_type, exc_val, exc_tb)` — runs when the `with` block ends, whether it ended normally or with an exception.

```python
class Timer:
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f} seconds")
        return False  # don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))
# prints: Elapsed: 0.0312 seconds (or whatever it took)
```

The pattern is always the same: `__enter__` sets things up, `__exit__` tears them down.

### The `__exit__` Parameters

The three parameters to `__exit__` tell you about any exception that occurred:

- `exc_type` — the exception class (e.g., `ValueError`), or `None` if no exception
- `exc_val` — the exception instance, or `None`
- `exc_tb` — the traceback object, or `None`

If the `with` block completed normally, all three are `None`.

Here's the important part: if `__exit__` returns `True`, the exception is **suppressed** — it won't propagate. If it returns `False` (or `None`, which is falsy), the exception continues as normal.

```python
class SuppressErrors:
    def __init__(self, *exception_types):
        self.exception_types = exception_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and issubclass(exc_type, self.exception_types):
            print(f"Suppressed: {exc_val}")
            return True  # swallow the exception
        return False      # let other exceptions propagate

with SuppressErrors(ZeroDivisionError):
    result = 1 / 0   # suppressed!
    print("This line never runs")

print("But this one does — the exception was caught")
```

Be careful with suppression. Most of the time, you want `__exit__` to return `False` and let exceptions propagate normally.

### Generator-Based Context Managers with `@contextmanager`

Writing a whole class for a simple context manager can feel like overkill. The `contextlib` module gives you a decorator that lets you write context managers as generator functions:

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.perf_counter()
    yield  # <-- this is where the `with` block runs
    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed:.4f} seconds")

with timer():
    total = sum(range(1_000_000))
```

The recipe is:
1. Code **before** `yield` = setup (`__enter__`)
2. The `yield` value = the `as` variable (optional)
3. Code **after** `yield` = teardown (`__exit__`)

If you need to handle exceptions inside the generator, wrap `yield` in a `try`/`finally`:

```python
@contextmanager
def managed_resource():
    print("Acquiring resource")
    resource = {"status": "open"}
    try:
        yield resource
    finally:
        resource["status"] = "closed"
        print("Resource released")
```

The `finally` block ensures cleanup runs even if the `with` block raises an exception.

### contextlib Utilities

The `contextlib` module has several handy context managers built in:

```python
from contextlib import suppress, redirect_stdout, closing
import io

# suppress() — cleanly ignore specific exceptions
import os
with suppress(FileNotFoundError):
    os.remove("file_that_might_not_exist.txt")
# no error, even if the file doesn't exist

# redirect_stdout() — capture print output
f = io.StringIO()
with redirect_stdout(f):
    print("This goes to f, not the screen")
captured = f.getvalue()  # "This goes to f, not the screen\n"

# closing() — call .close() on anything when the block ends
# Useful for objects that have .close() but aren't context managers
from contextlib import closing
with closing(some_legacy_connection()) as conn:
    conn.do_stuff()
# conn.close() is called automatically
```

`suppress()` is especially useful — it's a cleaner alternative to an empty `except` block.

### Nested Context Managers

You can nest `with` statements in a couple of ways:

```python
# Stack them on separate lines
with open("input.txt") as infile:
    with open("output.txt", "w") as outfile:
        outfile.write(infile.read())

# Combine them in one statement (comma-separated)
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    outfile.write(infile.read())

# Python 3.10+ — parenthesized form for cleaner multi-line
with (
    open("input.txt") as infile,
    open("output.txt", "w") as outfile,
):
    outfile.write(infile.read())
```

All three versions do the same thing. The parenthesized form in Python 3.10+ is great when you have several context managers and want to keep the code readable.

### Async Context Managers

If you're working with `asyncio`, you can write async context managers too. Same concept, just async:

```python
class AsyncDBConnection:
    async def __aenter__(self):
        self.conn = await connect_to_database()
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()

# Used with `async with`
async with AsyncDBConnection() as conn:
    results = await conn.query("SELECT * FROM users")
```

There's also `contextlib.asynccontextmanager` for the generator-based approach. We won't go deep into async here — just know that the pattern mirrors the synchronous version exactly.

### Practical Use Cases

Context managers show up everywhere in real code:

- **File handling** — open, read/write, auto-close
- **Database connections** — connect, query, auto-disconnect
- **Transactions** — begin, do work, commit or rollback
- **Locking** — acquire lock, do work, release lock
- **Timing** — record start time, do work, compute elapsed
- **Temporary changes** — change directory/config, do work, restore original
- **Resource pooling** — check out a resource, use it, return it to the pool
- **Testing** — set up fixtures, run tests, tear down

Any time you have a "setup/teardown" or "acquire/release" pattern, a context manager is the right tool.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- The `with` statement guarantees cleanup, even when exceptions occur
- Any object with `__enter__` and `__exit__` methods is a context manager
- `__exit__` receives exception info and can suppress exceptions by returning `True`
- `@contextmanager` from `contextlib` lets you write context managers as simple generators
- `contextlib` provides useful utilities like `suppress()`, `redirect_stdout()`, and `closing()`
- Use context managers anywhere you have a "setup then teardown" pattern
- Async context managers use `async with`, `__aenter__`, and `__aexit__`
