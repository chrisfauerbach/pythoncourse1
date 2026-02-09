# Hello World

## Objective

Write your very first Python program and understand what's happening when you run it.

## Concepts Covered

- The `print()` function
- Strings (text in quotes)
- How Python runs your code top-to-bottom
- Comments

## Prerequisites

- None — this is the very beginning!

## Lesson

### Your First Line of Python

Every programming journey starts the same way — printing something to the screen. In Python, that looks like this:

```python
print("Hello, World!")
```

That's it. One line. When you run this, Python will display:

```
Hello, World!
```

### What's Actually Happening?

Let's break it down:

- **`print`** is a built-in function. It tells Python "display this on the screen." You'll use it constantly.
- **`(`** and **`)`** are parentheses. They wrap what you're passing to the function — this is called an "argument."
- **`"Hello, World!"`** is a **string** — a piece of text. The quotes tell Python "this is text, not code." You can use either double quotes `"` or single quotes `'` — both work the same way.

### Printing Multiple Things

You can pass multiple items to `print()`, separated by commas. Python will add a space between each one:

```python
print("Hello", "World")    # Output: Hello World
print("I", "love", "Python")  # Output: I love Python
```

### Comments

See that `#` symbol? Anything after `#` on a line is a **comment**. Python ignores it completely — it's just a note for humans reading the code.

```python
# This is a comment — Python skips this line entirely
print("This runs")  # Comments can go at the end of a line too
```

Use comments to explain *why* you're doing something, not *what* you're doing. The code itself should be clear enough to show what's happening.

### Empty Lines and Whitespace

Python doesn't care about blank lines between statements. Use them to organize your code and make it readable:

```python
print("Section 1")
print("Still section 1")

print("Section 2 — notice the blank line above for readability")
```

### Special Characters in Strings

Sometimes you need to include characters that have special meaning. Use a backslash `\` to "escape" them:

```python
print("She said \"hello\"")   # Output: She said "hello"
print("Line 1\nLine 2")       # \n creates a new line
print("Tab\there")             # \t creates a tab
```

Or just use the other type of quote to avoid escaping:

```python
print('She said "hello"')     # Single quotes outside, double inside
print("It's easy")            # Double quotes outside, single inside
```

### The print() Function in Detail

`print()` has a few handy tricks:

```python
# Change what goes between items (default is a space)
print("2025", "02", "09", sep="-")   # Output: 2025-02-09

# Change what goes at the end (default is a newline)
print("Loading", end="...")
print("Done!")                        # Output: Loading...Done!

# Print an empty line
print()
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- `print()` displays text on the screen
- Strings are text wrapped in quotes (single or double — your choice)
- Comments start with `#` and are ignored by Python
- Python runs your code from top to bottom, one line at a time
- `print()` supports `sep` and `end` parameters for formatting control
