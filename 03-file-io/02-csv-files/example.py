"""
CSV Files — Example Code
==========================

Run this file:
    python3 example.py

A complete walkthrough of Python's csv module. This script creates its own
sample CSV files, demonstrates every major feature, and cleans up after itself.
"""

import csv
import os

# We'll put all our temp files in the same directory as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_FILES = []  # Track files we create so we can clean them up at the end


def temp_path(filename):
    """Helper: build a path in the script directory and track it for cleanup."""
    path = os.path.join(SCRIPT_DIR, filename)
    TEMP_FILES.append(path)
    return path


# -----------------------------------------------------------------------------
# 1. Writing a CSV file with csv.writer()
# -----------------------------------------------------------------------------

print("=" * 60)
print("1. Writing a CSV file with csv.writer()")
print("=" * 60)

# Let's create a sample CSV from scratch
people_path = temp_path("_temp_people.csv")

with open(people_path, "w", newline="") as f:
    writer = csv.writer(f)

    # writerow() writes a single row — pass it a list
    writer.writerow(["name", "age", "city"])

    # You can write one row at a time
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Chicago"])
    writer.writerow(["Charlie", 35, "Houston"])

print(f"Created: {people_path}")

# Let's see what the file looks like on disk
with open(people_path) as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 2. Writing multiple rows at once with writerows()
# -----------------------------------------------------------------------------

print("=" * 60)
print("2. Writing multiple rows at once with writerows()")
print("=" * 60)

scores_path = temp_path("_temp_scores.csv")

rows = [
    ["student", "math", "science", "english"],
    ["Alice", 92, 88, 95],
    ["Bob", 78, 85, 82],
    ["Charlie", 95, 91, 88],
    ["Diana", 67, 72, 90],
    ["Eve", 88, 94, 79],
]

with open(scores_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)  # Write all rows in one call

print(f"Created: {scores_path}")

with open(scores_path) as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 3. Reading a CSV file with csv.reader()
# -----------------------------------------------------------------------------

print("=" * 60)
print("3. Reading a CSV file with csv.reader()")
print("=" * 60)

with open(people_path, newline="") as f:
    reader = csv.reader(f)

    # Grab the header row first using next()
    header = next(reader)
    print(f"Header: {header}")

    # Now loop over the data rows
    for row in reader:
        # Each row is a list of strings
        name, age, city = row
        print(f"  {name} is {age} years old and lives in {city}")

print()

# -----------------------------------------------------------------------------
# 4. csv.DictReader — rows as dictionaries
# -----------------------------------------------------------------------------

print("=" * 60)
print("4. csv.DictReader — rows as dictionaries")
print("=" * 60)

# DictReader uses the header row as keys — much more readable!
with open(people_path, newline="") as f:
    reader = csv.DictReader(f)

    # reader.fieldnames gives you the column names
    print(f"Columns: {reader.fieldnames}")

    for row in reader:
        # Access values by column name instead of index
        print(f"  {row['name']} lives in {row['city']}")

print()

# -----------------------------------------------------------------------------
# 5. csv.DictWriter — writing from dictionaries
# -----------------------------------------------------------------------------

print("=" * 60)
print("5. csv.DictWriter — writing from dictionaries")
print("=" * 60)

products_path = temp_path("_temp_products.csv")
fieldnames = ["product", "price", "in_stock"]

