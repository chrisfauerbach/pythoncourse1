"""
Decorators — Example Code
============================

Run this file:
    python3 example.py

A complete walkthrough of decorators in Python — from the ground up.
Every section builds on the previous one.
"""

import functools
import time

# -----------------------------------------------------------------------------
# 1. Functions are first-class objects
# -----------------------------------------------------------------------------

# You can assign functions to variables, pass them around, return them.
# This is what makes decorators possible.

def shout(text):
    return text.upper() + "!"

# Assign the function to a new name — no parentheses, so we're NOT calling it
yell = shout

print("1. Functions as first-class objects")
print(f"   shout('hello') = {shout('hello')}")
print(f"   yell('hello')  = {yell('hello')}")  # Same function, different name
print()

# -----------------------------------------------------------------------------
# 2. Inner functions and closures
# -----------------------------------------------------------------------------

# A function defined inside another function. The inner function can access
# variables from the outer function's scope — that's a closure.

def make_greeter(greeting):
    """Returns a function that greets with the given greeting."""
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

say_hello = make_greeter("Hello")
say_hola = make_greeter("Hola")

print("2. Inner functions and closures")
print(f"   say_hello('Alice') = {say_hello('Alice')}")
print(f"   say_hola('Bob')    = {say_hola('Bob')}")
print()

# -----------------------------------------------------------------------------
# 3. The decorator pattern — manual version
# -----------------------------------------------------------------------------

# A decorator takes a function, wraps it, and returns the wrapper.
# Here we do it manually (no @ syntax yet).

def simple_decorator(func):
    def wrapper():
        print("   [before]")
        func()
        print("   [after]")
    return wrapper

def say_hi():
    print("   Hi there!")

# Manually decorate by reassigning
say_hi = simple_decorator(say_hi)

print("3. The decorator pattern (manual)")
say_hi()
print()

# -----------------------------------------------------------------------------
# 4. The @ syntax — syntactic sugar
# -----------------------------------------------------------------------------

# This does exactly the same thing as section 3, but with cleaner syntax.

def announce(func):
    def wrapper():
        print(f"   >>> About to call {func.__name__}()")
        func()
        print(f"   >>> Finished {func.__name__}()")
    return wrapper

@announce
def say_goodbye():
    print("   Goodbye!")

print("4. The @ syntax")
say_goodbye()
print()

# -----------------------------------------------------------------------------
# 5. Handling function arguments with *args and **kwargs
# -----------------------------------------------------------------------------

# Real functions take arguments. The wrapper needs to pass them through.

