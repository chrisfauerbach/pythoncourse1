"""
Sets — Example Code
=====================

Run this file:
    python3 example.py

Sets are unordered collections of unique elements. This file walks through
everything you need to know — creating sets, modifying them, and using
the powerful set operations that make them so useful.
"""

# -----------------------------------------------------------------------------
# 1. Creating sets
# -----------------------------------------------------------------------------

# Curly braces with values
fruits = {"apple", "banana", "cherry"}
print("Fruits:", fruits)

# From a string — each character becomes an element
letters = set("hello")
print("Letters in 'hello':", letters)  # Only one 'l'!

# From a list — duplicates are removed automatically
numbers = set([1, 2, 2, 3, 3, 3, 4])
print("Deduplicated numbers:", numbers)  # {1, 2, 3, 4}

# The deduplication trick — super useful in practice
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
unique_names = set(names)
print("Unique names:", unique_names)

# -----------------------------------------------------------------------------
# 2. The empty set gotcha
# -----------------------------------------------------------------------------

# This is a dict, NOT a set!
not_a_set = {}
print("\nType of {}:", type(not_a_set))  # <class 'dict'>

# This is how you make an empty set
empty_set = set()
print("Type of set():", type(empty_set))  # <class 'set'>

# -----------------------------------------------------------------------------
# 3. Adding and removing elements
# -----------------------------------------------------------------------------

print("\n--- Adding and Removing ---")

colors = {"red", "green", "blue"}
print("Starting colors:", colors)

# .add() — add a single element
colors.add("yellow")
print("After add('yellow'):", colors)

# Adding a duplicate does nothing
colors.add("red")
print("After add('red') again:", colors)  # No change

# .discard() — remove safely (no error if missing)
colors.discard("green")
print("After discard('green'):", colors)
colors.discard("purple")  # No error, even though "purple" isn't there
print("After discard('purple'):", colors)  # No change, no error

# .remove() — remove or raise KeyError
colors.remove("blue")
print("After remove('blue'):", colors)
# colors.remove("blue")  # Would raise KeyError — already removed!

# .pop() — remove and return an arbitrary element
popped = colors.pop()
print(f"Popped '{popped}', remaining: {colors}")

# .clear() — remove everything
colors.clear()
print("After clear():", colors)  # set()

# -----------------------------------------------------------------------------
# 4. Membership testing (the in keyword)
# -----------------------------------------------------------------------------

print("\n--- Membership Testing ---")

languages = {"Python", "JavaScript", "Rust", "Go"}

print("Python" in languages)      # True
print("Java" in languages)        # False
print("Java" not in languages)    # True

# -----------------------------------------------------------------------------
# 5. Iterating over a set
# -----------------------------------------------------------------------------

print("\n--- Iterating ---")

# You can loop over a set, but remember: the order is NOT guaranteed
primes = {2, 3, 5, 7, 11, 13}
print("Primes:", end=" ")
for p in primes:
    print(p, end=" ")
print()  # Newline

# -----------------------------------------------------------------------------
# 6. Set operations — operators
# -----------------------------------------------------------------------------

print("\n--- Set Operations (Operators) ---")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(f"a = {a}")
print(f"b = {b}")

# Union — everything from both
print(f"a | b  (union):                {a | b}")

# Intersection — only what's in both
print(f"a & b  (intersection):         {a & b}")

# Difference — in a but not in b
print(f"a - b  (difference):           {a - b}")

# Symmetric difference — in either, but not both
print(f"a ^ b  (symmetric difference): {a ^ b}")

# -----------------------------------------------------------------------------
# 7. Set operations — method equivalents
# -----------------------------------------------------------------------------

print("\n--- Set Operations (Methods) ---")

# Methods work the same as operators
print(f"a.union(b):                    {a.union(b)}")
print(f"a.intersection(b):             {a.intersection(b)}")
print(f"a.difference(b):               {a.difference(b)}")
print(f"a.symmetric_difference(b):     {a.symmetric_difference(b)}")

