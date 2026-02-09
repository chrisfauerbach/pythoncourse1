# Control Flow

## Objective

Learn how to make your programs make decisions using `if`, `elif`, `else`, and pattern matching with `match/case`.

## Concepts Covered

- `if` statements and indentation
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- `elif` and `else`
- Logical operators (`and`, `or`, `not`)
- Truthy and falsy values revisited
- Nested `if` statements
- Ternary expressions (conditional expressions)
- `match/case` (Python 3.10+ structural pattern matching)
- Common pitfalls

## Prerequisites

- [Variables and Types](../02-variables-and-types/) — you should know how variables, types, and booleans work

## Lesson

### The if Statement

Up until now, every line of your code has run from top to bottom, no exceptions. That changes here. An `if` statement lets Python *decide* whether to run a block of code:

```python
age = 18

if age >= 18:
    print("You can vote!")
```

Two things to notice:

- **The colon `:`** at the end of the `if` line. It's required. Forget it and Python will yell at you.
- **The indentation.** The indented line belongs to the `if` block. Python uses whitespace (4 spaces by convention) to define code blocks — not curly braces `{}` like JavaScript or C. This is one of Python's most distinctive features.

If the condition is `True`, the indented code runs. If it's `False`, Python skips it entirely.

### Comparison Operators

You need these to build conditions:

```python
x = 10

x == 10    # True   (equal to — note the DOUBLE equals sign)
x != 5     # True   (not equal to)
x > 5      # True   (greater than)
x < 20     # True   (less than)
x >= 10    # True   (greater than or equal to)
x <= 9     # False  (less than or equal to)
```

**Big warning:** `=` is assignment, `==` is comparison. Mixing them up is one of the most common beginner mistakes:

```python
x = 10     # This SETS x to 10
x == 10    # This CHECKS if x equals 10
```

### elif and else

What if you need to check multiple conditions? That's where `elif` (short for "else if") and `else` come in:

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade: {grade}")   # Your grade: B
```

Here's how it works:

- Python checks each condition **from top to bottom**
- The **first** condition that's `True` wins — its block runs and everything else is skipped
- `else` is the catch-all — it runs only if nothing above matched
- `else` is optional. You can have `if`/`elif` without an `else`

### Logical Operators

Combine multiple conditions with `and`, `or`, and `not`:

```python
age = 25
has_license = True

# and — both must be True
if age >= 16 and has_license:
    print("You can drive!")

# or — at least one must be True
if age < 13 or age > 65:
    print("You get a discount!")

# not — flips True to False and vice versa
is_banned = False
if not is_banned:
    print("Welcome in!")
```

You can combine as many as you want, but keep it readable. If your condition is getting long, consider breaking it into variables:

```python
# Hard to read
if age >= 18 and has_license and not is_banned and country == "US":
    print("OK")

# Much clearer
is_eligible = age >= 18 and has_license
is_allowed = not is_banned and country == "US"
if is_eligible and is_allowed:
    print("OK")
```

### Truthy and Falsy Values Revisited

You learned about truthy/falsy in the variables lesson. Here's where it really matters. Python doesn't require conditions to be explicit booleans — any value works:

```python
name = "Alice"

# Instead of this:
if name != "":
    print("Name is set")

# You can just write this:
if name:
    print("Name is set")
```

Quick reminder of what's **falsy** in Python:
- `False`
- `0`, `0.0`
- `""` (empty string)
- `None`
- `[]`, `{}`, `()` (empty collections — you'll learn these later)

**Everything else is truthy.** This is a very Pythonic pattern you'll see everywhere.

### Nested if Statements

You can put `if` statements inside other `if` statements. Each level gets another indent:

```python
has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Welcome to the R-rated movie!")
    else:
        print("Sorry, you must be 18+")
else:
    print("You need a ticket first!")
```

Nesting works, but don't go too deep — more than 2-3 levels usually means you should rethink your approach. Often you can flatten nested ifs with `and`:

```python
# Same logic, flattened
if has_ticket and age >= 18:
    print("Welcome to the R-rated movie!")
elif has_ticket:
    print("Sorry, you must be 18+")
else:
    print("You need a ticket first!")
```

### Ternary Expressions (Conditional Expressions)

Sometimes you just need a quick "this or that" assignment. Python has a one-liner for that:

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

The format is: `value_if_true if condition else value_if_false`

It's great for simple cases but don't overuse it. If the logic is complex, a regular `if`/`else` is much clearer.

```python
# Fine — short and obvious
label = "even" if x % 2 == 0 else "odd"

# Don't do this — hard to read
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
```

### match/case (Python 3.10+)

Python 3.10 introduced structural pattern matching with `match/case`. Think of it like a cleaner alternative to long `if`/`elif` chains when you're checking a single value:

```python
command = "quit"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "quit":
        print("Goodbye!")
    case _:
        print("Unknown command")
```

The `_` is a wildcard — it matches anything, like `else` in an `if` chain.

`match/case` can do much more (matching patterns, destructuring, etc.), but for now just know it exists as an option when you're comparing one value against several possibilities.

### Common Pitfalls

**1. `=` vs `==`**
```python
# WRONG — this assigns, doesn't compare
# if x = 10:

# RIGHT — double equals for comparison
if x == 10:
    print("x is 10")
```

**2. Forgetting the colon**
```python
# WRONG — missing colon
# if x > 5
#     print("big")

# RIGHT
if x > 5:
    print("big")
```

**3. Wrong indentation**
```python
# WRONG — inconsistent indentation causes IndentationError
# if x > 5:
#     print("big")
#       print("number")     # Too much indent!

# RIGHT — all lines in a block use the same indent
if x > 5:
    print("big")
    print("number")
```

**4. Using `or` incorrectly**
```python
# WRONG — this doesn't do what you think!
# "red" is truthy, so this is always True
# if color == "red" or "blue":

# RIGHT
if color == "red" or color == "blue":
    print("Primary color")

# EVEN BETTER
if color in ("red", "blue"):
    print("Primary color")
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- `if`, `elif`, and `else` let your program make decisions
- Python uses **indentation** (4 spaces) to define code blocks — no braces needed
- Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Combine conditions with `and`, `or`, `not`
- Any value can be used as a condition — Python evaluates its "truthiness"
- Ternary expressions (`x if condition else y`) are handy for simple one-liners
- `match/case` (Python 3.10+) is great for matching a value against multiple options
- Watch out for `=` vs `==`, missing colons, and inconsistent indentation
