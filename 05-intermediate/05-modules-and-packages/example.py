"""
Modules and Packages — Example Code
=====================================

Run this file:
    python3 example.py

This file demonstrates how to import modules, explore them, and use the
standard library. Since modules and packages are about organizing code across
files, we focus on the import patterns and built-in tools you'll use every day.
"""

# -----------------------------------------------------------------------------
# 1. Basic import — the whole module
# -----------------------------------------------------------------------------

# When you import the whole module, you access everything with module.name
# This is the most common style and keeps things very explicit.

import math

print("=" * 60)
print("1. BASIC IMPORT")
print("=" * 60)

print(f"  math.pi       = {math.pi}")
print(f"  math.e        = {math.e}")
print(f"  math.sqrt(144) = {math.sqrt(144)}")
print(f"  math.floor(3.7) = {math.floor(3.7)}")
print(f"  math.ceil(3.2)  = {math.ceil(3.2)}")
print()

# -----------------------------------------------------------------------------
# 2. from...import — grab specific things
# -----------------------------------------------------------------------------

# When you only need a couple things, pull them out directly.
# No prefix needed — they become local names.

from random import randint, choice, shuffle

print("=" * 60)
print("2. FROM...IMPORT")
print("=" * 60)

print(f"  randint(1, 100) = {randint(1, 100)}")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"  choice({fruits}) = {choice(fruits)}")

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(f"  shuffle([1, 2, 3, 4, 5]) = {numbers}")
print()

# -----------------------------------------------------------------------------
# 3. import...as — aliasing for convenience
# -----------------------------------------------------------------------------

# Give a module a shorter name. You'll see this a lot with popular libraries.

import datetime as dt
import collections as col

print("=" * 60)
print("3. IMPORT...AS (ALIASING)")
print("=" * 60)

