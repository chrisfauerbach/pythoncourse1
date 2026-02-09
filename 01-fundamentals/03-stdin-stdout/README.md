# Standard Input and Output

## Objective

Learn how to get input from the user, format output with f-strings, and understand the full power of Python's `print()` and `input()` functions.

## Concepts Covered

- The `input()` function -- getting text from the user
- `input()` always returns a string -- converting with `int()` and `float()`
- `print()` revisited -- f-strings (formatted string literals)
- f-string expressions and formatting (`:,.2f`, `:>10`, etc.)
- Printing to stderr with `file=sys.stderr`
- String concatenation vs f-strings (why f-strings win)
- Multi-line output

## Prerequisites

- [Hello World](../01-hello-world/) -- you should know how to use `print()`
- [Variables and Types](../02-variables-and-types/) -- you should understand types and type conversion

## Lesson

### Getting Input from the User

So far, all the data in our programs has been hardcoded. But real programs talk to people. The `input()` function pauses your program and waits for the user to type something:

```python
name = input("What's your name? ")
print("Hello,", name)
```

When Python hits `input()`, it:
1. Displays the prompt string (the part in quotes)
2. Waits for the user to type something and press Enter
3. Returns whatever they typed as a **string**

That last part is important -- let's dig into it.

### input() Always Returns a String

No matter what the user types, `input()` gives you a string. Even if they type a number:

```python
age = input("How old are you? ")
print(type(age))   # <class 'str'> -- it's a string, not an int!
```

If the user types `25`, you get the *string* `"25"`, not the *number* `25`. This means you can't do math with it directly:

```python
age = input("How old are you? ")
# age + 1   # TypeError! Can't add str and int
age = int(age)   # Convert to integer first
print(age + 1)   # Now this works
```

Use `int()` or `float()` to convert the string to a number:

```python
birth_year = int(input("Birth year: "))      # Convert to int in one step
price = float(input("Enter the price: "))    # Convert to float in one step
```

Wrapping `input()` inside `int()` or `float()` is a common pattern. You'll see it everywhere.

### print() Revisited -- f-strings

You already know `print()` from Lesson 1. But now it's time to learn the best way to format output: **f-strings** (formatted string literals).

Put an `f` before the opening quote, then put expressions inside `{}` curly braces:

```python
name = "Alice"
age = 30
print(f"My name is {name} and I'm {age} years old.")
# Output: My name is Alice and I'm 30 years old.
```

The `f` stands for "formatted." Python evaluates whatever is inside the `{}` and inserts the result into the string. You can put any valid Python expression in there:

```python
x = 10
print(f"{x} squared is {x ** 2}")       # 10 squared is 100
print(f"Half of {x} is {x / 2}")        # Half of 10 is 5.0
print(f"{'hello'.upper()}")              # HELLO
```

### f-string Formatting Options

Here's where f-strings get really powerful. After the expression, add a colon `:` followed by a format specifier:

#### Decimal places

```python
pi = 3.14159265
print(f"Pi is approximately {pi:.2f}")    # Pi is approximately 3.14
print(f"Pi to 4 decimals: {pi:.4f}")      # Pi to 4 decimals: 3.1416
```

The `.2f` means "2 decimal places, fixed-point notation."

#### Width and alignment

```python
name = "Alice"
print(f"'{name:<15}'")   # 'Alice          '  (left-aligned, 15 chars wide)
print(f"'{name:>15}'")   # '          Alice'  (right-aligned)
print(f"'{name:^15}'")   # '     Alice     '  (centered)
```

#### Number formatting

```python
big_number = 1234567
print(f"{big_number:,}")       # 1,234,567   (comma separator)
print(f"{big_number:_}")       # 1_234_567   (underscore separator)

price = 49.9
print(f"${price:>8.2f}")      # $   49.90   (right-aligned, 2 decimals)

percentage = 0.856
print(f"{percentage:.1%}")     # 85.6%       (percentage format)
```

#### Combining them

```python
# Right-align a price in a 10-character-wide field, with 2 decimal places
total = 1234.5
print(f"Total: ${total:>10,.2f}")   # Total: $  1,234.50
```

### Printing to stderr

By default, `print()` sends output to **stdout** (standard output). But sometimes you want to send error messages to **stderr** (standard error) -- this is how well-behaved command-line programs work:

```python
import sys

print("This goes to stdout")
print("Error: something went wrong!", file=sys.stderr)
```

Both lines show up on screen, but they're going to different streams. This matters when you redirect output to a file -- errors still show up on screen while normal output goes to the file.

### String Concatenation vs f-strings

You *can* build strings by gluing them together with `+`, but f-strings are almost always better:

```python
# Concatenation -- clunky and error-prone
name = "Alice"
age = 30
message = "My name is " + name + " and I'm " + str(age) + " years old."

# f-string -- clean and readable
message = f"My name is {name} and I'm {age} years old."
```

Why f-strings win:
- **No manual `str()` conversion** -- f-strings handle it automatically
- **Easier to read** -- you see the final string structure at a glance
- **Faster** -- Python can optimize f-strings better than concatenation
- **Less error-prone** -- no forgetting spaces or `str()` calls

The only time concatenation makes sense is when you're just joining two simple strings: `first + last`.

### Multi-line Output

For longer output, you have a few options:

```python
# Multiple print() calls
print("Line 1")
print("Line 2")
print("Line 3")

# Triple-quoted f-string
name = "Alice"
score = 95
print(f"""
Report Card
===========
Student: {name}
Score:   {score}%
Grade:   {'A' if score >= 90 else 'B'}
""")

# Using \n inside a string
print("Line 1\nLine 2\nLine 3")
```

Triple-quoted f-strings are great when you need to build a structured block of text with variables mixed in.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- `input("prompt")` gets text from the user and always returns a string
- Convert input to numbers with `int()` or `float()` -- wrap them around `input()` for a clean one-liner
- f-strings (`f"..."`) let you embed expressions directly in strings with `{}`
- Format specifiers go after a colon: `{value:.2f}`, `{value:>10}`, `{value:,}`
- Use `file=sys.stderr` to send error messages to standard error
- Prefer f-strings over string concatenation -- they're cleaner, faster, and less error-prone
- Triple-quoted f-strings are great for multi-line formatted output
