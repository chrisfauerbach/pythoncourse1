# The Collections Module

## Objective

Learn the specialized container types in Python's `collections` module — powerful upgrades to the built-in `dict`, `list`, `set`, and `tuple` that solve common problems with less code.

## Concepts Covered

- `Counter` — counting things effortlessly
- `defaultdict` — dictionaries with automatic default values
- `namedtuple` — tuples with named fields
- `deque` — double-ended queues for fast appends and pops from both ends
- `OrderedDict` — ordered dictionaries (mostly historical, but still useful)
- `ChainMap` — searching multiple dicts as one

## Prerequisites

- Dictionaries, lists, tuples, and sets
- Basic understanding of functions and classes

## Lesson

### What Is the Collections Module?

Python's built-in containers (`dict`, `list`, `set`, `tuple`) cover most situations. But sometimes you need something a little more specialized — a dictionary that counts things, a tuple with named fields, or a list that's fast at both ends.

That's what the `collections` module is for. It gives you container types that are built on top of the basics but add specific superpowers. You import them like this:

```python
from collections import Counter, defaultdict, namedtuple, deque, OrderedDict, ChainMap
```

Let's go through each one.

---

### Counter — Counting Things

`Counter` is a dictionary subclass designed for counting. Give it any iterable, and it counts how many times each element appears:

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

It works on strings too (counting characters):

```python
letters = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

#### most_common()

Get the top N most frequent items:

```python
count = Counter("abracadabra")
print(count.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]
```

#### Arithmetic on Counters

You can add, subtract, and combine Counters:

```python
morning = Counter(coffee=3, tea=1)
afternoon = Counter(coffee=1, tea=2, water=1)

total = morning + afternoon    # Counter({'coffee': 4, 'tea': 3, 'water': 1})
diff = morning - afternoon     # Counter({'coffee': 2}) — drops zero/negative
```

This makes Counters great for things like combining inventory counts or comparing frequency distributions.

---

### defaultdict — Dictionaries with Default Values

With a regular `dict`, accessing a missing key raises a `KeyError`. With `defaultdict`, missing keys get a default value automatically:

```python
from collections import defaultdict

# Group words by their first letter
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)

# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

Without `defaultdict`, you'd need to check `if key not in dict` or use `dict.setdefault()` every time. The `defaultdict` version is cleaner.

#### Common Factory Functions

The argument to `defaultdict` is a callable that produces the default value:

| Factory | Default Value | Use Case |
|---------|--------------|----------|
| `list` | `[]` | Grouping items by key |
| `int` | `0` | Counting occurrences |
| `set` | `set()` | Collecting unique items by key |
| `str` | `""` | Building strings by key |
| `lambda: "N/A"` | `"N/A"` | Custom default value |

```python
# Counting with defaultdict(int)
word_count = defaultdict(int)
for word in "the cat sat on the mat".split():
    word_count[word] += 1
# {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
```

---

### namedtuple — Tuples with Named Fields

Regular tuples are accessed by index, which can get confusing:

```python
point = (3, 7)
print(point[0])  # Is this x? y? Who knows?
```

`namedtuple` lets you give names to the fields:

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(p.x)  # 3
print(p.y)  # 7
```

They're still tuples — you can unpack them, index them, and iterate over them. But the named fields make your code far more readable.

#### _replace() — Creating Modified Copies

Named tuples are immutable (like regular tuples), so you can't change a field directly. Instead, use `_replace()` to get a new tuple with one or more fields changed:

```python
Color = namedtuple("Color", ["red", "green", "blue"])
sky = Color(135, 206, 235)
dark_sky = sky._replace(red=50, green=80)
# Color(red=50, green=80, blue=235)
```

#### _asdict() — Converting to a Dictionary

```python
print(sky._asdict())  # {'red': 135, 'green': 206, 'blue': 235}
```

#### When to Use namedtuple vs dataclass

- **namedtuple**: Immutable, lightweight, tuple-compatible. Great for simple data records.
- **dataclass** (from the `dataclasses` module): Mutable by default, supports methods, type hints, default values. Better for complex objects.

If you just need a simple, immutable container with named fields, `namedtuple` is perfect. If you need mutability, methods, or inheritance, reach for `dataclass`.

---

### deque — Double-Ended Queue

A `deque` (pronounced "deck") is like a list but optimized for fast appends and pops from **both ends**. Lists are fast at the right end but slow at the left (because everything has to shift over).

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)        # Add to right: deque([1, 2, 3, 4])
d.appendleft(0)    # Add to left:  deque([0, 1, 2, 3, 4])
d.pop()            # Remove from right: 4
d.popleft()        # Remove from left:  0
```

