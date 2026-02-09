"""
NumPy Basics — Example Code
=============================

Run this file:
    python3 example.py

A hands-on tour of NumPy fundamentals. Each section demonstrates a core
concept with real output so you can see exactly what's happening.
"""

import sys

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Run: pip install numpy")
    sys.exit(0)

import time


# -----------------------------------------------------------------------------
# 1. Creating arrays — many ways to build them
# -----------------------------------------------------------------------------

print("=" * 60)
print("1. CREATING ARRAYS")
print("=" * 60)

# From a Python list — the most common way
a = np.array([1, 2, 3, 4, 5])
print("From a list:     ", a)

# 2D array (matrix) from nested lists
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("2D array (matrix):")
print(matrix)

# All zeros — great for initializing data structures
zeros = np.zeros(5)
print("Zeros (1D):      ", zeros)

zeros_2d = np.zeros((2, 4))
print("Zeros (2x4):")
print(zeros_2d)

# All ones
ones = np.ones((2, 3))
print("Ones (2x3):")
print(ones)

# np.arange — like range() but returns an array
r = np.arange(0, 10, 2)
print("arange(0, 10, 2):", r)

# np.linspace — evenly spaced numbers between endpoints
lin = np.linspace(0, 1, 5)
print("linspace(0, 1, 5):", lin)
print()


# -----------------------------------------------------------------------------
# 2. Array attributes — understanding what you're working with
# -----------------------------------------------------------------------------

print("=" * 60)
print("2. ARRAY ATTRIBUTES")
print("=" * 60)

a = np.array([[10, 20, 30],
              [40, 50, 60]])

print("Array:")
print(a)
print(f"  .shape = {a.shape}")    # (2, 3) — 2 rows, 3 columns
print(f"  .ndim  = {a.ndim}")     # 2 — it's a 2D array
print(f"  .size  = {a.size}")     # 6 — total elements
print(f"  .dtype = {a.dtype}")    # int64 — 64-bit integers
print()


# -----------------------------------------------------------------------------
# 3. Indexing and slicing — getting at your data
# -----------------------------------------------------------------------------

print("=" * 60)
print("3. INDEXING AND SLICING")
print("=" * 60)

# 1D indexing — works just like Python lists
a = np.array([10, 20, 30, 40, 50])
print("Array:           ", a)
print("a[0] (first):    ", a[0])
print("a[-1] (last):    ", a[-1])
print("a[1:4] (slice):  ", a[1:4])
print("a[::2] (every 2):", a[::2])
print()

# 2D indexing — row, col syntax
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("Matrix:")
print(m)
print(f"m[0, 0] (top-left):       {m[0, 0]}")
print(f"m[1, 2] (row 1, col 2):   {m[1, 2]}")
print(f"m[0] (first row):         {m[0]}")
print(f"m[:, 1] (second column):  {m[:, 1]}")
print(f"m[0:2, 1:] (submatrix):")
print(m[0:2, 1:])
print()


# -----------------------------------------------------------------------------
# 4. Array arithmetic — element-wise operations
# -----------------------------------------------------------------------------

print("=" * 60)
print("4. ARRAY ARITHMETIC")
print("=" * 60)

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(f"a = {a}")
print(f"b = {b}")
print(f"a + b   = {a + b}")        # Element-wise addition
print(f"a * b   = {a * b}")        # Element-wise multiplication
print(f"a ** 2  = {a ** 2}")       # Square each element
print(f"b / a   = {b / a}")        # Element-wise division
print()

# Broadcasting — a scalar is "broadcast" across the whole array
print("Broadcasting with a scalar:")
print(f"a * 10  = {a * 10}")
print(f"a + 100 = {a + 100}")
print()


# -----------------------------------------------------------------------------
# 5. Useful functions — aggregation and math
# -----------------------------------------------------------------------------

print("=" * 60)
print("5. USEFUL FUNCTIONS")
print("=" * 60)

data = np.array([4, 1, 7, 3, 9, 2])
print(f"data = {data}")
print(f"  np.sum(data)  = {np.sum(data)}")
print(f"  np.mean(data) = {np.mean(data):.3f}")
print(f"  np.std(data)  = {np.std(data):.3f}")
print(f"  np.min(data)  = {np.min(data)}")
print(f"  np.max(data)  = {np.max(data)}")
print(f"  np.sort(data) = {np.sort(data)}")
print()

# Axis parameter — crucial for 2D data
m = np.array([[1, 2, 3],
              [4, 5, 6]])
print("Matrix:")
print(m)
print(f"  np.sum(m)          = {np.sum(m)}")
print(f"  np.sum(m, axis=0)  = {np.sum(m, axis=0)}  (sum down each column)")
print(f"  np.sum(m, axis=1)  = {np.sum(m, axis=1)}  (sum across each row)")
print()


# -----------------------------------------------------------------------------
# 6. Reshaping arrays — rearrange without changing data
# -----------------------------------------------------------------------------

print("=" * 60)
print("6. RESHAPING ARRAYS")
print("=" * 60)

a = np.arange(12)
print(f"Original (1D):  {a}")

