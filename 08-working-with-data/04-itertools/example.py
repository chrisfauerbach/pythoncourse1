"""
Itertools -- Example Code
===========================

Run this file:
    python3 example.py

A tour of Python's itertools module -- fast, memory-efficient building blocks
for working with iterators. We'll cover infinite iterators, finite iterators,
combinatorics, grouping, accumulation, and practical patterns.
"""

import itertools
import operator

# -----------------------------------------------------------------------------
# 1. Infinite iterators -- count(), cycle(), repeat()
# -----------------------------------------------------------------------------

# count() -- counts from a start value, stepping by a given amount
# Be careful! This runs forever if you don't stop it.
print("count(10, 3) -- first 6 values:")
for i in itertools.count(10, 3):
    if i > 25:
        break
    print(f"  {i}", end="")
print()

# cycle() -- repeats an iterable endlessly
# Great for assigning things in rotation (colors, teams, shifts, etc.)
print("\ncycle(['A', 'B', 'C']) -- first 8 values:")
colors = itertools.cycle(["A", "B", "C"])
for _ in range(8):
    print(f"  {next(colors)}", end="")
print()

# repeat() -- repeats a single value, optionally a fixed number of times
print("\nrepeat('hey', 4):")
print(f"  {list(itertools.repeat('hey', 4))}")

# A practical use of repeat: multiply each number by 10 using map()
print("\nUsing repeat with map -- multiply each number by 10:")
numbers = [1, 2, 3, 4, 5]
result = list(map(pow, numbers, itertools.repeat(2)))
print(f"  pow(n, 2) for {numbers} = {result}")

# -----------------------------------------------------------------------------
# 2. Finite iterators -- chain(), compress(), dropwhile(), takewhile(),
#                         islice(), zip_longest()
# -----------------------------------------------------------------------------

# chain() -- glue multiple iterables together end-to-end
print("\n" + "=" * 60)
print("chain([1, 2], [3, 4], [5, 6]):")
print(f"  {list(itertools.chain([1, 2], [3, 4], [5, 6]))}")

# chain.from_iterable() -- same thing, but takes a single iterable of iterables
# This is the go-to way to flatten a list of lists
nested = [[1, 2], [3, 4], [5, 6]]
print(f"\nchain.from_iterable({nested}):")
print(f"  {list(itertools.chain.from_iterable(nested))}")

# compress() -- filter data using a parallel list of True/False selectors
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
working = [True, True, True, True, True, False, False]
print(f"\ncompress(days, working):")
print(f"  {list(itertools.compress(days, working))}")

# dropwhile() -- skip items WHILE condition is True, yield everything after
data = [1, 3, 5, 7, 2, 4, 6]
print(f"\ndropwhile(x < 5, {data}):")
print(f"  {list(itertools.dropwhile(lambda x: x < 5, data))}")

# takewhile() -- yield items WHILE condition is True, stop at first False
print(f"\ntakewhile(x < 5, {data}):")
print(f"  {list(itertools.takewhile(lambda x: x < 5, data))}")

# islice() -- slice any iterator (even infinite ones!) like a list
# islice(iterable, stop) or islice(iterable, start, stop, step)
print("\nislice(count(), 5, 15, 2) -- even numbers from count() starting at 5:")
print(f"  {list(itertools.islice(itertools.count(), 5, 15, 2))}")

print("\nislice(range(100), 3) -- first 3 items:")
print(f"  {list(itertools.islice(range(100), 3))}")

# zip_longest() -- like zip(), but fills in missing values instead of stopping
names = ["Alice", "Bob", "Carol"]
scores = [95, 87]
print(f"\nzip_longest({names}, {scores}, fillvalue='???'):")
print(f"  {list(itertools.zip_longest(names, scores, fillvalue='???'))}")

# -----------------------------------------------------------------------------
# 3. Combinatoric iterators -- product(), permutations(), combinations(),
#                               combinations_with_replacement()
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# product() -- Cartesian product (like nested for-loops)
print("product('AB', '12'):")
print(f"  {list(itertools.product('AB', '12'))}")

# product with repeat -- Cartesian product of an iterable with itself
print("\nproduct([0, 1], repeat=3) -- all 3-bit binary numbers:")
for combo in itertools.product([0, 1], repeat=3):
    print(f"  {''.join(str(b) for b in combo)}", end="")
print()

# permutations() -- all possible orderings of r items
print("\npermutations('ABC', 2) -- all 2-letter orderings:")
print(f"  {list(itertools.permutations('ABC', 2))}")

