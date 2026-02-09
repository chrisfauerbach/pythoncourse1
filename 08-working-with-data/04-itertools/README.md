# Itertools

## Objective

Learn to use Python's `itertools` module -- a toolbox of fast, memory-efficient building blocks for working with iterators. Once you get comfortable with itertools, you'll find yourself writing less code that runs faster.

## Concepts Covered

- What itertools is and why it exists
- Infinite iterators: `count()`, `cycle()`, `repeat()`
- Finite iterators: `chain()`, `compress()`, `dropwhile()`, `takewhile()`, `islice()`, `zip_longest()`
- Combinatoric iterators: `product()`, `permutations()`, `combinations()`, `combinations_with_replacement()`
- Grouping with `groupby()`
- Running totals with `accumulate()`
- Applying functions with `starmap()`
- Cloning iterators with `tee()`
- Practical patterns (flatten, chunk, sliding window, round-robin)
- Memory efficiency -- why itertools returns iterators, not lists

## Prerequisites

- Comfortable with loops, lists, and tuples
- Basic understanding of iterators and generators
- Familiarity with `lambda` and simple functions

## Lesson

### What Is itertools?

The `itertools` module is part of Python's standard library -- no `pip install` needed. It gives you a collection of fast, memory-efficient functions that produce **iterators** for common patterns. Think of it as a Swiss Army knife for looping.

```python
import itertools
```

The key insight: itertools functions return **iterators**, not lists. They generate values one at a time, on demand. That means they can handle enormous (even infinite!) sequences without eating up all your memory.

### Infinite Iterators

These never stop on their own -- you need to break out manually or use something like `islice()` to grab a finite chunk.

**`count(start=0, step=1)`** -- counts up forever:

```python
from itertools import count

for i in count(10, 2):    # 10, 12, 14, 16, ...
    if i > 20:
        break
    print(i)
```

**`cycle(iterable)`** -- loops through an iterable endlessly:

```python
from itertools import cycle

colors = cycle(["red", "green", "blue"])
for _ in range(7):
    print(next(colors))   # red, green, blue, red, green, blue, red
```

**`repeat(value, times=None)`** -- repeats a value forever (or a set number of times):

```python
from itertools import repeat

list(repeat("hello", 3))  # ['hello', 'hello', 'hello']
```

### Finite Iterators

These consume one or more iterables and produce a new (finite) iterator.

**`chain(*iterables)`** -- glues multiple iterables together end-to-end:

```python
from itertools import chain

list(chain([1, 2], [3, 4], [5, 6]))  # [1, 2, 3, 4, 5, 6]
```

**`chain.from_iterable(iterable)`** -- same idea, but takes a single iterable of iterables. Great for flattening:

```python
nested = [[1, 2], [3, 4], [5, 6]]
list(chain.from_iterable(nested))  # [1, 2, 3, 4, 5, 6]
```

**`compress(data, selectors)`** -- filters data using a parallel list of booleans:

```python
from itertools import compress

data = ["a", "b", "c", "d", "e"]
mask = [True, False, True, False, True]
list(compress(data, mask))  # ['a', 'c', 'e']
```

**`dropwhile(predicate, iterable)`** -- skips items as long as the predicate is True, then yields everything after:

```python
from itertools import dropwhile

list(dropwhile(lambda x: x < 5, [1, 3, 5, 2, 7]))  # [5, 2, 7]
```

**`takewhile(predicate, iterable)`** -- the opposite -- yields items while the predicate is True, then stops:

```python
from itertools import takewhile

list(takewhile(lambda x: x < 5, [1, 3, 5, 2, 7]))  # [1, 3]
```

**`islice(iterable, stop)` / `islice(iterable, start, stop, step)`** -- like list slicing, but for any iterator:

```python
from itertools import islice

list(islice(range(100), 5, 10))  # [5, 6, 7, 8, 9]
```

This is how you grab a finite chunk from an infinite iterator -- `islice(count(), 10)` gives you the first 10 values.

**`zip_longest(*iterables, fillvalue=None)`** -- like `zip()`, but continues until the *longest* iterable is exhausted:

```python
from itertools import zip_longest

names = ["Alice", "Bob"]
scores = [95, 87, 92]
list(zip_longest(names, scores, fillvalue="N/A"))
# [('Alice', 95), ('Bob', 87), ('N/A', 92)]
```

### Combinatoric Iterators

These generate every possible combination, permutation, or product from your data.

**`product(*iterables, repeat=1)`** -- Cartesian product (like nested for loops):

```python
from itertools import product

list(product("AB", "12"))
# [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

# repeat parameter is like product with itself:
list(product([0, 1], repeat=3))  # all 3-bit binary combos
```

**`permutations(iterable, r=None)`** -- all possible orderings:

```python
from itertools import permutations

list(permutations("ABC", 2))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
```

