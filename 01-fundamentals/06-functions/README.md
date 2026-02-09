# Functions

## Objective

Learn how to write reusable blocks of code with functions — the single most important tool for organizing your programs.

## Concepts Covered

- Why functions matter (reuse, organization, abstraction)
- Defining functions with `def`
- Parameters and arguments
- Return values
- Default parameter values
- Keyword arguments vs positional arguments
- `*args` and `**kwargs`
- Docstrings — documenting your functions
- Scope — local vs global variables
- Functions as first-class objects
- Type hints (brief intro)

## Prerequisites

- [Loops](../05-loops/) — you should be comfortable with `for` and `while` loops

## Lesson

### Why Functions?

Imagine you need to calculate sales tax in ten different places in your code. Without functions, you'd copy-paste the same formula ten times. When the tax rate changes, you'd have to update it in all ten places. That's a bug waiting to happen.

Functions solve three problems at once:

1. **Reuse** — Write the logic once, use it anywhere
2. **Organization** — Break a big program into small, named pieces
3. **Abstraction** — Hide the messy details behind a clean interface

### Defining Functions with `def`

You create a function with the `def` keyword:

```python
def greet():
    print("Hello there!")

# Call the function
greet()   # Output: Hello there!
greet()   # You can call it as many times as you want
```

The pattern is: `def function_name():` followed by an indented body. The body can be as many lines as you need.

**Convention:** Function names use `snake_case` in Python — lowercase words separated by underscores.

### Parameters and Arguments

Functions become useful when they accept input:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")    # Output: Hello, Alice!
greet("Bob")      # Output: Hello, Bob!
```

- **Parameter** is the variable name in the function definition (`name`)
- **Argument** is the actual value you pass when calling it (`"Alice"`)

People use these terms interchangeably in casual conversation, and that's fine.

You can have as many parameters as you need:

```python
def introduce(name, age, city):
    print(f"I'm {name}, {age} years old, from {city}.")

introduce("Alice", 30, "Seattle")
```

### Return Values

Most functions don't just print things — they compute a value and hand it back to you with `return`:

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

Once Python hits a `return` statement, the function is done. Any code after `return` won't run:

```python
def check(x):
    if x > 0:
        return "positive"
    return "not positive"
    print("this never runs")   # Unreachable code
```

**What if there's no return?** The function implicitly returns `None`:

```python
def say_hi():
    print("Hi!")

result = say_hi()   # Prints "Hi!"
print(result)        # None
```

### Default Parameter Values

You can give parameters a default value. If the caller doesn't provide one, the default kicks in:

```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))       # 25 (exponent defaults to 2)
print(power(5, 3))    # 125 (exponent is 3)
print(power(2, 10))   # 1024
```

**Rule:** Parameters with defaults must come after parameters without defaults:

```python
# VALID
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# INVALID — this causes a SyntaxError
# def greet(greeting="Hello", name):
#     print(f"{greeting}, {name}!")
```

### Keyword Arguments vs Positional Arguments

When calling a function, you can pass arguments by position or by name:

```python
def describe_pet(name, animal, age):
    print(f"{name} is a {animal}, age {age}")

# Positional — order matters
describe_pet("Buddy", "dog", 5)

# Keyword — order doesn't matter
describe_pet(animal="cat", age=3, name="Whiskers")

# Mix both — positional first, then keyword
describe_pet("Goldie", animal="fish", age=2)
```

Keyword arguments make your code more readable, especially when a function has many parameters.

### `*args` and `**kwargs`

Sometimes you want a function that accepts any number of arguments.

#### `*args` — Variable Positional Arguments

The `*args` parameter collects extra positional arguments into a tuple:

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3))          # 6
print(total(10, 20, 30, 40))   # 100
print(total(5))                 # 5
```

#### `**kwargs` — Variable Keyword Arguments

The `**kwargs` parameter collects extra keyword arguments into a dictionary:

```python
def build_profile(**info):
    for key, value in info.items():
        print(f"  {key}: {value}")

build_profile(name="Alice", age=30, city="Seattle")
# Output:
#   name: Alice
#   age: 30
#   city: Seattle
```

You can combine them all — just keep the right order: regular parameters, `*args`, keyword-only parameters, `**kwargs`:

```python
def example(required, *args, option="default", **kwargs):
    print(f"required: {required}")
    print(f"args: {args}")
    print(f"option: {option}")
    print(f"kwargs: {kwargs}")
```

### Docstrings — Documenting Your Functions

A docstring is a string that goes right after the `def` line. It describes what the function does:

```python
def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    import math
    return math.pi * radius ** 2
```

For more complex functions, you can include parameters and return info:

```python
def convert_temp(temp, direction="F_to_C"):
    """
    Convert a temperature between Fahrenheit and Celsius.

    Args:
        temp: The temperature value to convert.
        direction: "F_to_C" or "C_to_F" (default: "F_to_C").

    Returns:
        The converted temperature as a float.
    """
    if direction == "F_to_C":
        return (temp - 32) * 5 / 9
    return temp * 9 / 5 + 32
```

You can access a function's docstring with `help(function_name)` or `function_name.__doc__`. Get in the habit of writing docstrings — your future self will thank you.

### Scope — Local vs Global Variables

Variables created inside a function are **local** — they only exist inside that function:

```python
def my_function():
    secret = 42        # Local variable
    print(secret)      # Works fine

my_function()
# print(secret)        # NameError! 'secret' doesn't exist out here
```

Variables created outside functions are **global** — they can be read from inside a function, but not modified (by default):

```python
greeting = "Hello"     # Global variable

def say_greeting():
    print(greeting)    # Reading a global — works fine

say_greeting()         # Output: Hello
```

If you try to assign to a global variable inside a function, Python creates a new local variable instead:

```python
count = 0

def increment():
    count = count + 1   # This FAILS — Python gets confused

# To actually modify a global, use the 'global' keyword:
def increment():
    global count
    count = count + 1   # Now it works
```

**Best practice:** Avoid `global`. Instead, pass values in as arguments and return results. Functions that don't depend on or modify global state are easier to understand and test.

### Functions as First-Class Objects

In Python, functions are values — just like strings or numbers. You can store them in variables, put them in lists, and pass them as arguments to other functions:

```python
def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

def apply(func, message):
    return func(message)

print(apply(shout, "hello"))     # HELLO!
print(apply(whisper, "HELLO"))   # hello...
```

This pattern is incredibly powerful and shows up everywhere in Python — in sorting, filtering, decorators, and more. We'll explore this in depth in later lessons.

### Type Hints (Brief Intro)

Python lets you add optional type annotations to your functions. They don't change how the code runs, but they make it clearer and help tools like editors catch mistakes:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0
```

The `-> str` part means "this function returns a string." It's just a hint — Python won't stop you from returning something else. But it's great documentation and widely used in professional codebases.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Define functions with `def function_name(parameters):` and an indented body
- `return` sends a value back to the caller; without it, a function returns `None`
- Default parameters let you make arguments optional: `def f(x, y=10):`
- Use keyword arguments for clarity: `greet(name="Alice")`
- `*args` collects extra positional arguments; `**kwargs` collects extra keyword arguments
- Docstrings document what a function does — always write them
- Variables inside a function are local; avoid using `global`
- Functions are first-class objects — you can pass them around like any other value
- Type hints (`def f(x: int) -> str:`) add clarity without changing behavior
