"""
Command-Line Arguments with argparse — Example Code
======================================================

Run this file with different arguments to see how argparse works:

    python3 example.py
    python3 example.py --help
    python3 example.py Alice
    python3 example.py Alice --shout --times 3

Because argparse reads from the command line, this file works a bit
differently than others in this course. We demonstrate each concept
in its own function, then run them all with simulated arguments so
you can see the output without typing anything special.

To try the REAL command-line version, run:
    python3 example.py --interactive Alice --shout --times 3
"""

import argparse
import sys

# -----------------------------------------------------------------------------
# 1. sys.argv — the manual approach
# -----------------------------------------------------------------------------

def demo_sys_argv():
    """Show what sys.argv looks like."""
    print("1. sys.argv — the raw command line")
    print(f"   sys.argv = {sys.argv}")
    print(f"   Script name: {sys.argv[0]}")
    print(f"   Number of arguments: {len(sys.argv) - 1}")
    print()

# -----------------------------------------------------------------------------
# 2. Basic argparse — positional and optional arguments
# -----------------------------------------------------------------------------

def demo_basic_argparse():
    """Demonstrate positional and optional arguments."""
    print("2. Basic argparse — positional and optional arguments")

    # Create a parser (we pass args manually so this runs without command-line input)
    parser = argparse.ArgumentParser(description="Greet someone nicely")
    parser.add_argument("name", help="Person to greet")
    parser.add_argument("--greeting", default="Hello", help="Greeting to use")
    parser.add_argument("--shout", action="store_true", help="YELL the greeting")

    # Simulate different command-line inputs
    test_cases = [
        ["Alice"],
        ["Bob", "--greeting", "Howdy"],
        ["Charlie", "--shout"],
        ["Diana", "--greeting", "Hey", "--shout"],
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        message = f"{args.greeting}, {args.name}!"
        if args.shout:
            message = message.upper()
        print(f"   args: {args_list}")
        print(f"   output: {message}")
        print()

# -----------------------------------------------------------------------------
# 3. Argument types — int, float, and automatic validation
# -----------------------------------------------------------------------------

def demo_types():
    """Demonstrate type conversion and validation."""
    print("3. Argument types and validation")

    parser = argparse.ArgumentParser()
    parser.add_argument("width", type=int, help="Width in pixels")
    parser.add_argument("height", type=int, help="Height in pixels")
    parser.add_argument("--scale", type=float, default=1.0, help="Scale factor")

    test_cases = [
        ["800", "600"],
        ["1920", "1080", "--scale", "0.5"],
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        actual_w = int(args.width * args.scale)
        actual_h = int(args.height * args.scale)
        print(f"   args: {args_list}")
        print(f"   Requested: {args.width}x{args.height}, scale: {args.scale}")
        print(f"   Actual:    {actual_w}x{actual_h}")
        print()

# -----------------------------------------------------------------------------
# 4. Choices — restricting allowed values
# -----------------------------------------------------------------------------

def demo_choices():
    """Demonstrate the choices parameter."""
    print("4. Choices — restricting allowed values")

    parser = argparse.ArgumentParser()
    parser.add_argument("--level", choices=["debug", "info", "warning", "error"],
                        default="info", help="Log level")
    parser.add_argument("--format", choices=["json", "csv", "text"],
                        default="text", help="Output format")

    test_cases = [
        [],
        ["--level", "debug", "--format", "json"],
        ["--level", "error"],
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        print(f"   args: {args_list if args_list else '(none)'}")
        print(f"   level={args.level}, format={args.format}")
        print()

# -----------------------------------------------------------------------------
# 5. nargs — accepting multiple values
# -----------------------------------------------------------------------------

def demo_nargs():
    """Demonstrate nargs for multiple values."""
    print("5. nargs — accepting multiple values")

    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+", help="One or more files to process")
    parser.add_argument("--exclude", nargs="*", default=[], help="Patterns to exclude")

    test_cases = [
        ["report.csv"],
        ["data1.csv", "data2.csv", "data3.csv"],
        ["data.csv", "--exclude", "*.tmp", "*.bak"],
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        print(f"   args: {args_list}")
        print(f"   files:   {args.files}")
        print(f"   exclude: {args.exclude}")
        print()

# -----------------------------------------------------------------------------
# 6. Short flags — -v instead of --verbose
# -----------------------------------------------------------------------------

def demo_short_flags():
    """Demonstrate short flag aliases."""
    print("6. Short flags — convenient abbreviations")

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="Show details")
    parser.add_argument("-o", "--output", default="stdout", help="Output destination")
    parser.add_argument("-n", "--count", type=int, default=1, help="Repeat count")

    test_cases = [
        [],
        ["-v"],
        ["-v", "-o", "results.txt", "-n", "5"],
        ["--verbose", "--output", "results.txt", "--count", "5"],  # Same as above
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        print(f"   args: {args_list if args_list else '(none)'}")
        print(f"   verbose={args.verbose}, output={args.output}, count={args.count}")
        print()

# -----------------------------------------------------------------------------
# 7. Defaults and required — controlling what's mandatory
# -----------------------------------------------------------------------------

def demo_defaults():
    """Demonstrate defaults and required arguments."""
    print("7. Defaults and required arguments")

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="File to read (positional = always required)")
    parser.add_argument("--output", default="output.txt", help="Output file (default: output.txt)")
    parser.add_argument("--mode", required=True, help="Processing mode (required even though it's optional-style)")

    test_cases = [
        ["data.csv", "--mode", "fast"],
        ["report.json", "--mode", "careful", "--output", "results.txt"],
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        print(f"   args: {args_list}")
        print(f"   input={args.input_file}, output={args.output}, mode={args.mode}")
        print()

# -----------------------------------------------------------------------------
# 8. Subcommands — building multi-mode tools
# -----------------------------------------------------------------------------

def demo_subcommands():
    """Demonstrate subcommands like git commit, git push, etc."""
    print("8. Subcommands — multi-mode tools")

    parser = argparse.ArgumentParser(description="A simple task manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'add' subcommand
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="Task description")
    add_parser.add_argument("--priority", choices=["low", "medium", "high"],
                            default="medium", help="Task priority")

    # 'list' subcommand
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--all", action="store_true", help="Include completed tasks")
    list_parser.add_argument("--priority", choices=["low", "medium", "high"],
                             help="Filter by priority")

    # 'done' subcommand
    done_parser = subparsers.add_parser("done", help="Mark a task as complete")
    done_parser.add_argument("task_id", type=int, help="Task ID to mark as done")

    test_cases = [
        ["add", "Write documentation", "--priority", "high"],
        ["add", "Buy groceries"],
        ["list"],
        ["list", "--all", "--priority", "high"],
        ["done", "1"],
    ]

    for args_list in test_cases:
        args = parser.parse_args(args_list)
        print(f"   args: {args_list}")
        print(f"   parsed: {args}")
        print()

# -----------------------------------------------------------------------------
# 9. The help flag — auto-generated documentation
# -----------------------------------------------------------------------------

def demo_help():
    """Show what auto-generated help looks like."""
    print("9. Auto-generated --help output")
    print("   (This is what users see when they run your script with --help)")
    print()

    parser = argparse.ArgumentParser(
        description="Resize images in a directory to a target size.",
        epilog="Example: python3 resize.py photos/ --width 800 --format png"
    )
    parser.add_argument("directory", help="Directory containing images")
    parser.add_argument("--width", type=int, default=1024, help="Target width in pixels (default: 1024)")
    parser.add_argument("--height", type=int, help="Target height (default: auto based on aspect ratio)")
    parser.add_argument("--format", choices=["png", "jpg", "webp"], default="jpg",
                        help="Output format (default: jpg)")
    parser.add_argument("-q", "--quality", type=int, default=85,
                        help="Compression quality 1-100 (default: 85)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without doing it")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Print detailed progress")

    # Print the help text (format_help() returns it as a string)
    for line in parser.format_help().split("\n"):
        print(f"   {line}")
    print()

# -----------------------------------------------------------------------------
# 10. Interactive mode — try it yourself!
# -----------------------------------------------------------------------------

def interactive_mode():
    """Parse actual command-line arguments when run with --interactive."""
    parser = argparse.ArgumentParser(description="Greet someone (interactive demo)")
    parser.add_argument("name", help="Person to greet")
    parser.add_argument("--greeting", default="Hello", help="Greeting to use")
    parser.add_argument("--shout", action="store_true", help="YELL the greeting")
    parser.add_argument("--times", type=int, default=1, help="Repeat the greeting N times")

    # Remove '--interactive' from args before parsing
    filtered_args = [a for a in sys.argv[1:] if a != "--interactive"]
    args = parser.parse_args(filtered_args)

    message = f"{args.greeting}, {args.name}!"
    if args.shout:
        message = message.upper()

    for _ in range(args.times):
        print(message)

# -----------------------------------------------------------------------------
# Run all demos
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # If run with --interactive, use real command-line arguments
    if "--interactive" in sys.argv:
        interactive_mode()
    else:
        demo_sys_argv()
        demo_basic_argparse()
        demo_types()
        demo_choices()
        demo_nargs()
        demo_short_flags()
        demo_defaults()
        demo_subcommands()
        demo_help()

        print("=" * 60)
        print("   ARGPARSE EXAMPLES COMPLETE!")
        print("=" * 60)
        print()
        print("Try the interactive mode:")
        print("   python3 example.py --interactive Alice --shout --times 3")
        print()
        print("Now try the exercises to build your own CLI tools!")
