"""
CSV Files — Exercises
======================

Practice problems to test your understanding of Python's csv module.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

Each exercise creates its own data files and cleans up after itself.
"""

import csv
import os

# All temp files go in the same directory as this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def temp_path(filename):
    """Helper: build an absolute path for a temp file."""
    return os.path.join(SCRIPT_DIR, filename)


def cleanup(*paths):
    """Helper: remove temp files if they exist."""
    for path in paths:
        if os.path.exists(path):
            os.remove(path)


# =============================================================================
# Exercise 1: Create and read a student CSV
#
# 1. Create a CSV file called "_temp_ex1_students.csv" with these columns:
#      name, age, grade
#    and these rows:
#      Alice, 20, 88
#      Bob, 22, 75
#      Charlie, 21, 92
#      Diana, 23, 65
#      Eve, 20, 95
#
# 2. Read the file back using csv.reader() and print each student like:
#      Alice is 20 years old with a grade of 88
#
# 3. Clean up the temp file when done.
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Filter rows from a CSV
#
# 1. Create the same student CSV as Exercise 1.
# 2. Use csv.DictReader to read it.
# 3. Print only the students whose grade is above 80, like:
#      High performers:
#      Alice — 88
#      Charlie — 92
#      Eve — 95
#
# 4. Clean up the temp file when done.
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Convert comma-separated to tab-separated
#
# 1. Create a comma-separated CSV "_temp_ex3_input.csv" with columns:
#      city, country, population
#    and a few rows of data (make them up).
#
# 2. Read the comma-separated file and write it out as a tab-separated
#    file called "_temp_ex3_output.tsv".
#
# 3. Read the TSV file back and print each row to prove it worked.
# 4. Clean up both temp files.
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Calculate statistics from a CSV
#
# 1. Create a CSV "_temp_ex4_sales.csv" with columns:
#      product, units_sold, price_each
#    and these rows:
#      Widget, 150, 9.99
#      Gadget, 85, 24.99
#      Doohickey, 200, 4.50
#      Thingamajig, 60, 49.99
#      Whatchamacallit, 120, 14.99
#
# 2. Read the file and calculate:
#      - Total revenue (units_sold * price_each for each row, summed up)
#      - Average units sold
#      - The product with the highest revenue
#      - The product with the lowest units sold
#
# 3. Print the results neatly.
# 4. Clean up the temp file.
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Merge two CSV files
#
# 1. Create "_temp_ex5_students.csv" with columns:
#      student_id, name
#    Data:
#      101, Alice
#      102, Bob
#      103, Charlie
#      104, Diana
#
# 2. Create "_temp_ex5_grades.csv" with columns:
#      student_id, subject, grade
#    Data:
#      101, Math, 92
#      102, Math, 78
#      103, Math, 88
#      101, Science, 85
#      102, Science, 90
#      104, Science, 76
#
# 3. Merge the two files: for each grade row, look up the student's name
#    and write a new CSV "_temp_ex5_merged.csv" with columns:
#      name, subject, grade
#
# 4. Print the merged result.
# 5. Clean up all three temp files.
#
# Hint: Read the students file into a dictionary mapping student_id -> name
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Add a computed column
#
# 1. Create "_temp_ex6_scores.csv" with columns:
#      name, math, science, english
#    Data:
#      Alice, 92, 88, 95
#      Bob, 78, 85, 82
#      Charlie, 55, 62, 58
#      Diana, 90, 94, 91
#      Eve, 45, 50, 47
#
# 2. Read the file and write a NEW CSV "_temp_ex6_results.csv" that has
#    all the original columns PLUS two new columns:
#      average — the average of the three scores (rounded to 1 decimal)
#      status  — "Pass" if average >= 60, otherwise "Fail"
#
# 3. Print the results.
# 4. Clean up both temp files.
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    path = temp_path("_temp_ex1_students.csv")

    # Write the CSV
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "grade"])
        writer.writerows([
            ["Alice", 20, 88],
            ["Bob", 22, 75],
            ["Charlie", 21, 92],
            ["Diana", 23, 65],
            ["Eve", 20, 95],
        ])

    # Read and print it
    with open(path, newline="") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            name, age, grade = row
            print(f"  {name} is {age} years old with a grade of {grade}")

    cleanup(path)


def solution_2():
    path = temp_path("_temp_ex2_students.csv")

    # Write the CSV
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "grade"])
        writer.writerows([
            ["Alice", 20, 88],
            ["Bob", 22, 75],
            ["Charlie", 21, 92],
            ["Diana", 23, 65],
            ["Eve", 20, 95],
        ])

    # Read and filter
    print("  High performers:")
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["grade"]) > 80:
                print(f"    {row['name']} — {row['grade']}")

    cleanup(path)


