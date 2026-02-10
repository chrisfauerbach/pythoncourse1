"""
Command-Line Arguments with argparse — Exercises
===================================================

Practice building CLI tools with argparse.
Try to solve each exercise before looking at the solutions below!

Unlike most exercises in this course, these are designed to be run
with command-line arguments. But each exercise also has a "test mode"
that simulates arguments so you can verify your solution by just
running:
    python3 exercises.py
"""

import argparse
import sys


# =============================================================================
# Exercise 1: Simple greeter
#
# Build a CLI tool that accepts a name (positional) and an optional
# --greeting flag (default: "Hello").
#
# Usage:
#   python3 exercises.py greet Alice
#   python3 exercises.py greet Bob --greeting "Good morning"
#
# Expected output:
#   Hello, Alice!
#   Good morning, Bob!
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    # Create a parser, add a 'name' positional argument and a '--greeting'
    # optional argument with default "Hello", then format and print the message.
    #
    # Test with simulated args:
    # parser = argparse.ArgumentParser()
    # ...
    # for test_args in [["Alice"], ["Bob", "--greeting", "Good morning"]]:
    #     args = parser.parse_args(test_args)
    #     print(f"{args.greeting}, {args.name}!")
    pass


# =============================================================================
# Exercise 2: File line counter
#
# Build a CLI tool that accepts one or more filenames (positional, nargs="+")
# and an optional --count-blank flag that controls whether blank lines are
# counted.
#
# Don't actually read files — just parse the arguments and print what
# would happen.
#
# Usage:
#   python3 exercises.py count data.txt
#   python3 exercises.py count file1.txt file2.txt --count-blank
#
# Expected output:
#   Would count lines in: ['data.txt'] (skip blank: True)
#   Would count lines in: ['file1.txt', 'file2.txt'] (skip blank: False)
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    # Create a parser with 'files' (nargs="+") and '--count-blank' (store_true)
    #
    # Test with simulated args:
    # for test_args in [["data.txt"], ["file1.txt", "file2.txt", "--count-blank"]]:
    #     args = parser.parse_args(test_args)
    #     skip = not args.count_blank
    #     print(f"Would count lines in: {args.files} (skip blank: {skip})")
    pass


# =============================================================================
# Exercise 3: Temperature converter
#
# Build a CLI that takes a temperature value (float) and a --unit flag
# with choices ["C", "F"]. Default unit is "C".
# If unit is C, convert to Fahrenheit. If F, convert to Celsius.
#
# Usage:
#   python3 exercises.py convert 100 --unit C
#   python3 exercises.py convert 72 --unit F
#
# Expected output:
#   100.0°C = 212.0°F
#   72.0°F = 22.2°C
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    # Create a parser with 'temp' (type=float) and '--unit' (choices, default "C")
    # Then do the conversion and print the result.
    #
    # Test with simulated args:
    # for test_args in [["100", "--unit", "C"], ["72", "--unit", "F"], ["0"]]:
    #     args = parser.parse_args(test_args)
    #     if args.unit == "C":
    #         converted = round(args.temp * 9/5 + 32, 1)
    #         print(f"{args.temp}°C = {converted}°F")
    #     else:
    #         converted = round((args.temp - 32) * 5/9, 1)
    #         print(f"{args.temp}°F = {converted}°C")
    pass


# =============================================================================
# Exercise 4: Password generator (arguments only — no actual generation)
#
# Build a CLI with these options:
#   --length   (int, default 16)      — password length
#   --no-upper (store_true)           — exclude uppercase letters
#   --no-digits (store_true)          — exclude digits
#   --special  (store_true)           — include special characters
#   --count    (int, default 1)       — how many passwords to generate
#
# Just print the configuration — don't actually generate passwords.
#
# Expected output:
#   Config: length=16, upper=True, digits=True, special=False, count=1
#   Config: length=32, upper=True, digits=False, special=True, count=5
#   Config: length=8, upper=False, digits=True, special=False, count=3
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    # Create a parser with all the options listed above.
    # Print the resolved configuration.
    #
    # Test with simulated args:
    # for test_args in [
    #     [],
    #     ["--length", "32", "--no-digits", "--special", "--count", "5"],
    #     ["--length", "8", "--no-upper", "--count", "3"],
    # ]:
    #     args = parser.parse_args(test_args)
    #     print(f"Config: length={args.length}, upper={not args.no_upper}, "
    #           f"digits={not args.no_digits}, special={args.special}, "
    #           f"count={args.count}")
    pass


