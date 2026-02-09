"""
Generators — Example Code
===========================

Run this file:
    python3 example.py

Generators are lazy iterators that produce values one at a time. This file
walks through every major concept — from basic yield to pipelines and .send().
"""

import sys

# -----------------------------------------------------------------------------
# 1. Your first generator function
# -----------------------------------------------------------------------------

# Any function with `yield` in it is a generator function.
# Calling it doesn't run the body — it returns a generator object.

def count_up_to(n):
    """Yield integers from 1 up to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Create the generator — nothing runs yet
gen = count_up_to(5)
print("Type of gen:", type(gen))  # <class 'generator'>

# Pull values out one at a time with next()
print("next():", next(gen))  # 1
print("next():", next(gen))  # 2

# Or use a for loop — it calls next() automatically and stops at StopIteration
print("Remaining values:", end=" ")
for num in gen:
    print(num, end=" ")
print()  # newline

# -----------------------------------------------------------------------------
# 2. How yield pauses and resumes execution
# -----------------------------------------------------------------------------

# This is the core idea. Watch the print statements to see exactly when
# each part of the function runs.

def step_by_step():
    print("  -> Starting the generator")
    yield "first"
    print("  -> Resuming after first yield")
    yield "second"
    print("  -> Resuming after second yield")
    yield "third"
    print("  -> Generator is finished (StopIteration coming next)")

print("\nStep-by-step execution:")
stepper = step_by_step()

for value in stepper:
    print(f"  Got: {value!r}")

# -----------------------------------------------------------------------------
# 3. Generator expressions — the lazy cousin of list comprehensions
# -----------------------------------------------------------------------------

# List comprehension — builds the entire list in memory
squares_list = [x**2 for x in range(10)]

# Generator expression — same values, but produced lazily
squares_gen = (x**2 for x in range(10))

print(f"\nList:      {squares_list}")
print(f"Generator: {squares_gen}")  # shows a generator object, not values

# You can pass generator expressions directly to functions
total = sum(x**2 for x in range(10))
print(f"Sum of squares 0-9: {total}")

# Find the first square over 50
first_big = next(x**2 for x in range(100) if x**2 > 50)
print(f"First square > 50: {first_big}")

# -----------------------------------------------------------------------------
# 4. Generators are single-use (exhaustion)
# -----------------------------------------------------------------------------

print("\nGenerator exhaustion:")
gen = (letter for letter in "ABC")

print("First pass: ", list(gen))   # ['A', 'B', 'C']
print("Second pass:", list(gen))   # [] — empty! It's used up.

# If you need multiple passes, create a new generator each time
# or just use a list.

# -----------------------------------------------------------------------------
# 5. Memory efficiency — generators vs lists
# -----------------------------------------------------------------------------

# Let's compare memory usage between a list and a generator
# that represent the same sequence of 100,000 numbers.

big_list = [x * 2 for x in range(100_000)]
big_gen = (x * 2 for x in range(100_000))

list_size = sys.getsizeof(big_list)
gen_size = sys.getsizeof(big_gen)

print(f"\nMemory comparison (100,000 items):")
print(f"  List size:      {list_size:>10,} bytes")
print(f"  Generator size: {gen_size:>10,} bytes")
print(f"  Ratio: list is ~{list_size // gen_size}x larger")

# The generator is tiny because it only stores its internal state,
# not all 100,000 values. It computes each value when asked.

# -----------------------------------------------------------------------------
# 6. yield from — delegating to sub-generators
# -----------------------------------------------------------------------------

def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 3
    yield 4

# Without yield from — you'd need nested loops
def combined_manual():
    for val in gen_a():
        yield val
    for val in gen_b():
        yield val

# With yield from — clean and simple
def combined_yield_from():
    yield from gen_a()
    yield from gen_b()

print(f"\nCombined (manual):     {list(combined_manual())}")
print(f"Combined (yield from): {list(combined_yield_from())}")

# yield from works with any iterable, not just generators
def letters_and_numbers():
    yield from "abc"           # strings are iterable
    yield from [1, 2, 3]      # lists too
    yield from range(10, 13)  # and ranges

print(f"Mixed iterables: {list(letters_and_numbers())}")

# -----------------------------------------------------------------------------
# 7. Sending values into generators with .send()
# -----------------------------------------------------------------------------

# Generators can receive values too. The sent value becomes the
# result of the yield expression inside the generator.

def running_average():
    """A generator that tracks a running average of sent values."""
    total = 0.0
    count = 0
    average = 0.0
    while True:
        value = yield average    # yield current average, receive new value
        total += value
        count += 1
        average = total / count

print("\nRunning average with .send():")
avg = running_average()
next(avg)  # prime the generator — advance to the first yield

for num in [10, 20, 30, 40, 50]:
    result = avg.send(num)
    print(f"  Sent {num:>2}, running average: {result:.1f}")

# -----------------------------------------------------------------------------
# 8. Generator pipelines — chaining generators together
# -----------------------------------------------------------------------------

# Each generator does one small job. Data flows through lazily.

# Simulate a log file as a list of strings (in real life, you'd read a file)
raw_log_lines = [
    "2025-01-15 INFO  Server started on port 8080",
    "2025-01-15 DEBUG Connection pool initialized",
    "2025-01-15 ERROR Failed to connect to database",
    "2025-01-15 INFO  Retrying database connection",
    "2025-01-15 ERROR Timeout after 30 seconds",
    "2025-01-15 INFO  Database connection established",
    "2025-01-15 WARN  High memory usage detected",
    "2025-01-15 ERROR Disk space below threshold",
]

# Stage 1: Read lines (simulated — in real life, read from a file)
def read_lines(lines):
    for line in lines:
        yield line.strip()

# Stage 2: Filter — only keep ERROR lines
def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

# Stage 3: Transform — extract just the message part
def extract_messages(lines):
    for line in lines:
        # Split on the log level and take the message
        parts = line.split("ERROR", 1)
        yield parts[1].strip() if len(parts) > 1 else line

# Stage 4: Format for output
def format_output(messages):
    for i, msg in enumerate(messages, 1):
        yield f"  [{i}] {msg}"

# Chain the pipeline together
print("\nGenerator pipeline — error log report:")
pipeline = format_output(
    extract_messages(
        filter_errors(
            read_lines(raw_log_lines)
        )
    )
)

# Pull values through the entire pipeline lazily
for line in pipeline:
    print(line)

# -----------------------------------------------------------------------------
# 9. Infinite generators
# -----------------------------------------------------------------------------

# Generators can run forever — they only produce values when asked.

def infinite_ids(prefix="ID"):
    """Generate unique IDs forever."""
    n = 1
    while True:
        yield f"{prefix}-{n:04d}"
        n += 1

def fibonacci():
    """Generate Fibonacci numbers forever."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Take just the first few from an infinite generator
