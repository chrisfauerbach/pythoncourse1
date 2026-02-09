"""
Reading and Writing Text Files — Exercises
============================================

Practice problems to test your understanding of file I/O.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

All exercises create their own temporary files and clean up after themselves,
so you can run this as many times as you want.
"""

import os
import tempfile

# Create a temp directory that all exercises share
TMPDIR = tempfile.mkdtemp(prefix="pyexercises_")


# =============================================================================
# Exercise 1: Write and read back
#
# Given the list `names` below:
# 1. Write each name to a file called "names.txt" (in TMPDIR), one per line
# 2. Read the file back into a NEW list called `names_from_file`
# 3. Print each name from the list you read back
# 4. Verify the lists match by printing: "Match: True" or "Match: False"
#
# Hint: Remember to strip newlines when reading back!
# =============================================================================

def exercise_1():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    filepath = os.path.join(TMPDIR, "names.txt")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Count lines, words, and characters
#
# A file "story.txt" is created for you below.
# Read it and print:
#   Lines: <count>
#   Words: <count>
#   Characters: <count>
#
# Count characters INCLUDING newlines (just use len() on the full text).
# Count words by splitting on whitespace.
#
# Hint: To count lines, you can split on "\n" or use .readlines()
# =============================================================================

def exercise_2():
    # Setup — create the file to work with
    filepath = os.path.join(TMPDIR, "story.txt")
    with open(filepath, "w") as f:
        f.write("The quick brown fox jumps over the lazy dog.\n")
        f.write("Pack my box with five dozen liquor jugs.\n")
        f.write("How vexingly quick daft zebras jump.\n")

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Append log entries
#
# Write a function body that:
# 1. Creates a file "app.log" in TMPDIR (if it doesn't already exist)
# 2. Appends these three log entries to it, one at a time (three separate
#    open/write/close cycles using "a" mode):
#      "[INFO] Application started"
#      "[WARNING] Disk space low"
#      "[ERROR] Connection failed"
# 3. Reads the file and prints all entries
#
# The point: each append should open, write one line, and close the file —
# simulating how a real application logs messages over time.
# =============================================================================

def exercise_3():
    filepath = os.path.join(TMPDIR, "app.log")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Copy with line numbers
#
# A file "poem.txt" is created for you below.
# Read it and write a new file "poem_numbered.txt" where each line is
# prefixed with its line number, like:
#
#   1: Two roads diverged in a yellow wood,
#   2: And sorry I could not travel both
#   3: And be one traveler, long I stood
#   4: And looked down one as far as I could
#   5: To where it bent in the undergrowth;
#
# Print the contents of the numbered file.
#
# Hint: enumerate() with a start of 1 is your friend here.
# =============================================================================

def exercise_4():
    # Setup — create the source file
    filepath = os.path.join(TMPDIR, "poem.txt")
    with open(filepath, "w") as f:
        f.write("Two roads diverged in a yellow wood,\n")
        f.write("And sorry I could not travel both\n")
        f.write("And be one traveler, long I stood\n")
        f.write("And looked down one as far as I could\n")
        f.write("To where it bent in the undergrowth;\n")

    output_path = os.path.join(TMPDIR, "poem_numbered.txt")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Find and replace
#
# A file "config.txt" is created for you below.
# Read it, replace every occurrence of "localhost" with "192.168.1.100",
# and write the result back to the SAME file.
# Print the updated file contents.
#
# Hint: Read the entire file, use .replace(), then write it back.
# =============================================================================

def exercise_5():
    # Setup — create the config file
    filepath = os.path.join(TMPDIR, "config.txt")
    with open(filepath, "w") as f:
        f.write("host=localhost\n")
        f.write("database=localhost:5432\n")
        f.write("cache=localhost:6379\n")
        f.write("debug=true\n")

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Merge files with headers
#
# Three files are created for you below: "part1.txt", "part2.txt", "part3.txt"
# Merge them into a single file "merged.txt" with this format:
#
#   === part1.txt ===
#   (contents of part1)
#
#   === part2.txt ===
#   (contents of part2)
#
#   === part3.txt ===
#   (contents of part3)
#
# There should be a blank line between each section.
# Print the merged file contents.
#
# Hint: Loop over the filenames, read each one, write a header + contents.
# =============================================================================