# But methods accept ANY iterable, not just sets
print(f"a.union([10, 20]):             {a.union([10, 20])}")
print(f"a.intersection(range(3, 8)):   {a.intersection(range(3, 8))}")

# -----------------------------------------------------------------------------
# 8. Subset, superset, and disjoint
# -----------------------------------------------------------------------------

print("\n--- Subset, Superset, Disjoint ---")

small = {1, 2, 3}
big = {1, 2, 3, 4, 5, 6}
other = {10, 20, 30}

# Subset — is every element of small also in big?
print(f"{small} <= {big}:  {small <= big}")         # True
print(f"issubset: {small.issubset(big)}")           # True

# Strict subset — subset and NOT equal
print(f"{small} < {big}:   {small < big}")          # True
equal = {1, 2, 3}
print(f"{small} < {equal}: {small < equal}")        # False (they're equal)

# Superset — does big contain all of small?
print(f"{big} >= {small}:  {big >= small}")         # True
print(f"issuperset: {big.issuperset(small)}")       # True

# Disjoint — do they share NO elements?
print(f"{small} disjoint {other}:  {small.isdisjoint(other)}")  # True
print(f"{small} disjoint {big}:    {small.isdisjoint(big)}")    # False

# -----------------------------------------------------------------------------
# 9. Frozen sets — immutable sets
# -----------------------------------------------------------------------------

print("\n--- Frozen Sets ---")

# A frozenset can't be modified after creation
fs = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", fs)

# All read operations work fine
print("3 in fs:", 3 in fs)
print("fs & {2, 3, 4, 10}:", fs & {2, 3, 4, 10})

# You can use frozensets as dictionary keys
role_permissions = {
    frozenset({"read"}): "viewer",
    frozenset({"read", "write"}): "editor",
    frozenset({"read", "write", "delete"}): "admin",
}

my_perms = frozenset({"read", "write"})
print(f"Permissions {set(my_perms)} -> role: {role_permissions[my_perms]}")

# You can also put frozensets inside regular sets
set_of_sets = {frozenset({1, 2}), frozenset({3, 4})}
print("Set of frozensets:", set_of_sets)

# -----------------------------------------------------------------------------
# 10. Performance — sets vs lists for membership testing
# -----------------------------------------------------------------------------

print("\n--- Performance ---")

import time

# Build a large list and a large set with the same data
size = 1_000_000
big_list = list(range(size))
big_set = set(range(size))

# Search for an element near the end
target = size - 1

# Time the list lookup
start = time.time()
for _ in range(100):
    _ = target in big_list
list_time = time.time() - start

# Time the set lookup
start = time.time()
for _ in range(100):
    _ = target in big_set
set_time = time.time() - start

print(f"List lookup (100x): {list_time:.4f}s")
print(f"Set  lookup (100x): {set_time:.6f}s")
if set_time > 0:
    print(f"Set is ~{list_time / set_time:.0f}x faster")
else:
    print("Set is way faster")

# -----------------------------------------------------------------------------
# 11. Practical example — deduplication while preserving order
# -----------------------------------------------------------------------------

print("\n--- Bonus: Dedup While Preserving Order ---")

# set() removes duplicates but loses order. Here's a trick to keep order:
items = ["banana", "apple", "cherry", "apple", "banana", "date", "cherry"]
seen = set()
unique_ordered = []
for item in items:
    if item not in seen:
        seen.add(item)
        unique_ordered.append(item)

print("Original: ", items)
print("Unique (ordered):", unique_ordered)

# -----------------------------------------------------------------------------
# 12. Putting it all together
# -----------------------------------------------------------------------------

print()
print("=" * 40)
print("   SETS COMPLETE!")
print("=" * 40)
print()
print("Sets are your go-to for uniqueness, fast lookups, and set math.")
print("Try the exercises in exercises.py to practice!")