**`combinations(iterable, r)`** -- all subsets of size r (order doesn't matter):

```python
from itertools import combinations

list(combinations("ABCD", 2))
# [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
```

**`combinations_with_replacement(iterable, r)`** -- same as above, but items can repeat:

```python
from itertools import combinations_with_replacement

list(combinations_with_replacement("AB", 3))
# [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'B', 'B'), ('B', 'B', 'B')]
```

### Grouping with groupby()

`groupby(iterable, key=None)` groups consecutive elements that share the same key. **Critical rule: your data must be sorted by the grouping key first!** If it's not sorted, you'll get multiple groups for the same key.

```python
from itertools import groupby

data = [("math", "Alice"), ("math", "Bob"), ("science", "Carol"), ("science", "Dave")]

for subject, students in groupby(data, key=lambda x: x[0]):
    print(subject, "->", [s[1] for s in students])
# math -> ['Alice', 'Bob']
# science -> ['Carol', 'Dave']
```

### accumulate() -- Running Totals and More

`accumulate(iterable, func=operator.add)` produces running results. By default it does a running sum, but you can pass any two-argument function:

```python
from itertools import accumulate
import operator

list(accumulate([1, 2, 3, 4, 5]))                  # [1, 3, 6, 10, 15]  running sum
list(accumulate([1, 2, 3, 4, 5], operator.mul))     # [1, 2, 6, 24, 120]  running product
list(accumulate([3, 1, 4, 1, 5], max))              # [3, 3, 4, 4, 5]  running max
```

### starmap() -- Unpacking Arguments

`starmap(function, iterable)` is like `map()`, but it unpacks each element as arguments. Perfect when your data is already paired up:

```python
from itertools import starmap

pairs = [(2, 3), (4, 5), (6, 7)]
list(starmap(pow, pairs))       # [8, 1024, 279936]  -- pow(2,3), pow(4,5), pow(6,7)
list(starmap(max, [(3, 1), (5, 2), (4, 8)]))  # [3, 5, 8]
```

### tee() -- Cloning Iterators

`tee(iterable, n=2)` creates `n` independent copies of an iterator. This is useful when you need to iterate through the same data multiple times but your source is a one-shot iterator:

```python
from itertools import tee

original = iter([1, 2, 3, 4, 5])
copy1, copy2 = tee(original)

print(list(copy1))  # [1, 2, 3, 4, 5]
print(list(copy2))  # [1, 2, 3, 4, 5]
```

**Important:** Once you call `tee()`, don't use the original iterator anymore -- it'll mess up the copies.

### Practical Patterns

These are common real-world patterns you can build with itertools.

**Flatten a list of lists:**

```python
nested = [[1, 2], [3], [4, 5, 6]]
flat = list(chain.from_iterable(nested))  # [1, 2, 3, 4, 5, 6]
```

**Chunk a list into groups of n:**

```python
def chunked(iterable, n):
    it = iter(iterable)
    while chunk := list(islice(it, n)):
        yield chunk

list(chunked(range(10), 3))  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```

**Sliding window:**

```python
def sliding_window(iterable, n):
    it = iter(iterable)
    window = list(islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window = window[1:] + [item]
        yield tuple(window)

list(sliding_window([1, 2, 3, 4, 5], 3))
# [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
```

**Round-robin across iterables:**

```python
def round_robin(*iterables):
    """Yield one item from each iterable, rotating through them."""
    iterators = [iter(it) for it in iterables]
    while iterators:
        next_round = []
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                continue
            else:
                next_round.append(it)
        iterators = next_round
```

### itertools Recipes from the Docs

The official Python docs include a [recipes section](https://docs.python.org/3/library/itertools.html#itertools-recipes) with battle-tested patterns. A couple worth knowing:

**`pairwise()`** (built-in since Python 3.10) -- gives you overlapping pairs:

```python
from itertools import pairwise  # Python 3.10+

list(pairwise([1, 2, 3, 4]))  # [(1, 2), (2, 3), (3, 4)]
```

**`batched()`** (built-in since Python 3.12) -- splits an iterable into fixed-size chunks:

```python
from itertools import batched  # Python 3.12+

list(batched("ABCDEFG", 3))  # [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]
```

### Memory Efficiency

This is the whole reason itertools exists. Compare these two approaches for processing a million numbers:

```python
# This creates a full list in memory -- all million items at once
squares = [x**2 for x in range(1_000_000)]

# This generates values one at a time -- barely uses any memory
from itertools import islice, count
squares = (x**2 for x in count())
first_ten = list(islice(squares, 10))
```

When you chain itertools functions together, you build a **pipeline** where each value flows through every step before the next value is even generated. No intermediate lists are created. This is why itertools can process datasets that are larger than your available memory.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- `itertools` is a standard library module -- no installation needed
- All itertools functions return **iterators**, not lists -- wrap in `list()` when you need to see the results
- Infinite iterators (`count`, `cycle`, `repeat`) run forever -- always limit them with `islice()` or a `break`
- `chain()` glues iterables together; `chain.from_iterable()` flattens one level
- `groupby()` groups consecutive elements -- **sort your data first** or you'll get fragmented groups
- Combinatoric tools (`product`, `permutations`, `combinations`) generate every possible arrangement -- watch out, these can produce huge outputs
- `accumulate()` builds running totals (or running anything -- pass your own function)
- `starmap()` applies a function to pre-unpacked arguments
- The real power is chaining itertools together into memory-efficient pipelines
- Check the [official recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes) for more patterns
