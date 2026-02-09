"""
Lambda and Closures — Example Code
=====================================

Run this file:
    python3 example.py

This file demonstrates lambda functions, map/filter/reduce, sorting with
lambdas, closures, function factories, the nonlocal keyword, and the
classic "closures in loops" gotcha.
"""

from functools import reduce

# -----------------------------------------------------------------------------
# 1. Lambda basics — small anonymous functions
# -----------------------------------------------------------------------------

# A regular function...
def double_def(x):
    return x * 2

# ...and the same thing as a lambda
double_lambda = lambda x: x * 2

print("1. Lambda basics")
print(f"   double_def(5)    = {double_def(5)}")
print(f"   double_lambda(5) = {double_lambda(5)}")

# Multiple arguments
add = lambda a, b: a + b
print(f"   add(3, 7) = {add(3, 7)}")

# Ternary expression inside a lambda
classify = lambda x: "even" if x % 2 == 0 else "odd"
print(f"   classify(4) = {classify(4)}")
print(f"   classify(7) = {classify(7)}")

# Default arguments work too
greet = lambda name="World": f"Hello, {name}!"
print(f"   greet()        = {greet()}")
print(f"   greet('Alice') = {greet('Alice')}")
print()

# -----------------------------------------------------------------------------
# 2. map() — apply a function to every item in an iterable
# -----------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Square every number
squared = list(map(lambda x: x ** 2, numbers))

# Convert temperatures from Fahrenheit to Celsius
temps_f = [32, 72, 100, 212]
temps_c = list(map(lambda f: round((f - 32) * 5 / 9, 1), temps_f))

print("2. map() with lambda")
print(f"   numbers:  {numbers}")
print(f"   squared:  {squared}")
print(f"   temps_f:  {temps_f}")
print(f"   temps_c:  {temps_c}")
print()

# -----------------------------------------------------------------------------
# 3. filter() — keep items where the function returns True
# -----------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
big_numbers = list(filter(lambda x: x > 5, numbers))

# Filter strings by length
words = ["hi", "hello", "hey", "greetings", "yo", "sup"]
long_words = list(filter(lambda w: len(w) > 3, words))

print("3. filter() with lambda")
print(f"   numbers:     {numbers}")
print(f"   evens:       {evens}")
print(f"   big_numbers: {big_numbers}")
print(f"   words:       {words}")
print(f"   long_words:  {long_words}")
print()

# -----------------------------------------------------------------------------
# 4. reduce() — combine all items into a single value
# -----------------------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Sum all numbers: ((((1+2)+3)+4)+5) = 15
total = reduce(lambda a, b: a + b, numbers)

# Find the maximum: keeps the larger of each pair
maximum = reduce(lambda a, b: a if a > b else b, numbers)

# Join words with a separator
words = ["Python", "is", "fun"]
sentence = reduce(lambda a, b: a + " " + b, words)

print("4. reduce() with lambda")
print(f"   numbers:  {numbers}")
print(f"   total:    {total}")
print(f"   maximum:  {maximum}")
print(f"   words:    {words}")
print(f"   sentence: {sentence}")
print()

# -----------------------------------------------------------------------------
# 5. Sorting with lambda — one of the most common use cases
# -----------------------------------------------------------------------------

# Sort tuples by second element (score)
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92), ("Diana", 81)]
by_score = sorted(students, key=lambda s: s[1])
by_score_desc = sorted(students, key=lambda s: s[1], reverse=True)

print("5. Sorting with lambda")
print(f"   students:       {students}")
print(f"   by_score:       {by_score}")
print(f"   by_score_desc:  {by_score_desc}")

# Sort dicts by a field
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
by_age = sorted(people, key=lambda p: p["age"])
print(f"   by_age: {by_age}")

# Sort by multiple criteria — grade first, then name
roster = [("Alice", "B"), ("Bob", "A"), ("Charlie", "B"), ("Diana", "A")]
by_grade_name = sorted(roster, key=lambda s: (s[1], s[0]))
print(f"   by_grade_name:  {by_grade_name}")

# Sort strings case-insensitively
mixed_case = ["banana", "Apple", "cherry", "Date"]
sorted_ci = sorted(mixed_case, key=lambda s: s.lower())
print(f"   sorted_ci:      {sorted_ci}")
print()

# -----------------------------------------------------------------------------
# 6. Closures — functions that remember their enclosing scope
# -----------------------------------------------------------------------------

def make_greeter(greeting):
    """Return a function that greets people with a specific greeting."""
    def greet(name):
        return f"{greeting}, {name}!"  # 'greeting' is captured from the enclosing scope
    return greet

hello = make_greeter("Hello")
howdy = make_greeter("Howdy")
hola = make_greeter("Hola")

print("6. Closures — functions that remember")
print(f"   hello('Alice')   = {hello('Alice')}")
print(f"   howdy('Bob')     = {howdy('Bob')}")
print(f"   hola('Charlie')  = {hola('Charlie')}")

# You can inspect what a closure captured
print(f"   hello.__closure__[0].cell_contents = {hello.__closure__[0].cell_contents!r}")
print()

