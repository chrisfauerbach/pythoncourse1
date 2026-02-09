"""
Pandas Basics — Example Code
==============================

Run this file:
    python3 example.py

A hands-on tour of Pandas fundamentals. We'll create DataFrames from scratch
(no external files needed) and walk through every major feature: viewing data,
selecting, filtering, sorting, grouping, and handling missing values.
"""

import sys

try:
    import pandas as pd
except ImportError:
    print("Pandas is not installed. Run: pip install pandas")
    sys.exit(0)

# -----------------------------------------------------------------------------
# 1. Series — a 1D labeled array
# -----------------------------------------------------------------------------

print("=" * 60)
print("1. SERIES")
print("=" * 60)

# A Series is like a list with labels
temperatures = pd.Series([72, 68, 75, 80, 65], index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print("Daily temperatures:")
print(temperatures)
print()

# You can access values by label or compute stats instantly
print(f"Wednesday: {temperatures['Wed']}")
print(f"Average:   {temperatures.mean()}")
print(f"Highest:   {temperatures.max()}")
print()

# -----------------------------------------------------------------------------
# 2. Creating DataFrames — from a dictionary
# -----------------------------------------------------------------------------

print("=" * 60)
print("2. CREATING DATAFRAMES — FROM A DICT")
print("=" * 60)

# Each key becomes a column, each value is a list of row values
employees = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "department": ["Engineering", "Marketing", "Engineering", "Marketing", "Engineering", "HR"],
    "salary": [95000, 65000, 102000, 70000, 88000, 72000],
    "years": [5, 3, 8, 4, 2, 6]
})

print(employees)
print()

# -----------------------------------------------------------------------------
# 3. Creating DataFrames — from a list of dicts
# -----------------------------------------------------------------------------

print("=" * 60)
print("3. CREATING DATAFRAMES — FROM A LIST OF DICTS")
print("=" * 60)

# Each dict is a row — handy when building data one record at a time
products = pd.DataFrame([
    {"product": "Laptop", "price": 999.99, "stock": 50},
    {"product": "Mouse", "price": 29.99, "stock": 200},
    {"product": "Keyboard", "price": 79.99, "stock": 150},
    {"product": "Monitor", "price": 349.99, "stock": 75},
    {"product": "Webcam", "price": 69.99, "stock": 120},
])

print(products)
print()

# -----------------------------------------------------------------------------
# 4. Viewing data — your first look at a dataset
# -----------------------------------------------------------------------------

print("=" * 60)
print("4. VIEWING DATA")
print("=" * 60)

# .head() and .tail() — peek at the beginning and end
print("--- head(3) ---")
print(employees.head(3))
print()

print("--- tail(2) ---")
print(employees.tail(2))
print()

# .shape — how many rows and columns?
print(f"Shape: {employees.shape}  (rows, columns)")
print()

# .info() — column names, types, and non-null counts
print("--- info() ---")
employees.info()
print()

# .describe() — quick statistics for numeric columns
print("--- describe() ---")
print(employees.describe())
print()

# .columns and .dtypes — what columns do we have?
print(f"Columns: {list(employees.columns)}")
print(f"Types:\n{employees.dtypes}")
print()

# -----------------------------------------------------------------------------
# 5. Selecting data — columns and rows
# -----------------------------------------------------------------------------

print("=" * 60)
print("5. SELECTING DATA")
print("=" * 60)

# Select a single column (returns a Series)
print("--- Single column: employees['name'] ---")
print(employees["name"])
print()

# Select multiple columns (returns a DataFrame)
print("--- Multiple columns: employees[['name', 'salary']] ---")
print(employees[["name", "salary"]])
print()

# .loc[] — select by label (index label and column name)
print("--- .loc[0] — row with index label 0 ---")
print(employees.loc[0])
print()

print("--- .loc[1:3] — rows with labels 1, 2, and 3 (inclusive!) ---")
print(employees.loc[1:3])
print()

print("--- .loc[0, 'name'] — specific cell ---")
print(employees.loc[0, "name"])
print()

# .iloc[] — select by integer position
print("--- .iloc[0:2] — first two rows (exclusive end, like normal slicing) ---")
print(employees.iloc[0:2])
print()

print("--- .iloc[0, 2] — first row, third column ---")
print(employees.iloc[0, 2])
print()

# -----------------------------------------------------------------------------
# 6. Filtering rows — the really powerful stuff
# -----------------------------------------------------------------------------

print("=" * 60)
print("6. FILTERING ROWS")
print("=" * 60)

# Single condition — who earns more than 80,000?
high_earners = employees[employees["salary"] > 80000]
print("--- Salary > 80,000 ---")
print(high_earners)
print()

# Multiple conditions — engineers with 5+ years
senior_engineers = employees[
    (employees["department"] == "Engineering") & (employees["years"] >= 5)
]
print("--- Engineers with 5+ years ---")
print(senior_engineers)
print()

