# Pandas Basics

## Objective

Learn how to work with structured data using Pandas — the most important Python library for data analysis. By the end of this lesson, you'll be able to create, explore, filter, sort, group, and summarize tabular data like a pro.

## Concepts Covered

- What Pandas is and why it matters
- Series and DataFrame — the two core data structures
- Creating DataFrames from dicts, lists, and CSV files
- Viewing and exploring data
- Selecting, filtering, and sorting data
- Adding and removing columns
- Grouping and aggregation
- Handling missing data
- Reading and writing CSV files

## Prerequisites

- Python fundamentals (variables, lists, dicts, loops)
- Basic familiarity with NumPy is helpful but not required

## Lesson

### What Is Pandas?

Pandas is a Python library that gives you powerful, easy-to-use data structures for working with structured (tabular) data — think spreadsheets, database tables, or CSV files. If you're doing any kind of data analysis, data cleaning, or data science in Python, Pandas is the tool you'll reach for first.

Install it with pip:

```bash
pip install pandas
```

The convention is to import it as `pd`:

```python
import pandas as pd
```

### Series — 1D Labeled Array

A **Series** is like a list, but with labels (an index). Think of it as a single column in a spreadsheet:

```python
import pandas as pd

temperatures = pd.Series([72, 68, 75, 80], index=["Mon", "Tue", "Wed", "Thu"])
print(temperatures)
# Mon    72
# Tue    68
# Wed    75
# Thu    80

print(temperatures["Wed"])  # 75
print(temperatures.mean())  # 73.75
```

Series are useful on their own, but they really shine as the building blocks of DataFrames.

### DataFrame — The Star of the Show

A **DataFrame** is a 2D labeled data structure — basically a table with rows and columns. Each column is a Series. This is where you'll spend 90% of your time with Pandas.

```python
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 35],
    "city": ["NYC", "LA", "Chicago"]
}

df = pd.DataFrame(data)
print(df)
#       name  age     city
# 0    Alice   30      NYC
# 1      Bob   25       LA
# 2  Charlie   35  Chicago
```

### Creating DataFrames

There are several ways to create a DataFrame. Here are the most common:

**From a dictionary** (columns as keys):

```python
df = pd.DataFrame({
    "product": ["Widget", "Gadget", "Doohickey"],
    "price": [9.99, 24.99, 4.99],
    "stock": [100, 50, 200]
})
```

**From a list of dictionaries** (rows as dicts):

```python
df = pd.DataFrame([
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 87},
    {"name": "Charlie", "score": 92}
])
```

**From a CSV file**:

```python
df = pd.read_csv("sales_data.csv")
```

### Viewing Data

Once you have a DataFrame, the first thing you'll want to do is look at it. Pandas gives you several handy methods:

```python
df.head()        # First 5 rows (or df.head(3) for first 3)
df.tail()        # Last 5 rows
df.shape         # (num_rows, num_columns) — it's a property, not a method
df.info()        # Column names, types, non-null counts
df.describe()    # Statistics for numeric columns (mean, std, min, max, etc.)
df.columns       # List of column names
df.dtypes        # Data type of each column
```

These are your go-to tools for understanding a dataset you've never seen before.

### Selecting Data

**Select a single column** (returns a Series):

```python
df["name"]           # Bracket notation — always works
df.name              # Dot notation — works if column name has no spaces
```

**Select multiple columns** (returns a DataFrame):

```python
df[["name", "age"]]  # Pass a list of column names
```

**Select rows by label with `.loc[]`**:

```python
df.loc[0]              # Row with index label 0
df.loc[0:2]            # Rows with labels 0, 1, and 2 (inclusive!)
df.loc[0, "name"]      # Specific cell: row 0, column "name"
df.loc[:, "name"]      # All rows, just the "name" column
```

**Select rows by position with `.iloc[]`**:

```python
df.iloc[0]             # First row (position 0)
df.iloc[0:2]           # First two rows (exclusive end — like regular slicing)
df.iloc[0, 1]          # First row, second column
```

The key difference: `.loc[]` uses labels (inclusive end), `.iloc[]` uses integer positions (exclusive end, like normal Python slicing).

### Filtering Rows

This is one of the most useful things in Pandas. You filter rows using boolean conditions:

```python
# Find all rows where age is greater than 30
df[df["age"] > 30]

# Multiple conditions — use & (and), | (or), ~ (not)
# IMPORTANT: wrap each condition in parentheses
df[(df["age"] > 25) & (df["city"] == "NYC")]

# Filter using .isin() for multiple values
df[df["city"].isin(["NYC", "LA"])]
```

### Adding and Removing Columns

**Add a new column** — just assign to it:

```python
df["senior"] = df["age"] >= 30          # Boolean column
df["birth_year"] = 2026 - df["age"]     # Computed column
```

**Remove a column** with `.drop()`:

```python
df = df.drop(columns=["birth_year"])            # Drop one column
df = df.drop(columns=["senior", "birth_year"])  # Drop multiple
```

### Sorting

**Sort by column values**:

```python
df.sort_values("age")                         # Ascending (default)
df.sort_values("age", ascending=False)        # Descending
df.sort_values(["city", "age"])               # Sort by multiple columns
```

**Sort by index**:

```python
df.sort_index()                               # Sort rows by their index
```

### Grouping and Aggregation

`.groupby()` is how you split data into groups and calculate summaries — like a pivot table in Excel:

```python
# Average age by city
df.groupby("city")["age"].mean()

# Multiple aggregations
df.groupby("city")["age"].agg(["mean", "count", "max"])

# Group by multiple columns
df.groupby(["city", "department"])["salary"].sum()
```

Common aggregation functions: `.sum()`, `.mean()`, `.count()`, `.min()`, `.max()`, `.median()`, `.std()`.

### Handling Missing Data

Real-world data is messy. Pandas uses `NaN` (Not a Number) to represent missing values:

```python
# Check for missing values
df.isna()              # Boolean DataFrame — True where values are missing
df.isna().sum()        # Count of missing values per column

# Fill missing values
df["age"].fillna(0)                # Replace NaN with 0
df["age"].fillna(df["age"].mean()) # Replace NaN with the column mean

# Drop rows with missing values
df.dropna()                        # Drop any row that has a NaN
df.dropna(subset=["age"])          # Only drop if "age" is NaN
```

### Reading and Writing CSV

CSV (Comma-Separated Values) is the most common file format for tabular data:

```python
# Reading
df = pd.read_csv("data.csv")
df = pd.read_csv("data.csv", index_col=0)              # Use first column as index
df = pd.read_csv("data.csv", usecols=["name", "age"])  # Only load specific columns

# Writing
df.to_csv("output.csv")
df.to_csv("output.csv", index=False)   # Don't write the index column
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Pandas is the go-to library for working with tabular data in Python
- A **Series** is a 1D labeled array; a **DataFrame** is a 2D table (collection of Series)
- Use `.head()`, `.info()`, `.describe()`, and `.shape` to explore data quickly
- Use `.loc[]` for label-based selection and `.iloc[]` for position-based selection
- Filter rows with boolean conditions: `df[df["col"] > value]`
- `.groupby()` lets you split, aggregate, and summarize data in powerful ways
- Handle missing data with `.isna()`, `.fillna()`, and `.dropna()`
- `pd.read_csv()` and `.to_csv()` are how you get data in and out of DataFrames
