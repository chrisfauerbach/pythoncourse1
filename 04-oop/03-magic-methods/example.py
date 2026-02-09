"""
Magic Methods — Example Code
==============================

Run this file:
    python3 example.py

This file demonstrates how magic methods (dunder methods) let your custom
classes integrate with Python's built-in syntax — operators, print(), len(),
for loops, with statements, and more.
"""

from functools import total_ordering
import time

# -----------------------------------------------------------------------------
# 1. String representation — __str__ vs __repr__
# -----------------------------------------------------------------------------

# __repr__ is for developers (debugging, REPL). Aim for valid Python code.
# __str__ is for users (print, str()). Aim for readability.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        # Developer-friendly — could recreate the object from this string
        return f"Product({self.name!r}, {self.price})"

    def __str__(self):
        # User-friendly — something nice to display
        return f"{self.name} (${self.price:.2f})"


print("=" * 60)
print("1. STRING REPRESENTATION: __str__ vs __repr__")
print("=" * 60)

laptop = Product("Laptop", 999.99)

# print() calls __str__
print(f"print(laptop):       {laptop}")

# repr() calls __repr__
print(f"repr(laptop):        {repr(laptop)}")

# Inside containers (lists, dicts), Python uses __repr__
products = [Product("Mouse", 29.99), Product("Keyboard", 79.99)]
print(f"List of products:    {products}")

print()


# -----------------------------------------------------------------------------
# 2. Comparison operators — with @functools.total_ordering
# -----------------------------------------------------------------------------

# Instead of writing all 6 comparison methods (__eq__, __ne__, __lt__, __le__,
# __gt__, __ge__), use @total_ordering. Just define __eq__ and __lt__, and
# Python fills in the rest.

@total_ordering
class Money:
    def __init__(self, amount, currency="USD"):
        self.amount = round(amount, 2)
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount}, {self.currency!r})"

    def __str__(self):
        symbols = {"USD": "$", "EUR": "\u20ac", "GBP": "\u00a3"}
        symbol = symbols.get(self.currency, self.currency + " ")
        return f"{symbol}{self.amount:.2f}"

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError(f"Can't compare {self.currency} with {other.currency}")
        return self.amount < other.amount


print("=" * 60)
print("2. COMPARISON OPERATORS: Money class with @total_ordering")
print("=" * 60)

price1 = Money(10.00)
price2 = Money(25.50)
price3 = Money(10.00)

print(f"{price1} == {price3}:  {price1 == price3}")    # True (same amount)
print(f"{price1} == {price2}:  {price1 == price2}")    # False
print(f"{price1} <  {price2}:  {price1 < price2}")     # True
print(f"{price2} >  {price1}:  {price2 > price1}")     # True (auto-derived!)
print(f"{price1} <= {price3}:  {price1 <= price3}")    # True (auto-derived!)
print(f"{price2} >= {price1}:  {price2 >= price1}")    # True (auto-derived!)

# Sorting works automatically because __lt__ is defined
prices = [Money(42.00), Money(7.99), Money(15.50), Money(3.25)]
print(f"Sorted: {sorted(prices)}")

print()


# -----------------------------------------------------------------------------
# 3. Arithmetic operators — Vector class
# -----------------------------------------------------------------------------

# __add__, __sub__, __mul__, __truediv__ let you use +, -, *, / on objects.
# Always return a NEW object — don't modify the original.

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        # Vector + Vector -> element-wise addition
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Vector - Vector -> element-wise subtraction
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # Vector * number -> scale both components
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        # Vector / number -> divide both components
        return Vector(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


print("=" * 60)
print("3. ARITHMETIC OPERATORS: Vector class")
print("=" * 60)

v1 = Vector(2, 3)
v2 = Vector(5, 1)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")       # Vector(7, 4)
print(f"v2 - v1 = {v2 - v1}")       # Vector(3, -2)
print(f"v1 * 3  = {v1 * 3}")        # Vector(6, 9)
print(f"v2 / 2  = {v2 / 2}")        # Vector(2.5, 0.5)

# You can chain operations — each one returns a new Vector
result = (v1 + v2) * 2
print(f"(v1 + v2) * 2 = {result}")  # Vector(14, 8)

print()


# -----------------------------------------------------------------------------
# 4. Container protocol — Playlist class
# -----------------------------------------------------------------------------

# __len__, __getitem__, __setitem__, __delitem__, __contains__ let your objects
# behave like lists or dictionaries.

class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self._songs)} songs)"

    def add(self, song):
        """Add a song to the playlist."""
        self._songs.append(song)

    def __len__(self):
        """len(playlist) -> number of songs."""
        return len(self._songs)

    def __getitem__(self, index):
        """playlist[i] -> get song at index i. Supports slicing too!"""
        return self._songs[index]

    def __setitem__(self, index, value):
        """playlist[i] = song -> replace song at index i."""
        self._songs[index] = value

    def __delitem__(self, index):
        """del playlist[i] -> remove song at index i."""
        del self._songs[index]

    def __contains__(self, song):
        """song in playlist -> check if song is in the playlist."""
        return song in self._songs


print("=" * 60)
print("4. CONTAINER PROTOCOL: Playlist class")
print("=" * 60)

rock = Playlist("Classic Rock")
rock.add("Stairway to Heaven")
rock.add("Bohemian Rhapsody")
rock.add("Hotel California")
rock.add("Free Bird")

# len() works
print(f"Playlist: {rock}")
print(f"Length:   {len(rock)} songs")

# Indexing works (including negative indexing!)
print(f"First:    {rock[0]}")
print(f"Last:     {rock[-1]}")