# .isin() — filter to specific values
marketing_hr = employees[employees["department"].isin(["Marketing", "HR"])]
print("--- Marketing or HR ---")
print(marketing_hr)
print()

# -----------------------------------------------------------------------------
# 7. Adding and removing columns
# -----------------------------------------------------------------------------

print("=" * 60)
print("7. ADDING AND REMOVING COLUMNS")
print("=" * 60)

# Add a computed column — monthly salary
employees["monthly_salary"] = (employees["salary"] / 12).round(2)
print("--- Added 'monthly_salary' column ---")
print(employees[["name", "salary", "monthly_salary"]])
print()

# Add a boolean column — is this person a senior employee?
employees["is_senior"] = employees["years"] >= 5
print("--- Added 'is_senior' column ---")
print(employees[["name", "years", "is_senior"]])
print()

# Remove columns with .drop()
employees = employees.drop(columns=["monthly_salary", "is_senior"])
print("--- Dropped 'monthly_salary' and 'is_senior' ---")
print(f"Columns now: {list(employees.columns)}")
print()

# -----------------------------------------------------------------------------
# 8. Sorting
# -----------------------------------------------------------------------------

print("=" * 60)
print("8. SORTING")
print("=" * 60)

# Sort by salary (ascending)
print("--- Sorted by salary (ascending) ---")
print(employees.sort_values("salary"))
print()

# Sort by salary (descending)
print("--- Sorted by salary (descending) ---")
print(employees.sort_values("salary", ascending=False))
print()

# Sort by multiple columns — department first, then salary within each department
print("--- Sorted by department, then salary (descending) ---")
print(employees.sort_values(["department", "salary"], ascending=[True, False]))
print()

# -----------------------------------------------------------------------------
# 9. Grouping and aggregation — summarize your data
# -----------------------------------------------------------------------------

print("=" * 60)
print("9. GROUPING AND AGGREGATION")
print("=" * 60)

# Average salary by department
print("--- Average salary by department ---")
print(employees.groupby("department")["salary"].mean())
print()

# Multiple aggregations at once
print("--- Department summary (mean, count, max salary) ---")
dept_summary = employees.groupby("department")["salary"].agg(["mean", "count", "max"])
print(dept_summary)
print()

# Total years of experience per department
print("--- Total years by department ---")
print(employees.groupby("department")["years"].sum())
print()

# -----------------------------------------------------------------------------
# 10. Handling missing data
# -----------------------------------------------------------------------------

print("=" * 60)
print("10. HANDLING MISSING DATA")
print("=" * 60)

# Let's create a DataFrame with some missing values
survey = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [30, None, 35, 28, None],
    "score": [85, 92, None, 78, 95],
    "city": ["NYC", "LA", None, "NYC", "Chicago"]
})

print("--- Survey data (with missing values) ---")
print(survey)
print()

# Check what's missing
print("--- Missing values per column ---")
print(survey.isna().sum())
print()

# Fill missing ages with the mean
filled = survey.copy()
filled["age"] = filled["age"].fillna(filled["age"].mean())
print("--- After filling missing ages with mean ---")
print(filled)
print()

# Drop rows that have ANY missing value
print("--- After dropna() — only complete rows ---")
print(survey.dropna())
print()

# Drop rows only if 'score' is missing
print("--- After dropna(subset=['score']) ---")
print(survey.dropna(subset=["score"]))
print()

# -----------------------------------------------------------------------------
# 11. Reading/writing CSV (demonstration)
# -----------------------------------------------------------------------------

print("=" * 60)
print("11. READING/WRITING CSV")
print("=" * 60)

# Write a DataFrame to CSV
import tempfile
import os

csv_path = os.path.join(tempfile.gettempdir(), "employees_demo.csv")
employees.to_csv(csv_path, index=False)
print(f"Wrote employees to: {csv_path}")

# Read it back
df_from_csv = pd.read_csv(csv_path)
print("Read it back:")
print(df_from_csv)
print()

# Clean up the temp file
os.remove(csv_path)
print(f"Cleaned up temp file.")
print()

# -----------------------------------------------------------------------------
# 12. Putting it all together — a mini analysis
# -----------------------------------------------------------------------------

print("=" * 60)
print("12. PUTTING IT ALL TOGETHER")
print("=" * 60)

# Let's answer some questions about our employee data
print("Dataset:")
print(employees)
print()

# Who is the highest paid employee?
top_earner = employees.loc[employees["salary"].idxmax()]
print(f"Highest paid: {top_earner['name']} (${top_earner['salary']:,})")

# What's the average salary?
print(f"Average salary: ${employees['salary'].mean():,.2f}")

# Which department has the highest average salary?
dept_avg = employees.groupby("department")["salary"].mean()
top_dept = dept_avg.idxmax()
print(f"Highest-paying department: {top_dept} (avg ${dept_avg[top_dept]:,.2f})")

# How many employees per department?
print(f"\nHeadcount by department:")
print(employees["department"].value_counts())

print()
print("=" * 60)
print("That's Pandas basics! Check out exercises.py to practice.")
print("=" * 60)
