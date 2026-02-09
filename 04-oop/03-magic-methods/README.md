# Magic Methods

## Objective

Understand Python's magic methods (also called "dunder methods") and how they let your custom classes work seamlessly with Python's built-in syntax — operators, loops, `len()`, `print()`, `with` statements, and more.

## Concepts Covered

- What magic methods are and why they exist
- String representation: `__str__` vs `__repr__`
- Comparison operators: `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`
- The `@functools.total_ordering` shortcut
- Arithmetic operators: `__add__`, `__sub__`, `__mul__`, `__truediv__`
- Container protocol: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`
- Iteration protocol: `__iter__`, `__next__`
- Callable objects: `__call__`
- Context manager protocol: `__enter__`, `__exit__`
- Making objects hashable: `__hash__`

## Prerequisites

- [Classes and Objects](../01-classes-and-objects/)
- Basic understanding of Python operators and built-in functions

## Lesson

### What Are Magic Methods?

Magic methods are special methods whose names start and end with double underscores — like `__init__`, `__str__`, or `__add__`. You've already been using one: `__init__` is a magic method that runs when you create an object.

The "magic" part is that Python calls these methods automatically when you use certain syntax. You never call `obj.__add__(other)` directly — you just write `obj + other` and Python handles the translation for you.

```python
# When you write this...        Python actually calls this...
len(my_list)                   # my_list.__len__()
str(my_obj)                    # my_obj.__str__()
my_obj == other                # my_obj.__eq__(other)
my_obj + other                 # my_obj.__add__(other)
my_obj[0]                      # my_obj.__getitem__(0)
for item in my_obj:            # my_obj.__iter__() and __next__()
```

The whole point is to make your classes feel like native Python types. Instead of calling `vector.add(other_vector)`, you can just write `vector + other_vector`. That's much more natural.

### String Representation: `__str__` vs `__repr__`

These two methods both return strings, but they serve different purposes:

- **`__str__`** — the "pretty" version. This is what `print()` and `str()` use. It's meant for end users.
- **`__repr__`** — the "developer" version. This is what you see in the REPL and in debugging. Ideally, it should look like valid Python code that could recreate the object.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p)          # Calls __str__  -> (3, 4)
print(repr(p))    # Calls __repr__ -> Point(3, 4)
print([p])        # Items inside containers use __repr__ -> [Point(3, 4)]
```

**Pro tip:** If you only define one, define `__repr__`. Python will use it as a fallback for `__str__` too. But if you define `__str__` without `__repr__`, the REPL will still show the ugly default like `<__main__.Point object at 0x...>`.

### Comparison Operators

You can make your objects support `==`, `!=`, `<`, `<=`, `>`, and `>=` by implementing these methods:

| Operator | Method       |
|----------|-------------|
| `==`     | `__eq__`    |
| `!=`     | `__ne__`    |
| `<`      | `__lt__`    |
| `<=`     | `__le__`    |
| `>`      | `__gt__`    |
| `>=`     | `__ge__`    |

```python
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Can't compare different currencies")
        return self.amount < other.amount
```

**Important:** When you define `__eq__`, Python automatically makes your object unhashable (sets `__hash__` to `None`). We'll cover how to fix that later.

### `@functools.total_ordering` — The Lazy (Smart) Way

Implementing all six comparison methods is tedious. The `@functools.total_ordering` decorator lets you define just `__eq__` and ONE of the ordering methods (usually `__lt__`), and Python figures out the rest:

```python
from functools import total_ordering

@total_ordering
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if self.currency != other.currency:
            raise ValueError("Can't compare different currencies")
        return self.amount < other.amount

# Now all of these work automatically:
# Money(10) <= Money(20)  -> True  (derived from __eq__ and __lt__)
# Money(20) > Money(10)   -> True  (derived from __lt__ with swapped args)
# Money(20) >= Money(10)  -> True  (derived from __eq__ and __lt__)
```

### Arithmetic Operators

Make your objects support `+`, `-`, `*`, `/` and more:

