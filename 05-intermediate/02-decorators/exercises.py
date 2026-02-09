"""
Decorators — Exercises
========================

Practice problems to test your understanding of decorators.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import functools
import time


# =============================================================================
# Exercise 1: Timer decorator
#
# Write a decorator called `timer` that prints how long a function takes
# to execute. Use `time.perf_counter()` for accuracy.
#
# Expected behavior:
#   @timer
#   def slow_func():
#       time.sleep(0.5)
#
#   slow_func()
#   # Output: slow_func took 0.5012 seconds
#
# Remember to:
#   - Use @functools.wraps to preserve the function's metadata
#   - Use *args, **kwargs so it works with any function
#   - Return the original function's return value
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE — define the timer decorator

    # Uncomment to test:
    # @timer
    # def waste_time(n):
    #     """Sum numbers the slow way."""
    #     return sum(range(n))
    #
    # result = waste_time(1_000_000)
    # print(f"  Result: {result}")
    # print(f"  Name preserved: {waste_time.__name__}")
    # print(f"  Doc preserved: {waste_time.__doc__}")
    pass


# =============================================================================
# Exercise 2: Call logger
#
# Write a decorator called `log_calls` that prints the function name,
# its arguments, and its return value every time the function is called.
#
# Expected output:
#   @log_calls
#   def add(a, b):
#       return a + b
#
#   add(3, 5)
#   # Output:
#   #   Calling add(3, 5)
#   #   add returned 8
#
#   add(10, b=20)
#   # Output:
#   #   Calling add(10, b=20)
#   #   add returned 30
#
# Hint: Use repr() for argument formatting and join args/kwargs nicely.
# =============================================================================

def exercise_2():
    # YOUR CODE HERE — define the log_calls decorator

    # Uncomment to test:
    # @log_calls
    # def add(a, b):
    #     return a + b
    #
    # @log_calls
    # def greet(name, greeting="Hello"):
    #     return f"{greeting}, {name}!"
    #
    # add(3, 5)
    # add(10, b=20)
    # greet("Alice")
    # greet("Bob", greeting="Hey")
    pass


# =============================================================================
# Exercise 3: Retry decorator
#
# Write a decorator called `retry` that retries a function up to `max_attempts`
# times if it raises an exception. If all attempts fail, re-raise the last
# exception.
#
# This is a decorator WITH arguments, so you'll need the three-layer pattern:
#   factory -> decorator -> wrapper
#
# Expected behavior:
#   @retry(max_attempts=3)
#   def flaky_function():
#       import random
#       if random.random() < 0.7:
#           raise ValueError("Random failure!")
#       return "Success!"
#
#   flaky_function()  # Retries up to 3 times before giving up
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE — define the retry decorator factory

    # Uncomment to test:
    # attempt_count = 0
    #
    # @retry(max_attempts=5)
    # def sometimes_fails():
    #     nonlocal attempt_count
    #     attempt_count += 1
    #     if attempt_count < 3:
    #         raise ValueError(f"Attempt {attempt_count} failed!")
    #     return f"Succeeded on attempt {attempt_count}"
    #
    # result = sometimes_fails()
    # print(f"  Result: {result}")
    pass


# =============================================================================
# Exercise 4: Repeat decorator with arguments
#
# Write a decorator factory called `repeat` that takes an integer `n` and
# calls the decorated function `n` times. Return the result of the last call.
#
# Expected behavior:
#   @repeat(n=3)
#   def say_hello(name):
#       print(f"Hello, {name}!")
#       return f"Greeted {name}"
#
#   result = say_hello("Alice")
#   # Output:
#   #   Hello, Alice!
#   #   Hello, Alice!
#   #   Hello, Alice!
#   # result == "Greeted Alice"
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define the repeat decorator factory

    # Uncomment to test:
    # @repeat(n=4)
    # def countdown(n):
    #     print(f"  {n}!", end=" ")
    #     return n
    #
    # result = countdown(3)
    # print()
    # print(f"  Last return value: {result}")
    # print(f"  Name preserved: {countdown.__name__}")
    pass


# =============================================================================
# Exercise 5: Memoize decorator
#
# Write a decorator called `memoize` that caches the results of function calls.
# If the function is called with the same arguments again, return the cached
# result instead of recalculating.
#
# Use a dictionary as the cache. The key should be (args, tuple of kwargs items).
#
# Expected behavior:
#   @memoize
#   def expensive(n):
#       print(f"  Computing expensive({n})...")
#       time.sleep(0.1)
#       return n * n
#
#   expensive(5)   # Prints "Computing..." and returns 25
#   expensive(5)   # Returns 25 immediately — no "Computing..." printed
#   expensive(10)  # Prints "Computing..." and returns 100
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define the memoize decorator

    # Uncomment to test:
    # @memoize
    # def expensive(n):
    #     print(f"  Computing expensive({n})...")
    #     return n * n
    #
    # print(f"  First call:  expensive(5) = {expensive(5)}")
    # print(f"  Cached call: expensive(5) = {expensive(5)}")
    # print(f"  New call:    expensive(10) = {expensive(10)}")
    # print(f"  Cached call: expensive(10) = {expensive(10)}")
    pass


# =============================================================================
# Exercise 6: Type checker decorator
#
# Write a decorator factory called `enforce_types` that validates the types
# of a function's arguments at runtime. It should accept keyword arguments
# mapping parameter names to expected types.
#
# If an argument doesn't match, raise a TypeError with a helpful message.
#
# Expected behavior:
#   @enforce_types(name=str, age=int)
#   def register(name, age):
#       return f"{name} is {age} years old"
#
#   register("Alice", 30)        # Works fine
#   register("Alice", "thirty")  # Raises TypeError
#
# Hint: Use `inspect.signature` to map argument names to their values,
# or zip the function's parameter names with the provided args.
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define the enforce_types decorator factory

    # Uncomment to test:
    # @enforce_types(name=str, age=int, score=float)
    # def register(name, age, score):
    #     return f"{name}, age {age}, score {score}"
    #
    # print(f"  Valid call: {register('Alice', 30, 95.5)}")
    #
    # try:
    #     register("Bob", "thirty", 95.5)
    # except TypeError as e:
    #     print(f"  Caught TypeError: {e}")
    #
    # try:
    #     register("Charlie", 25, "high")
    # except TypeError as e:
    #     print(f"  Caught TypeError: {e}")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f"  {func.__name__} took {elapsed:.4f} seconds")
            return result
        return wrapper

    @timer
    def waste_time(n):
        """Sum numbers the slow way."""
        return sum(range(n))

    result = waste_time(1_000_000)
    print(f"  Result: {result}")
    print(f"  Name preserved: {waste_time.__name__}")
    print(f"  Doc preserved: {waste_time.__doc__}")


def solution_2():
    def log_calls(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_str = ", ".join(repr(a) for a in args)
            kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))
            print(f"  Calling {func.__name__}({all_args})")
            result = func(*args, **kwargs)
            print(f"  {func.__name__} returned {result!r}")
            return result
        return wrapper

    @log_calls
    def add(a, b):
        return a + b

    @log_calls
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    add(3, 5)
    add(10, b=20)
    greet("Alice")
    greet("Bob", greeting="Hey")


def solution_3():
    def retry(max_attempts=3):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                last_exception = None
                for attempt in range(1, max_attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        last_exception = e
                        print(f"  Attempt {attempt}/{max_attempts} failed: {e}")
                raise last_exception
            return wrapper
        return decorator

    attempt_count = 0

    @retry(max_attempts=5)
    def sometimes_fails():
        nonlocal attempt_count
        attempt_count += 1
        if attempt_count < 3:
            raise ValueError(f"Attempt {attempt_count} failed!")
        return f"Succeeded on attempt {attempt_count}"

    result = sometimes_fails()
    print(f"  Result: {result}")


def solution_4():
    def repeat(n=2):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                result = None
                for _ in range(n):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator

    @repeat(n=4)
    def countdown(n):
        print(f"  {n}!", end=" ")
        return n

    result = countdown(3)
    print()
    print(f"  Last return value: {result}")
    print(f"  Name preserved: {countdown.__name__}")


def solution_5():
    def memoize(func):
        cache = {}

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                print(f"  [cache hit for {func.__name__}{args}]")
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        return wrapper

    @memoize
    def expensive(n):
        print(f"  Computing expensive({n})...")
        return n * n

    print(f"  First call:  expensive(5) = {expensive(5)}")
    print(f"  Cached call: expensive(5) = {expensive(5)}")
    print(f"  New call:    expensive(10) = {expensive(10)}")
    print(f"  Cached call: expensive(10) = {expensive(10)}")


def solution_6():
    import inspect

    def enforce_types(**type_hints):
        def decorator(func):
            sig = inspect.signature(func)

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                bound = sig.bind(*args, **kwargs)
                bound.apply_defaults()
                for param_name, value in bound.arguments.items():
                    if param_name in type_hints:
                        expected = type_hints[param_name]
                        if not isinstance(value, expected):
                            raise TypeError(
                                f"Argument '{param_name}' must be {expected.__name__}, "
                                f"got {type(value).__name__}"
                            )
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @enforce_types(name=str, age=int, score=float)
    def register(name, age, score):
        return f"{name}, age {age}, score {score}"

    print(f"  Valid call: {register('Alice', 30, 95.5)}")

    try:
        register("Bob", "thirty", 95.5)
    except TypeError as e:
        print(f"  Caught TypeError: {e}")

    try:
        register("Charlie", 25, "high")
    except TypeError as e:
        print(f"  Caught TypeError: {e}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Timer decorator", exercise_1),
        ("Call logger", exercise_2),
        ("Retry decorator", exercise_3),
        ("Repeat with arguments", exercise_4),
        ("Memoize decorator", exercise_5),
        ("Type checker decorator", exercise_6),
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
    print("To see solutions in action, uncomment the test")
    print("code in each exercise, or run the solution_N()")
    print("functions directly.")
