# Variables and Types

## Objective

Learn how to store data in variables and understand Python's core data types.

## Concepts Covered

- Creating and naming variables
- Python's core types: `int`, `float`, `str`, `bool`, `None`
- Checking types with `type()`
- Type conversion (casting)
- Basic arithmetic operators
- Dynamic typing — what it means and why it matters

## Prerequisites

- [Hello World](../01-hello-world/) — you should know how to use `print()`

## Lesson

### What's a Variable?

A variable is a name that points to a value. Think of it like a label you stick on a box — the label is the name, the box holds the data.

```python
age = 25
name = "Alice"
```

That's it. No special keywords, no type declarations. Python figures out the type automatically — this is called **dynamic typing**.

### Naming Rules

Variable names must follow a few rules:

```python
# VALID names
age = 25
first_name = "Alice"
_private = "hidden"
player1 = "Mario"
MAX_SIZE = 100          # ALL_CAPS is a convention for constants

# INVALID names — these will cause errors
# 1st_place = "Gold"   # Can't start with a number
# my-name = "Alice"    # No hyphens (Python thinks it's subtraction)
# class = "Math"       # Can't use Python keywords (class, if, for, etc.)
```

**Convention:** Python uses `snake_case` for variable names — lowercase words separated by underscores. You'll see this everywhere.

### The Core Types

Python has a handful of built-in types you'll use constantly:

#### Integers (`int`) — Whole numbers

```python
age = 25
temperature = -10
population = 8_000_000_000   # Underscores make big numbers readable
```

#### Floats (`float`) — Decimal numbers

```python
price = 9.99
pi = 3.14159
temperature = -40.0
```

**Heads up:** Floating-point math can be surprising:

```python
print(0.1 + 0.2)   # Output: 0.30000000000000004 (not 0.3!)
```

This isn't a Python bug — it's how all computers store decimals. We'll deal with this properly later, but just know it's a thing.

#### Strings (`str`) — Text

```python
name = "Alice"
greeting = 'Hello!'
paragraph = """This is a
multi-line string."""
empty = ""   # An empty string is still a string
```

#### Booleans (`bool`) — True or False

```python
is_active = True
game_over = False
```

Note the capital `T` and `F`. Python is case-sensitive — `true` and `false` won't work.

#### None — The "nothing" value

```python
result = None   # No value assigned yet
```

`None` is Python's way of saying "this variable exists, but it has no value." It's not zero, it's not an empty string — it's *nothing*.

### Checking Types

Use `type()` to find out what type a variable is:

```python
age = 25
print(type(age))      # <class 'int'>

price = 9.99
print(type(price))    # <class 'float'>

name = "Alice"
print(type(name))     # <class 'str'>

active = True
print(type(active))   # <class 'bool'>
```

### Arithmetic Operators

Python works like a calculator:

```python
a = 10
b = 3

print(a + b)     # 13    Addition
print(a - b)     # 7     Subtraction
print(a * b)     # 30    Multiplication
print(a / b)     # 3.333 Division (always returns a float!)
print(a // b)    # 3     Floor division (rounds down to int)
print(a % b)     # 1     Modulo (remainder after division)
print(a ** b)    # 1000  Exponentiation (10 to the power of 3)
```

**Important:** Regular division `/` always returns a float, even when dividing evenly:

```python
print(10 / 2)    # 5.0 (not 5)
print(10 // 2)   # 5   (use // for an integer result)
```

### Assignment Shortcuts

Instead of writing `x = x + 5`, Python has shorthand operators:

```python
score = 100
score += 10    # Same as: score = score + 10  → 110
score -= 20    # Same as: score = score - 20  → 90
score *= 2     # Same as: score = score * 2   → 180
score /= 3     # Same as: score = score / 3   → 60.0
```

### Type Conversion (Casting)

Sometimes you need to convert between types:

```python
# String to integer
age_str = "25"
age = int(age_str)        # 25 (as an integer)

# String to float
price_str = "9.99"
price = float(price_str)  # 9.99 (as a float)

# Number to string
count = 42
message = "The answer is " + str(count)   # Must convert to str to concatenate

# Float to integer (truncates — does NOT round)
pi = 3.99
print(int(pi))   # 3 (just chops off the decimal)

# Integer to float
x = 5
print(float(x))  # 5.0
```

**Common gotcha:** You can't add a string and a number directly:

```python
# age = 25
# print("Age: " + age)    # TypeError!
print("Age: " + str(25))  # Works: "Age: 25"
print("Age:", 25)          # Even better — let print() handle it
```

### Multiple Assignment

Python lets you assign multiple variables at once:

```python
# Assign multiple variables in one line
x, y, z = 1, 2, 3

# Assign the same value to multiple variables
a = b = c = 0

# Swap two variables (no temp variable needed!)
x, y = y, x
```

### Dynamic Typing

In Python, a variable can change types freely:

```python
x = 42          # x is an int
x = "hello"     # now x is a string
x = [1, 2, 3]   # now x is a list
```

This is different from languages like Java or C where a variable is locked to one type. It's flexible but can cause bugs if you're not careful — that's why `type()` is handy for debugging.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Variables are created with `=` — no type declarations needed
- Python's core types: `int`, `float`, `str`, `bool`, `None`
- Use `type()` to check a variable's type
- Division `/` always returns a float; use `//` for integer division
- Convert between types with `int()`, `float()`, `str()`, `bool()`
- Python uses `snake_case` for variable names by convention
- Variables can change type at any time (dynamic typing)
