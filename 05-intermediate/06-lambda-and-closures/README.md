# Lambda and Closures

## Objective

Understand Python's lambda functions for writing quick throwaway functions, and closures for creating functions that remember their environment — two powerful tools that unlock elegant, concise code.

## Concepts Covered

- Lambda function syntax and when to use them
- `map()`, `filter()`, and `reduce()` with lambda
- Sorting with lambda as a key function
- What closures are and how they capture variables
- Function factories and encapsulation with closures
- The `nonlocal` keyword
- Common gotchas with closures in loops

## Prerequisites

- [Functions](../../01-fundamentals/06-functions/)

## Lesson

### Lambda Functions

A **lambda** is a small, anonymous function defined with the `lambda` keyword. It takes arguments and returns the result of a single expression — no `def`, no name, no `return` statement needed:

```python
# Regular function
def double(x):
    return x * 2

# Same thing as a lambda
double = lambda x: x * 2

print(double(5))  # 10
```

The syntax is: `lambda arguments: expression`

A few things to notice:

- **Single expression only.** You can't put multiple statements, loops, or `if` blocks in a lambda. Just one expression that gets evaluated and returned.
- **Anonymous.** Lambdas don't need a name. You'll often use them inline, passed directly to another function.
- **Same power as a one-liner `def`.** Anything you can write as a single expression works — ternaries, method calls, arithmetic, etc.

```python
# Multiple arguments
add = lambda a, b: a + b

# Ternary expression inside a lambda
classify = lambda x: "even" if x % 2 == 0 else "odd"

# Default arguments work too
greet = lambda name="World": f"Hello, {name}!"
```

### When to Use Lambda vs def

Lambdas shine when you need a short, throwaway function — usually as an argument to another function. Here are the good use cases:

```python
# Sorting by a custom key
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
students.sort(key=lambda s: s[1])

# Quick callback
buttons = {"save": lambda: print("Saved!"), "quit": lambda: print("Bye!")}

# Inline with map/filter (more on this below)
squares = list(map(lambda x: x ** 2, [1, 2, 3, 4]))
```

### When NOT to Use Lambda

If you find yourself doing any of these, just use `def` instead:

- **Complex logic.** If the expression is hard to read at a glance, a named function is better.
- **Reusing it.** If you're assigning a lambda to a variable and using it in multiple places, you've just written a worse version of `def`.
- **Needs documentation.** Lambdas can't have docstrings.

```python
# Bad — this is hard to read and you're naming it anyway
process = lambda x: x.strip().lower().replace(" ", "_") if isinstance(x, str) else str(x)

# Good — clear, readable, documentable
def process(x):
    """Normalize a value into a clean string identifier."""
    if isinstance(x, str):
        return x.strip().lower().replace(" ", "_")
    return str(x)
```

The rule of thumb: **if the lambda doesn't fit comfortably in one short line, use `def`.**

### map(), filter(), and reduce() with Lambda

These built-in functions pair naturally with lambdas for quick data transformations.

**`map(function, iterable)`** applies a function to every item:

```python
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
# [2, 4, 6, 8, 10]
```

**`filter(function, iterable)`** keeps items where the function returns `True`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8]
```

**`reduce(function, iterable)`** combines items into a single value (must import from `functools`):

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
# 15 — same as 1+2+3+4+5
```

A quick note: list comprehensions often do the same job as `map()` and `filter()`, and many Pythonistas prefer them for readability:

```python
# These are equivalent:
doubled = list(map(lambda x: x * 2, numbers))
doubled = [x * 2 for x in numbers]  # Most people prefer this
```

### Sorting with Lambda as Key Function

One of the most common uses of lambda is with `sorted()` and `.sort()`. The `key` parameter takes a function that extracts a comparison value from each item:

```python
# Sort strings by length
words = ["banana", "pie", "strawberry", "fig"]
sorted_words = sorted(words, key=lambda w: len(w))
# ['pie', 'fig', 'banana', 'strawberry']

# Sort dicts by a specific field
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]
by_age = sorted(people, key=lambda p: p["age"])

# Sort by multiple criteria (tuple trick)
students = [("Alice", "B"), ("Bob", "A"), ("Charlie", "B")]
by_grade_then_name = sorted(students, key=lambda s: (s[1], s[0]))
# [('Bob', 'A'), ('Alice', 'B'), ('Charlie', 'B')]
```

