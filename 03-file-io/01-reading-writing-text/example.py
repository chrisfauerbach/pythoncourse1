"""
Reading and Writing Text Files — Example Code
===============================================

Run this file:
    python3 example.py

This example is fully self-contained. It creates temporary files, demonstrates
every reading and writing technique from the lesson, and cleans up after itself.
"""

import os
import tempfile

# We'll do everything inside a temporary directory so nothing is left behind
tmpdir = tempfile.mkdtemp(prefix="pylesson_")
print(f"Working in temporary directory: {tmpdir}\n")

# -----------------------------------------------------------------------------
# 1. Writing a file with .write()
# -----------------------------------------------------------------------------

# Mode "w" creates a new file (or overwrites an existing one)
# .write() does NOT add newlines — you must include \n yourself
filepath = os.path.join(tmpdir, "greeting.txt")

with open(filepath, "w") as f:
    f.write("Hello from Python!\n")
    f.write("This is the second line.\n")
    f.write("And this is the third.\n")

print("1. Wrote greeting.txt with .write()")

# -----------------------------------------------------------------------------
# 2. Reading an entire file with .read()
# -----------------------------------------------------------------------------

# Mode "r" opens a file for reading — this is the default mode
with open(filepath, "r") as f:
    content = f.read()  # One big string with everything

print("\n2. Read entire file with .read():")
print(content)

# -----------------------------------------------------------------------------
# 3. Reading one line at a time with .readline()
# -----------------------------------------------------------------------------

# Each call to .readline() advances to the next line
# Returns "" (empty string) when there's nothing left
with open(filepath, "r") as f:
    first = f.readline()    # "Hello from Python!\n"
    second = f.readline()   # "This is the second line.\n"
    third = f.readline()    # "And this is the third.\n"
    fourth = f.readline()   # "" — end of file

print("3. Read lines one at a time with .readline():")
print(f"   Line 1: {first.strip()}")
print(f"   Line 2: {second.strip()}")
print(f"   Line 3: {third.strip()}")
print(f"   Line 4 (empty): {fourth!r}")  # !r shows the repr — you'll see ''

# -----------------------------------------------------------------------------
# 4. Reading all lines into a list with .readlines()
# -----------------------------------------------------------------------------

# Each item in the list includes the trailing \n
with open(filepath, "r") as f:
    raw_lines = f.readlines()

print("\n4. Read all lines with .readlines():")
print(f"   Raw: {raw_lines}")

# Strip the newlines for cleaner data
clean_lines = [line.strip() for line in raw_lines]
print(f"   Clean: {clean_lines}")

# -----------------------------------------------------------------------------
# 5. Iterating line by line — the memory-efficient way
# -----------------------------------------------------------------------------

# This doesn't load the whole file into memory at once
# Perfect for large files
print("\n5. Iterating line by line:")
with open(filepath, "r") as f:
    for i, line in enumerate(f, 1):
        print(f"   Line {i}: {line.rstrip()}")

# -----------------------------------------------------------------------------
# 6. Writing a list of strings with .writelines()
# -----------------------------------------------------------------------------

# .writelines() does NOT add newlines between items — include them yourself
fruits_path = os.path.join(tmpdir, "fruits.txt")
fruits = ["apple\n", "banana\n", "cherry\n", "dragonfruit\n"]

with open(fruits_path, "w") as f:
    f.writelines(fruits)

print("\n6. Wrote fruits.txt with .writelines()")
with open(fruits_path, "r") as f:
    print(f"   Contents: {f.read()}", end="")

# -----------------------------------------------------------------------------
# 7. A cleaner pattern — writing a list without pre-adding \n
# -----------------------------------------------------------------------------

colors_path = os.path.join(tmpdir, "colors.txt")
colors = ["red", "green", "blue", "yellow"]

with open(colors_path, "w") as f:
    for color in colors:
        f.write(color + "\n")

# You can also do it in one shot with a generator expression
with open(colors_path, "w") as f:
    f.writelines(color + "\n" for color in colors)

print("\n7. Wrote colors.txt from a plain list:")
with open(colors_path, "r") as f:
    print(f"   Contents: {f.read()}", end="")

# -----------------------------------------------------------------------------
# 8. Appending to a file with mode "a"
# -----------------------------------------------------------------------------

# "a" mode adds to the end without erasing existing content
# If the file doesn't exist, it creates it
log_path = os.path.join(tmpdir, "log.txt")

with open(log_path, "a") as f:
    f.write("First log entry\n")

with open(log_path, "a") as f:
    f.write("Second log entry\n")

with open(log_path, "a") as f:
    f.write("Third log entry\n")

print("\n8. Appended three entries to log.txt:")
with open(log_path, "r") as f:
    print(f"   {f.read()}", end="")

# -----------------------------------------------------------------------------
# 9. Exclusive creation with mode "x"
# -----------------------------------------------------------------------------

# "x" mode creates a new file, but FAILS if it already exists
# This prevents accidentally overwriting important data
new_path = os.path.join(tmpdir, "brand_new.txt")

with open(new_path, "x") as f:
    f.write("This file was created with 'x' mode.\n")

print("\n9. Created brand_new.txt with 'x' mode")

# Trying to create it again would raise FileExistsError
try:
    with open(new_path, "x") as f:
        f.write("This won't work!\n")
