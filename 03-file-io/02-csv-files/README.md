# CSV Files

## Objective

Learn how to read, write, and manipulate CSV files using Python's built-in `csv` module. CSV is one of the most common data formats you'll encounter, and Python makes it painless to work with.

## Concepts Covered

- What CSV files are and why they're everywhere
- The `csv` module -- `csv.reader()` and `csv.writer()`
- Reading CSV files row by row
- Writing CSV files
- `csv.DictReader` -- reading rows as dictionaries
- `csv.DictWriter` -- writing from dictionaries
- Handling different delimiters (TSV, pipe-separated, etc.)
- Quoting options (`csv.QUOTE_ALL`, `csv.QUOTE_MINIMAL`, etc.)
- Common gotchas (newline, encoding, etc.)

## Prerequisites

- Reading and writing text files (`open()`, `with` statements)
- Basic data structures (lists, dictionaries)
- Loops and string formatting

## Lesson

### What CSV Files Are (and Why They're Everywhere)

CSV stands for **Comma-Separated Values**. It's a plain text format where each line is a row of data, and values within a row are separated by commas:

```
name,age,city
Alice,30,New York
Bob,25,Chicago
Charlie,35,Houston
```

That's it -- no fancy formatting, no binary encoding, just text. This simplicity is exactly why CSV is everywhere:

- Spreadsheet apps (Excel, Google Sheets) export and import CSV
- Databases can dump tables as CSV
- APIs and data feeds often use CSV for bulk data
- It's human-readable -- you can open it in any text editor

You *could* read CSV files by splitting strings on commas, but that breaks the moment a value contains a comma (`"New York, NY"`). That's why Python gives us the `csv` module.

### The csv Module

The `csv` module is part of Python's standard library -- no installation needed:

```python
import csv
```

It handles all the messy edge cases: quoted fields, commas inside values, different line endings, and more.

### Reading CSV Files with csv.reader()

`csv.reader()` takes a file object and returns an iterator. Each iteration gives you one row as a list of strings:

```python
import csv

with open("people.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Output:

```
['name', 'age', 'city']
['Alice', '30', 'New York']
['Bob', '25', 'Chicago']
```

Notice that **everything comes back as strings** -- even numbers. You'll need to convert them yourself with `int()` or `float()`.

The first row is usually the header. A common pattern is to grab it separately:

```python
with open("people.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)       # Grab the first row
    for row in reader:          # Loop over the remaining data rows
        name, age, city = row
        print(f"{name} is {age} years old")
```

### Writing CSV Files with csv.writer()

`csv.writer()` wraps a file object and gives you `.writerow()` and `.writerows()`:

```python
import csv

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "city"])         # Write one row
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Chicago"])
```

Or write everything at once with `.writerows()`:

```python
rows = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Chicago"],
]

with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

### csv.DictReader -- Rows as Dictionaries

`csv.DictReader` is the more Pythonic way to read CSV files. It uses the header row as dictionary keys, so you can access values by column name instead of index:

```python
import csv

with open("people.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} lives in {row['city']}")
```

Each `row` is a dictionary like `{'name': 'Alice', 'age': '30', 'city': 'New York'}`. This is much more readable than `row[0]`, `row[1]`, etc. -- especially when your CSV has 20 columns.

### csv.DictWriter -- Writing from Dictionaries

`csv.DictWriter` is the writing counterpart. You pass it a list of field names, then write dictionaries:

```python
import csv

fieldnames = ["name", "age", "city"]

with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()                                # Writes the header row
    writer.writerow({"name": "Alice", "age": 30, "city": "New York"})
    writer.writerow({"name": "Bob", "age": 25, "city": "Chicago"})
```

### Handling Different Delimiters

Not all "CSV" files use commas. Tab-separated (TSV), pipe-separated, and semicolon-separated files are all common. Just use the `delimiter` parameter:

```python
# Reading a tab-separated file
with open("data.tsv", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Writing a pipe-separated file
with open("data.psv", "w", newline="") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["name", "age", "city"])
```

### Quoting Options

The `csv` module has several quoting modes that control when values get wrapped in quotes:

- **`csv.QUOTE_MINIMAL`** (default) -- only quote fields that contain the delimiter, a quote character, or a newline
- **`csv.QUOTE_ALL`** -- quote every field, always
- **`csv.QUOTE_NONNUMERIC`** -- quote everything except numbers; when reading, converts unquoted fields to floats
- **`csv.QUOTE_NONE`** -- never quote anything (use `escapechar` to handle special characters)

```python
import csv

row = ["Alice", 30, "New York, NY"]

# QUOTE_MINIMAL (default) — only "New York, NY" gets quoted
writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)

# QUOTE_ALL — every field gets quoted: "Alice","30","New York, NY"
writer = csv.writer(f, quoting=csv.QUOTE_ALL)
```

### Common Gotchas

**1. Always use `newline=""` when opening CSV files.**

```python
# Correct
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)

# Wrong -- may produce blank lines between rows on Windows
with open("data.csv", "w") as f:
    writer = csv.writer(f)
```

The `csv` module handles line endings itself. If you don't pass `newline=""`, Python's default newline translation can add extra blank lines on Windows.

**2. Everything is a string when reading.**

`csv.reader()` and `csv.DictReader` always return strings. If you need numbers, convert them:

```python
age = int(row["age"])
price = float(row["price"])
```

**3. Watch your encoding.**

Most CSV files are UTF-8, but you'll occasionally run into files with different encodings (especially from older Windows software):

```python
# Explicitly specify encoding
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

# For old Windows files, try:
with open("data.csv", newline="", encoding="latin-1") as f:
    reader = csv.reader(f)
```

**4. Don't forget headers with DictWriter.**

`csv.DictWriter` won't write a header row automatically -- you need to call `writer.writeheader()` explicitly.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- CSV is a simple text format where commas separate values -- Python's `csv` module handles the tricky edge cases for you
- `csv.reader()` and `csv.writer()` work with lists of values (rows as lists)
- `csv.DictReader` and `csv.DictWriter` work with dictionaries (rows as dicts) -- usually more readable
- Always open CSV files with `newline=""` to avoid blank-line issues
- Use the `delimiter` parameter for TSV, pipe-separated, or other non-comma formats
- Everything comes back as strings -- convert to `int()` or `float()` when you need numbers
- Quoting options let you control how special characters are handled in the output