def solution_3():
    csv_path = temp_path("_temp_ex3_input.csv")
    tsv_path = temp_path("_temp_ex3_output.tsv")

    # Create the comma-separated file
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["city", "country", "population"])
        writer.writerows([
            ["Tokyo", "Japan", 13960000],
            ["Delhi", "India", 11030000],
            ["Shanghai", "China", 24870000],
            ["São Paulo", "Brazil", 12330000],
        ])

    # Read CSV, write TSV
    with open(csv_path, newline="") as infile, \
         open(tsv_path, "w", newline="") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile, delimiter="\t")
        for row in reader:
            writer.writerow(row)

    # Read the TSV back to prove it worked
    print("  Tab-separated output:")
    with open(tsv_path, newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            print(f"    {row}")

    cleanup(csv_path, tsv_path)


def solution_4():
    path = temp_path("_temp_ex4_sales.csv")

    # Create the CSV
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "units_sold", "price_each"])
        writer.writerows([
            ["Widget", 150, 9.99],
            ["Gadget", 85, 24.99],
            ["Doohickey", 200, 4.50],
            ["Thingamajig", 60, 49.99],
            ["Whatchamacallit", 120, 14.99],
        ])

    # Read and calculate statistics
    total_revenue = 0
    total_units = 0
    count = 0
    best_product = ""
    best_revenue = 0
    worst_product = ""
    worst_units = float("inf")

    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            units = int(row["units_sold"])
            price = float(row["price_each"])
            revenue = units * price

            total_revenue += revenue
            total_units += units
            count += 1

            if revenue > best_revenue:
                best_revenue = revenue
                best_product = row["product"]

            if units < worst_units:
                worst_units = units
                worst_product = row["product"]

    avg_units = total_units / count

    print(f"  Total revenue:         ${total_revenue:,.2f}")
    print(f"  Average units sold:    {avg_units:.1f}")
    print(f"  Highest revenue:       {best_product} (${best_revenue:,.2f})")
    print(f"  Lowest units sold:     {worst_product} ({worst_units} units)")

    cleanup(path)


def solution_5():
    students_path = temp_path("_temp_ex5_students.csv")
    grades_path = temp_path("_temp_ex5_grades.csv")
    merged_path = temp_path("_temp_ex5_merged.csv")

    # Create students file
    with open(students_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "name"])
        writer.writerows([
            [101, "Alice"],
            [102, "Bob"],
            [103, "Charlie"],
            [104, "Diana"],
        ])

    # Create grades file
    with open(grades_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "subject", "grade"])
        writer.writerows([
            [101, "Math", 92],
            [102, "Math", 78],
            [103, "Math", 88],
            [101, "Science", 85],
            [102, "Science", 90],
            [104, "Science", 76],
        ])

    # Build a lookup dictionary: student_id -> name
    student_lookup = {}
    with open(students_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            student_lookup[row["student_id"]] = row["name"]

    # Merge: read grades, look up names, write merged file
    with open(grades_path, newline="") as infile, \
         open(merged_path, "w", newline="") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=["name", "subject", "grade"])
        writer.writeheader()

        for row in reader:
            name = student_lookup.get(row["student_id"], "Unknown")
            writer.writerow({
                "name": name,
                "subject": row["subject"],
                "grade": row["grade"],
            })

    # Print the merged result
    print("  Merged result:")
    with open(merged_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"    {row['name']} — {row['subject']}: {row['grade']}")

    cleanup(students_path, grades_path, merged_path)


def solution_6():
    input_path = temp_path("_temp_ex6_scores.csv")
    output_path = temp_path("_temp_ex6_results.csv")

    # Create the input CSV
    with open(input_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "math", "science", "english"])
        writer.writerows([
            ["Alice", 92, 88, 95],
            ["Bob", 78, 85, 82],
            ["Charlie", 55, 62, 58],
            ["Diana", 90, 94, 91],
            ["Eve", 45, 50, 47],
        ])

    # Read, compute, and write the output
    with open(input_path, newline="") as infile, \
         open(output_path, "w", newline="") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ["average", "status"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            math = int(row["math"])
            science = int(row["science"])
            english = int(row["english"])
            avg = round((math + science + english) / 3, 1)
            status = "Pass" if avg >= 60 else "Fail"

            row["average"] = avg
            row["status"] = status
            writer.writerow(row)

    # Print the results
    print("  Results with computed columns:")
    with open(output_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"    {row['name']:>10}  avg={row['average']:>5}  {row['status']}")

    cleanup(input_path, output_path)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Create and read a student CSV", exercise_1),
        ("Filter rows from a CSV", exercise_2),
        ("Convert comma-separated to tab-separated", exercise_3),
        ("Calculate statistics from a CSV", exercise_4),
        ("Merge two CSV files", exercise_5),
        ("Add a computed column", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
