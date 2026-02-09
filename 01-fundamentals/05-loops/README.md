# Loops

## Objective

Learn how to repeat actions in your code using `for` loops and `while` loops, and pick up the essential tools that make looping in Python powerful and readable.

## Concepts Covered

- `for` loops — iterating over sequences (lists, strings, ranges)
- The `range()` function
- `while` loops — repeating while a condition is true
- `break` — exit a loop early
- `continue` — skip to the next iteration
- `else` clause on loops
- Nested loops
- `enumerate()` — getting index and value
- `zip()` — iterating over multiple sequences
- Common pitfalls (infinite loops, off-by-one errors)

## Prerequisites

- [Control Flow](../04-control-flow/) — you should know how `if`/`elif`/`else` works

## Lesson

### For Loops — Iterating Over Sequences

The `for` loop is how you walk through a collection of items, one at a time. Python's `for` is really a "for each" — it grabs each item from a sequence and runs a block of code with it:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:

```
apple
banana
cherry
```

You can loop over anything iterable — lists, strings, tuples, and more:

```python
# Looping over a string — one character at a time
for char in "hello":
    print(char)

# Looping over a tuple
for color in ("red", "green", "blue"):
    print(color)
```

### The range() Function

`range()` generates a sequence of numbers. It's the go-to when you need a loop that runs a specific number of times.

```python
# range(n) — numbers from 0 to n-1
for i in range(5):
    print(i)    # 0, 1, 2, 3, 4

# range(start, stop) — numbers from start to stop-1
for i in range(2, 6):
    print(i)    # 2, 3, 4, 5

# range(start, stop, step) — count by step
for i in range(0, 10, 2):
    print(i)    # 0, 2, 4, 6, 8

# Counting backwards
for i in range(5, 0, -1):
    print(i)    # 5, 4, 3, 2, 1
```

**Heads up:** `range()` stops *before* the stop value. `range(5)` gives you `0, 1, 2, 3, 4` — not `5`. This trips up everyone at first, but it actually makes sense because `range(5)` produces exactly 5 numbers.

### While Loops — Repeat While a Condition Is True

A `while` loop keeps running as long as its condition is `True`:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Use `while` when you don't know ahead of time how many iterations you'll need — like waiting for user input or searching for something.

### Break — Exit a Loop Early

`break` immediately exits the loop, skipping any remaining iterations:

```python
for number in range(100):
    if number == 5:
        break
    print(number)    # Prints 0, 1, 2, 3, 4
```

This works in both `for` and `while` loops. It's especially useful for search patterns — once you've found what you're looking for, there's no reason to keep looping.

### Continue — Skip to the Next Iteration

`continue` skips the rest of the current iteration and jumps to the next one:

```python
for number in range(5):
    if number == 2:
        continue
    print(number)    # Prints 0, 1, 3, 4 (skips 2)
```

Use `continue` when you want to skip certain items but keep the loop going. It's great for filtering out things you don't care about.

### Else Clause on Loops

This one surprises people — Python lets you put an `else` on a loop. The `else` block runs only if the loop completed *without* hitting a `break`:

```python
# for/else example
for number in [2, 4, 6, 8]:
    if number % 2 != 0:
        print("Found an odd number!")
        break
else:
    print("All numbers were even!")    # This runs — no break happened

# while/else example
attempts = 0
while attempts < 3:
    attempts += 1
    if attempts == 5:    # This never happens
        break
else:
    print("Loop finished without break")    # This runs
```

Think of `else` on a loop as "no break." If the loop runs to completion naturally, the `else` block fires. If `break` exits the loop, `else` is skipped. It's perfect for search-and-not-found patterns.

### Nested Loops

You can put loops inside loops. The inner loop runs completely for each iteration of the outer loop:

```python
for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end="  ")
    print()    # New line after each row
```

Output:

```
(0, 0)  (0, 1)  (0, 2)
(1, 0)  (1, 1)  (1, 2)
(2, 0)  (2, 1)  (2, 2)
```

Keep an eye on performance with nested loops — if both loops iterate over `n` items, you're doing `n * n` operations. That adds up fast.

### enumerate() — Getting Index and Value

When you need both the position and the value in a loop, `enumerate()` is your best friend:

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

Output:

```
0: apple
1: banana
2: cherry
```

You can set a custom start number:

```python
for rank, fruit in enumerate(fruits, start=1):
    print(f"#{rank}: {fruit}")
# #1: apple
# #2: banana
# #3: cherry
```

This is way better than manually tracking an index variable — cleaner and less error-prone.

### zip() — Iterating Over Multiple Sequences

`zip()` lets you loop over two (or more) sequences in parallel, pairing up items by position:

```python
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

Output:

```
Alice: 95
Bob: 87
Charlie: 92
```

If the sequences have different lengths, `zip()` stops at the shortest one. No error — it just stops early.

### Common Pitfalls

#### Infinite Loops

If the condition in a `while` loop never becomes `False`, it runs forever:

```python
# DON'T DO THIS (infinite loop!)
# count = 0
# while count < 5:
#     print(count)
#     # Oops — forgot to increment count!
```

Always make sure your loop has a way to end. If you accidentally create an infinite loop, press `Ctrl+C` to stop it.

#### Off-by-One with range()

Remember: `range(n)` produces `0` through `n-1`, not `1` through `n`:

```python
# Want numbers 1 through 5?
for i in range(1, 6):    # NOT range(1, 5)!
    print(i)             # 1, 2, 3, 4, 5
```

#### Modifying a List While Looping Over It

Don't add or remove items from a list you're currently looping over — it leads to weird bugs. Make a copy first, or build a new list.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- `for` loops iterate over sequences (lists, strings, ranges, etc.)
- `range(n)` gives you `0` to `n-1` — the stop value is excluded
- `while` loops repeat as long as a condition is `True`
- `break` exits a loop early; `continue` skips to the next iteration
- `else` on a loop runs only when the loop finishes without `break`
- `enumerate()` gives you both the index and the value — use it instead of manual counters
- `zip()` pairs up items from multiple sequences for parallel iteration
- Always make sure `while` loops have a way to terminate
- Avoid modifying a list while looping over it
