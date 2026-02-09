# NumPy Basics

## Objective

Learn the fundamentals of NumPy — Python's powerhouse library for fast numerical computing. By the end of this lesson, you'll be able to create arrays, perform vectorized math, filter data, and understand why NumPy is the foundation of Python's entire data science ecosystem.

## Concepts Covered

- What NumPy is and why it matters
- Creating arrays in multiple ways
- Array attributes (shape, dtype, ndim, size)
- Indexing and slicing (1D and 2D)
- Element-wise arithmetic and broadcasting
- Aggregation functions (sum, mean, std, min, max)
- Reshaping, flattening, and transposing
- Boolean indexing (filtering with conditions)
- Stacking and splitting arrays
- Random number generation
- NumPy vs Python lists (speed and vectorization)

## Prerequisites

- Comfortable with Python basics (variables, loops, lists)
- Understanding of list indexing and slicing

## Lesson

### What Is NumPy and Why Does It Matter?

NumPy (short for "Numerical Python") is a library that gives Python fast, memory-efficient arrays and a huge collection of mathematical operations. If you've ever tried doing math on large lists in pure Python, you know it's painfully slow. NumPy fixes that.

Here's why it matters:

- **Speed** — NumPy arrays are stored in contiguous memory and operations run in optimized C code. It's often 10-100x faster than Python lists for numerical work.
- **Foundation** — Nearly every data science library in Python builds on NumPy. Pandas DataFrames, scikit-learn models, SciPy functions, Matplotlib plots — they all use NumPy arrays under the hood.
- **Vectorization** — Instead of writing loops to process data element by element, you write clean, readable expressions that operate on entire arrays at once.

### Installing NumPy

NumPy doesn't come with Python's standard library. Install it with pip:

```bash
pip install numpy
```

Then import it. The convention is to alias it as `np`:

```python
import numpy as np
```

You'll see `np` used everywhere in the Python data science world. Stick with this convention — everyone expects it.

### Creating Arrays

The core of NumPy is the `ndarray` (n-dimensional array). There are many ways to create one:

```python
import numpy as np

# From a Python list
a = np.array([1, 2, 3, 4, 5])

# 2D array (matrix) from nested lists
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# All zeros
zeros = np.zeros(5)          # [0. 0. 0. 0. 0.]
zeros_2d = np.zeros((3, 4))  # 3 rows, 4 columns

# All ones
ones = np.ones((2, 3))       # 2 rows, 3 columns of 1.0

# A range of numbers (like Python's range, but returns an array)
r = np.arange(0, 10, 2)      # [0, 2, 4, 6, 8]

# Evenly spaced numbers between two endpoints
lin = np.linspace(0, 1, 5)   # [0.0, 0.25, 0.5, 0.75, 1.0]
```

**Key difference**: `np.arange()` takes a step size, while `np.linspace()` takes the number of points you want. Use `linspace` when you care about the number of points, and `arange` when you care about the step size.

### Array Attributes

Every array carries useful metadata:

```python
a = np.array([[1, 2, 3], [4, 5, 6]])

a.shape   # (2, 3)  — 2 rows, 3 columns
a.ndim    # 2       — number of dimensions
a.size    # 6       — total number of elements
a.dtype   # int64   — data type of each element
```

- **`.shape`** — A tuple of dimension sizes. This is the one you'll check most often.
- **`.dtype`** — NumPy arrays are homogeneous (every element is the same type). Common dtypes: `int64`, `float64`, `bool`.
- **`.ndim`** — Number of axes. A 1D array has `ndim=1`, a matrix has `ndim=2`.
- **`.size`** — Total element count (product of all dimensions).

### Indexing and Slicing

NumPy indexing works like Python list indexing, but extended to multiple dimensions.

**1D indexing:**

```python
a = np.array([10, 20, 30, 40, 50])

a[0]      # 10       — first element
a[-1]     # 50       — last element
a[1:4]    # [20, 30, 40] — slice from index 1 to 3
a[::2]    # [10, 30, 50] — every other element
```

**2D indexing:**

```python
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

m[0, 0]     # 1       — row 0, col 0
m[1, 2]     # 6       — row 1, col 2
m[0]        # [1, 2, 3] — entire first row
m[:, 1]     # [2, 5, 8] — entire second column
m[0:2, 1:]  # [[2, 3], [5, 6]] — submatrix
```

The `row, col` syntax is the key thing here. A comma separates dimensions. A colon `:` means "all" along that axis.

### Array Arithmetic (Element-wise Operations)

This is where NumPy really shines. Arithmetic operators work element by element — no loops needed:

```python
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

a + b     # [11, 22, 33, 44]
a * b     # [10, 40, 90, 160]
a ** 2    # [1, 4, 9, 16]
b / a     # [10.0, 10.0, 10.0, 10.0]
```

**Broadcasting** lets you combine arrays with different shapes. The simplest case — operating an array with a scalar:

```python
a = np.array([1, 2, 3])
a * 10    # [10, 20, 30]  — the 10 is "broadcast" across the array
a + 100   # [101, 102, 103]
```

Broadcasting also works with higher dimensions, but the basic idea is always the same: NumPy stretches the smaller array to match the larger one, then does the operation element-wise.

