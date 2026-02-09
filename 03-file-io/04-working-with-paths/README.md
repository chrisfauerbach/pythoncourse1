# Working with Paths

## Objective

Learn how to work with file and directory paths in Python using the modern `pathlib` module — so your code works correctly on Windows, macOS, and Linux without headaches.

## Concepts Covered

- Why path handling matters (cross-platform compatibility)
- The `pathlib` module — the modern way (Python 3.4+)
- Creating `Path` objects
- Inspecting path components (`.name`, `.stem`, `.suffix`, `.parent`, `.parts`)
- Building paths with the `/` operator
- Checking if paths exist
- Listing directory contents with `.iterdir()`, `.glob()`, `.rglob()`
- Creating and removing directories and files
- Reading and writing shortcuts (`.read_text()`, `.write_text()`)
- `os.path` vs `pathlib` comparison
- Common real-world patterns

## Prerequisites

- Reading and writing files (previous lessons in this section)
- Basic understanding of your computer's file system

## Lesson

### Why Path Handling Matters

Here's a trap that catches a lot of beginners. You write this on your Mac:

```python
path = "data/reports/sales.csv"
```

It works great! Then your coworker runs it on Windows and gets an error — because Windows uses backslashes (`data\reports\sales.csv`). Hardcoding path separators is fragile and will break across operating systems.

Python's `pathlib` module solves this. It gives you `Path` objects that automatically handle separators, joining, and all the other fiddly stuff — no matter what OS you're on.

### The pathlib Module — The Modern Way

`pathlib` was added in Python 3.4 and it's now the recommended way to work with paths. Import it like this:

```python
from pathlib import Path
```

That single import is all you need for 99% of path operations.

### Creating Path Objects

There are several ways to create a `Path`:

```python
from pathlib import Path

# From a string
p = Path("my_folder/my_file.txt")

# Current working directory
cwd = Path.cwd()

# User's home directory
home = Path.home()

# From multiple parts (joined automatically)
p = Path("my_folder", "subfolder", "file.txt")
```

### Path Components — Taking Paths Apart

Every path has components you can pull out easily:

```python
p = Path("/home/alice/projects/report.csv")

p.name       # "report.csv"    — the final file/folder name
p.stem       # "report"        — the name without its extension
p.suffix     # ".csv"          — the file extension (with the dot)
p.parent     # Path("/home/alice/projects")  — the parent directory
p.parts      # ("/", "home", "alice", "projects", "report.csv")
p.anchor     # "/"             — the root part of the path
```

These are properties, not methods — no parentheses needed.

### Building Paths with the / Operator

This is one of the coolest things about `pathlib`. You can use the `/` operator to join path segments:

```python
base = Path("/home/alice")
full = base / "projects" / "report.csv"
# Result: Path("/home/alice/projects/report.csv")
```

This is way cleaner than string concatenation and always uses the right separator for your OS. It's equivalent to `os.path.join()` but much more readable.

### Checking Paths — Does It Exist?

Before you work with a file, you usually want to check if it's actually there:

```python
p = Path("some_file.txt")

p.exists()    # True if the path exists at all
p.is_file()   # True if it exists AND is a regular file
p.is_dir()    # True if it exists AND is a directory
```

These return simple booleans — perfect for `if` statements:

```python
config = Path("config.json")
if config.is_file():
    data = config.read_text()
else:
    print("Config file not found!")
```

### Listing Directory Contents

`pathlib` makes it easy to see what's inside a directory:

```python
folder = Path("my_project")

# List everything in the directory (one level)
for item in folder.iterdir():
    print(item)

# Find files matching a pattern (one level)
for py_file in folder.glob("*.py"):
    print(py_file)

# Find files matching a pattern (recursive — all subdirectories)
for py_file in folder.rglob("*.py"):
    print(py_file)
```

The difference between `.glob()` and `.rglob()` is important:
- `.glob("*.py")` only looks in the immediate directory
- `.rglob("*.py")` digs into every subdirectory, recursively

### Creating and Removing Directories and Files

```python
# Create a single directory
Path("new_folder").mkdir()

# Create nested directories (like mkdir -p)
Path("a/b/c").mkdir(parents=True, exist_ok=True)
```

The `parents=True` flag creates all the intermediate directories. The `exist_ok=True` flag means "don't crash if the directory already exists." You'll almost always want both.

```python
# Remove an empty directory
Path("new_folder").rmdir()

# Delete a file
Path("old_file.txt").unlink()

# Delete a file (don't error if missing — Python 3.8+)
Path("maybe_exists.txt").unlink(missing_ok=True)

# Rename/move a file
Path("old_name.txt").rename("new_name.txt")
```

Note: `.rmdir()` only works on **empty** directories. For removing a directory tree, you'll need `shutil.rmtree()`.

### Reading and Writing Shortcuts

`Path` objects have built-in methods for quick file I/O — no need to open and close file handles:

```python
p = Path("notes.txt")

# Write text to a file (creates or overwrites)
p.write_text("Hello from pathlib!")

# Read the entire file as a string
content = p.read_text()

# For binary files (images, etc.)
data = Path("photo.jpg").read_bytes()
Path("copy.jpg").write_bytes(data)
```

These are great for small files. For large files or line-by-line processing, stick with `open()`.

### os.path vs pathlib — A Brief Comparison

Before `pathlib`, everyone used `os.path`. You'll still see it in older code. Here's how they compare:

| Task | `os.path` (old way) | `pathlib` (modern way) |
|------|---------------------|----------------------|
| Join paths | `os.path.join("a", "b")` | `Path("a") / "b"` |
| Get filename | `os.path.basename(p)` | `p.name` |
| Get extension | `os.path.splitext(p)[1]` | `p.suffix` |
| Check exists | `os.path.exists(p)` | `p.exists()` |
| Get parent dir | `os.path.dirname(p)` | `p.parent` |
| Absolute path | `os.path.abspath(p)` | `p.resolve()` |
| List directory | `os.listdir(p)` | `p.iterdir()` |

`pathlib` wins on readability every time. The `Path` object approach feels natural — you're calling methods on the path itself instead of passing strings into functions.

**When to use `os.path`:** Basically never for new code. Some older libraries might return strings instead of `Path` objects, but you can always wrap them: `Path(some_string)`.

### Common Patterns

**Find all files of a specific type:**

```python
# All .csv files anywhere in a project
csv_files = list(Path("my_project").rglob("*.csv"))
```

**Walk a directory tree:**

```python
def show_tree(directory, indent=0):
    path = Path(directory)
    for item in sorted(path.iterdir()):
        print("  " * indent + item.name)
        if item.is_dir():
            show_tree(item, indent + 1)
```

**Ensure a parent directory exists before writing:**

```python
output = Path("results/2025/january/report.csv")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text("date,sales\n2025-01-01,100")
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Always use `pathlib.Path` instead of hardcoded string paths — your code will work on any OS
- Use the `/` operator to build paths: `Path("dir") / "subdir" / "file.txt"`
- `.name`, `.stem`, `.suffix`, and `.parent` let you inspect any part of a path
- `.exists()`, `.is_file()`, and `.is_dir()` check what's on disk
- `.glob()` searches one level; `.rglob()` searches recursively
- `.mkdir(parents=True, exist_ok=True)` is your friend for creating directories safely
- `.read_text()` and `.write_text()` are handy shortcuts for small files
- Prefer `pathlib` over `os.path` in all new code — it's cleaner and more Pythonic
