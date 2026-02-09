# Reading and Writing Text Files

## Objective

Learn how to read from and write to text files in Python. File I/O is one of the most practical skills you'll use — from reading configuration files to saving program output.

## Concepts Covered

- Opening files with `open()` and the different file modes
- The `with` statement (context manager) for safe file handling
- Reading files: `.read()`, `.readline()`, `.readlines()`, and line-by-line iteration
- Writing files: `.write()` and `.writelines()`
- Appending to existing files
- File encoding (`utf-8` and the `encoding` parameter)
- Common patterns and pitfalls

## Prerequisites

- Basic Python (variables, strings, lists, loops)
- f-strings are used in examples but aren't the focus

## Lesson

### Opening Files with `open()`

Python's built-in `open()` function is your gateway to working with files. It takes a filename and a **mode** that tells Python what you want to do:

```python
file = open("notes.txt", "r")   # Open for reading
```

Here are the file modes you'll use:

| Mode | Name       | What It Does                                           |
|------|------------|--------------------------------------------------------|
| `r`  | Read       | Read an existing file. **This is the default.**        |
| `w`  | Write      | Create a new file or **overwrite** an existing one.    |
| `a`  | Append     | Add to the end of a file (creates it if it doesn't exist). |
| `x`  | Exclusive  | Create a new file, but **fail** if it already exists.  |
| `r+` | Read+Write | Read and write to an existing file.                    |

The big one to watch out for is `"w"` — it **erases everything** in the file the moment you open it. More on that in the pitfalls section.

### The `with` Statement — Your Best Friend

Every time you `open()` a file, you need to `close()` it when you're done. If you don't, bad things can happen — data might not get written, and you'll leak system resources. Here's the old way:

```python
file = open("notes.txt", "r")
content = file.read()
file.close()    # Easy to forget this!
```

The **`with` statement** handles closing automatically, even if an error occurs:

```python
with open("notes.txt", "r") as file:
    content = file.read()
# File is automatically closed here, no matter what
```

**Always use `with`.** Seriously. There's almost never a reason not to. Every example in this lesson uses it, and yours should too.

### Reading Files

There are several ways to read a file, each useful in different situations.

#### `.read()` — Read the Entire File at Once

```python
with open("notes.txt", "r") as file:
    content = file.read()       # One big string with everything
    print(content)
```

Great for small files. Be careful with huge files — this loads the entire thing into memory.

#### `.readline()` — Read One Line at a Time

```python
with open("notes.txt", "r") as file:
    first_line = file.readline()    # Reads "Line 1\n"
    second_line = file.readline()   # Reads "Line 2\n"
```

Each call advances to the next line. Returns an empty string `""` when there's nothing left.

#### `.readlines()` — Read All Lines into a List

```python
with open("notes.txt", "r") as file:
    lines = file.readlines()    # ["Line 1\n", "Line 2\n", "Line 3\n"]
```

Notice that each line **keeps its newline character** (`\n`). You'll often want to strip those off:

```python
lines = [line.strip() for line in file.readlines()]
```

#### Iterating Line by Line — The Best Way for Large Files

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

This is **memory-efficient** because it reads one line at a time instead of loading the whole file. This is the way to go for processing large files.

### Writing Files

#### `.write()` — Write a String to a File

```python
with open("output.txt", "w") as file:
    file.write("Hello, file!\n")
    file.write("Second line.\n")
```

Important: `.write()` does **not** add a newline automatically. You need to include `\n` yourself.

#### `.writelines()` — Write a List of Strings

```python
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

Despite the name, `.writelines()` does **not** add newlines between items. You need to include them in each string.

### Appending to Files

Use mode `"a"` to add content to the end of a file without erasing what's already there:

```python
with open("log.txt", "a") as file:
    file.write("New entry at the bottom\n")
```

If the file doesn't exist yet, `"a"` mode creates it — same as `"w"`, but without the danger of overwriting.

### File Encoding

Text files are stored as bytes, and **encoding** is the system that maps bytes to characters. The standard is **UTF-8**, which handles every language and most symbols.

Python 3 usually defaults to UTF-8, but it depends on your system. To be safe and explicit:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Cafe, naive, resume\n")
```

Always specify `encoding="utf-8"` when your files might contain non-ASCII characters (accents, emoji, other languages). It's a good habit even when they don't.

### Common Patterns

#### Read an entire file into a string

```python
with open("data.txt", "r") as f:
    text = f.read()
```

#### Read lines into a clean list (no trailing newlines)

```python
with open("data.txt", "r") as f:
    lines = [line.rstrip("\n") for line in f]
```

#### Write a list of items as lines

```python
names = ["Alice", "Bob", "Charlie"]
with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")
```

Or in one shot:

```python
with open("names.txt", "w") as f:
    f.writelines(name + "\n" for name in names)
```

### Checking if a File Exists

Before reading a file, you might want to check if it actually exists. Use the `os.path` module:

```python
import os

if os.path.exists("data.txt"):
    with open("data.txt", "r") as f:
        content = f.read()
else:
    print("File not found!")
```

Or the more modern `pathlib`:

```python
from pathlib import Path

path = Path("data.txt")
if path.exists():
    content = path.read_text()
```

### Common Pitfalls

**1. Forgetting to close files**
Always use `with`. If you don't, data might not be flushed to disk, and you'll leak file handles. The `with` statement makes this a non-issue.

**2. Accidentally overwriting with `"w"` mode**
Opening a file with `"w"` **immediately erases** its contents — before you write a single byte. If you meant to add to the end, use `"a"`. This is one of the most common mistakes, and there's no undo.

**3. Newline characters sneaking in**
When you read lines, each one ends with `\n`. If you forget to strip it, you'll get unexpected blank lines when printing or extra whitespace when comparing strings:

```python
line = "Alice\n"
print(line)         # Prints "Alice" followed by TWO newlines (one from \n, one from print)
print(line.strip()) # Prints "Alice" with just one newline from print
```

**4. Reading a file that doesn't exist**
Opening a nonexistent file in `"r"` mode raises `FileNotFoundError`. Either check first with `os.path.exists()` or handle it with a `try/except` block.

**5. Using the wrong encoding**
If you see garbled text or get a `UnicodeDecodeError`, it's almost always an encoding mismatch. Specify `encoding="utf-8"` explicitly to avoid system-dependent surprises.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Use `open()` with a mode (`"r"`, `"w"`, `"a"`, `"x"`, `"r+"`) to work with files
- **Always** use the `with` statement — it closes the file for you automatically
- `.read()` grabs everything; iterating line by line is best for large files
- `.write()` and `.writelines()` do **not** add newlines — you must include `\n`
- Mode `"w"` erases the file on open — use `"a"` to append instead
- Specify `encoding="utf-8"` to avoid encoding surprises
- Strip newlines from lines with `.strip()` or `.rstrip("\n")`