### Useful Functions

NumPy comes loaded with functions for aggregation and computation:

```python
a = np.array([4, 1, 7, 3, 9, 2])

np.sum(a)     # 26     — total of all elements
np.mean(a)    # 4.333  — average
np.std(a)     # 2.687  — standard deviation
np.min(a)     # 1      — smallest value
np.max(a)     # 9      — largest value
np.sort(a)    # [1, 2, 3, 4, 7, 9] — returns a sorted copy
```

For 2D arrays, you can specify an axis:

```python
m = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(m)          # 21    — sum of everything
np.sum(m, axis=0)  # [5, 7, 9]   — sum down each column
np.sum(m, axis=1)  # [6, 15]     — sum across each row
```

The `axis` parameter is crucial when working with matrices. Think of it this way: `axis=0` collapses rows (operates down), `axis=1` collapses columns (operates across).

### Reshaping Arrays

You can rearrange an array's shape without changing its data:

```python
a = np.arange(12)            # [ 0,  1,  2, ..., 11]

# Reshape into a 3x4 matrix
b = a.reshape(3, 4)
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]

# Flatten back to 1D
c = b.flatten()              # [ 0,  1,  2, ..., 11]

# Transpose — swap rows and columns
d = b.T
# [[ 0,  4,  8],
#  [ 1,  5,  9],
#  [ 2,  6, 10],
#  [ 3,  7, 11]]
```

**Important**: `.reshape()` requires the total number of elements to match. You can't reshape 12 elements into a 3x5 matrix — the math doesn't work out.

Use `-1` as a wildcard dimension and NumPy will figure it out:

```python
a = np.arange(12)
a.reshape(3, -1)   # 3 rows, NumPy calculates 4 columns
a.reshape(-1, 6)   # NumPy calculates 2 rows, 6 columns
```

### Boolean Indexing (Filtering)

This is one of NumPy's most powerful features. You can use a condition to create a boolean mask, then use that mask to select elements:

```python
a = np.array([15, 22, 8, 31, 5, 19])

# Create a boolean mask
mask = a > 10          # [True, True, False, True, False, True]

# Use it to filter
a[mask]                # [15, 22, 31, 19]

# Or do it in one step — this is how most people write it
a[a > 10]              # [15, 22, 31, 19]

# Combine conditions with & (and) and | (or)
a[(a > 10) & (a < 25)]  # [15, 22, 19]
```

**Watch out**: Use `&` and `|` for element-wise boolean operations, not `and` and `or`. And always wrap each condition in parentheses.

### Stacking and Splitting

Need to combine or split arrays? NumPy has you covered:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stack vertically (row on top of row)
np.vstack([a, b])
# [[1, 2, 3],
#  [4, 5, 6]]

# Stack horizontally (side by side)
np.hstack([a, b])     # [1, 2, 3, 4, 5, 6]

# Split an array into equal parts
c = np.array([1, 2, 3, 4, 5, 6])
np.split(c, 3)        # [array([1, 2]), array([3, 4]), array([5, 6])]
```

### Random Numbers

NumPy's random module is great for simulations, testing, and generating sample data:

```python
# Random integers between low (inclusive) and high (exclusive)
np.random.randint(1, 7)        # One random die roll
np.random.randint(1, 7, 10)    # 10 random die rolls

# Random floats between 0 and 1
np.random.rand(5)              # 5 uniform random numbers

# Random numbers from a normal distribution (bell curve)
np.random.normal(0, 1, 1000)   # mean=0, std=1, 1000 samples
```

For reproducibility, set a seed so you get the same random numbers every time:

```python
np.random.seed(42)
np.random.rand(3)    # Always produces the same 3 numbers
```

### NumPy vs Python Lists

Why not just use regular Python lists? Let's see:

```python
import time

size = 1_000_000

# Python list approach
python_list = list(range(size))
start = time.time()
result = [x * 2 for x in python_list]
python_time = time.time() - start

# NumPy approach
numpy_array = np.arange(size)
start = time.time()
result = numpy_array * 2
numpy_time = time.time() - start

print(f"Python list: {python_time:.4f}s")
print(f"NumPy array: {numpy_time:.4f}s")
```

NumPy is typically 10-100x faster because:

1. **Contiguous memory** — Array data is packed tightly in memory, not scattered around like list pointers.
2. **Compiled C loops** — Operations run in optimized, pre-compiled C code instead of Python's interpreter.
3. **Vectorization** — The CPU can process multiple array elements in a single instruction.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- NumPy is the foundation of numerical computing in Python — learn it well and everything else gets easier
- `np.array()` creates arrays; `np.zeros()`, `np.ones()`, `np.arange()`, and `np.linspace()` create common patterns
- Check `.shape`, `.dtype`, `.ndim`, and `.size` to understand any array
- Arithmetic on arrays is element-wise — no loops needed
- Boolean indexing (`a[a > 5]`) is the clean, fast way to filter data
- `.reshape()`, `.flatten()`, and `.T` let you rearrange data without copying
- `axis=0` means "down the rows," `axis=1` means "across the columns"
- NumPy arrays crush Python lists in speed — always use them for numerical work
