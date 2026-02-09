"""
Pandas Basics — Exercises
==========================

Practice problems to test your understanding of Pandas.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import sys

try:
    import pandas as pd
except ImportError:
    print("Pandas is not installed. Run: pip install pandas")
    sys.exit(0)


# =============================================================================
# Exercise 1: Create and explore a DataFrame
#
# Create a DataFrame called `students` from the following dictionary:
#   - "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
#   - "grade": [88, 95, 72, 91, 85, 67]
#   - "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
#
# Then print:
#   1. The first 3 rows using .head()
#   2. The shape of the DataFrame
#   3. The output of .describe()
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Select and filter data
#
# Using the same student data from Exercise 1, do the following:
#   1. Select just the "name" and "grade" columns and print them
#   2. Use .loc[] to get the row at index 2
#   3. Find all students with a grade of 85 or higher and print them
#
# =============================================================================

def exercise_2():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Add a computed column and sort
#
# Using the same student data:
#   1. Add a column "passed" that is True if grade >= 70, False otherwise
#   2. Add a column "letter_grade" based on these rules:
#      - 90+  -> "A"
#      - 80+  -> "B"
#      - 70+  -> "C"
#      - below 70 -> "F"
#      (Hint: you can write a function and use .apply())
#   3. Sort by grade descending and print the result
#
# =============================================================================

def exercise_3():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Group by and aggregate
#
# Using the same student data:
#   1. Group by "subject" and calculate the mean grade for each subject
#   2. Group by "subject" and get the count, mean, min, and max grade
#   3. Which subject has the higher average grade? Print the answer.
#
# =============================================================================

def exercise_4():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Handle missing data
#
# Create this DataFrame with some missing values:
#   data = {
#       "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
#       "hours_studied": [5, None, 8, None, 6],
#       "test_score": [88, 76, None, 92, 85]
#   }
#
# Then:
#   1. Print how many missing values each column has
#   2. Fill the missing hours_studied with the column median
#   3. Drop any rows that still have missing values
#   4. Print the cleaned DataFrame
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Build a sales report
#
# Create this sales DataFrame:
#   data = {
#       "salesperson": ["Alice", "Bob", "Alice", "Charlie", "Bob",
#                        "Alice", "Charlie", "Bob", "Charlie", "Alice"],
#       "region": ["North", "South", "North", "South", "North",
#                   "South", "North", "South", "North", "South"],
#       "amount": [250, 180, 310, 420, 150, 275, 360, 210, 290, 195]
#   }
#
# Build a report that shows:
#   1. Total sales per salesperson (sorted highest to lowest)
#   2. Average sale per region
#   3. The top salesperson (highest total) — print their name and total
#   4. A summary table: group by salesperson AND region, showing total
#      and count of sales
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })

    print("First 3 rows:")
    print(students.head(3))
    print()

    print(f"Shape: {students.shape}")
    print()

    print("Describe:")
    print(students.describe())


def solution_2():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })

    # 1. Select columns
    print("Name and grade:")
    print(students[["name", "grade"]])
    print()

    # 2. loc for row at index 2
    print("Row at index 2:")
    print(students.loc[2])
    print()

    # 3. Filter: grade >= 85
    print("Grade 85 or higher:")
    print(students[students["grade"] >= 85])


def solution_3():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })

    # 1. Boolean column
    students["passed"] = students["grade"] >= 70

    # 2. Letter grade using apply
    def get_letter(grade):
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        else:
            return "F"

    students["letter_grade"] = students["grade"].apply(get_letter)

    # 3. Sort by grade descending
    print(students.sort_values("grade", ascending=False).to_string(index=False))


def solution_4():
    students = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
        "grade": [88, 95, 72, 91, 85, 67],
        "subject": ["Math", "Science", "Math", "Science", "Math", "Science"]
    })

    # 1. Mean grade per subject
    print("Mean grade by subject:")
    avg_by_subject = students.groupby("subject")["grade"].mean()
    print(avg_by_subject)
    print()

    # 2. Multiple aggregations
    print("Detailed stats by subject:")
    print(students.groupby("subject")["grade"].agg(["count", "mean", "min", "max"]))
    print()

    # 3. Which subject wins?
    top_subject = avg_by_subject.idxmax()
    print(f"Highest average: {top_subject} ({avg_by_subject[top_subject]:.1f})")


def solution_5():
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "hours_studied": [5, None, 8, None, 6],
        "test_score": [88, 76, None, 92, 85]
    }
    df = pd.DataFrame(data)

    # 1. Count missing values
    print("Missing values per column:")
    print(df.isna().sum())
    print()

    # 2. Fill hours_studied with median
    df["hours_studied"] = df["hours_studied"].fillna(df["hours_studied"].median())
    print("After filling hours_studied with median:")
    print(df)
    print()

    # 3. Drop rows still missing
    df = df.dropna()
    print("After dropping remaining NaN rows:")
    print(df)


def solution_6():
    data = {
        "salesperson": ["Alice", "Bob", "Alice", "Charlie", "Bob",
                         "Alice", "Charlie", "Bob", "Charlie", "Alice"],
        "region": ["North", "South", "North", "South", "North",
                    "South", "North", "South", "North", "South"],
        "amount": [250, 180, 310, 420, 150, 275, 360, 210, 290, 195]
    }
    sales = pd.DataFrame(data)

    # 1. Total sales per salesperson
    total_by_person = sales.groupby("salesperson")["amount"].sum().sort_values(ascending=False)
    print("Total sales per salesperson:")
    print(total_by_person)
    print()

    # 2. Average sale per region
    print("Average sale per region:")
    print(sales.groupby("region")["amount"].mean())
    print()

    # 3. Top salesperson
    top_name = total_by_person.idxmax()
    top_total = total_by_person.max()
    print(f"Top salesperson: {top_name} (${top_total:,})")
    print()

    # 4. Summary table
    print("Sales by salesperson and region:")
    summary = sales.groupby(["salesperson", "region"])["amount"].agg(["sum", "count"])
    summary.columns = ["total", "num_sales"]
    print(summary)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Create and explore a DataFrame", exercise_1),
        ("Select and filter data", exercise_2),
        ("Add a computed column and sort", exercise_3),
        ("Group by and aggregate", exercise_4),
        ("Handle missing data", exercise_5),
        ("Build a sales report", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