print("\nInfinite ID generator (first 5):")
id_gen = infinite_ids("USER")
for _ in range(5):
    print(f"  {next(id_gen)}")

# You can use itertools.islice to take a slice from any iterator
from itertools import islice

print("\nFirst 10 Fibonacci numbers:")
fib_numbers = list(islice(fibonacci(), 10))
print(f"  {fib_numbers}")

# -----------------------------------------------------------------------------
# 10. Generators vs iterator classes
# -----------------------------------------------------------------------------

# A generator is just a shortcut for writing an iterator.
# Here's the same thing both ways:

# Iterator class — lots of boilerplate
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Generator function — clean and simple
def countdown(start):
    while start > 0:
        yield start
        start -= 1

print("\nIterator class vs generator function:")
print(f"  Class:     {list(Countdown(5))}")
print(f"  Generator: {list(countdown(5))}")

# Both produce the same result. Both support for loops, next(), etc.
# Generators have __iter__ and __next__ automatically.

gen = countdown(3)
print(f"\n  Has __iter__: {hasattr(gen, '__iter__')}")
print(f"  Has __next__: {hasattr(gen, '__next__')}")

# -----------------------------------------------------------------------------
# 11. Putting it all together
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("   GENERATORS COMPLETE!")
print("=" * 50)
print()
print("You've seen yield, generator expressions, yield from,")
print(".send(), pipelines, infinite generators, and more.")
print("Try the exercises in exercises.py to practice!")
