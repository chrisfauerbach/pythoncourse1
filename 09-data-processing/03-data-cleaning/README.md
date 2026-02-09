# Data Cleaning

## Objective

Learn how to take messy, real-world data and whip it into shape using pandas. By the end of this lesson, you'll have a complete toolkit for detecting and fixing the most common data quality problems.

## Concepts Covered

- Why data cleaning matters
- Detecting and handling missing values
- Removing duplicate records
- Converting data types
- Cleaning strings (whitespace, case, formatting)
- Renaming columns
- Detecting and handling outliers
- Applying custom transformations
- Building a complete cleaning workflow

## Prerequisites

- DataFrames basics (creating, indexing, selecting)
- Basic pandas operations
- Python string methods
- `pip install pandas` (the exercises require it)

## Lesson

### Why Data Cleaning Matters

Here's the truth about data in the real world: it's a mess. Surveys have typos. Databases have gaps. Spreadsheets have columns where someone typed "N/A" instead of leaving it blank, or "yes", "Yes", "YES", and "y" all mean the same thing.

Data scientists spend a huge chunk of their time — some estimates say 60-80% — just cleaning data before they can do anything useful with it. If your data is garbage, your analysis will be garbage too. No fancy model can save you from bad inputs.

The good news? Pandas makes data cleaning surprisingly painless once you know the patterns.

### Common Data Quality Issues

Before you can fix problems, you need to know what to look for:

| Problem | Example |
|---|---|
| **Missing values** | Empty cells, `NaN`, `None`, "N/A" |
| **Duplicates** | Same record entered twice |
| **Wrong types** | Numbers stored as strings (`"42"` instead of `42`) |
| **Inconsistent formatting** | `"New York"`, `"new york"`, `"NEW YORK"`, `" New York "` |
| **Outliers** | Age of 999, salary of -50000 |
| **Invalid data** | Email without `@`, date of `2025-13-45` |

Let's tackle each one.

---

### Handling Missing Data

Missing data is the most common problem you'll encounter. Pandas represents missing values as `NaN` (Not a Number) for numeric data and `None` or `NaN` for other types.

#### Detecting Missing Values

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Alice", "Bob", None, "Diana"],
    "age": [25, np.nan, 30, 35],
    "city": ["NYC", "LA", "NYC", None]
})

# Which values are missing?
print(df.isna())         # True where values are missing
print(df.notna())        # True where values are present

# Count missing values per column
print(df.isna().sum())

# What percentage of each column is missing?
print(df.isna().mean() * 100)
```

#### Dropping Missing Values

Sometimes the simplest approach is to just remove rows with missing data:

```python
# Drop any row that has at least one missing value
df.dropna()

# Drop rows only if ALL values are missing
df.dropna(how="all")

# Drop rows missing values in specific columns only
df.dropna(subset=["name", "age"])

# Require at least 2 non-null values per row
df.dropna(thresh=2)
```

**Be careful** — dropping rows means losing data. If 40% of your rows have missing values, you don't want to throw away nearly half your dataset.

#### Filling Missing Values

Often it's better to fill in the blanks with something reasonable:

```python
# Fill with a specific value
df["age"].fillna(0)
df["city"].fillna("Unknown")

# Fill with the column's mean, median, or mode
df["age"].fillna(df["age"].mean())
df["age"].fillna(df["age"].median())
df["city"].fillna(df["city"].mode()[0])

# Forward fill — use the previous row's value
df["city"].ffill()

# Backward fill — use the next row's value
df["city"].bfill()

# Interpolate — estimate based on surrounding values (great for time series)
df["age"].interpolate()
```

The right strategy depends on your data. Mean/median works for numeric data, mode for categories, and forward/backward fill for time-ordered data.

---

### Removing Duplicates

Duplicate records can skew your analysis. Maybe a form was submitted twice, or a merge went wrong.

```python
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "email": ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@y.com"]
})

# Which rows are duplicates? (first occurrence is NOT marked as duplicate)
print(df.duplicated())

# Check for duplicates in specific columns only
print(df.duplicated(subset=["name"]))

# Count total duplicates
print(df.duplicated().sum())

# Drop duplicates — keeps the first occurrence by default
df.drop_duplicates()

# Keep the last occurrence instead
df.drop_duplicates(keep="last")

# Check duplicates based on specific columns
df.drop_duplicates(subset=["name"])
```

---

### Data Type Conversion

Data often arrives with the wrong types. A column of numbers might be stored as strings because one entry was "N/A". Dates might be plain text.

```python
df = pd.DataFrame({
    "price": ["10.50", "20.00", "15.75"],
    "quantity": ["3", "5", "2"],
    "date": ["2025-01-15", "2025-02-20", "2025-03-10"]
})

print(df.dtypes)  # Everything is 'object' (string)

# Convert with .astype()
df["quantity"] = df["quantity"].astype(int)
df["price"] = df["price"].astype(float)

# pd.to_numeric() is safer — handles errors gracefully
df["price"] = pd.to_numeric(df["price"], errors="coerce")  # bad values become NaN

# pd.to_datetime() for date strings
df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)  # Now they're the right types!
```

The `errors="coerce"` parameter is your friend. Instead of crashing on a bad value like `"N/A"`, it quietly converts it to `NaN` so you can deal with it later.

---

### String Cleaning

Messy strings are everywhere. Extra spaces, mixed capitalization, typos — it all needs to go.

Pandas gives you the `.str` accessor that lets you run string methods on entire columns at once:

```python
df = pd.DataFrame({
    "name": ["  Alice  ", "BOB", "charlie", " Diana Jones "],
    "city": ["new york", "Los Angeles", "NEW YORK", "los angeles"],
    "phone": ["555-1234", "555.5678", "555 9012", "555-3456"]
})