# -----------------------------------------------------------------------------
# 7. Function factories — closures that create specialized functions
# -----------------------------------------------------------------------------

def make_power(exp):
    """Return a function that raises numbers to the given power."""
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)
fourth = make_power(4)

print("7. Function factories")
print(f"   square(5) = {square(5)}")
print(f"   cube(5)   = {cube(5)}")
print(f"   fourth(5) = {fourth(5)}")

# Another factory: discount appliers
def make_discount(percent):
    """Return a function that applies a discount to a price."""
    def apply(price):
        return round(price * (1 - percent / 100), 2)
    return apply

half_off = make_discount(50)
twenty_pct = make_discount(20)

print(f"   half_off(100)    = {half_off(100)}")
print(f"   twenty_pct(100)  = {twenty_pct(100)}")
print()

# -----------------------------------------------------------------------------
# 8. Encapsulation with closures — hiding state without a class
# -----------------------------------------------------------------------------

def make_counter(start=0):
    """Create a simple counter with increment and get_count functions."""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    def get_count():
        return count

    return increment, get_count

inc, get = make_counter()
inc()
inc()
inc()

print("8. Encapsulation with closures")
print(f"   After 3 increments: get() = {get()}")
inc()
inc()
print(f"   After 2 more:       get() = {get()}")
print()

# -----------------------------------------------------------------------------
# 9. Closures vs classes — same behavior, different style
# -----------------------------------------------------------------------------

# Closure version
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

# Class version
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

closure_triple = make_multiplier(3)
class_triple = Multiplier(3)

print("9. Closures vs classes")
print(f"   closure_triple(10) = {closure_triple(10)}")
print(f"   class_triple(10)   = {class_triple(10)}")
print(f"   (Both produce the same result — closures are just simpler for this)")
print()

# -----------------------------------------------------------------------------
# 10. The nonlocal keyword — modifying captured variables
# -----------------------------------------------------------------------------

def make_accumulator(initial=0):
    """Return a function that adds to a running total."""
    total = initial

    def add(amount):
        nonlocal total   # Without this, 'total += amount' would fail
        total += amount
        return total

    return add

acc = make_accumulator()
print("10. The nonlocal keyword")
print(f"    acc(10) = {acc(10)}")
print(f"    acc(5)  = {acc(5)}")
print(f"    acc(20) = {acc(20)}")

# Start from a different initial value
acc2 = make_accumulator(100)
print(f"    acc2(1) = {acc2(1)}")
print(f"    acc2(1) = {acc2(1)}")
print()

# -----------------------------------------------------------------------------
# 11. Common gotcha — closures in loops (late binding)
# -----------------------------------------------------------------------------

print("11. Closures in loops (late binding gotcha)")

# THE BUG: all functions share the same variable 'i'
functions_buggy = []
for i in range(5):
    functions_buggy.append(lambda: i)

results_buggy = [f() for f in functions_buggy]
print(f"    Buggy:  {results_buggy}")     # [4, 4, 4, 4, 4] — whoops!

# THE FIX: default argument captures the value at creation time
functions_fixed = []
for i in range(5):
    functions_fixed.append(lambda i=i: i)  # i=i captures the current value

results_fixed = [f() for f in functions_fixed]
print(f"    Fixed:  {results_fixed}")      # [0, 1, 2, 3, 4] — correct!
print()

# -----------------------------------------------------------------------------
# 12. Putting it all together — a practical example
# -----------------------------------------------------------------------------

print("12. Putting it all together")

# Build a simple data pipeline using lambdas and closures
def make_pipeline(*functions):
    """Chain multiple functions into a single pipeline."""
    def pipeline(value):
        result = value
        for func in functions:
            result = func(result)
        return result
    return pipeline

# Create reusable transformation steps
clean = make_pipeline(
    lambda s: s.strip(),           # Remove whitespace
    lambda s: s.lower(),           # Lowercase
    lambda s: s.replace(" ", "_")  # Replace spaces with underscores
)

print(f"    clean('  Hello World  ') = {clean('  Hello World  ')!r}")
print(f"    clean(' Python IS Fun') = {clean(' Python IS Fun')!r}")
print()

# Sort a dataset using a closure-based key factory
def sort_by_field(field):
    """Return a key function for sorting dicts by a specific field."""
    return lambda item: item[field]

employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 95000},
    {"name": "Bob", "dept": "Marketing", "salary": 72000},
    {"name": "Charlie", "dept": "Engineering", "salary": 110000},
    {"name": "Diana", "dept": "Marketing", "salary": 85000},
]

by_salary = sorted(employees, key=sort_by_field("salary"))
by_name = sorted(employees, key=sort_by_field("name"))

print("    Sorted by salary:")
for emp in by_salary:
    print(f"      {emp['name']:10} {emp['dept']:15} ${emp['salary']:,}")

print("    Sorted by name:")
for emp in by_name:
    print(f"      {emp['name']:10} {emp['dept']:15} ${emp['salary']:,}")

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("   LAMBDA AND CLOSURES COMPLETE!")
print("=" * 50)
print()
print("Lambdas keep your code concise. Closures let functions remember.")
print("Try the exercises to practice both!")