# combinations() -- subsets of r items (order doesn't matter)
print("\ncombinations('ABCD', 2) -- all 2-item subsets:")
print(f"  {list(itertools.combinations('ABCD', 2))}")

# combinations_with_replacement() -- subsets where items can repeat
print("\ncombinations_with_replacement('AB', 3):")
print(f"  {list(itertools.combinations_with_replacement('AB', 3))}")

# A practical example: generating all possible dice rolls with two dice
print("\nAll unique dice sums (2 dice, 1-6):")
dice_rolls = list(itertools.product(range(1, 7), repeat=2))
print(f"  Total possible rolls: {len(dice_rolls)}")
print(f"  First 5: {dice_rolls[:5]}...")

# -----------------------------------------------------------------------------
# 4. Grouping with groupby()
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# groupby() groups CONSECUTIVE items that share the same key.
# IMPORTANT: Data must be sorted by the grouping key first!

# Example: group students by their grade letter
students = [
    ("Alice", "A"),
    ("David", "A"),
    ("Bob", "B"),
    ("Eve", "B"),
    ("Carol", "C"),
]

# Data is already sorted by grade -- groupby will work correctly
print("groupby(students, key=grade):")
for grade, group in itertools.groupby(students, key=lambda s: s[1]):
    names = [name for name, _ in group]
    print(f"  Grade {grade}: {names}")

# What happens if you DON'T sort first? Let's see:
unsorted = [("Alice", "A"), ("Bob", "B"), ("Carol", "A"), ("Dave", "B")]
print("\nWARNING -- groupby on UNSORTED data (fragmented groups):")
for grade, group in itertools.groupby(unsorted, key=lambda s: s[1]):
    names = [name for name, _ in group]
    print(f"  Grade {grade}: {names}")

# Fix: sort first, then group
print("\nFIXED -- sort first, then groupby:")
sorted_data = sorted(unsorted, key=lambda s: s[1])
for grade, group in itertools.groupby(sorted_data, key=lambda s: s[1]):
    names = [name for name, _ in group]
    print(f"  Grade {grade}: {names}")

# -----------------------------------------------------------------------------
# 5. accumulate() -- running totals and more
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# Default: running sum
numbers = [1, 2, 3, 4, 5]
print(f"accumulate({numbers}) -- running sum:")
print(f"  {list(itertools.accumulate(numbers))}")

# Running product
print(f"\naccumulate({numbers}, operator.mul) -- running product:")
print(f"  {list(itertools.accumulate(numbers, operator.mul))}")

# Running max
temps = [72, 68, 75, 71, 80, 77]
print(f"\naccumulate({temps}, max) -- running max temperature:")
print(f"  {list(itertools.accumulate(temps, max))}")

# Practical: running bank balance from transactions
transactions = [1000, -200, -50, 300, -75, -100]
print(f"\nRunning balance from transactions {transactions}:")
balance = list(itertools.accumulate(transactions))
print(f"  {balance}")

# With an initial value (Python 3.8+)
print(f"\naccumulate([10, 20, 30], initial=100) -- starting from 100:")
print(f"  {list(itertools.accumulate([10, 20, 30], initial=100))}")

# -----------------------------------------------------------------------------
# 6. starmap() -- applying a function to pre-paired arguments
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# starmap() unpacks each tuple as arguments to the function
# It's like map(), but for functions that take multiple arguments

pairs = [(2, 3), (4, 5), (10, 2)]
print(f"starmap(pow, {pairs}):")
print(f"  {list(itertools.starmap(pow, pairs))}")
print(f"  That's pow(2,3)=8, pow(4,5)=1024, pow(10,2)=100")

# Great for applying operations to coordinate pairs
points = [(1, 4), (2, 5), (3, 6)]
print(f"\nstarmap(lambda x,y: x+y, {points}):")
print(f"  {list(itertools.starmap(lambda x, y: x + y, points))}")

# Compare: map() vs starmap()
print("\nmap(max, [3,1], [5,2], [4,8]) -- one arg from each iterable:")
print(f"  {list(map(max, [3, 1], [5, 2], [4, 8]))}")
print("starmap(max, [(3,1), (5,2), (4,8)]) -- unpack each tuple:")
print(f"  {list(itertools.starmap(max, [(3, 1), (5, 2), (4, 8)]))}")

# -----------------------------------------------------------------------------
# 7. tee() -- creating independent copies of an iterator
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# tee() clones an iterator into n independent copies
# Once you call tee(), don't use the original anymore!

original = iter([10, 20, 30, 40, 50])
copy_a, copy_b, copy_c = itertools.tee(original, 3)