# Slicing works because __getitem__ delegates to the list
print(f"First 2:  {rock[:2]}")

# 'in' operator works
print(f"'Hotel California' in playlist: {'Hotel California' in rock}")
print(f"'Yesterday' in playlist:        {'Yesterday' in rock}")

# Assignment works
rock[1] = "We Will Rock You"
print(f"After replacing index 1: {rock[:]}")

# Deletion works
del rock[-1]
print(f"After deleting last:     {rock[:]}")

# __getitem__ even enables for loops!
print("All songs:")
for i, song in enumerate(rock, 1):
    print(f"  {i}. {song}")

print()


# -----------------------------------------------------------------------------
# 5. Iteration protocol — Countdown class
# -----------------------------------------------------------------------------

# __iter__ + __next__ let your objects work with for loops directly.
# Raise StopIteration from __next__ when there are no more items.

class Countdown:
    """Counts down from a starting number to 0."""

    def __init__(self, start):
        self.start = start
        self.current = start

    def __iter__(self):
        # Reset so we can iterate multiple times
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

    def __repr__(self):
        return f"Countdown({self.start})"


print("=" * 60)
print("5. ITERATION PROTOCOL: Countdown class")
print("=" * 60)

countdown = Countdown(5)

# for loop uses __iter__ and __next__ under the hood
print("Countdown:", end=" ")
for num in countdown:
    print(num, end=" ")
print()  # newline

# Works with list(), sum(), and other things that consume iterables
print(f"As list: {list(Countdown(3))}")
print(f"Sum:     {sum(Countdown(10))}")

print()


# -----------------------------------------------------------------------------
# 6. Callable objects — __call__
# -----------------------------------------------------------------------------

# __call__ lets you use an object as if it were a function.
# Great for objects that need to remember state between "calls."

class RunningAverage:
    """Keeps a running average. Call it with new values to update."""

    def __init__(self):
        self.values = []

    def __call__(self, new_value):
        self.values.append(new_value)
        avg = sum(self.values) / len(self.values)
        return avg

    def __repr__(self):
        return f"RunningAverage({len(self.values)} values, avg={self():.2f})" if self.values else "RunningAverage(empty)"


print("=" * 60)
print("6. CALLABLE OBJECTS: RunningAverage class")
print("=" * 60)

avg = RunningAverage()

# Use it like a function — each call updates the running average
test_scores = [85, 92, 78, 95, 88]
for score in test_scores:
    current_avg = avg(score)
    print(f"  Added {score}, running average: {current_avg:.1f}")

# It's callable, so callable() returns True
print(f"callable(avg): {callable(avg)}")

print()


# -----------------------------------------------------------------------------
# 7. Context manager protocol — __enter__ and __exit__
# -----------------------------------------------------------------------------

# __enter__ and __exit__ let your objects work with "with" statements.
# __enter__ sets things up. __exit__ cleans things up (even if an error occurs).

class Timer:
    """A context manager that measures elapsed time."""

    def __init__(self, label="Block"):
        self.label = label
        self.elapsed = 0

    def __enter__(self):
        self.start = time.time()
        return self  # This becomes the "as" variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start
        print(f"  [{self.label}] Elapsed: {self.elapsed:.6f} seconds")
        return False  # Don't suppress exceptions


print("=" * 60)
print("7. CONTEXT MANAGER: Timer class")
print("=" * 60)

# Time a block of code using "with"
with Timer("Sum of squares"):
    total = sum(x * x for x in range(1_000_000))
    print(f"  Result: {total}")

with Timer("String building"):
    result = "-".join(str(i) for i in range(10_000))
    print(f"  String length: {len(result)}")

print()


# -----------------------------------------------------------------------------
# 8. Making objects hashable — __hash__ and __eq__
# -----------------------------------------------------------------------------

# If you define __eq__, Python makes your class unhashable by default.
# To use objects as dict keys or in sets, you need to define __hash__ too.
# Rule: objects that are equal MUST have the same hash.

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        if not isinstance(other, Color):
            return NotImplemented
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def __hash__(self):
        # Use the same fields as __eq__ to compute the hash
        return hash((self.r, self.g, self.b))


print("=" * 60)
print("8. HASHABLE OBJECTS: Color class")
print("=" * 60)

# Because Color is hashable, it works as a dict key
color_names = {
    Color(255, 0, 0): "red",
    Color(0, 255, 0): "green",
    Color(0, 0, 255): "blue",
}

# Look up a color — a NEW Color(255, 0, 0) matches the key because
# __eq__ says they're equal and __hash__ gives the same hash
lookup = Color(255, 0, 0)
print(f"{lookup} -> {color_names[lookup]}")

# Colors work in sets too
unique_colors = {Color(255, 0, 0), Color(0, 0, 255), Color(255, 0, 0)}
print(f"Unique colors: {unique_colors}")
print(f"Count: {len(unique_colors)} (duplicate red was removed)")

print()


# -----------------------------------------------------------------------------
# 9. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 60)
print("THAT'S A WRAP!")
print("=" * 60)
print()
print("Magic methods covered:")
print("  __str__, __repr__     -> how your object looks when printed")
print("  __eq__, __lt__, etc.  -> comparison operators (==, <, >, ...)")
print("  __add__, __sub__, etc -> arithmetic operators (+, -, *, /)")
print("  __len__, __getitem__  -> container behavior (len, indexing)")
print("  __iter__, __next__    -> for loop support")
print("  __call__              -> make objects callable like functions")
print("  __enter__, __exit__   -> with statement support")
print("  __hash__              -> dict keys and set membership")
print()
print("Try modifying the classes above and running this file again!")
