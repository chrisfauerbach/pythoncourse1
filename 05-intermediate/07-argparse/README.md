# Command-Line Arguments with argparse

## Objective

Learn how to build Python scripts that accept command-line arguments, flags, and options — turning your scripts from hardcoded one-trick ponies into flexible, reusable tools.

## Concepts Covered

- Why command-line arguments matter
- `sys.argv` — the manual approach (and why it's painful)
- `argparse` — Python's built-in argument parser
- Positional vs optional arguments
- Argument types, defaults, and choices
- Boolean flags (`--verbose`, `--dry-run`)
- Subcommands (like `git commit`, `git push`)
- Help text and documentation

## Prerequisites

- [Fundamentals](../../01-fundamentals/) — functions, strings, control flow
- [Error Handling](../01-error-handling/) — helpful for understanding how argparse reports errors

## Lesson

### Why bother with command-line arguments?

Right now, if you want to change the behavior of a script, you probably edit the code. That's fine for learning, but in the real world you want scripts that work like tools:

```bash
python3 backup.py /home/docs --compress --verbose
python3 resize_images.py photos/ --width 800 --format png
```

Instead of changing the code every time, you pass in what you want when you run it.

### The hard way: sys.argv

Python gives you `sys.argv` — a list of everything typed on the command line:

```python
import sys
print(sys.argv)  # ['script.py', 'arg1', 'arg2']
```

This works but gets ugly fast. You have to manually check if arguments exist, convert types, handle errors, and write your own help text. For anything beyond one or two arguments, it's a headache.

### The right way: argparse

`argparse` is a standard library module that handles all of that for you:

```python
import argparse

parser = argparse.ArgumentParser(description="Greet someone")
parser.add_argument("name", help="Person to greet")
parser.add_argument("--shout", action="store_true", help="YELL the greeting")

args = parser.parse_args()

greeting = f"Hello, {args.name}!"
if args.shout:
    greeting = greeting.upper()
print(greeting)
```

Now you get:
- Automatic `--help` output
- Type checking and error messages
- Clean access via `args.name`, `args.shout`, etc.

### Positional vs optional arguments

**Positional** arguments are required and order matters:

```python
parser.add_argument("filename")       # Required, first thing after the script name
parser.add_argument("destination")    # Required, second thing
```

**Optional** arguments start with `--` (or `-` for short form):

```python
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-o", "--output", default="result.txt")
```

### Types, defaults, and choices

argparse can convert arguments to the right type and restrict allowed values:

```python
parser.add_argument("count", type=int)                        # Must be an integer
parser.add_argument("--level", type=int, default=1)           # Default to 1
parser.add_argument("--color", choices=["red", "green", "blue"])  # Only these values
parser.add_argument("--tags", nargs="+")                      # One or more values → list
```

### Boolean flags

For on/off switches, use `store_true` or `store_false`:

```python
parser.add_argument("--verbose", action="store_true")   # Default False, --verbose sets True
parser.add_argument("--no-color", action="store_true")   # Default False, --no-color sets True
```

### Subcommands

For tools that have multiple modes (like `git commit` vs `git push`):

```python
subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add an item")
add_parser.add_argument("item")

list_parser = subparsers.add_parser("list", help="List all items")
list_parser.add_argument("--all", action="store_true")
```

### Putting it together

A well-structured CLI script follows this pattern:

```python
def main():
    parser = argparse.ArgumentParser(description="What this tool does")
    # ... add arguments ...
    args = parser.parse_args()
    # ... use args to do the work ...

if __name__ == "__main__":
    main()
```

This keeps your script both importable and runnable.

## Code Examples

See [example.py](example.py) for runnable demonstrations of all these concepts.

## Exercises

Try the exercises in [exercises.py](exercises.py) — build your own CLI tools!

## Key Takeaways

- `sys.argv` works but doesn't scale — use `argparse` instead
- Positional arguments are required; optional arguments start with `--`
- argparse handles type conversion, defaults, choices, and error messages for you
- `store_true` is the go-to for boolean flags
- Subcommands let you build multi-mode tools like `git`
- Always wrap your CLI logic in `main()` with `if __name__ == "__main__"`
- The auto-generated `--help` flag is one of argparse's best features — write good help text!