def log_call(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"   Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"   {func.__name__} returned {result!r}")
        return result
    return wrapper

@log_call
def multiply(a, b):
    return a * b

@log_call
def greet(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

print("5. Handling arguments with *args and **kwargs")
multiply(6, 7)
greet("Alice", punctuation="!!!")
print()

# -----------------------------------------------------------------------------
# 6. The metadata problem and functools.wraps
# -----------------------------------------------------------------------------

# Without @functools.wraps, the wrapper replaces the original function's
# name and docstring. Let's see the problem and the fix.

def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def good_decorator(func):
    @functools.wraps(func)  # <-- This is the fix
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def add_bad(a, b):
    """Add two numbers together."""
    return a + b

@good_decorator
def add_good(a, b):
    """Add two numbers together."""
    return a + b

print("6. functools.wraps preserves metadata")
print(f"   Without @wraps: name={add_bad.__name__!r}, doc={add_bad.__doc__!r}")
print(f"   With @wraps:    name={add_good.__name__!r}, doc={add_good.__doc__!r}")
print()

# -----------------------------------------------------------------------------
# 7. A practical decorator: timing
# -----------------------------------------------------------------------------

def timer(func):
    """Measure and print the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"   {func.__name__} took {elapsed:.6f} seconds")
        return result
    return wrapper

@timer
def slow_sum(n):
    """Sum numbers from 0 to n using a loop (intentionally slow)."""
    total = 0
    for i in range(n):
        total += i
    return total

print("7. Practical decorator: timing")
result = slow_sum(1_000_000)
print(f"   Result: {result}")
print()

# -----------------------------------------------------------------------------
# 8. Decorators with arguments (decorator factories)
# -----------------------------------------------------------------------------

# When you want @repeat(n=3), you need a function that RETURNS a decorator.
# Three layers: factory -> decorator -> wrapper

def repeat(n=2):
    """Decorator factory: repeat a function n times."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(n=3)
def say_hello_again():
    print("   Hello again!")

print("8. Decorators with arguments (decorator factory)")
say_hello_again()
print()

# Another example: a decorator that slows down a function

def slow_down(seconds=1):
    """Decorator factory: pause before calling the function."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"   Waiting {seconds}s before calling {func.__name__}...")
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@slow_down(seconds=0.5)
def quick_task():
    print("   Task complete!")

print("   (slow_down example — waits 0.5 seconds)")
quick_task()
print()

# -----------------------------------------------------------------------------
# 9. Stacking multiple decorators
# -----------------------------------------------------------------------------

# Decorators apply bottom-up: the one closest to the function wraps first.

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def format_text(text):
    return text

# italic wraps first, then bold wraps that result
# Equivalent to: format_text = bold(italic(format_text))

print("9. Stacking multiple decorators")
print(f"   @bold @italic 'hello' = {format_text('hello')}")
print("   Applied bottom-up: italic first, then bold wraps the result")
print()

# -----------------------------------------------------------------------------
# 10. Class-based decorators (using __call__)
# -----------------------------------------------------------------------------

# Any callable can be a decorator. A class with __call__ works perfectly,
# and it's great when you need the decorator to maintain state.

class CountCalls:
    """Decorator that counts how many times a function is called."""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"   Call #{self.count} to {self.func.__name__}()")
        return self.func(*args, **kwargs)

@CountCalls
def say_something():
    print("   Something!")

print("10. Class-based decorators")
say_something()
say_something()
say_something()
print(f"   Total calls: {say_something.count}")
print()

# -----------------------------------------------------------------------------
# 11. Built-in decorators: @property, @staticmethod, @classmethod
# -----------------------------------------------------------------------------

class Circle:
    """A circle with a radius — demonstrates built-in decorators."""

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Read the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius with validation."""
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        """Calculated property — no need to call it like a method."""
        import math
        return math.pi * self._radius ** 2

    @staticmethod
    def is_valid_radius(value):
        """Static method — no self or cls needed."""
        return isinstance(value, (int, float)) and value > 0

    @classmethod
    def unit_circle(cls):
        """Class method — creates a circle with radius 1."""
        return cls(1)

print("11. Built-in decorators: @property, @staticmethod, @classmethod")
c = Circle(5)
print(f"   Radius: {c.radius}")          # @property — access like an attribute
print(f"   Area: {c.area:.2f}")           # @property — calculated on the fly
print(f"   Is 3.5 valid? {Circle.is_valid_radius(3.5)}")  # @staticmethod
unit = Circle.unit_circle()               # @classmethod
print(f"   Unit circle radius: {unit.radius}")
print()

# -----------------------------------------------------------------------------
# 12. functools.lru_cache — built-in memoization
# -----------------------------------------------------------------------------

# lru_cache remembers previous results so the function doesn't recompute them.
# Without it, fibonacci(35) would take seconds. With it, it's instant.

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    """Compute the nth Fibonacci number (recursively, with caching)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("12. functools.lru_cache — built-in memoization")
print(f"   fibonacci(10) = {fibonacci(10)}")
print(f"   fibonacci(30) = {fibonacci(30)}")
print(f"   fibonacci(50) = {fibonacci(50)}")
print(f"   Cache info: {fibonacci.cache_info()}")
print()

# You can clear the cache if needed:
# fibonacci.cache_clear()

# -----------------------------------------------------------------------------
# 13. Putting it all together — a real-world logging decorator
# -----------------------------------------------------------------------------

def log(level="INFO"):
    """Decorator factory that logs function calls at a specified level."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(repr(a) for a in args)
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))
            print(f"   [{level}] {func.__name__}({all_args})")
            try:
                result = func(*args, **kwargs)
                print(f"   [{level}] {func.__name__} -> {result!r}")
                return result
            except Exception as e:
                print(f"   [ERROR] {func.__name__} raised {type(e).__name__}: {e}")
                raise
        return wrapper
    return decorator

@log(level="DEBUG")
def divide(a, b):
    return a / b

print("13. Real-world example: logging decorator with level")
divide(10, 3)
print()
try:
    divide(10, 0)
except ZeroDivisionError:
    print("   (caught the ZeroDivisionError above)")
print()

# -----------------------------------------------------------------------------
# 14. Summary
# -----------------------------------------------------------------------------

print("=" * 50)
print("   DECORATORS EXAMPLE COMPLETE!")
print("=" * 50)
print()
print("Decorators are everywhere in Python:")
print("  - Flask/Django use them for routing (@app.route)")
print("  - pytest uses them for fixtures and markers")
print("  - dataclasses uses @dataclass")
print("  - functools gives you @lru_cache, @wraps, and more")
print()
print("The pattern: take a function, wrap it, return the wrapper.")
print("Once you see it, you can't unsee it!")