with open(products_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # Don't forget this — DictWriter won't write headers automatically!
    writer.writeheader()

    # Write rows as dictionaries — order doesn't matter
    writer.writerow({"product": "Widget", "price": 9.99, "in_stock": True})
    writer.writerow({"in_stock": False, "product": "Gadget", "price": 24.99})
    writer.writerow({"product": "Doohickey", "price": 4.50, "in_stock": True})

print(f"Created: {products_path}")

with open(products_path) as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 6. Handling different delimiters (TSV, pipe-separated, etc.)
# -----------------------------------------------------------------------------

print("=" * 60)
print("6. Handling different delimiters")
print("=" * 60)

# Tab-separated (TSV)
tsv_path = temp_path("_temp_data.tsv")
with open(tsv_path, "w", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(["name", "score", "grade"])
    writer.writerow(["Alice", 92, "A"])
    writer.writerow(["Bob", 78, "B"])

print("Tab-separated file contents:")
with open(tsv_path) as f:
    print(f.read())

# Pipe-separated
pipe_path = temp_path("_temp_data.psv")
with open(pipe_path, "w", newline="") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["name", "score", "grade"])
    writer.writerow(["Alice", 92, "A"])
    writer.writerow(["Bob", 78, "B"])

print("Pipe-separated file contents:")
with open(pipe_path) as f:
    print(f.read())

# Reading them back — just pass the same delimiter
print("Reading the TSV back:")
with open(tsv_path, newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(f"  {row}")

print()

# -----------------------------------------------------------------------------
# 7. Quoting options
# -----------------------------------------------------------------------------

print("=" * 60)
print("7. Quoting options")
print("=" * 60)

# A row with a tricky value (contains a comma)
sample_row = ["Alice", 30, "New York, NY"]

# QUOTE_MINIMAL (default) — only quotes fields that need it
quote_min_path = temp_path("_temp_quote_minimal.csv")
with open(quote_min_path, "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(sample_row)
with open(quote_min_path) as f:
    print(f"QUOTE_MINIMAL:    {f.read().strip()}")

# QUOTE_ALL — every field gets quoted
quote_all_path = temp_path("_temp_quote_all.csv")
with open(quote_all_path, "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(sample_row)
with open(quote_all_path) as f:
    print(f"QUOTE_ALL:        {f.read().strip()}")

# QUOTE_NONNUMERIC — quotes everything except numbers
quote_nonnum_path = temp_path("_temp_quote_nonnumeric.csv")
with open(quote_nonnum_path, "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(sample_row)
with open(quote_nonnum_path) as f:
    print(f"QUOTE_NONNUMERIC: {f.read().strip()}")

# QUOTE_NONE — never adds quotes (needs escapechar for special chars)
quote_none_path = temp_path("_temp_quote_none.csv")
with open(quote_none_path, "w", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar="\\")
    writer.writerow(sample_row)
with open(quote_none_path) as f:
    print(f"QUOTE_NONE:       {f.read().strip()}")

print()

# -----------------------------------------------------------------------------
# 8. A practical example — read, filter, and write
# -----------------------------------------------------------------------------

print("=" * 60)
print("8. Practical example — read, filter, and write")
print("=" * 60)

# Let's read the scores file, find students who scored above 90 in math,
# and write them to a new file.

honor_roll_path = temp_path("_temp_honor_roll.csv")

with open(scores_path, newline="") as infile, \
     open(honor_roll_path, "w", newline="") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        if int(row["math"]) > 90:
            writer.writerow(row)
            print(f"  {row['student']} made the honor roll (math: {row['math']})")

print()
print("Honor roll CSV:")
with open(honor_roll_path) as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 9. Values with commas and quotes — the csv module handles it
# -----------------------------------------------------------------------------

print("=" * 60)
print("9. Values with commas and quotes — edge cases handled!")
print("=" * 60)

tricky_path = temp_path("_temp_tricky.csv")

# These values would break a naive split-on-comma approach
tricky_rows = [
    ["title", "author", "description"],
    ["The Great Gatsby", "F. Scott Fitzgerald", 'A story about "the American Dream"'],
    ["Moby Dick", "Herman Melville", "A whale tale, literally"],
    ["War, Peace, and Everything", "Leo Tolstoy", "It's long"],
]

with open(tricky_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(tricky_rows)

print("Raw file (notice the quoting):")
with open(tricky_path) as f:
    print(f.read())

print("Parsed correctly by csv.reader:")
with open(tricky_path, newline="") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        print(f"  Title: {row[0]}")
        print(f"  Desc:  {row[2]}")
        print()

# -----------------------------------------------------------------------------
# 10. Cleanup — remove all temp files
# -----------------------------------------------------------------------------

print("=" * 60)
print("10. Cleaning up temp files")
print("=" * 60)

for filepath in TEMP_FILES:
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"  Removed: {os.path.basename(filepath)}")

print()
print("=" * 60)
print("  CSV FILES EXAMPLE COMPLETE!")
print("=" * 60)
print()
print("You've seen csv.reader, csv.writer, DictReader, DictWriter,")
print("different delimiters, quoting options, and edge case handling.")
print("Try modifying this file and running it again!")
