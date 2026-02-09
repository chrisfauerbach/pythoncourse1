"""
Magic Methods — Exercises
==========================

Practice problems to test your understanding of magic methods.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import time


# =============================================================================
# Exercise 1: Fraction class — __str__ and __repr__
#
# Create a Fraction class that stores a numerator and denominator.
#
# - __repr__ should return something like: Fraction(3, 4)
# - __str__ should return something like:  3/4
#
# Test it:
#   f = Fraction(3, 4)
#   print(f)         -> 3/4
#   print(repr(f))   -> Fraction(3, 4)
#   print([f])       -> [Fraction(3, 4)]
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE — define the Fraction class, then test it
    pass


# =============================================================================
# Exercise 2: Temperature class — comparison operators
#
# Create a Temperature class that stores degrees and a scale ("C" or "F").
# Add a helper method _to_celsius() that converts to Celsius for comparison.
#
# Implement __eq__ and __lt__, then use @functools.total_ordering to get
# the rest for free.
#
# Test it:
#   t1 = Temperature(100, "C")
#   t2 = Temperature(212, "F")   # 212F == 100C
#   t3 = Temperature(0, "C")
#
#   print(t1 == t2)   -> True  (both are 100C)
#   print(t3 < t1)    -> True
#   print(t1 >= t3)   -> True
#
# Hint: The conversion formula is: C = (F - 32) * 5/9
# =============================================================================

def exercise_2():
    # YOUR CODE HERE — define the Temperature class, then test it
    pass


# =============================================================================
# Exercise 3: Vector class — arithmetic operators
#
# Create a Vector class with x, y, z components.
# Implement:
#   __add__  -> Vector + Vector (element-wise)
#   __sub__  -> Vector - Vector (element-wise)
#   __mul__  -> Vector * scalar (scale all components)
#   __repr__ -> Vector(x, y, z)
#
# Test it:
#   v1 = Vector(1, 2, 3)
#   v2 = Vector(4, 5, 6)
#   print(v1 + v2)   -> Vector(5, 7, 9)
#   print(v2 - v1)   -> Vector(3, 3, 3)
#   print(v1 * 10)   -> Vector(10, 20, 30)
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE — define the Vector class, then test it
    pass


# =============================================================================
# Exercise 4: Deck class — container protocol
#
# Create a Deck class that represents a deck of playing cards.
# Store the cards as a list of strings like "Ace of Spades", "2 of Hearts", etc.
#
# Implement:
#   __init__    -> build a full 52-card deck
#   __len__     -> number of cards in the deck
#   __getitem__ -> access cards by index (and slicing)
#   __contains__ -> check if a card is in the deck
#
# Use these ranks and suits:
#   ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
#   suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#
# Test it:
#   deck = Deck()
#   print(len(deck))                           -> 52
#   print(deck[0])                             -> Ace of Hearts
#   print(deck[-1])                            -> King of Spades
#   print("Ace of Spades" in deck)             -> True
#   print("Joker" in deck)                     -> False
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define the Deck class, then test it
    pass


# =============================================================================
# Exercise 5: Timer class — context manager
#
# Create a Timer context manager that:
#   - Records the start time in __enter__
#   - Calculates and stores the elapsed time in __exit__
#   - Has an elapsed attribute you can access after the block
#
# Test it:
#   with Timer() as t:
#       total = sum(range(1_000_000))
#   print(f"Elapsed: {t.elapsed:.4f} seconds")
#
# Bonus: Add a label parameter so it prints itself:
#   with Timer("Heavy computation"):
#       total = sum(range(1_000_000))
#   # prints: [Heavy computation] 0.0312 seconds
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define the Timer class, then test it
    pass


# =============================================================================
# Exercise 6: Custom Range class — iteration protocol
#
# Create a FloatRange class that works like range() but supports floats.
#
# FloatRange(start, stop, step) should:
#   - Implement __iter__ (return self)
#   - Implement __next__ (return next value or raise StopIteration)
#
# Test it:
#   for val in FloatRange(0.0, 1.0, 0.2):
#       print(f"{val:.1f}", end=" ")
#   # Output: 0.0 0.2 0.4 0.6 0.8
#
#   print(list(FloatRange(1.0, 2.0, 0.3)))
#   # Output: [1.0, 1.3, 1.6, 1.9]
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define the FloatRange class, then test it
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    class Fraction:
        def __init__(self, numerator, denominator):
            self.numerator = numerator
            self.denominator = denominator

        def __repr__(self):
            return f"Fraction({self.numerator}, {self.denominator})"

        def __str__(self):
            return f"{self.numerator}/{self.denominator}"

    f1 = Fraction(3, 4)
    f2 = Fraction(1, 2)
    print(f"str:  {f1}")
    print(f"repr: {repr(f1)}")
    print(f"list: {[f1, f2]}")


def solution_2():
    from functools import total_ordering

    @total_ordering
    class Temperature:
        def __init__(self, degrees, scale="C"):
            self.degrees = degrees
            self.scale = scale

        def _to_celsius(self):
            if self.scale == "C":
                return self.degrees
            return (self.degrees - 32) * 5 / 9

        def __repr__(self):
            return f"Temperature({self.degrees}, {self.scale!r})"

        def __str__(self):
            return f"{self.degrees}\u00b0{self.scale}"

        def __eq__(self, other):
            if not isinstance(other, Temperature):
                return NotImplemented
            return round(self._to_celsius(), 6) == round(other._to_celsius(), 6)

        def __lt__(self, other):
            if not isinstance(other, Temperature):
                return NotImplemented
            return self._to_celsius() < other._to_celsius()

    t1 = Temperature(100, "C")
    t2 = Temperature(212, "F")
    t3 = Temperature(0, "C")

    print(f"{t1} == {t2}: {t1 == t2}")   # True — both are 100C
    print(f"{t3} <  {t1}: {t3 < t1}")    # True
    print(f"{t1} >= {t3}: {t1 >= t3}")   # True (auto-derived)
    print(f"{t3} <= {t2}: {t3 <= t2}")   # True (auto-derived)


def solution_3():
    class Vector:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __repr__(self):
            return f"Vector({self.x}, {self.y}, {self.z})"

        def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

        def __sub__(self, other):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

        def __mul__(self, scalar):
            return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v2 - v1 = {v2 - v1}")
    print(f"v1 * 10 = {v1 * 10}")


def solution_4():
    class Deck:
        def __init__(self):
            ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                     "8", "9", "10", "Jack", "Queen", "King"]
            suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
            self._cards = [f"{rank} of {suit}"
                           for suit in suits for rank in ranks]

        def __len__(self):
            return len(self._cards)

        def __getitem__(self, index):
            return self._cards[index]

        def __contains__(self, card):
            return card in self._cards

    deck = Deck()
    print(f"Cards in deck: {len(deck)}")
    print(f"First card:    {deck[0]}")
    print(f"Last card:     {deck[-1]}")
    print(f"Top 3:         {deck[:3]}")
    print(f"'Ace of Spades' in deck: {'Ace of Spades' in deck}")
    print(f"'Joker' in deck:         {'Joker' in deck}")


def solution_5():
    class Timer:
        def __init__(self, label=None):
            self.label = label
            self.elapsed = 0

        def __enter__(self):
            self.start = time.time()
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.elapsed = time.time() - self.start
            if self.label:
                print(f"  [{self.label}] {self.elapsed:.4f} seconds")
            return False

    with Timer("Sum to 1 million") as t:
        total = sum(range(1_000_000))
        print(f"  Total: {total}")
    print(f"  Elapsed: {t.elapsed:.4f} seconds")


def solution_6():
    class FloatRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step
            self.current = start

        def __iter__(self):
            self.current = self.start
            return self

        def __next__(self):
            if self.current >= self.stop:
                raise StopIteration
            value = round(self.current, 10)
            self.current += self.step
            return value

    print("FloatRange(0.0, 1.0, 0.2):", end=" ")
    for val in FloatRange(0.0, 1.0, 0.2):
        print(f"{val:.1f}", end=" ")
    print()

    print(f"FloatRange(1.0, 2.0, 0.3): {list(FloatRange(1.0, 2.0, 0.3))}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Fraction class: __str__ and __repr__", exercise_1),
        ("Temperature class: comparison operators", exercise_2),
        ("Vector class: arithmetic operators", exercise_3),
        ("Deck class: container protocol", exercise_4),
        ("Timer class: context manager", exercise_5),
        ("FloatRange class: iteration protocol", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
    print()
    print("Solutions:")
    print()

    solutions = [
        ("Fraction class", solution_1),
        ("Temperature class", solution_2),
        ("Vector class", solution_3),
        ("Deck class", solution_4),
        ("Timer class", solution_5),
        ("FloatRange class", solution_6),
    ]

    for i, (title, func) in enumerate(solutions, 1):
        print("=" * 50)
        print(f"SOLUTION {i}: {title}")
        print("=" * 50)
        func()
        print()
