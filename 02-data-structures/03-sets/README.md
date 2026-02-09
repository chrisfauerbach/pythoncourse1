# Sets

## Objective

Understand Python sets — an unordered collection of unique elements — and learn when (and why) they're the right tool for the job.

## Concepts Covered

- What sets are and how they differ from lists
- Creating sets and the empty set gotcha
- Adding and removing elements
- Set operations: union, intersection, difference, symmetric difference
- Subset, superset, and disjoint checks
- Frozen sets (immutable sets)
- When to use sets vs lists
- Performance: O(1) membership testing

## Prerequisites

- [Lists and Tuples](../01-lists-and-tuples/)
- [Dictionaries](../02-dictionaries/) — helpful but not required

## Lesson

### What Is a Set?

A set is an **unordered** collection of **unique** elements. Think of it like a bag of items where:

- **No duplicates** — each element can only appear once
- **No order** — there's no "first" or "last" item, so no indexing with `[0]`
- **Fast lookups** — checking if something is in a set is extremely fast

If you've ever needed to remove duplicates from a list or quickly check membership, sets are your best friend.

### Creating Sets

Use curly braces `{}` with comma-separated values:

```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

You can also use the `set()` constructor:

```python
vowels = set("aeiou")          # {'a', 'e', 'i', 'o', 'u'}
from_list = set([1, 2, 2, 3])  # {1, 2, 3} — duplicates removed!
```

That last one is a super handy trick — converting a list to a set instantly removes all duplicates.

### The Empty Set Gotcha

This is a classic Python "gotcha" that trips up everyone at least once:

```python
# This creates an empty DICTIONARY, not a set!
not_a_set = {}
print(type(not_a_set))  # <class 'dict'>

# This creates an empty set
actually_a_set = set()
print(type(actually_a_set))  # <class 'set'>
```

Why? Because `{}` was already taken by dictionaries. Python chose to keep backward compatibility, so `set()` is the only way to create an empty set.

### Adding and Removing Elements

#### Adding

```python
colors = {"red", "green"}
colors.add("blue")        # Add a single element
print(colors)             # {"red", "green", "blue"}
```

Adding an element that already exists does nothing — no error, no duplicate.

#### Removing

There are several ways to remove elements, each with different behavior:

```python
colors = {"red", "green", "blue"}

# .discard() — removes if present, does nothing if not
colors.discard("red")      # Removes "red"
colors.discard("purple")   # No error, just does nothing

# .remove() — removes if present, raises KeyError if not
colors.remove("green")     # Removes "green"
# colors.remove("purple")  # KeyError! "purple" not in set

# .pop() — removes and returns an arbitrary element
item = colors.pop()        # Removes some element (you can't predict which)

# .clear() — removes everything
colors.clear()             # set()
```

Use `.discard()` when you don't care if the element exists. Use `.remove()` when it *should* exist and something is wrong if it doesn't.

### Set Operations

This is where sets really shine. Python gives you both **operators** and **method** equivalents for all the classic set operations.

#### Union — all elements from both sets

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b            # {1, 2, 3, 4, 5}
a.union(b)       # {1, 2, 3, 4, 5}
```

#### Intersection — elements in both sets

```python
a & b              # {3}
a.intersection(b)  # {3}
```

#### Difference — elements in the first set but not the second

```python
a - b              # {1, 2}
a.difference(b)    # {1, 2}
```

#### Symmetric Difference — elements in either set, but not both

```python
a ^ b                       # {1, 2, 4, 5}
a.symmetric_difference(b)   # {1, 2, 4, 5}
```

The methods have one advantage over the operators: they accept any iterable, not just sets. So `a.union([4, 5, 6])` works, but `a | [4, 5, 6]` doesn't.

### Subset, Superset, and Disjoint

You can check relationships between sets:

```python
small = {1, 2}
big = {1, 2, 3, 4, 5}
other = {10, 20}

# Is every element of small also in big?
small.issubset(big)     # True
small <= big            # True

# Strict subset (subset but not equal)
small < big             # True

# Does big contain every element of small?
big.issuperset(small)   # True
big >= small            # True

# Strict superset
big > small             # True

# Do the two sets share NO elements at all?
small.isdisjoint(other)  # True
big.isdisjoint(other)    # True
small.isdisjoint(big)    # False — they share {1, 2}
```

### Frozen Sets

A `frozenset` is just like a set, but **immutable** — you can't add or remove elements after creation. This makes them:

- **Hashable** — so you can use them as dictionary keys or put them inside other sets
- **Safe** — you know nobody can accidentally modify them

```python
fs = frozenset([1, 2, 3])

# All the read operations work
print(3 in fs)            # True
print(fs | {4, 5})        # frozenset({1, 2, 3, 4, 5})

# But you can't modify them
# fs.add(4)               # AttributeError!

# Use as a dict key (normal sets can't do this)
permissions = {
    frozenset({"read"}): "viewer",
    frozenset({"read", "write"}): "editor",
    frozenset({"read", "write", "admin"}): "admin",
}
```

### When to Use Sets vs Lists

Use a **set** when:
- You need unique elements (automatic deduplication)
- You need fast membership testing ("is X in this collection?")
- You want to do set operations (union, intersection, etc.)
- Order doesn't matter

Use a **list** when:
- Order matters
- You need duplicates
- You need to access elements by index

### Performance: Why Sets Are Fast

Checking if an element is in a **list** requires scanning every element — that's **O(n)** time (it gets slower as the list grows).

Checking if an element is in a **set** uses a hash table — that's **O(1)** time (same speed no matter how big the set is).

```python
# Slow — checks up to 1 million items
big_list = list(range(1_000_000))
999_999 in big_list  # Scans the entire list

# Fast — instant lookup
big_set = set(range(1_000_000))
999_999 in big_set   # Hash lookup, basically instant
```

If you're doing a lot of `in` checks on a large collection, converting it to a set first can make your code dramatically faster.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Sets are unordered collections of unique elements — no duplicates, no indexing
- Create sets with `{1, 2, 3}` but use `set()` for an empty set (`{}` makes a dict!)
- `.add()` adds elements, `.discard()` removes safely, `.remove()` removes or raises `KeyError`
- Union (`|`), intersection (`&`), difference (`-`), and symmetric difference (`^`) are the core set operations
- Check relationships with `.issubset()`, `.issuperset()`, `.isdisjoint()` or `<=`, `>=`, `<`, `>`
- `frozenset` is an immutable set — hashable and usable as dict keys
- Sets have O(1) membership testing, making them way faster than lists for `in` checks
- Converting a list to a set is the easiest way to remove duplicates