### What Are Closures?

A **closure** is a function that remembers values from the scope where it was created, even after that scope has finished executing. It happens when an inner function references variables from an enclosing function:

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"  # Uses 'greeting' from enclosing scope
    return greet

hello = make_greeter("Hello")
howdy = make_greeter("Howdy")

print(hello("Alice"))   # Hello, Alice!
print(howdy("Bob"))     # Howdy, Bob!
```

Here's what happened: `make_greeter` finished running, but `greet` still has access to the `greeting` variable. The inner function "closed over" that variable — hence the name *closure*.

### How Closures Work — The Enclosing Scope

Python looks up variables using the **LEGB** rule: Local, Enclosing, Global, Built-in. Closures live in the **Enclosing** part. When you return an inner function, Python attaches the enclosing variables to it:

```python
def outer():
    message = "I'm from outer!"

    def inner():
        print(message)  # 'message' isn't local — Python checks enclosing scope

    return inner

fn = outer()  # outer() finishes, but 'message' survives inside fn
fn()          # I'm from outer!
```

You can inspect what a closure captured:

```python
print(fn.__closure__)           # Shows the closure cell objects
print(fn.__closure__[0].cell_contents)  # "I'm from outer!"
```

### Practical Closure Use Cases

**Function factories** — create specialized versions of a function:

```python
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube = make_power(3)

print(square(5))  # 25
print(cube(5))    # 125
```

**Encapsulation** — hide state without a full class:

```python
def make_counter(start=0):
    count = [start]  # Using a list so we can modify it (or use nonlocal)

    def increment():
        count[0] += 1
        return count[0]

    def get_count():
        return count[0]

    return increment, get_count

inc, get = make_counter()
inc()
inc()
inc()
print(get())  # 3
```

### Closures vs Classes

Sometimes a closure is simpler than a class. Compare:

```python
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
```

Both work the same way. The closure is less code and easier to read for simple cases. Use a class when you need multiple methods, inheritance, or complex state management.

### The nonlocal Keyword

By default, you can *read* enclosing variables in a closure but can't *reassign* them. If you try, Python creates a new local variable instead. The `nonlocal` keyword fixes this:

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count    # "I mean the 'count' from the enclosing scope"
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

Without `nonlocal`, the line `count += 1` would raise an `UnboundLocalError` because Python sees the assignment and treats `count` as a local variable.

### Common Gotcha: Closures in Loops (Late Binding)

This is one of the most common Python traps. Closures capture *variables*, not *values*. So if the variable changes, the closure sees the new value:

```python
# Bug! All functions return 4
functions = []
for i in range(5):
    functions.append(lambda: i)

print([f() for f in functions])  # [4, 4, 4, 4, 4] — not [0, 1, 2, 3, 4]!
```

By the time you call the lambdas, the loop has finished and `i` is `4`. Every lambda shares the *same* `i`.

**The fix:** use a default argument to capture the current value:

```python
# Fixed! Default argument captures the value at creation time
functions = []
for i in range(5):
    functions.append(lambda i=i: i)

print([f() for f in functions])  # [0, 1, 2, 3, 4]
```

The default argument `i=i` evaluates immediately when the lambda is created, so each lambda gets its own snapshot of `i`.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Lambda functions are anonymous, single-expression functions: `lambda x: x * 2`
- Use lambdas for short throwaway functions — sorting keys, quick callbacks, `map`/`filter`
- If a lambda gets complex or needs a name, switch to `def`
- `map()`, `filter()`, and `reduce()` apply functions across iterables — but list comprehensions often read better
- A closure is an inner function that captures variables from its enclosing scope
- Closures are great for function factories and lightweight encapsulation
- Use `nonlocal` when you need to modify (not just read) an enclosing variable
- Watch out for late binding in loops — use default arguments to capture current values
