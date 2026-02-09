"""
Data Cleaning — Example Code
==============================

Run this file:
    python3 example.py

This example creates a deliberately messy dataset and walks through cleaning
it step by step. By the end, you'll see a complete before-and-after.
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
# The messy dataset — this is what real data looks like!
# =============================================================================

print("=" * 60)
print("  DATA CLEANING — STEP BY STEP")
print("=" * 60)
print()

# Let's create a "customer orders" dataset with every common problem
messy_data = pd.DataFrame({
    "Customer Name": [
        "  Alice Smith  ", "bob jones", "CHARLIE BROWN", "  Diana Prince",
        "bob jones", "Eve Wilson", None, "  Alice Smith  ", "frank miller",
        "Grace Lee", "  HANK HILL ", "eve wilson"
    ],
    "Email": [
        "alice@email.com", "bob@email.com", "charlie@email.com", "diana@email.com",
        "bob@email.com", "eve@email.com", "unknown@email.com", "alice@email.com",
        "frank@email.com", "grace@email.com", "hank@email.com", "Eve@Email.com"
    ],
    "Order Amount": [
        "150.00", "200", "75.50", "N/A",
        "200", "50000", "25.00", "150.00",
        "-10", "300.00", "89.99", "45"
    ],
    "Order Date": [
        "2025-01-15", "01/20/2025", "2025-02-01", "2025-02-14",
        "01/20/2025", "2025-03-01", "March 5, 2025", "2025-01-15",
        "2025-03-10", "not a date", "2025-03-20", "2025-04-01"
    ],
    "Status": [
        "delivered", "Shipped", "DELIVERED", "pending",
        "Shipped", "delivered", "Pending", "delivered",
        "cancelled", "Delivered", "SHIPPED", "Delivered"
    ],
    "Rating": [
        4.5, 3.0, np.nan, 5.0,
        3.0, np.nan, 2.5, 4.5,
        np.nan, 4.0, np.nan, 3.5
    ]
})

print("ORIGINAL MESSY DATA:")
print("-" * 60)
print(messy_data.to_string())
print()
print(f"Shape: {messy_data.shape}")
print(f"\nData types:\n{messy_data.dtypes}")
print(f"\nMissing values:\n{messy_data.isna().sum()}")
print()

# Let's work on a copy so we can compare at the end
df = messy_data.copy()


# -----------------------------------------------------------------------------
# 1. Clean up column names
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 1: Clean column names")
print("=" * 60)

print(f"\nBefore: {list(df.columns)}")

df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

print(f"After:  {list(df.columns)}")
print()


# -----------------------------------------------------------------------------
# 2. Remove duplicate rows
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 2: Remove duplicates")
print("=" * 60)

print(f"\nRows before: {len(df)}")
print(f"Duplicate rows found: {df.duplicated().sum()}")

# Show which rows are duplicates
dupes = df[df.duplicated(keep=False)]
print(f"\nAll rows involved in duplication:")
print(dupes[["customer_name", "email", "order_amount"]].to_string())

df = df.drop_duplicates()
print(f"\nRows after removing duplicates: {len(df)}")
print()


# -----------------------------------------------------------------------------
# 3. Fix data types
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 3: Fix data types")
print("=" * 60)

print(f"\norder_amount dtype before: {df['order_amount'].dtype}")
print(f"Sample values: {df['order_amount'].tolist()[:5]}")

# to_numeric with coerce turns "N/A" into NaN instead of crashing
df["order_amount"] = pd.to_numeric(df["order_amount"], errors="coerce")
print(f"order_amount dtype after:  {df['order_amount'].dtype}")
print(f"NaN values created (from 'N/A'): {df['order_amount'].isna().sum()}")

# Parse dates — pandas is smart enough to handle multiple formats
print(f"\norder_date dtype before: {df['order_date'].dtype}")
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print(f"order_date dtype after:  {df['order_date'].dtype}")
print(f"NaN dates (unparseable): {df['order_date'].isna().sum()}")
print()


# -----------------------------------------------------------------------------
# 4. Handle missing values
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 4: Handle missing values")
print("=" * 60)

print(f"\nMissing values before:")
print(df.isna().sum())

# Strategy for each column:
# - customer_name: drop rows where name is missing (can't identify the customer)
# - order_amount: fill with median (a reasonable middle ground)
# - order_date: drop rows where date is missing (essential for time analysis)
# - rating: fill with median (common for optional fields)

df = df.dropna(subset=["customer_name"])
print(f"\nDropped rows with missing customer_name. Rows: {len(df)}")

median_amount = df["order_amount"].median()
df["order_amount"] = df["order_amount"].fillna(median_amount)
print(f"Filled missing order_amount with median: {median_amount}")

df = df.dropna(subset=["order_date"])
print(f"Dropped rows with missing order_date. Rows: {len(df)}")

median_rating = df["rating"].median()
df["rating"] = df["rating"].fillna(median_rating)
print(f"Filled missing ratings with median: {median_rating}")

print(f"\nMissing values after:")
print(df.isna().sum())
print()


# -----------------------------------------------------------------------------
# 5. Clean strings
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 5: Clean strings")
print("=" * 60)

print(f"\nCustomer names before:")
print(df["customer_name"].tolist())

# Strip whitespace and standardize to Title Case
df["customer_name"] = df["customer_name"].str.strip().str.title()

print(f"\nCustomer names after:")
print(df["customer_name"].tolist())

# Standardize email to lowercase
df["email"] = df["email"].str.lower().str.strip()

# Standardize status to title case
print(f"\nStatus values before: {df['status'].unique().tolist()}")
df["status"] = df["status"].str.strip().str.title()
print(f"Status values after:  {df['status'].unique().tolist()}")
print()


# -----------------------------------------------------------------------------
# 6. Handle outliers
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 6: Handle outliers")
print("=" * 60)

print(f"\nOrder amount stats before:")
print(df["order_amount"].describe())

# Flag suspicious values
print(f"\nNegative amounts: {(df['order_amount'] < 0).sum()}")
print(f"Extremely high amounts (>10000): {(df['order_amount'] > 10000).sum()}")

# Use IQR method to identify outliers
Q1 = df["order_amount"].quantile(0.25)
Q3 = df["order_amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nIQR bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")

outliers = df[(df["order_amount"] < lower_bound) | (df["order_amount"] > upper_bound)]
print(f"Outliers found: {len(outliers)}")
if len(outliers) > 0:
    print(outliers[["customer_name", "order_amount"]].to_string())

# Clip instead of removing — cap extreme values at the bounds
df["order_amount"] = df["order_amount"].clip(lower=max(0, lower_bound), upper=upper_bound)

print(f"\nOrder amount stats after clipping:")
print(df["order_amount"].describe())
print()


# -----------------------------------------------------------------------------
# 7. Apply custom transformations
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 7: Custom transformations")
print("=" * 60)

# Create a "name_length" column just for fun
df["name_length"] = df["customer_name"].apply(len)

# Map status to a numeric priority
priority_map = {"Pending": 1, "Shipped": 2, "Delivered": 3, "Cancelled": 0}
df["priority"] = df["status"].map(priority_map)

# Custom function: categorize order amounts
def categorize_amount(amount):
    if amount < 50:
        return "Small"
    elif amount < 200:
        return "Medium"
    else:
        return "Large"

df["order_size"] = df["order_amount"].apply(categorize_amount)

print("\nNew columns added:")
print(df[["customer_name", "order_amount", "order_size", "status", "priority"]].to_string())
print()


# -----------------------------------------------------------------------------
# 8. Validate the cleaned data
# -----------------------------------------------------------------------------

print("=" * 60)
print("STEP 8: Validate cleaned data")
print("=" * 60)

print(f"\nFinal shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isna().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")
print(f"\nOrder amount range: [{df['order_amount'].min():.2f}, {df['order_amount'].max():.2f}]")
print(f"Status values: {sorted(df['status'].unique().tolist())}")
print(f"Rating range: [{df['rating'].min()}, {df['rating'].max()}]")

# Quick sanity checks
assert df.isna().sum().sum() == 0, "Still have missing values!"
assert df.duplicated().sum() == 0, "Still have duplicates!"
assert (df["order_amount"] >= 0).all(), "Negative order amounts!"
assert df["rating"].between(0, 5).all(), "Ratings out of range!"

print("\nAll validation checks passed!")
print()


# -----------------------------------------------------------------------------
# 9. Final comparison
# -----------------------------------------------------------------------------

print("=" * 60)
print("FINAL CLEANED DATA")
print("=" * 60)
print()
print(df.to_string())
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"  Original rows:  {len(messy_data)}")
print(f"  Final rows:     {len(df)}")
print(f"  Rows removed:   {len(messy_data) - len(df)}")
print(f"  Columns added:  {len(df.columns) - len(messy_data.columns)}")
print()
print("Problems fixed:")
print("  - Cleaned column names (spaces -> underscores, lowercase)")
print("  - Removed duplicate rows")
print("  - Converted order_amount from string to float")
print("  - Parsed order_date strings into datetime objects")
print("  - Filled missing ratings with median")
print("  - Dropped rows with missing names or unparseable dates")
print("  - Stripped whitespace and standardized string casing")
print("  - Clipped outlier order amounts")
print("  - Added derived columns (order_size, priority, name_length)")
print()
print("That's data cleaning in a nutshell! Messy in, clean out.")
