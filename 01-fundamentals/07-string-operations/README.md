# String Operations

## Objective

Master Python's string manipulation toolkit — indexing, slicing, built-in methods, formatting, and more. Strings are everywhere in programming, so this is one of the most practical lessons you'll go through.

## Concepts Covered

- Strings as sequences (indexing, negative indexing)
- Slicing strings
- String methods (case, search, modify, check, split/join)
- String immutability
- f-string formatting (alignment, padding, number formats)
- Raw strings

## Prerequisites

- [Variables and Types](../02-variables-and-types/) — you should understand that strings are a core type
- [Hello World](../01-hello-world/) — you should know how to use `print()`

## Lesson

### Strings Are Sequences

A string is a sequence of characters. Each character has a position — called an **index** — starting at zero:

```python
s = "Python"
#    P  y  t  h  o  n
#    0  1  2  3  4  5
```

You access individual characters with square brackets:

```python
s = "Python"
print(s[0])   # P
print(s[1])   # y
print(s[5])   # n
```

Try to access an index that doesn't exist and you'll get an `IndexError`:

```python
# s[10]   # IndexError: string index out of range
```

### Negative Indexing

Python lets you count from the end using negative numbers. `-1` is the last character, `-2` is second-to-last, and so on:

```python
s = "Python"
#    P   y   t   h   o   n
#   -6  -5  -4  -3  -2  -1

print(s[-1])   # n (last character)
print(s[-2])   # o (second to last)
print(s[-6])   # P (same as s[0])
```

This is super handy when you want the last character of a string without knowing its length.

### Slicing

Slicing lets you grab a chunk of a string. The syntax is `s[start:stop]`, where `start` is included but `stop` is **not** (it goes up to but not including `stop`):

```python
s = "Hello, World!"

print(s[0:5])    # Hello
print(s[7:12])   # World
print(s[:5])     # Hello    (omit start = start from beginning)
print(s[7:])     # World!   (omit stop = go to the end)
print(s[:])      # Hello, World!  (copy of the whole string)
```

You can also add a **step** — `s[start:stop:step]`:

```python
s = "abcdefgh"

print(s[0:8:2])   # aceg   (every 2nd character)
print(s[1:8:2])   # bdfh   (every 2nd character, starting at index 1)
print(s[::3])     # adg    (every 3rd character)
```

The classic trick — **reverse a string** with `[::-1]`:

```python
s = "Hello"
print(s[::-1])   # olleH
```

### String Methods — Case

Python strings come with tons of built-in methods. Let's start with case conversion:

```python
s = "hello, world"

print(s.upper())       # HELLO, WORLD
print(s.lower())       # hello, world
print(s.title())       # Hello, World
print(s.capitalize())  # Hello, world  (only first character)
print(s.swapcase())    # HELLO, WORLD

mixed = "hElLo"
print(mixed.swapcase())  # HeLlO
```

**Remember:** These methods return a *new* string — they don't change the original. (More on that in the immutability section below.)

### String Methods — Search

Find things inside a string:

```python
s = "the quick brown fox jumps over the lazy dog"

# find() — returns the index of the first occurrence, or -1 if not found
print(s.find("fox"))       # 16
print(s.find("cat"))       # -1 (not found)

# index() — same as find(), but raises ValueError if not found
print(s.index("fox"))      # 16
# s.index("cat")           # ValueError!

# count() — how many times does a substring appear?
print(s.count("the"))      # 2

# startswith() and endswith() — check the beginning or end
print(s.startswith("the"))   # True
print(s.endswith("dog"))     # True
print(s.endswith("cat"))     # False
```

**Pro tip:** Use `find()` when you're not sure the substring exists and want to avoid an error. Use `index()` when it *should* be there and you want Python to yell at you if it's not.

### String Methods — Modify

Methods that return modified versions of your string:

```python
# strip() — remove leading/trailing whitespace (or other characters)
messy = "   hello   "
print(messy.strip())        # "hello"
print(messy.lstrip())       # "hello   " (left side only)
print(messy.rstrip())       # "   hello" (right side only)

# You can strip specific characters too
dashes = "---hello---"
print(dashes.strip("-"))    # "hello"

# replace() — swap one substring for another
s = "I like cats"
print(s.replace("cats", "dogs"))   # I like dogs
print(s.replace("l", "L"))        # I Like cats (replaces ALL occurrences)

# Limit replacements with a third argument
s = "aaa bbb aaa"
print(s.replace("aaa", "xxx", 1))  # xxx bbb aaa (only first one)
```

