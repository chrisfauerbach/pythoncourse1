# Comprehensions

## Objective

Learn to build lists, dicts, and sets in a single expressive line using comprehensions — one of Python's most beloved features.

## Concepts Covered

- List comprehensions (basic, filtered, transformed)
- Nested list comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions
- When to use comprehensions vs. regular loops

## Prerequisites

- [Dictionaries](../02-dictionaries/) and [Sets](../03-sets/)

## Lesson

### What Are Comprehensions?

A comprehension is a concise way to create a new collection by transforming and/or filtering items from an existing iterable. Instead of writing a multi-line loop that builds up a list piece by piece, you describe *what you want* in a single expression.

Comprehensions are considered "Pythonic" — they're a hallmark of clean, idiomatic Python code. Once you get the hang of them, you'll reach for them constantly.

### List Comprehensions — Basic Syntax

The simplest form takes every item from an iterable, applies an expression, and collects the results into a new list:

```python
[expression for item in iterable]
```

Here's the classic comparison. Without a comprehension:

```python
squares = []
for n in range(5):
    squares.append(n ** 2)
# squares = [0, 1, 4, 9, 16]
```

With a comprehension:

```python
squares = [n ** 2 for n in range(5)]
# squares = [0, 1, 4, 9, 16]
```

Same result, one line, easier to read once you know the pattern.

### Filtering with `if`

Add an `if` clause at the end to keep only items that pass a condition:

```python
[expression for item in iterable if condition]
```

Example — only even numbers:

```python
evens = [n for n in range(10) if n % 2 == 0]
# evens = [0, 2, 4, 6, 8]
```

The equivalent loop:

```python
evens = []
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
```

### Transforming with `if/else`

What if you want to include *every* item but transform it differently based on a condition? Put the `if/else` *before* the `for`:

```python
[expression_if_true if condition else expression_if_false for item in iterable]
```

Example — label numbers as "even" or "odd":

```python
labels = ["even" if n % 2 == 0 else "odd" for n in range(5)]
# labels = ["even", "odd", "even", "odd", "even"]
```

**Key difference:**
- `if` at the **end** = filter (fewer items in result)
- `if/else` at the **front** = transform (same number of items in result)

This trips people up at first. Just remember: filtering goes at the end, transforming goes at the front.

### Nested Comprehensions

You can nest `for` clauses to work with nested data. The order reads left to right, just like nested loops:

```python
[expression for outer in iterable1 for inner in iterable2]
```

Flatten a matrix (list of lists) into a single list:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
# flat = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

The equivalent nested loop:

```python
flat = []
for row in matrix:
    for num in row:
        flat.append(num)
```

You can also *create* nested structures. Transpose a matrix (swap rows and columns):

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# transposed = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
```

### Dictionary Comprehensions

Same idea, but you produce `key: value` pairs inside curly braces:

```python
{key_expr: value_expr for item in iterable}
```

Example — map each word to its length:

```python
words = ["hello", "world", "python"]
lengths = {word: len(word) for word in words}
# lengths = {"hello": 5, "world": 5, "python": 6}
```

Invert a dictionary (swap keys and values):

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# inverted = {1: "a", 2: "b", 3: "c"}
```

You can filter too:

```python
scores = {"Alice": 92, "Bob": 67, "Carol": 85, "Dave": 43}
passing = {name: score for name, score in scores.items() if score >= 70}
# passing = {"Alice": 92, "Carol": 85}
```

### Set Comprehensions

Curly braces without the colon give you a set — duplicates are automatically removed:

```python
{expression for item in iterable}
```

Example — unique first letters:

```python
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
first_letters = {word[0] for word in words}
# first_letters = {"a", "b", "c"}
```

### Generator Expressions

Replace the square brackets with parentheses and you get a **generator expression** — a lazy version that produces values one at a time instead of building the whole list in memory:

```python
(expression for item in iterable)
```

Example:

```python
# This creates a list in memory (all values computed at once)
sum_list = sum([n ** 2 for n in range(1000000)])

# This uses a generator (values computed one at a time — much less memory)
sum_gen = sum(n ** 2 for n in range(1000000))
```

Both produce the same result, but the generator version is more memory-efficient. You'll often see generators passed directly to functions like `sum()`, `max()`, `min()`, and `any()`.

Note: you can't index into a generator or iterate over it twice. It's a one-shot deal. If you need to reuse the values, use a list comprehension instead.

### When NOT to Use Comprehensions

Comprehensions are great, but they're not always the right call:

**Don't use them for side effects.** If you're not building a collection, use a regular loop:

```python
# Bad — creating a list just to throw it away
[print(x) for x in items]

# Good — a regular loop is the right tool here
for x in items:
    print(x)
```

**Don't sacrifice readability.** If your comprehension spans multiple lines and requires serious mental gymnastics to parse, just write a loop. There's no prize for fitting everything on one line.

```python
# This is getting hard to follow...
result = [transform(x) for group in data if valid(group)
          for x in group.items() if x.is_active and x.score > threshold]

# A loop with comments would be kinder to future-you
result = []
for group in data:
    if valid(group):
        for x in group.items():
            if x.is_active and x.score > threshold:
                result.append(transform(x))
```

**Rule of thumb:** If a comprehension doesn't fit comfortably on one line (maybe two), consider a loop instead.

### Comprehension vs. Loop — Side by Side

Here's a quick reference showing equivalent code:

| Goal | Loop | Comprehension |
|------|------|---------------|
| Transform | `for x in items: result.append(f(x))` | `[f(x) for x in items]` |
| Filter | `for x in items: if p(x): result.append(x)` | `[x for x in items if p(x)]` |
| Filter + Transform | `for x in items: if p(x): result.append(f(x))` | `[f(x) for x in items if p(x)]` |
| Dict from list | `for x in items: d[key(x)] = val(x)` | `{key(x): val(x) for x in items}` |

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- List comprehensions `[expr for x in iterable]` are the bread and butter — use them to build lists concisely
- Add `if` at the end to filter: `[expr for x in iterable if condition]`
- Add `if/else` at the front to transform: `[a if cond else b for x in iterable]`
- Dict comprehensions use `{key: val for ...}`, set comprehensions use `{expr for ...}`
- Generator expressions `(expr for ...)` are lazy and memory-efficient
- Readability beats cleverness — if a comprehension is hard to read, use a loop instead
- Never use a comprehension just for side effects (like printing)