# Reshape into a 3x4 matrix
b = a.reshape(3, 4)
print("Reshaped (3x4):")
print(b)

# Flatten back to 1D
c = b.flatten()
print(f"Flattened:      {c}")

# Transpose — swap rows and columns
print("Transposed (4x3):")
print(b.T)

# Using -1 as a wildcard
d = a.reshape(2, -1)  # NumPy figures out the second dimension
print(f"reshape(2, -1) gives shape {d.shape}")
print()


# -----------------------------------------------------------------------------
# 7. Boolean indexing — filtering data with conditions
# -----------------------------------------------------------------------------

print("=" * 60)
print("7. BOOLEAN INDEXING")
print("=" * 60)

scores = np.array([85, 42, 91, 67, 73, 55, 98, 38])
print(f"scores = {scores}")

# Create a boolean mask
passing = scores >= 60
print(f"scores >= 60:     {passing}")

# Use the mask to filter
print(f"Passing scores:   {scores[passing]}")

# One-liner — this is the common pattern
print(f"High scores (>90): {scores[scores > 90]}")

# Combining conditions — remember the parentheses!
mid_range = scores[(scores >= 60) & (scores <= 80)]
print(f"Mid-range (60-80): {mid_range}")
print()


# -----------------------------------------------------------------------------
# 8. Stacking and splitting — combining and dividing arrays
# -----------------------------------------------------------------------------

print("=" * 60)
print("8. STACKING AND SPLITTING")
print("=" * 60)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"a = {a}")
print(f"b = {b}")

# Vertical stack — rows on top of each other
vstacked = np.vstack([a, b])
print("vstack:")
print(vstacked)

# Horizontal stack — side by side
hstacked = np.hstack([a, b])
print(f"hstack: {hstacked}")

# Splitting
c = np.array([10, 20, 30, 40, 50, 60])
parts = np.split(c, 3)
print(f"\nSplitting {c} into 3 parts:")
for i, part in enumerate(parts):
    print(f"  Part {i}: {part}")
print()


# -----------------------------------------------------------------------------
# 9. Random numbers — simulations and sample data
# -----------------------------------------------------------------------------

print("=" * 60)
print("9. RANDOM NUMBERS")
print("=" * 60)

# Set a seed so results are reproducible
np.random.seed(42)

# Random integers — like rolling dice
dice_rolls = np.random.randint(1, 7, 10)
print(f"10 dice rolls:    {dice_rolls}")

# Random floats between 0 and 1
uniform = np.random.rand(5)
print(f"5 uniform floats: {uniform}")

# Normal distribution (bell curve)
normal = np.random.normal(100, 15, 5)  # mean=100, std=15
print(f"5 normal values:  {normal}")
print()


# -----------------------------------------------------------------------------
# 10. NumPy vs Python lists — speed comparison
# -----------------------------------------------------------------------------

print("=" * 60)
print("10. NUMPY vs PYTHON LISTS (SPEED)")
print("=" * 60)

size = 1_000_000

# Python list approach
python_list = list(range(size))
start = time.time()
result_list = [x * 2 for x in python_list]
python_time = time.time() - start

# NumPy approach
numpy_array = np.arange(size)
start = time.time()
result_numpy = numpy_array * 2
numpy_time = time.time() - start

print(f"Multiplying {size:,} elements by 2:")
print(f"  Python list: {python_time:.4f}s")
print(f"  NumPy array: {numpy_time:.4f}s")

if numpy_time > 0:
    speedup = python_time / numpy_time
    print(f"  NumPy was ~{speedup:.0f}x faster!")
print()


# -----------------------------------------------------------------------------
# 11. Putting it all together — a mini data analysis
# -----------------------------------------------------------------------------

print("=" * 60)
print("11. PUTTING IT ALL TOGETHER")
print("=" * 60)

# Simulate test scores for 5 students across 4 exams
np.random.seed(123)
scores = np.random.randint(50, 100, size=(5, 4))
students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
exams = ["Exam 1", "Exam 2", "Exam 3", "Exam 4"]

print("Test Scores:")
print(f"{'':>8}", end="")
for exam in exams:
    print(f"{exam:>8}", end="")
print()

for name, row in zip(students, scores):
    print(f"{name:>8}", end="")
    for score in row:
        print(f"{score:>8}", end="")
    print()

print()
print("Per-student averages:")
averages = np.mean(scores, axis=1)
for name, avg in zip(students, averages):
    print(f"  {name}: {avg:.1f}")

print()
print("Per-exam averages:")
exam_avgs = np.mean(scores, axis=0)
for exam, avg in zip(exams, exam_avgs):
    print(f"  {exam}: {avg:.1f}")

print(f"\nOverall class average: {np.mean(scores):.1f}")
print(f"Highest score: {np.max(scores)}")
print(f"Lowest score:  {np.min(scores)}")

# Who got the highest score?
row, col = np.unravel_index(np.argmax(scores), scores.shape)
print(f"Top performer: {students[row]} on {exams[col]} ({scores[row, col]})")

print()
print("=" * 60)
print("   NUMPY BASICS COMPLETE!")
print("=" * 60)
print()
print("Try changing the examples above and run the file again!")