def exercise_6():
    # Setup — create the source files
    files = {
        "part1.txt": "Alpha\nBravo\nCharlie\n",
        "part2.txt": "Delta\nEcho\nFoxtrot\n",
        "part3.txt": "Golf\nHotel\nIndia\n",
    }
    for name, content in files.items():
        with open(os.path.join(TMPDIR, name), "w") as f:
            f.write(content)

    output_path = os.path.join(TMPDIR, "merged.txt")
    filenames = ["part1.txt", "part2.txt", "part3.txt"]
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    filepath = os.path.join(TMPDIR, "names.txt")

    # Write names to file
    with open(filepath, "w") as f:
        for name in names:
            f.write(name + "\n")

    # Read them back
    with open(filepath, "r") as f:
        names_from_file = [line.strip() for line in f]

    # Print and verify
    for name in names_from_file:
        print(f"  {name}")
    print(f"  Match: {names == names_from_file}")


def solution_2():
    filepath = os.path.join(TMPDIR, "story.txt")
    with open(filepath, "w") as f:
        f.write("The quick brown fox jumps over the lazy dog.\n")
        f.write("Pack my box with five dozen liquor jugs.\n")
        f.write("How vexingly quick daft zebras jump.\n")

    with open(filepath, "r") as f:
        text = f.read()

    lines = text.strip().split("\n")
    words = text.split()
    characters = len(text)

    print(f"  Lines: {len(lines)}")
    print(f"  Words: {len(words)}")
    print(f"  Characters: {characters}")


def solution_3():
    filepath = os.path.join(TMPDIR, "app.log")

    # Remove if it exists from a previous run so output is clean
    if os.path.exists(filepath):
        os.remove(filepath)

    entries = [
        "[INFO] Application started",
        "[WARNING] Disk space low",
        "[ERROR] Connection failed",
    ]

    # Append each entry separately (three open/write/close cycles)
    for entry in entries:
        with open(filepath, "a") as f:
            f.write(entry + "\n")

    # Read and print
    with open(filepath, "r") as f:
        for line in f:
            print(f"  {line.rstrip()}")


def solution_4():
    filepath = os.path.join(TMPDIR, "poem.txt")
    with open(filepath, "w") as f:
        f.write("Two roads diverged in a yellow wood,\n")
        f.write("And sorry I could not travel both\n")
        f.write("And be one traveler, long I stood\n")
        f.write("And looked down one as far as I could\n")
        f.write("To where it bent in the undergrowth;\n")

    output_path = os.path.join(TMPDIR, "poem_numbered.txt")

    with open(filepath, "r") as infile, open(output_path, "w") as outfile:
        for i, line in enumerate(infile, 1):
            outfile.write(f"{i}: {line}")

    with open(output_path, "r") as f:
        for line in f:
            print(f"  {line.rstrip()}")


def solution_5():
    filepath = os.path.join(TMPDIR, "config.txt")
    with open(filepath, "w") as f:
        f.write("host=localhost\n")
        f.write("database=localhost:5432\n")
        f.write("cache=localhost:6379\n")
        f.write("debug=true\n")

    # Read, replace, write back
    with open(filepath, "r") as f:
        content = f.read()

    content = content.replace("localhost", "192.168.1.100")

    with open(filepath, "w") as f:
        f.write(content)

    # Print the result
    with open(filepath, "r") as f:
        for line in f:
            print(f"  {line.rstrip()}")


def solution_6():
    files = {
        "part1.txt": "Alpha\nBravo\nCharlie\n",
        "part2.txt": "Delta\nEcho\nFoxtrot\n",
        "part3.txt": "Golf\nHotel\nIndia\n",
    }
    for name, content in files.items():
        with open(os.path.join(TMPDIR, name), "w") as f:
            f.write(content)

    output_path = os.path.join(TMPDIR, "merged.txt")
    filenames = ["part1.txt", "part2.txt", "part3.txt"]

    with open(output_path, "w") as outfile:
        for i, filename in enumerate(filenames):
            if i > 0:
                outfile.write("\n")  # Blank line between sections
            outfile.write(f"=== {filename} ===\n")
            with open(os.path.join(TMPDIR, filename), "r") as infile:
                outfile.write(infile.read())

    with open(output_path, "r") as f:
        for line in f:
            print(f"  {line.rstrip()}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Write and read back", exercise_1),
        ("Count lines, words, and characters", exercise_2),
        ("Append log entries", exercise_3),
        ("Copy with line numbers", exercise_4),
        ("Find and replace", exercise_5),
        ("Merge files with headers", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
    print()
    print("To see the solutions run, edit this file and change")
    print("exercise_N() calls to solution_N() in the runner above.")

    # Cleanup temp files
    import shutil
    shutil.rmtree(TMPDIR, ignore_errors=True)
    print(f"\nCleaned up temp directory: {TMPDIR}")