except FileExistsError:
    print("   FileExistsError: Can't create — file already exists!")

# -----------------------------------------------------------------------------
# 10. Read+Write mode with "r+"
# -----------------------------------------------------------------------------

# "r+" lets you both read and write to an existing file
# The file pointer starts at the beginning
rw_path = os.path.join(tmpdir, "readwrite.txt")

# First, create a file to work with
with open(rw_path, "w") as f:
    f.write("AAAA\nBBBB\nCCCC\n")

# Now open in r+ mode — read first, then write at the current position
with open(rw_path, "r+") as f:
    original = f.read()
    # After reading, the pointer is at the end, so writing appends
    f.write("DDDD\n")

print("\n10. Used 'r+' mode to read and then write:")
with open(rw_path, "r") as f:
    print(f"   {f.read()}", end="")

# -----------------------------------------------------------------------------
# 11. File encoding — handling special characters
# -----------------------------------------------------------------------------

# Always specify encoding="utf-8" to be safe and portable
unicode_path = os.path.join(tmpdir, "unicode.txt")

with open(unicode_path, "w", encoding="utf-8") as f:
    f.write("English: Hello\n")
    f.write("French: Bonjour, cafe\n")
    f.write("Japanese: こんにちは\n")
    f.write("Emoji: 🐍🎉\n")

print("\n11. Wrote unicode.txt with encoding='utf-8':")
with open(unicode_path, "r", encoding="utf-8") as f:
    print(f"   {f.read()}", end="")

# -----------------------------------------------------------------------------
# 12. Checking if a file exists before reading
# -----------------------------------------------------------------------------

print("\n12. Checking if files exist:")

# Using os.path.exists()
print(f"   greeting.txt exists? {os.path.exists(filepath)}")
print(f"   nope.txt exists?     {os.path.exists(os.path.join(tmpdir, 'nope.txt'))}")

# Using a try/except approach — often preferred in Python ("ask forgiveness")
try:
    with open(os.path.join(tmpdir, "nope.txt"), "r") as f:
        data = f.read()
except FileNotFoundError:
    print("   Caught FileNotFoundError for nope.txt — handled gracefully!")

# -----------------------------------------------------------------------------
# 13. Common pitfall — "w" mode erases everything!
# -----------------------------------------------------------------------------

# Let's demonstrate the danger of "w" mode
danger_path = os.path.join(tmpdir, "danger.txt")

with open(danger_path, "w") as f:
    f.write("Very important data!\n")
    f.write("Do not delete!\n")

print("\n13. Pitfall demo — 'w' mode erases existing content:")
with open(danger_path, "r") as f:
    print(f"   Before: {f.read().strip()}")

# Opening with "w" IMMEDIATELY erases the file — even if we don't write anything!
with open(danger_path, "w") as f:
    f.write("Oops, everything is gone.\n")

with open(danger_path, "r") as f:
    print(f"   After:  {f.read().strip()}")

# -----------------------------------------------------------------------------
# 14. Common pitfall — newline characters
# -----------------------------------------------------------------------------

print("\n14. Pitfall demo — watch out for trailing newlines:")
with open(filepath, "r") as f:
    for line in f:
        # line includes \n — printing adds ANOTHER newline
        # This creates double-spaced output (a common surprise)
        pass

with open(filepath, "r") as f:
    lines = f.readlines()
    print(f"   With newline:    {lines[0]!r}")
    print(f"   After .strip():  {lines[0].strip()!r}")

# rstrip("\n") removes only the newline, not other whitespace
    print(f'   After .rstrip(): {lines[0].rstrip(chr(10))!r}')

# -----------------------------------------------------------------------------
# 15. Putting it all together — a practical example
# -----------------------------------------------------------------------------

print("\n15. Practical example — process a CSV-like file:")

# Create a simple data file
data_path = os.path.join(tmpdir, "scores.txt")
with open(data_path, "w") as f:
    f.write("Alice,95\n")
    f.write("Bob,82\n")
    f.write("Charlie,91\n")
    f.write("Diana,88\n")

# Read it, process it, write a report
report_path = os.path.join(tmpdir, "report.txt")
names_and_scores = []

with open(data_path, "r") as f:
    for line in f:
        name, score = line.strip().split(",")
        names_and_scores.append((name, int(score)))

average = sum(score for _, score in names_and_scores) / len(names_and_scores)

with open(report_path, "w", encoding="utf-8") as f:
    f.write("Score Report\n")
    f.write("=" * 30 + "\n")
    for name, score in names_and_scores:
        f.write(f"  {name:<10} {score:>3}\n")
    f.write("=" * 30 + "\n")
    f.write(f"  Average:   {average:.1f}\n")

with open(report_path, "r") as f:
    for line in f:
        print(f"   {line}", end="")

# -----------------------------------------------------------------------------
# Cleanup — remove all temporary files
# -----------------------------------------------------------------------------

print("\n")
print("=" * 50)
print("Cleaning up temporary files...")

import shutil
shutil.rmtree(tmpdir)
print(f"Removed {tmpdir}")

print()
print("=" * 50)
print("   FILE I/O EXAMPLES COMPLETE!")
print("=" * 50)
print()
print("Try modifying the examples above and run this file again!")
