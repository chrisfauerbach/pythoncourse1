# Generators

## Objective

Understand Python generators — lazy iterators that produce values one at a time instead of building entire collections in memory. Learn how to write them, chain them together, and use them to process data efficiently.

## Concepts Covered

- Generator functions with `yield`
- How `yield` pauses and resumes execution
- Generator expressions
- Generator exhaustion (single-use)
- Memory efficiency — generators vs lists
- `yield from` for delegating to sub-generators
- Sending values into generators with `.send()`
- Generator pipelines (chaining generators)
- Practical use cases
- Generators vs iterators

## Prerequisites

- Functions
- Iterables and `for` loops
- List comprehensions
- Basic understanding of the `__iter__` / `__next__` protocol (helpful but not required)

## Lesson

### What Is a Generator?

A generator is a special kind of iterator that produces values **lazily** — one at a time, on demand, instead of computing everything upfront and storing it all in memory.

Think of it like a bookmark in a book. Instead of photocopying every page at once (a list), a generator remembers where you left off and gives you the next page when you ask for it.

```python
# A list builds everything in memory at once
numbers_list = [x * 2 for x in range(1_000_000)]  # 1 million items in memory RIGHT NOW

# A generator produces values one at a time
numbers_gen = (x * 2 for x in range(1_000_000))    # almost no memory used yet
```

### Generator Functions with `yield`

A regular function uses `return` to send back a value and then it's done — the function is finished. A generator function uses `yield` instead. When Python hits `yield`, it **pauses** the function, hands back the value, and waits. The next time you ask for a value, it **resumes** right where it left off.

```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i       # pause here, hand back i
        i += 1        # resume here on next call

gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # StopIteration! No more values.
```

Any function that contains `yield` is automatically a generator function. Calling it doesn't run the body — it returns a generator object. The body only executes when you start pulling values out.

### How `yield` Pauses and Resumes

This is the key insight that makes generators powerful. Let's trace through exactly what happens:

```python
def my_generator():
    print("Step 1")
    yield "a"
    print("Step 2")
    yield "b"
    print("Step 3")

gen = my_generator()         # Nothing prints yet! Body hasn't run.
print(next(gen))             # Prints "Step 1", then yields "a"
print(next(gen))             # Prints "Step 2", then yields "b"
# next(gen) would print "Step 3" and then raise StopIteration
```

The function's entire state — local variables, where it was in a loop, everything — is frozen at each `yield` and restored when you call `next()` again. This is completely different from a regular function, which loses all its state after `return`.

### Generator Expressions

Just like list comprehensions create lists, **generator expressions** create generators. The syntax is identical except you use parentheses `()` instead of square brackets `[]`:

```python
# List comprehension — builds the entire list in memory
squares_list = [x**2 for x in range(10)]

# Generator expression — produces values lazily
squares_gen = (x**2 for x in range(10))
```

Generator expressions are perfect when you're passing data to a function that will consume it once:

```python
# No need to build an intermediate list — just pass a generator
total = sum(x**2 for x in range(1_000_000))
```

When a generator expression is the only argument to a function, you can drop the extra parentheses. `sum((x**2 for x in range(10)))` and `sum(x**2 for x in range(10))` are the same thing.

### Generators Are Single-Use (Exhaustion)

This is a common gotcha. Once a generator has yielded all its values, it's **done**. You can't rewind it or iterate over it again:

```python
gen = (x for x in [1, 2, 3])

print(list(gen))  # [1, 2, 3]
print(list(gen))  # [] — empty! The generator is exhausted.
```

If you need to iterate multiple times, either use a list or create a new generator each time.

### Memory Efficiency

This is the #1 reason to use generators. When working with large datasets, generators can be the difference between a program that runs smoothly and one that eats all your RAM:

```python
# BAD — loads entire file into memory as a list of lines
def get_lines_list(filename):
    with open(filename) as f:
        return f.readlines()   # every line stored in a list

# GOOD — yields one line at a time
def get_lines_gen(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

A list of 10 million items sits in memory all at once. A generator that produces 10 million items only ever holds **one item** in memory at a time. Same results, fraction of the memory.

### `yield from` — Delegating to Sub-Generators

When you want a generator to yield all the values from another iterable, you could write a loop:

```python
def flatten(nested):
    for sublist in nested:
        for item in sublist:
            yield item
```

But `yield from` does this more cleanly:

```python
def flatten(nested):
    for sublist in nested:
        yield from sublist
```

`yield from` delegates to another iterator, yielding each of its values as if your generator had yielded them directly. It's cleaner, faster, and the idiomatic way to compose generators.

```python
def gen_a():
    yield 1
    yield 2

def gen_b():
    yield from gen_a()   # yields 1, then 2
    yield 3              # then yields 3

print(list(gen_b()))  # [1, 2, 3]
```

### Sending Values into Generators with `.send()`

Generators aren't just one-way streets. You can **send values back into** a running generator using `.send()`. The sent value becomes the result of the `yield` expression inside the generator:

```python
def accumulator():
    total = 0
    while True:
        value = yield total    # yield current total, receive new value
        total += value

gen = accumulator()
next(gen)            # "prime" the generator — advance to the first yield
print(gen.send(10))  # 10  (total is now 10)
print(gen.send(20))  # 30  (total is now 30)
print(gen.send(5))   # 35  (total is now 35)
```

The first call must be `next(gen)` (or `gen.send(None)`) to advance the generator to its first `yield`. After that, `.send(value)` both sends a value *in* and gets the next yielded value *out*.

This is an advanced feature. You won't need it often, but it's powerful for building coroutines and stateful data processors.

### Generator Pipelines

One of the most elegant uses of generators is chaining them together into a **pipeline**. Each generator does one small job, and data flows through the chain:

```python
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_comments(lines):
    for line in lines:
        if not line.startswith("#"):
            yield line

def to_uppercase(lines):
    for line in lines:
        yield line.upper()

# Chain them together — data flows through lazily
pipeline = to_uppercase(filter_comments(read_lines("config.txt")))

for line in pipeline:
    print(line)
```

Each stage processes one item at a time. Nothing is stored in intermediate lists. The whole pipeline is lazy from start to finish. This pattern is incredibly useful for ETL (Extract, Transform, Load) workflows and data processing.

### Practical Use Cases

Here's where generators really shine:

- **Reading huge files** — process a 10 GB log file without loading it into memory
- **Infinite sequences** — generate IDs, timestamps, or mathematical sequences forever
- **Database result sets** — fetch rows in batches instead of loading millions at once
- **Data pipelines** — chain read, filter, transform, and write steps together
- **Streaming data** — process network data as it arrives, chunk by chunk

### Generators vs Iterators

Under the hood, generators are just a convenient way to create iterators. When you write a generator function, Python automatically gives the returned object `__iter__()` and `__next__()` methods:

```python
# The hard way — writing a full iterator class
class CountUpTo:
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# The easy way — a generator function
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
```

Both are valid. The generator version is just dramatically less code for the same result. Use iterator classes when you need extra methods or complex state. Use generators for everything else.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- A generator function uses `yield` instead of `return` — it pauses and resumes execution
- Generator expressions use parentheses `()` instead of square brackets `[]`
- Generators are **lazy** — they produce values one at a time, on demand
- Generators are **single-use** — once exhausted, they're empty
- Generators are **memory efficient** — ideal for large datasets and streaming
- `yield from` delegates to another iterable cleanly
- `.send()` lets you push values back into a running generator
- Generator pipelines chain small, focused generators into powerful data processing workflows
- Every generator is an iterator, but generators are much less code to write