now = dt.datetime.now()
print(f"  Current date/time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

today = dt.date.today()
print(f"  Today's date:      {today}")

# collections.Counter counts occurrences of each element
letters = col.Counter("mississippi")
print(f"  Counter('mississippi') = {dict(letters)}")
print()

# -----------------------------------------------------------------------------
# 4. The __name__ variable
# -----------------------------------------------------------------------------

# Every module has a __name__ variable. When you run a file directly, it's
# set to "__main__". When the file is imported, it's set to the module name.

print("=" * 60)
print("4. THE __name__ VARIABLE")
print("=" * 60)

print(f"  This file's __name__ = {__name__!r}")
print(f"  math's __name__      = {math.__name__!r}")
print(f"  datetime's __name__  = {dt.__name__!r}")
print()

# This is why we use "if __name__ == '__main__'" — it lets us write code that
# only runs when the file is executed directly, not when it's imported.

# -----------------------------------------------------------------------------
# 5. Exploring modules with dir() and help()
# -----------------------------------------------------------------------------

# dir() lists everything in a module — functions, classes, variables, etc.
# help() gives you the full documentation for a module or function.

print("=" * 60)
print("5. EXPLORING MODULES WITH dir()")
print("=" * 60)

# Let's see what's inside the 'string' module
import string

# Filter out private names (starting with _) to see the public API
public_names = [name for name in dir(string) if not name.startswith("_")]
print(f"  Public names in 'string' module:")
print(f"  {public_names}")
print()

# Some useful constants in the string module
print(f"  string.ascii_lowercase = {string.ascii_lowercase!r}")
print(f"  string.digits          = {string.digits!r}")
print(f"  string.punctuation     = {string.punctuation!r}")
print()

# To get help on any function, use help() in an interactive session:
#   help(math.sqrt)
#   help(random)

# -----------------------------------------------------------------------------
# 6. sys module — system info and configuration
# -----------------------------------------------------------------------------

import sys

print("=" * 60)
print("6. sys MODULE — SYSTEM INFO")
print("=" * 60)

print(f"  Python version:  {sys.version}")
print(f"  Platform:        {sys.platform}")
print(f"  Executable:      {sys.executable}")
print()

# sys.path is the module search path — Python looks here when you import
print("  Module search path (sys.path):")
for i, path in enumerate(sys.path[:5]):  # Show first 5 entries
    print(f"    [{i}] {path!r}")
if len(sys.path) > 5:
    print(f"    ... and {len(sys.path) - 5} more entries")
print()

# -----------------------------------------------------------------------------
# 7. os module — interacting with the operating system
# -----------------------------------------------------------------------------

import os

print("=" * 60)
print("7. os MODULE — OPERATING SYSTEM")
print("=" * 60)

print(f"  Current directory: {os.getcwd()}")
print(f"  Your user:         {os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))}")
print(f"  CPU count:         {os.cpu_count()}")
print()

# -----------------------------------------------------------------------------
# 8. pathlib — modern file path handling
# -----------------------------------------------------------------------------

from pathlib import Path

print("=" * 60)
print("8. pathlib — MODERN FILE PATHS")
print("=" * 60)

# Path objects are way nicer than string manipulation
current = Path.cwd()
print(f"  Current dir:    {current}")
print(f"  Home dir:       {Path.home()}")

# Build paths with / operator — clean and readable
config_path = Path.home() / ".config" / "myapp" / "settings.json"
print(f"  Config path:    {config_path}")
print(f"  File name:      {config_path.name}")
print(f"  File extension: {config_path.suffix}")
print(f"  Parent dir:     {config_path.parent}")

# Check this file's own path
this_file = Path(__file__)
print(f"  This script:    {this_file.name}")
print(f"  Absolute path:  {this_file.resolve()}")
print()

# -----------------------------------------------------------------------------
# 9. json module — working with JSON data
# -----------------------------------------------------------------------------

import json

print("=" * 60)
print("9. json MODULE — JSON DATA")
print("=" * 60)

# Python dict to JSON string
user = {
    "name": "Alice",
    "age": 30,
    "hobbies": ["reading", "coding", "hiking"],
    "active": True,
}

json_string = json.dumps(user, indent=2)
print(f"  Python dict -> JSON string:")
for line in json_string.split("\n"):
    print(f"    {line}")

# JSON string back to Python dict
parsed = json.loads(json_string)
print(f"  JSON string -> Python dict: {parsed['name']}, age {parsed['age']}")
print()

# -----------------------------------------------------------------------------
# 10. itertools — powerful iterator tools
# -----------------------------------------------------------------------------

import itertools

print("=" * 60)
print("10. itertools — ITERATOR TOOLS")
print("=" * 60)

# chain — combine multiple iterables into one
combined = list(itertools.chain([1, 2], [3, 4], [5, 6]))
print(f"  chain([1,2], [3,4], [5,6]) = {combined}")

# combinations — all possible pairs
items = ["A", "B", "C", "D"]
pairs = list(itertools.combinations(items, 2))
print(f"  combinations(['A','B','C','D'], 2) = {pairs}")

# cycle — repeat an iterable forever (we take just 7 items)
days = itertools.cycle(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
week_and_a_bit = [next(days) for _ in range(9)]
print(f"  cycle(weekdays)[:9] = {week_and_a_bit}")
print()

# -----------------------------------------------------------------------------
# 11. re module — regular expressions (quick taste)
# -----------------------------------------------------------------------------

import re

print("=" * 60)
print("11. re MODULE — REGULAR EXPRESSIONS")
print("=" * 60)

text = "Call me at 555-1234 or 555-5678. My zip is 90210."

# Find all phone number patterns
phones = re.findall(r"\d{3}-\d{4}", text)
print(f"  Text: {text!r}")
print(f"  Phone numbers found: {phones}")

# Find all standalone numbers
all_numbers = re.findall(r"\d+", text)
print(f"  All numbers found:   {all_numbers}")

# Check if a string matches a pattern
email = "user@example.com"
is_email = bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
print(f"  Is {email!r} an email? {is_email}")
print()

# -----------------------------------------------------------------------------
# 12. Putting it all together — a mini example
# -----------------------------------------------------------------------------

print("=" * 60)
print("12. PUTTING IT ALL TOGETHER")
print("=" * 60)

# Let's combine several modules to do something useful:
# Generate a random "project ID" with a timestamp

import string
import random
import datetime as dt

# Random 6-character alphanumeric code
chars = string.ascii_uppercase + string.digits
random_code = "".join(random.choices(chars, k=6))

# Current timestamp
timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

# Combine into a project ID
project_id = f"PROJ-{timestamp}-{random_code}"
print(f"  Generated project ID: {project_id}")

# Bonus: how many bytes is the Python executable?
python_path = Path(sys.executable)
if python_path.exists():
    size_mb = python_path.stat().st_size / (1024 * 1024)
    print(f"  Python binary size:   {size_mb:.1f} MB ({python_path})")

print()
print("=" * 60)
print("  MODULES AND PACKAGES EXAMPLE COMPLETE!")
print("=" * 60)
print()
print("Try running 'python3 -c \"import this\"' for a fun Easter egg!")