#### Rotation

Rotate elements right or left:

```python
d = deque([1, 2, 3, 4, 5])
d.rotate(2)   # Rotate right by 2: deque([4, 5, 1, 2, 3])
d.rotate(-2)  # Rotate left by 2:  deque([1, 2, 3, 4, 5])
```

#### maxlen — Fixed-Size Buffers

This is one of the most useful features. Set `maxlen` to create a buffer that automatically drops old items when new ones are added:

```python
history = deque(maxlen=3)
history.append("page1")
history.append("page2")
history.append("page3")
history.append("page4")  # "page1" is automatically dropped
print(history)  # deque(['page2', 'page3', 'page4'], maxlen=3)
```

This is perfect for "recent history" buffers, sliding windows, or keeping only the last N log entries.

---

### OrderedDict — Ordered Dictionaries

Since Python 3.7, regular `dict` preserves insertion order. So why does `OrderedDict` still exist?

Two reasons:

1. **`move_to_end()`** — move a key to the beginning or end:

```python
from collections import OrderedDict

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
od.move_to_end("a")          # Move "a" to the end
od.move_to_end("c", last=False)  # Move "c" to the beginning
```

2. **Equality considers order** — two `OrderedDicts` with the same items in different order are NOT equal. Two regular `dicts` with the same items in different order ARE equal:

```python
from collections import OrderedDict

d1 = OrderedDict([("a", 1), ("b", 2)])
d2 = OrderedDict([("b", 2), ("a", 1)])
print(d1 == d2)  # False — order matters!

# Compare with regular dicts:
print({"a": 1, "b": 2} == {"b": 2, "a": 1})  # True — order ignored
```

For most new code, regular `dict` is fine. Use `OrderedDict` when order matters for comparison or when you need `move_to_end()`.

---

### ChainMap — Searching Multiple Dicts as One

`ChainMap` groups multiple dictionaries into a single view. When you look up a key, it searches through the dicts in order — first match wins:

```python
from collections import ChainMap

defaults = {"color": "blue", "size": "medium", "debug": False}
user_prefs = {"color": "green"}
env_overrides = {"debug": True}

config = ChainMap(env_overrides, user_prefs, defaults)
print(config["color"])  # "green" — found in user_prefs
print(config["size"])   # "medium" — fell through to defaults
print(config["debug"])  # True — found in env_overrides
```

This is the classic **layered configuration** pattern: environment overrides beat user preferences, which beat defaults. `ChainMap` makes this trivial — no manual merging required.

The original dictionaries aren't copied. `ChainMap` just keeps references, so changes to the underlying dicts are reflected immediately.

---

### When to Use Each Collection Type

| Type | Use When... |
|------|-------------|
| `Counter` | You need to count things or find most common elements |
| `defaultdict` | You're grouping, counting, or collecting items by key |
| `namedtuple` | You want readable, immutable records with named fields |
| `deque` | You need fast appends/pops from both ends, or a fixed-size buffer |
| `OrderedDict` | You need order-aware equality or `move_to_end()` |
| `ChainMap` | You want to search multiple dicts as a layered stack |

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- The `collections` module provides specialized containers that solve common problems more cleanly than the built-in types
- `Counter` makes counting trivial — pass it any iterable and you get frequency counts instantly
- `defaultdict` eliminates boilerplate key-checking code when building up dictionaries
- `namedtuple` gives you readable, immutable records — a great lightweight alternative to classes
- `deque` is the go-to for fast double-ended operations and fixed-size buffers with `maxlen`
- `OrderedDict` still has niche uses even though `dict` is ordered in Python 3.7+
- `ChainMap` is perfect for layered configuration (defaults -> user -> environment)
- These aren't exotic — they're everyday tools that experienced Python developers reach for constantly