# =============================================================================
# Exercise 5: Subcommand tool
#
# Build a CLI with two subcommands:
#   greet <name> [--loud]     — print a greeting
#   math <a> <b> [--op +|-|*] — do math on two numbers
#
# Expected output:
#   Hello, Alice!
#   HELLO, BOB!
#   3 + 7 = 10
#   4 * 5 = 20
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    # Create a parser with subparsers for 'greet' and 'math'.
    # 'greet' takes a name and optional --loud flag.
    # 'math' takes two numbers (type=float) and optional --op (choices, default "+").
    #
    # Test with simulated args:
    # for test_args in [
    #     ["greet", "Alice"],
    #     ["greet", "Bob", "--loud"],
    #     ["math", "3", "7"],
    #     ["math", "4", "5", "--op", "*"],
    # ]:
    #     args = parser.parse_args(test_args)
    #     if args.command == "greet":
    #         msg = f"Hello, {args.name}!"
    #         print(msg.upper() if args.loud else msg)
    #     elif args.command == "math":
    #         ops = {"+": lambda a, b: a + b,
    #                "-": lambda a, b: a - b,
    #                "*": lambda a, b: a * b}
    #         result = ops[args.op](args.a, args.b)
    #         # Show as int if it's a whole number
    #         a = int(args.a) if args.a == int(args.a) else args.a
    #         b = int(args.b) if args.b == int(args.b) else args.b
    #         r = int(result) if result == int(result) else result
    #         print(f"{a} {args.op} {b} = {r}")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    parser = argparse.ArgumentParser(description="Greet someone")
    parser.add_argument("name", help="Person to greet")
    parser.add_argument("--greeting", default="Hello", help="Greeting to use")

    for test_args in [["Alice"], ["Bob", "--greeting", "Good morning"]]:
        args = parser.parse_args(test_args)
        print(f"{args.greeting}, {args.name}!")


def solution_2():
    parser = argparse.ArgumentParser(description="Count lines in files")
    parser.add_argument("files", nargs="+", help="Files to count")
    parser.add_argument("--count-blank", action="store_true",
                        help="Include blank lines in count")

    for test_args in [["data.txt"], ["file1.txt", "file2.txt", "--count-blank"]]:
        args = parser.parse_args(test_args)
        skip = not args.count_blank
        print(f"Would count lines in: {args.files} (skip blank: {skip})")


def solution_3():
    parser = argparse.ArgumentParser(description="Convert temperatures")
    parser.add_argument("temp", type=float, help="Temperature value")
    parser.add_argument("--unit", choices=["C", "F"], default="C",
                        help="Unit of input temperature (default: C)")

    for test_args in [["100", "--unit", "C"], ["72", "--unit", "F"], ["0"]]:
        args = parser.parse_args(test_args)
        if args.unit == "C":
            converted = round(args.temp * 9 / 5 + 32, 1)
            print(f"{args.temp}\u00b0C = {converted}\u00b0F")
        else:
            converted = round((args.temp - 32) * 5 / 9, 1)
            print(f"{args.temp}\u00b0F = {converted}\u00b0C")


def solution_4():
    parser = argparse.ArgumentParser(description="Password generator config")
    parser.add_argument("--length", type=int, default=16, help="Password length")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--special", action="store_true", help="Include special chars")
    parser.add_argument("--count", type=int, default=1, help="Number of passwords")

    for test_args in [
        [],
        ["--length", "32", "--no-digits", "--special", "--count", "5"],
        ["--length", "8", "--no-upper", "--count", "3"],
    ]:
        args = parser.parse_args(test_args)
        print(f"Config: length={args.length}, upper={not args.no_upper}, "
              f"digits={not args.no_digits}, special={args.special}, "
              f"count={args.count}")


def solution_5():
    parser = argparse.ArgumentParser(description="Multi-tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", help="Person to greet")
    greet_parser.add_argument("--loud", action="store_true", help="SHOUT")

    math_parser = subparsers.add_parser("math", help="Do math")
    math_parser.add_argument("a", type=float, help="First number")
    math_parser.add_argument("b", type=float, help="Second number")
    math_parser.add_argument("--op", choices=["+", "-", "*"], default="+",
                             help="Operation (default: +)")

    for test_args in [
        ["greet", "Alice"],
        ["greet", "Bob", "--loud"],
        ["math", "3", "7"],
        ["math", "4", "5", "--op", "*"],
    ]:
        args = parser.parse_args(test_args)
        if args.command == "greet":
            msg = f"Hello, {args.name}!"
            print(msg.upper() if args.loud else msg)
        elif args.command == "math":
            ops = {"+": lambda a, b: a + b,
                   "-": lambda a, b: a - b,
                   "*": lambda a, b: a * b}
            result = ops[args.op](args.a, args.b)
            a = int(args.a) if args.a == int(args.a) else args.a
            b = int(args.b) if args.b == int(args.b) else args.b
            r = int(result) if result == int(result) else result
            print(f"{a} {args.op} {b} = {r}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Simple greeter", exercise_1),
        ("File line counter", exercise_2),
        ("Temperature converter", exercise_3),
        ("Password generator config", exercise_4),
        ("Subcommand tool", exercise_5),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
