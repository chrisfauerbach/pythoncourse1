"""
Data Cleaning — Exercises
==========================

Practice problems to test your data cleaning skills.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("This lesson requires pandas and numpy.")
    print("Install them with:  pip install pandas numpy")
    print()
    print("If you're using a virtual environment, make sure it's activated first.")
    exit(0)


# =============================================================================
# Exercise 1: Detect and handle missing values
#
# The dataset below has missing values scattered around.
# Your tasks:
#   1. Print how many missing values are in each column
#   2. Fill missing ages with the median age
#   3. Fill missing cities with "Unknown"
#   4. Drop any rows where name is still missing
#   5. Print the cleaned DataFrame
#
# =============================================================================

def exercise_1():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", None, "Diana", "Eve", None, "Grace"],
        "age": [25, np.nan, 30, np.nan, 22, 45, np.nan],
        "city": ["NYC", "LA", None, "Chicago", None, "NYC", "LA"],
        "score": [88.5, 92.0, np.nan, 76.0, np.nan, 91.0, 85.0]
    })
    print("Original:")
    print(df)
    print()

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Find and remove duplicate records
#
# This dataset has some duplicate entries. Your tasks:
#   1. Print how many duplicate rows exist
#   2. Print which rows are duplicates (show all rows involved)
#   3. Remove duplicates, keeping the first occurrence
#   4. Also check: how many rows are duplicated by just the "email" column?
#   5. Print the cleaned DataFrame
#
# =============================================================================

def exercise_2():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Alice", "Diana", "Bob", "Eve"],
        "email": ["alice@test.com", "bob@test.com", "charlie@test.com",
                  "alice@test.com", "diana@test.com", "bob@test.com", "eve@test.com"],
        "signup_date": ["2025-01-01", "2025-01-05", "2025-01-10",
                        "2025-01-01", "2025-01-15", "2025-01-05", "2025-01-20"],
        "plan": ["Pro", "Basic", "Pro", "Pro", "Basic", "Basic", "Pro"]
    })
    print("Original:")
    print(df)
    print()

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Fix inconsistent string formatting
#
# This dataset has all sorts of string messiness — mixed case, extra spaces,
# inconsistent values. Your tasks:
#   1. Strip whitespace from all string columns
#   2. Standardize names to Title Case
#   3. Standardize cities to Title Case
#   4. Standardize department to lowercase
#   5. Print the unique cities and departments after cleaning
#
# =============================================================================

def exercise_3():
    df = pd.DataFrame({
        "name": ["  john smith  ", "JANE DOE", "bob Wilson", "  Sara Connor ",
                 "mike JONES", " Lisa Park"],
        "city": ["new york", "  NEW YORK", "los angeles", "LOS ANGELES  ",
                 "new york  ", "  los angeles"],
        "department": ["Engineering", "ENGINEERING", "  Sales", "sales ",
                       "ENGINEERING", "Sales  "]
    })
    print("Original:")
    print(df)
    print()

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Convert columns to proper types
#
# This dataset has numbers and dates stored as strings, plus some bad values
# mixed in. Your tasks:
#   1. Convert "price" to numeric (handle the "N/A" and "free" gracefully)
#   2. Convert "quantity" to integer (handle bad values)
#   3. Convert "date" to datetime
#   4. Print the dtypes before and after
#   5. Print how many NaN values were created by the conversions
#
# =============================================================================

def exercise_4():
    df = pd.DataFrame({
        "product": ["Widget", "Gadget", "Doohickey", "Thingamajig", "Whatsit"],
        "price": ["9.99", "24.50", "N/A", "free", "14.75"],
        "quantity": ["100", "fifty", "200", "75", "150"],
        "date": ["2025-01-15", "2025-02-20", "Jan 30 2025", "2025-03-10", "not a date"]
    })
    print("Original:")
    print(df)
    print(f"\nOriginal dtypes:\n{df.dtypes}")
    print()

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Clean a messy customer dataset
#
# This is a multi-step challenge. The dataset below has MANY problems.
# Clean it up by:
#   1. Clean column names (lowercase, underscores, no spaces)
#   2. Strip whitespace and standardize names to Title Case
#   3. Standardize emails to lowercase
#   4. Convert "Annual Income" to numeric
#   5. Fill missing incomes with the median
#   6. Standardize the "Member" column to boolean (True/False)
#   7. Remove any duplicate rows
#   8. Print the final clean DataFrame
#
# Hint: The "Member" column has values like "yes", "Yes", "Y", "no", "No", "N"
#
# =============================================================================

def exercise_5():
    df = pd.DataFrame({
        "Customer Name": [
            "  alice SMITH", "Bob Jones  ", "CHARLIE BROWN", "  diana prince  ",
            "Bob Jones  ", "eve wilson", "  alice SMITH"
        ],
        "Email Address": [
            "Alice@Email.COM", "  BOB@test.com", "charlie@test.com  ",
            "DIANA@test.COM", "  BOB@test.com", "Eve@Test.com", "Alice@Email.COM"
        ],
        "Annual Income": [
            "55000", "72000", "N/A", "91000", "72000", "48000", "55000"
        ],
        "Member": ["yes", "No", "Y", "YES", "No", "n", "yes"]
    })
    print("Original:")
    print(df)
    print()

    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Full data cleaning pipeline
#
# Build a complete cleaning pipeline for this messy sales dataset.
# Follow these steps:
#   1. Inspect: print shape, dtypes, missing values, and first few rows
#   2. Clean column names
#   3. Remove duplicates
#   4. Fix data types (amount should be float, date should be datetime)
#   5. Handle missing values (fill or drop, your choice — justify it)
#   6. Clean strings (product names, regions)
#   7. Handle outliers in the amount column (use IQR or clipping)
#   8. Validate: print final shape, dtypes, missing values, and summary stats
#
# This is open-ended — there's no single "right" answer.
# The goal is to practice thinking through each step systematically.
#
# =============================================================================

def exercise_6():
    np.random.seed(42)
    dates = ["2025-01-05", "2025-01-12", "2025-01-20", "2025-02-03",
             "2025-02-14", "Feb 28 2025", "2025-03-01", "2025-03-15",
             "not_a_date", "2025-04-01", "2025-04-10", "2025-01-12",
             "2025-02-14", "2025-05-01", "2025-05-15"]

    df = pd.DataFrame({
        "Product Name": [
            "  Widget A", "widget a", "GADGET B", "  Gadget B  ", "Widget A",
            "Doohickey C", "WIDGET A", "doohickey c", "Gadget B", "Widget A",
            "  DOOHICKEY C  ", "widget a", "Widget A", "Gadget B", "doohickey c"
        ],
        "Region": [
            "North", "NORTH", " north", "South", "south ",
            "  East", "WEST", "North", "South", "east",
            "West ", "NORTH", "south ", "East", "west"
        ],
        "Sale Amount": [
            "150.00", "200", "75.50", "300", "125",
            "50000", "89.99", "-25", "N/A", "175",
            "220", "200", "125", "310", "95"
        ],
        "Sale Date": dates,
        "Salesperson": [
            "Alice", "alice", None, "Bob", "  ALICE  ",
            "Charlie", "alice", "  charlie", "Bob", "Alice",
            "Charlie ", None, "Alice", "bob ", "Charlie"
        ]
    })
    print("=" * 50)
    print("RAW DATA — your job: clean it up!")
    print("=" * 50)
    print(df)
    print()

    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", None, "Diana", "Eve", None, "Grace"],
        "age": [25, np.nan, 30, np.nan, 22, 45, np.nan],
        "city": ["NYC", "LA", None, "Chicago", None, "NYC", "LA"],
        "score": [88.5, 92.0, np.nan, 76.0, np.nan, 91.0, 85.0]
    })

    # 1. Count missing values
    print("Missing values per column:")
    print(df.isna().sum())
    print()

    # 2. Fill missing ages with median
    df["age"] = df["age"].fillna(df["age"].median())

    # 3. Fill missing cities with "Unknown"
    df["city"] = df["city"].fillna("Unknown")

    # 4. Drop rows where name is missing
    df = df.dropna(subset=["name"])

    # 5. Fill remaining missing scores with median too
    df["score"] = df["score"].fillna(df["score"].median())

    print("Cleaned:")
    print(df)
    print(f"\nRemaining missing values:\n{df.isna().sum()}")


def solution_2():
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Alice", "Diana", "Bob", "Eve"],
        "email": ["alice@test.com", "bob@test.com", "charlie@test.com",
                  "alice@test.com", "diana@test.com", "bob@test.com", "eve@test.com"],
        "signup_date": ["2025-01-01", "2025-01-05", "2025-01-10",
                        "2025-01-01", "2025-01-15", "2025-01-05", "2025-01-20"],
        "plan": ["Pro", "Basic", "Pro", "Pro", "Basic", "Basic", "Pro"]
    })

    # 1. Count duplicates
    print(f"Duplicate rows: {df.duplicated().sum()}")

    # 2. Show all rows involved in duplication
    dupes = df[df.duplicated(keep=False)]
    print(f"\nAll rows involved in duplicates:")
    print(dupes)

    # 3. Remove duplicates
    df = df.drop_duplicates()
    print(f"\nAfter removing duplicates: {len(df)} rows")

    # 4. Check duplicates by email only
    email_dupes = df.duplicated(subset=["email"]).sum()
    print(f"Rows with duplicate emails (after dedup): {email_dupes}")

    # 5. Print result
    print(f"\nCleaned:")
    print(df)


def solution_3():
    df = pd.DataFrame({
        "name": ["  john smith  ", "JANE DOE", "bob Wilson", "  Sara Connor ",
                 "mike JONES", " Lisa Park"],
        "city": ["new york", "  NEW YORK", "los angeles", "LOS ANGELES  ",
                 "new york  ", "  los angeles"],
        "department": ["Engineering", "ENGINEERING", "  Sales", "sales ",
                       "ENGINEERING", "Sales  "]
    })

    # 1. Strip whitespace from all string columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # 2. Standardize names to Title Case
    df["name"] = df["name"].str.title()

    # 3. Standardize cities to Title Case
    df["city"] = df["city"].str.title()

    # 4. Standardize department to lowercase
    df["department"] = df["department"].str.lower()

    # 5. Print unique values
    print(f"Unique cities: {sorted(df['city'].unique().tolist())}")
    print(f"Unique departments: {sorted(df['department'].unique().tolist())}")
    print(f"\nCleaned:")
    print(df)


def solution_4():
    df = pd.DataFrame({
        "product": ["Widget", "Gadget", "Doohickey", "Thingamajig", "Whatsit"],
        "price": ["9.99", "24.50", "N/A", "free", "14.75"],
        "quantity": ["100", "fifty", "200", "75", "150"],
        "date": ["2025-01-15", "2025-02-20", "Jan 30 2025", "2025-03-10", "not a date"]
    })

    print(f"Dtypes before:\n{df.dtypes}\n")

    # 1. Convert price to numeric (coerce turns bad values into NaN)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # 2. Convert quantity to numeric first, then to Int64 (nullable integer)
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").astype("Int64")

    # 3. Convert date to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    print(f"Dtypes after:\n{df.dtypes}\n")

    # 4. Count NaN values created
    print(f"NaN values created:")
    print(df.isna().sum())
    print(f"\nResult:")
    print(df)


def solution_5():
    df = pd.DataFrame({
        "Customer Name": [
            "  alice SMITH", "Bob Jones  ", "CHARLIE BROWN", "  diana prince  ",
            "Bob Jones  ", "eve wilson", "  alice SMITH"
        ],
        "Email Address": [
            "Alice@Email.COM", "  BOB@test.com", "charlie@test.com  ",
            "DIANA@test.COM", "  BOB@test.com", "Eve@Test.com", "Alice@Email.COM"
        ],
        "Annual Income": [
            "55000", "72000", "N/A", "91000", "72000", "48000", "55000"
        ],
        "Member": ["yes", "No", "Y", "YES", "No", "n", "yes"]
    })

    # 1. Clean column names
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    # 2. Strip whitespace and standardize names
    df["customer_name"] = df["customer_name"].str.strip().str.title()

    # 3. Standardize emails
    df["email_address"] = df["email_address"].str.strip().str.lower()

    # 4. Convert income to numeric
    df["annual_income"] = pd.to_numeric(df["annual_income"], errors="coerce")

    # 5. Fill missing incomes with median
    df["annual_income"] = df["annual_income"].fillna(df["annual_income"].median())

    # 6. Standardize Member to boolean
    yes_values = {"yes", "y"}
    df["member"] = df["member"].str.strip().str.lower().isin(yes_values)

    # 7. Remove duplicates
    df = df.drop_duplicates()

    # 8. Print result
    print(f"Cleaned ({len(df)} rows):")
    print(df)
    print(f"\nDtypes:\n{df.dtypes}")


def solution_6():
    np.random.seed(42)
    dates = ["2025-01-05", "2025-01-12", "2025-01-20", "2025-02-03",
             "2025-02-14", "Feb 28 2025", "2025-03-01", "2025-03-15",
             "not_a_date", "2025-04-01", "2025-04-10", "2025-01-12",
             "2025-02-14", "2025-05-01", "2025-05-15"]

    df = pd.DataFrame({
        "Product Name": [
            "  Widget A", "widget a", "GADGET B", "  Gadget B  ", "Widget A",
            "Doohickey C", "WIDGET A", "doohickey c", "Gadget B", "Widget A",
            "  DOOHICKEY C  ", "widget a", "Widget A", "Gadget B", "doohickey c"
        ],
        "Region": [
            "North", "NORTH", " north", "South", "south ",
            "  East", "WEST", "North", "South", "east",
            "West ", "NORTH", "south ", "East", "west"
        ],
        "Sale Amount": [
            "150.00", "200", "75.50", "300", "125",
            "50000", "89.99", "-25", "N/A", "175",
            "220", "200", "125", "310", "95"
        ],
        "Sale Date": dates,
        "Salesperson": [
            "Alice", "alice", None, "Bob", "  ALICE  ",
            "Charlie", "alice", "  charlie", "Bob", "Alice",
            "Charlie ", None, "Alice", "bob ", "Charlie"
        ]
    })

    # STEP 1: Inspect
    print("--- INSPECTION ---")
    print(f"Shape: {df.shape}")
    print(f"\nDtypes:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isna().sum()}")
    print()

    # STEP 2: Clean column names
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
    print(f"Columns: {list(df.columns)}")

    # STEP 3: Clean strings first (so duplicates match properly)
    df["product_name"] = df["product_name"].str.strip().str.title()
    df["region"] = df["region"].str.strip().str.title()
    df["salesperson"] = df["salesperson"].str.strip().str.title()

    # STEP 4: Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows")

    # STEP 5: Fix data types
    df["sale_amount"] = pd.to_numeric(df["sale_amount"], errors="coerce")
    df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

    # STEP 6: Handle missing values
    # Fill missing salesperson with "Unknown" (we don't want to lose the sale data)
    df["salesperson"] = df["salesperson"].fillna("Unknown")
    # Fill missing sale_amount with median
    df["sale_amount"] = df["sale_amount"].fillna(df["sale_amount"].median())
    # Drop rows with unparseable dates
    df = df.dropna(subset=["sale_date"])

    # STEP 7: Handle outliers using IQR
    Q1 = df["sale_amount"].quantile(0.25)
    Q3 = df["sale_amount"].quantile(0.75)
    IQR = Q3 - Q1
    lower = max(0, Q1 - 1.5 * IQR)  # sales can't be negative
    upper = Q3 + 1.5 * IQR
    print(f"Clipping sale_amount to [{lower:.2f}, {upper:.2f}]")
    df["sale_amount"] = df["sale_amount"].clip(lower=lower, upper=upper)

    # STEP 8: Validate
    print("\n--- VALIDATION ---")
    print(f"Final shape: {df.shape}")
    print(f"\nDtypes:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isna().sum()}")
    print(f"\nSummary stats:\n{df.describe()}")
    print(f"\nUnique products: {sorted(df['product_name'].unique().tolist())}")
    print(f"Unique regions: {sorted(df['region'].unique().tolist())}")
    print(f"\nCleaned data:")
    print(df.to_string())


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Detect and handle missing values", exercise_1),
        ("Find and remove duplicate records", exercise_2),
        ("Fix inconsistent string formatting", exercise_3),
        ("Convert columns to proper types", exercise_4),
        ("Clean a messy customer dataset", exercise_5),
        ("Full data cleaning pipeline", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
