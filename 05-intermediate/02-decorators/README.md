# Decorators

## Objective

Understand decorators — one of Python's most powerful and elegant features. You'll learn how to write functions that modify other functions, and see why decorators are everywhere in real-world Python code.

## Concepts Covered

- What decorators are (functions that wrap other functions)
- Functions as first-class objects (quick recap)
- Building up to decorators step by step (inner functions, closures, the pattern)
- The `@decorator` syntax (syntactic sugar)
- Using `functools.wraps` to preserve metadata
- Decorators with arguments (decorator factories)
- Stacking multiple decorators
- Class-based decorators (using `__call__`)
- Common built-in decorators (`@property`, `@staticmethod`, `@classmethod`)
- Practical use cases: timing, logging, authentication, caching
- `functools.lru_cache` — built-in memoization decorator

## Prerequisites

- Functions (defining, calling, `*args` and `**kwargs`)
- Closures (inner functions that capture variables from their enclosing scope)
- Basic understanding of classes

## Lesson

### What Is a Decorator?

A decorator is a function that takes another function as input, adds some behavior to it, and returns a new function. That's it. It's a way to **modify or extend** what a function does without changing its actual code.

You've probably already seen the syntax:

```python
@my_decorator
def say_hello():
    print("Hello!")
```

That `@my_decorator` line is the decorator. But before we use that shorthand, let's understand what's actually happening underneath.

### Quick Recap: Functions Are First-Class Objects

In Python, functions are just objects. You can assign them to variables, pass them as arguments, and return them from other functions:

```python
def greet(name):
    return f"Hello, {name}!"

# Assign a function to a variable
say_hi = greet
print(say_hi("Alice"))  # Hello, Alice!

# Pass a function as an argument
def call_twice(func, arg):
    print(func(arg))
    print(func(arg))

call_twice(greet, "Bob")
```

This is the foundation that makes decorators possible.

### Building Up: Inner Functions and Closures

Functions can be defined inside other functions. The inner function can access variables from the outer function's scope — that's called a **closure**:

```python
def outer():
    message = "Hello from outer!"

    def inner():
        print(message)  # inner "closes over" the message variable

    return inner

my_func = outer()
my_func()  # Hello from outer!
```

The inner function remembers the environment it was created in, even after the outer function has finished running.

### The Decorator Pattern (Step by Step)

Now let's combine both ideas. A decorator is a function that:

1. Takes a function as an argument
2. Defines an inner (wrapper) function that calls the original
3. Returns the wrapper

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper
```

You use it by passing a function to the decorator:

```python
def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
```

Output:
```
Something before the function runs
Hello!
Something after the function runs
```

That line `say_hello = my_decorator(say_hello)` is the key. You're replacing `say_hello` with the wrapped version.

### The @ Syntax — Syntactic Sugar

Writing `say_hello = my_decorator(say_hello)` every time is clunky. Python gives you the `@` shorthand:

```python
@my_decorator
def say_hello():
    print("Hello!")
```

This does **exactly** the same thing as the manual version above. The `@` syntax is just cleaner and easier to read.

### Handling Arguments with *args and **kwargs

Most real functions take arguments. Your wrapper needs to pass them through:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Done with {func.__name__}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))  # Prints the log messages AND returns 8
```

Always use `*args, **kwargs` in your wrapper so it works with any function signature.

### The Problem: Lost Metadata

There's a catch. When you wrap a function, the wrapper **replaces** the original. That means things like `__name__` and `__doc__` now point to the wrapper, not the original:

```python
@my_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # "wrapper" — not "add"!
print(add.__doc__)   # None — the docstring is gone!
```

### The Fix: functools.wraps

The `functools.wraps` decorator copies over the original function's metadata to the wrapper:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)  # "add" — preserved!
print(add.__doc__)   # "Add two numbers." — preserved!
```

**Always use `@functools.wraps(func)`** on your wrapper function. It's a best practice you should never skip.

### Decorators with Arguments (Decorator Factories)

Sometimes you want to pass arguments to the decorator itself, like `@repeat(n=3)`. To do this, you need one more layer of nesting — a function that *returns* a decorator:

```python
import functools

def repeat(n=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=3)
def say_hi():
    print("Hi!")

say_hi()  # Prints "Hi!" three times
```

The pattern is: **factory -> decorator -> wrapper**. The factory takes the arguments, returns a decorator, and that decorator wraps the function. It looks like a lot of nesting, but once you see the pattern, it clicks.

### Stacking Multiple Decorators

You can apply multiple decorators to a single function. They're applied **bottom-up** (the one closest to the function runs first):

```python
@decorator_a
@decorator_b
def my_function():
    pass

# This is equivalent to:
# my_function = decorator_a(decorator_b(my_function))
```

Think of it like wrapping a gift: `decorator_b` is the inner wrapping, `decorator_a` is the outer wrapping. When you call the function, the outer decorator runs first.

### Class-Based Decorators

Any callable can be a decorator — not just functions. You can use a class with a `__call__` method:

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call #1 to say_hello \n Hello!
say_hello()  # Call #2 to say_hello \n Hello!
```

Class-based decorators are handy when you need the decorator to maintain **state** between calls (like a counter).

### Common Built-In Decorators (Recap)

You've likely seen these already — they're all decorators under the hood:

- **`@property`** — turns a method into a read-only attribute
- **`@staticmethod`** — defines a method that doesn't need `self` or `cls`
- **`@classmethod`** — defines a method that receives the class (`cls`) instead of an instance

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @staticmethod
    def is_valid_radius(value):
        return isinstance(value, (int, float)) and value > 0

    @classmethod
    def unit_circle(cls):
        return cls(1)
```

### Practical Use Cases

Decorators shine for **cross-cutting concerns** — things that apply to many functions but aren't part of the core logic:

- **Timing** — measure how long a function takes to run
- **Logging** — record when functions are called and with what arguments
- **Authentication** — check if a user is logged in before running a view
- **Rate limiting** — prevent a function from being called too frequently
- **Caching/Memoization** — store results so you don't recompute them
- **Retry logic** — automatically retry a function if it fails
- **Input validation** — check argument types or values before running

### functools.lru_cache — Built-In Memoization

Python ships with a powerful caching decorator. It remembers previous results so the function doesn't recompute them:

```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Instant — without caching this would take forever
```

`lru_cache` stands for "Least Recently Used cache." The `maxsize` parameter controls how many results it stores. Use `maxsize=None` for an unlimited cache.

You can check cache stats too:

```python
print(fibonacci.cache_info())
# CacheInfo(hits=48, misses=51, maxsize=128, currsize=51)
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- A decorator is a function that wraps another function to extend its behavior
- The `@decorator` syntax is shorthand for `func = decorator(func)`
- Always use `@functools.wraps(func)` on your wrapper to preserve the original function's metadata
- Use `*args, **kwargs` in your wrapper so it works with any function signature
- Decorator factories (decorators with arguments) need three levels of nesting: factory -> decorator -> wrapper
- Multiple decorators stack bottom-up — the one closest to the function is applied first
- Classes with `__call__` can act as decorators, which is useful for maintaining state
- `functools.lru_cache` is a powerful built-in decorator for memoization
- Decorators are ideal for cross-cutting concerns: timing, logging, caching, auth, retries, and validation