print("tee(iterator, 3) -- three independent copies:")
print(f"  copy_a: {list(copy_a)}")
print(f"  copy_b: {list(copy_b)}")
print(f"  copy_c: {list(copy_c)}")

# Practical use: check the first item without consuming the iterator
data_iter = iter(["header", "row1", "row2", "row3"])
peek, consume = itertools.tee(data_iter)
first = next(peek)
print(f"\nPeek at first item: '{first}'")
print(f"Full iterator still intact: {list(consume)}")

# -----------------------------------------------------------------------------
# 8. Practical patterns -- flatten, chunk, sliding window, round-robin
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# Pattern 1: Flatten a list of lists (one level deep)
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = list(itertools.chain.from_iterable(nested))
print(f"Flatten {nested}:")
print(f"  {flat}")

# Pattern 2: Chunk a list into groups of n
def chunked(iterable, n):
    """Split an iterable into chunks of size n."""
    it = iter(iterable)
    while chunk := list(itertools.islice(it, n)):
        yield chunk

print(f"\nChunk range(10) into groups of 3:")
print(f"  {list(chunked(range(10), 3))}")

# Pattern 3: Sliding window
def sliding_window(iterable, n):
    """Yield overlapping tuples of size n from the iterable."""
    it = iter(iterable)
    window = list(itertools.islice(it, n))
    if len(window) == n:
        yield tuple(window)
    for item in it:
        window = window[1:] + [item]
        yield tuple(window)

print(f"\nSliding window of size 3 over [1, 2, 3, 4, 5, 6]:")
print(f"  {list(sliding_window([1, 2, 3, 4, 5, 6], 3))}")

# Pattern 4: Round-robin across multiple iterables
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

print(f"\nRound-robin(['A','B','C'], [1,2], ['x','y','z','w']):")
print(f"  {list(round_robin(['A', 'B', 'C'], [1, 2], ['x', 'y', 'z', 'w']))}")

# -----------------------------------------------------------------------------
# 9. itertools recipes from the docs -- pairwise() and batched()
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# pairwise() -- overlapping pairs (Python 3.10+)
try:
    from itertools import pairwise
    print("pairwise([1, 2, 3, 4, 5]):")
    print(f"  {list(pairwise([1, 2, 3, 4, 5]))}")
except ImportError:
    print("pairwise() requires Python 3.10+")

# batched() -- fixed-size chunks as tuples (Python 3.12+)
try:
    from itertools import batched
    print("\nbatched('ABCDEFG', 3):")
    print(f"  {list(batched('ABCDEFG', 3))}")
except ImportError:
    print("\nbatched() requires Python 3.12+ -- using our chunked() instead:")
    print(f"  {[tuple(c) for c in chunked('ABCDEFG', 3)]}")

# -----------------------------------------------------------------------------
# 10. Memory efficiency -- itertools creates pipelines, not lists
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)

# Instead of creating huge intermediate lists, itertools functions
# can be chained together into a lazy pipeline.

# Example: find the first 5 square numbers greater than 100
# This doesn't create a list of all squares -- it generates them one by one
squares_over_100 = itertools.islice(
    (x for x in itertools.count(1) if x * x > 100),
    5
)
print("First 5 numbers whose squares exceed 100:")
result = list(squares_over_100)
print(f"  Numbers: {result}")
print(f"  Squares: {[x*x for x in result]}")

# Chaining itertools together: flatten, filter, and take first 5
data = [[1, -2, 3], [-4, 5, -6], [7, 8, -9, 10]]
pipeline = itertools.islice(
    filter(lambda x: x > 0,                          # Step 2: keep positives
           itertools.chain.from_iterable(data)),      # Step 1: flatten
    5                                                  # Step 3: take first 5
)
print(f"\nFlatten {data}, keep positives, take 5:")
print(f"  {list(pipeline)}")

# -----------------------------------------------------------------------------
# 11. Putting it all together
# -----------------------------------------------------------------------------

print("\n" + "=" * 60)
print("ITERTOOLS COMPLETE!")
print("=" * 60)
print()
print("You now know how to use:")
print("  - Infinite iterators:  count, cycle, repeat")
print("  - Finite iterators:    chain, compress, dropwhile, takewhile, islice, zip_longest")
print("  - Combinatorics:       product, permutations, combinations")
print("  - Grouping:            groupby (sort first!)")
print("  - Accumulation:        accumulate")
print("  - Argument unpacking:  starmap")
print("  - Iterator cloning:    tee")
print()
print("Try combining them into pipelines for maximum power!")