| Operator | Method          |
|----------|----------------|
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v2 - v1)      # Vector(2, 2)
print(v1 * 3)       # Vector(3, 6)
```

Always return a **new object** from these methods — don't modify the original. Arithmetic should feel like it does with numbers: `3 + 4` doesn't change `3`.

### Container Protocol: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`

These methods let your objects behave like lists, dicts, or other containers:

```python
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):                    # len(playlist)
        return len(self._songs)

    def __getitem__(self, index):         # playlist[0]
        return self._songs[index]

    def __setitem__(self, index, value):  # playlist[0] = "new song"
        self._songs[index] = value

    def __delitem__(self, index):         # del playlist[0]
        del self._songs[index]

    def __contains__(self, song):         # "song" in playlist
        return song in self._songs
```

A nice bonus: if you implement `__getitem__`, Python can automatically iterate over your object using indexes (0, 1, 2, ...) even without `__iter__`. But it's better to be explicit and implement `__iter__` too.

### Iteration Protocol: `__iter__` and `__next__`

To make your object work with `for` loops, you need the iteration protocol:

- **`__iter__`** — returns an iterator object (often `self`). Called once at the start of a `for` loop.
- **`__next__`** — returns the next value. Called repeatedly. Raise `StopIteration` when there are no more items.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1, 0
```

**Common pattern:** Often `__iter__` just returns `self`, and the same object acts as both the iterable and the iterator. But be careful — this means you can only iterate once. For reusable iteration, have `__iter__` return a separate iterator object.

### Callable Objects: `__call__`

The `__call__` method lets you use an object as if it were a function:

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double(5))    # 10  — looks like a function call!
print(triple(5))    # 15
```

This is great for objects that need to remember state between calls — like a counter, a cache, or a configurable function.

### Context Manager Protocol: `__enter__` and `__exit__`

These methods let your objects work with `with` statements. This is the pattern you see with file handling (`with open(...) as f:`) — and you can create your own:

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self                    # This becomes the "as" variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start
        print(f"Elapsed: {elapsed:.4f} seconds")
        return False                   # Don't suppress exceptions

with Timer() as t:
    # Do some work...
    total = sum(range(1_000_000))
    # When the block ends, __exit__ runs and prints the time
```

The `__exit__` method receives exception info (`exc_type`, `exc_val`, `exc_tb`). If everything went fine, they're all `None`. Return `True` to suppress the exception, or `False` to let it propagate (almost always return `False`).

### Making Objects Hashable: `__hash__`

For an object to be used as a dictionary key or placed in a set, it must be hashable. Two rules:

1. Objects that compare equal (`__eq__`) **must** have the same hash.
2. Once you define `__eq__`, Python sets `__hash__` to `None` (making the object unhashable). You have to opt back in by defining `__hash__` yourself.

```python
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def __hash__(self):
        return hash((self.r, self.g, self.b))

# Now you can use Color in sets and as dict keys
colors = {Color(255, 0, 0): "red", Color(0, 255, 0): "green"}
```

**Warning:** Only make objects hashable if they're immutable (or at least if the attributes used in `__eq__` and `__hash__` won't change). If a mutable object's hash changes after being stored in a set or dict, things break in confusing ways.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Magic methods let your classes integrate with Python's built-in syntax (`+`, `[]`, `for`, `with`, `==`, etc.)
- `__repr__` is for developers, `__str__` is for users — always implement `__repr__` at minimum
- `@functools.total_ordering` saves you from writing all six comparison methods — just define `__eq__` and `__lt__`
- Arithmetic methods should return new objects, never mutate the originals
- The container protocol (`__len__`, `__getitem__`, etc.) makes your objects behave like lists or dicts
- `__iter__` + `__next__` let your objects work with `for` loops
- `__call__` turns objects into callable "smart functions" with state
- `__enter__` + `__exit__` let your objects work with `with` statements for clean resource management
- If you define `__eq__`, you must also define `__hash__` if you want your objects to work in sets and dicts