# Strip leading/trailing whitespace
df["name"] = df["name"].str.strip()

# Standardize case
df["name"] = df["name"].str.title()       # "Alice", "Bob", "Charlie"
df["city"] = df["city"].str.lower()        # all lowercase
df["city"] = df["city"].str.title()        # "New York", "Los Angeles"

# Replace characters
df["phone"] = df["phone"].str.replace(".", "-", regex=False)
df["phone"] = df["phone"].str.replace(" ", "-")

# Check if a string contains a pattern
mask = df["city"].str.contains("york", case=False)

# Extract parts of strings with regex
df["area_code"] = df["phone"].str.extract(r"(\d{3})")
```

---

### Renaming Columns

Column names from spreadsheets or databases are often ugly — spaces, mixed case, special characters. Clean them up:

```python
df = pd.DataFrame({
    "First Name": [1], "Last Name": [2], "Email Address": [3]
})

# Rename specific columns
df = df.rename(columns={
    "First Name": "first_name",
    "Last Name": "last_name",
    "Email Address": "email"
})

# Or clean all column names at once
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Remove special characters from column names
df.columns = df.columns.str.replace(r"[^a-z0-9_]", "", regex=True)
```

A good convention is `snake_case` — all lowercase with underscores. It plays nicely with Python attribute access (`df.first_name` instead of `df["First Name"]`).

---

### Handling Outliers

Outliers are values that are way outside the normal range. They can be legitimate (a CEO's salary in an employee dataset) or errors (someone typed 999 for age). Either way, you need to decide what to do with them.

#### IQR Method (Interquartile Range)

The classic statistical approach — values beyond 1.5x the IQR from the quartiles are flagged as outliers:

```python
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = df[(df["salary"] < lower_bound) | (df["salary"] > upper_bound)]

# Remove outliers
df_clean = df[(df["salary"] >= lower_bound) & (df["salary"] <= upper_bound)]
```

#### Z-Score Method

Flag values more than 2-3 standard deviations from the mean:

```python
mean = df["salary"].mean()
std = df["salary"].std()

# Values with z-score > 3 are outliers
z_scores = (df["salary"] - mean) / std
df_clean = df[z_scores.abs() <= 3]
```

#### Clipping

Instead of removing outliers, you can cap them at a boundary:

```python
# Cap values at the 5th and 95th percentiles
lower = df["salary"].quantile(0.05)
upper = df["salary"].quantile(0.95)
df["salary"] = df["salary"].clip(lower=lower, upper=upper)
```

---

### Applying Custom Transformations

Sometimes you need cleaning logic that's specific to your data. That's where `.apply()` and `.map()` come in.

```python
# .apply() runs a function on every value in a column (or every row)
df["name"] = df["name"].apply(lambda x: x.strip().title() if isinstance(x, str) else x)

# Use a regular function for more complex logic
def clean_phone(phone):
    if pd.isna(phone):
        return phone
    digits = "".join(c for c in str(phone) if c.isdigit())
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone

df["phone"] = df["phone"].apply(clean_phone)

# .map() is great for replacing values using a dictionary
status_map = {"Y": "Active", "N": "Inactive", "y": "Active", "n": "Inactive"}
df["status"] = df["status"].map(status_map)

# .replace() works similarly but keeps values that don't match
df["status"] = df["status"].replace({"Y": "Active", "N": "Inactive"})
```

---

### Validating Cleaned Data

After cleaning, always check your work. Trust, but verify:

```python
# Check for remaining missing values
print(df.isna().sum())

# Check data types
print(df.dtypes)

# Check for duplicates
print(f"Duplicates remaining: {df.duplicated().sum()}")

# Look at basic stats — do the numbers make sense?
print(df.describe())

# Check unique values in categorical columns
print(df["status"].value_counts())

# Verify value ranges
assert df["age"].between(0, 120).all(), "Age values out of range!"
```

---

### A Complete Cleaning Workflow

Here's how it all comes together in practice:

```python
import pandas as pd

# Step 1: Load and inspect
df = pd.read_csv("messy_data.csv")
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df.describe())

# Step 2: Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Step 3: Remove duplicates
df = df.drop_duplicates()

# Step 4: Fix data types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Step 5: Handle missing values
df["name"] = df["name"].fillna("Unknown")
df["amount"] = df["amount"].fillna(df["amount"].median())
df = df.dropna(subset=["date"])  # drop rows where date is essential

# Step 6: Clean strings
df["name"] = df["name"].str.strip().str.title()
df["city"] = df["city"].str.strip().str.title()

# Step 7: Handle outliers
Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)
IQR = Q3 - Q1
df = df[df["amount"].between(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)]

# Step 8: Validate
print(f"Final shape: {df.shape}")
print(f"Missing values:\n{df.isna().sum()}")
print(f"Duplicates: {df.duplicated().sum()}")
```

---

## Code Example

Check out [`example.py`](example.py) for a complete working example that creates a messy dataset and cleans it step by step.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your data cleaning skills.

## Key Takeaways

- Real-world data is always messy — cleaning it is a core skill, not a chore to skip
- Use `.isna()` and `.notna()` to detect missing values, then decide whether to drop or fill them
- `.drop_duplicates()` removes duplicate rows; use `subset` to check specific columns
- `pd.to_numeric()` and `pd.to_datetime()` with `errors="coerce"` safely convert types
- The `.str` accessor gives you vectorized string operations — `.strip()`, `.lower()`, `.replace()`
- Handle outliers with IQR, z-scores, or `.clip()` depending on the situation
- `.apply()` lets you run any custom function across a column
- Always validate after cleaning — check types, missing values, ranges, and duplicates
- Build a consistent workflow: inspect, clean columns, deduplicate, fix types, fill gaps, clean strings, handle outliers, validate