### String Methods — Check

These return `True` or `False` and are great for validation:

```python
# isdigit() — all characters are digits?
print("12345".isdigit())    # True
print("123.45".isdigit())   # False (the dot isn't a digit)
print("".isdigit())         # False (empty string)

# isalpha() — all characters are letters?
print("Hello".isalpha())    # True
print("Hello!".isalpha())   # False (exclamation mark)

# isalnum() — all characters are letters or digits?
print("abc123".isalnum())   # True
print("abc 123".isalnum())  # False (space isn't alphanumeric)

# isspace() — all characters are whitespace?
print("   ".isspace())      # True
print(" \t\n ".isspace())   # True (tabs and newlines count)
print("".isspace())         # False (empty string)
```

### String Methods — Split and Join

These two are a power duo. You'll use them *all the time*:

```python
# split() — break a string into a list of pieces
sentence = "the quick brown fox"
words = sentence.split()        # Splits on whitespace by default
print(words)                    # ['the', 'quick', 'brown', 'fox']

# Split on a specific delimiter
date = "2025-02-09"
parts = date.split("-")
print(parts)                    # ['2025', '02', '09']

csv_line = "Alice,30,Engineer"
fields = csv_line.split(",")
print(fields)                   # ['Alice', '30', 'Engineer']

# join() — the opposite of split. Glue a list back together.
words = ["Hello", "World"]
print(" ".join(words))          # Hello World
print("-".join(words))          # Hello-World
print("".join(words))           # HelloWorld

# A common pattern: split, modify, rejoin
sentence = "the quick brown fox"
words = sentence.split()
shouted = [w.upper() for w in words]
print(" ".join(shouted))        # THE QUICK BROWN FOX
```

### Strings Are Immutable

This is important: **you cannot change a string in place**. Every string operation creates a new string.

```python
s = "Hello"
# s[0] = "h"   # TypeError: 'str' object does not support item assignment
```

If you want a "modified" string, you create a new one:

```python
s = "Hello"
s = "h" + s[1:]   # Create a new string "hello"
print(s)           # hello
```

This might feel weird, but it's by design. It makes strings safe to pass around your code — nobody can change them behind your back.

### f-strings Revisited — Alignment, Padding, and Number Formats

You've already seen basic f-strings like `f"Hello, {name}"`. Here are some more powerful formatting tricks:

```python
name = "Alice"
score = 95.678

# Width and alignment
print(f"{'left':<20}|")     # left                |
print(f"{'right':>20}|")    #                right|
print(f"{'center':^20}|")   #       center       |

# Padding with a fill character
print(f"{'hello':*^20}")    # *******hello********
print(f"{'hello':->20}")    # ---------------hello
print(f"{42:05d}")          # 00042 (pad with zeros)

# Number formatting
pi = 3.14159265
print(f"Pi: {pi:.2f}")           # Pi: 3.14 (2 decimal places)
print(f"Pi: {pi:.4f}")           # Pi: 3.1416 (4 decimal places)

big = 1_234_567
print(f"Population: {big:,}")    # Population: 1,234,567

# Percentages
ratio = 0.856
print(f"Score: {ratio:.1%}")     # Score: 85.6%
```

### Raw Strings

Normally, backslashes in strings have special meaning (`\n` = newline, `\t` = tab). But sometimes you want the literal backslash characters — like in Windows file paths or regular expressions.

Prefix the string with `r` to make it a **raw string**:

```python
# Normal string — \n is a newline
print("C:\new_folder")      # C: (then a newline) ew_folder — oops!

# Raw string — backslashes are treated literally
print(r"C:\new_folder")     # C:\new_folder

# Useful for regex patterns
import re
pattern = r"\d{3}-\d{4}"    # Matches patterns like 555-1234
```

Without the `r`, you'd have to double every backslash: `"\\d{3}-\\d{4}"`. Raw strings save you from that headache.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Strings are sequences — access characters with `s[0]`, `s[-1]`, etc.
- Slicing with `s[start:stop:step]` is incredibly powerful — learn it well
- Strings are **immutable** — every "modification" creates a new string
- The most useful methods: `.split()`, `.join()`, `.strip()`, `.replace()`, `.find()`, `.upper()`, `.lower()`
- Check methods (`.isdigit()`, `.isalpha()`, etc.) are great for input validation
- f-strings support alignment (`<`, `>`, `^`), padding, decimal precision (`.2f`), commas (`:,`), and percentages (`:.1%`)
- Use raw strings (`r"..."`) when you need literal backslashes (file paths, regex)
