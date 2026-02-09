# Async/Await Basics

## Objective

Understand what asynchronous programming is, why it exists, and how to write your first async Python code using `async`, `await`, and `asyncio`.

## Concepts Covered

- What async programming is and why you need it
- I/O-bound vs CPU-bound tasks
- Concurrency vs parallelism
- The event loop
- Coroutines (`async def`)
- The `await` keyword
- `asyncio.run()` — the entry point
- `asyncio.sleep()` vs `time.sleep()`
- Sequential vs concurrent execution
- `asyncio.gather()` — running multiple coroutines at once
- Return values from coroutines
- When to use async (and when not to)
- Common mistakes

## Prerequisites

- Functions, return values
- Basic understanding of how Python runs top-to-bottom
- `time` module (helpful but not required)

## Lesson

### Why Async? The Waiting Problem

Most programs spend a *lot* of time waiting. Waiting for a web server to respond. Waiting for a file to download. Waiting for a database query to finish. During all that waiting, your program is just... sitting there. Doing nothing.

That's the problem async programming solves. Instead of waiting around with your hands in your pockets, you go do something else useful and come back when the result is ready.

### I/O-Bound vs CPU-Bound

Before we dive in, you need to understand this distinction:

- **I/O-bound** — your code is slow because it's *waiting* for something external: network requests, file reads, database queries, API calls. The CPU is idle.
- **CPU-bound** — your code is slow because it's *computing* something heavy: crunching numbers, processing images, training a model. The CPU is maxed out.

Async programming is designed for **I/O-bound** tasks. If your CPU is the bottleneck, async won't help — you need multiprocessing or threads instead.

### Concurrency vs Parallelism

These two words get mixed up constantly, so let's be precise:

- **Concurrency** — managing multiple tasks that *overlap in time*. One task pauses, another runs. They take turns. Think of a single chef preparing three dishes by switching between them while things cook.
- **Parallelism** — multiple tasks running *at the exact same time* on different CPU cores. Think of three chefs each making a different dish simultaneously.

Async Python gives you **concurrency**, not parallelism. There's still one thread doing the work — it just switches between tasks when one is waiting. And that's perfectly fine for I/O-bound work, because the bottleneck isn't the CPU — it's the waiting.

### The Event Loop — The Brain of Async

The **event loop** is the engine that makes async work. It manages all your coroutines, decides which one runs next, and handles the switching.

Think of it like a **waiter in a restaurant**:

1. Table 1 places an order. The waiter sends it to the kitchen and *doesn't stand there waiting* — they move on.
2. Table 2 needs water. The waiter handles it.
3. Table 3 wants the check. Done.
4. The kitchen signals Table 1's food is ready. The waiter goes back and serves it.

The waiter is the event loop. The tables are your coroutines. The kitchen is your I/O operation. One waiter, multiple tables, no standing around doing nothing.

You almost never need to create or manage the event loop yourself. `asyncio.run()` does it for you.

### Coroutines — Functions That Can Pause

A **coroutine** is a special function that can be paused and resumed. You create one by using `async def` instead of `def`:

```python
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)    # Pause for 1 second (non-blocking)
    print("...World!")
```

Important: calling `say_hello()` does **not** run the function. It returns a *coroutine object*. To actually run it, you need to `await` it or pass it to `asyncio.run()`.

### await — "Pause Here Until This Is Done"

The `await` keyword is how you pause a coroutine and give control back to the event loop. When you write:

```python
result = await some_async_function()
```

You're saying: "Pause *this* coroutine. Go do other stuff if you want. Come back when `some_async_function()` has a result for me."

You can only use `await` inside an `async def` function. Using it in a regular function is a syntax error.

### asyncio.run() — The Entry Point

`asyncio.run()` is how you start the whole async engine from regular (synchronous) code. It creates an event loop, runs your coroutine, and cleans everything up:

```python
import asyncio

async def main():
    print("Starting...")
    await asyncio.sleep(1)
    print("Done!")

asyncio.run(main())
```

You typically call `asyncio.run()` exactly **once** — in your `if __name__ == "__main__"` block. Everything async flows from there.

### asyncio.sleep() vs time.sleep()

This is a critical distinction:

- **`time.sleep(2)`** — blocks the *entire* program. Nothing else runs. The event loop is frozen. The waiter stands at one table doing nothing for 2 seconds.
- **`asyncio.sleep(2)`** — pauses just *this* coroutine. The event loop is free to run other coroutines. The waiter moves on to other tables and comes back in 2 seconds.

**Never use `time.sleep()` in async code.** It defeats the entire purpose.

```python
# BAD — blocks everything
async def bad_example():
    time.sleep(2)   # The whole event loop freezes!

# GOOD — only pauses this coroutine
async def good_example():
    await asyncio.sleep(2)   # Event loop can do other work
```

### Sequential vs Concurrent Execution

Here's where async shows its power. Compare these two approaches:

**Sequential** — one after another:

```python
async def main():
    await task_that_takes_2_seconds()    # Wait 2s
    await task_that_takes_2_seconds()    # Wait 2s more
    await task_that_takes_2_seconds()    # Wait 2s more
    # Total: ~6 seconds
```

**Concurrent** — all at once:

```python
async def main():
    await asyncio.gather(
        task_that_takes_2_seconds(),
        task_that_takes_2_seconds(),
        task_that_takes_2_seconds(),
    )
    # Total: ~2 seconds (they all waited at the same time!)
```

Same tasks, same total work, but concurrent finishes in a third of the time because all three tasks were *waiting* simultaneously.

### asyncio.gather() — Run Multiple Coroutines Concurrently

`asyncio.gather()` takes multiple coroutines and runs them all concurrently. It returns when *all* of them are done:

```python
import asyncio

async def fetch_user():
    await asyncio.sleep(1)
    return {"name": "Alice"}

async def fetch_posts():
    await asyncio.sleep(1)
    return ["Post 1", "Post 2"]

async def main():
    user, posts = await asyncio.gather(
        fetch_user(),
        fetch_posts(),
    )
    print(user)    # {"name": "Alice"}
    print(posts)   # ["Post 1", "Post 2"]
```

Both fetches take 1 second each, but `gather()` runs them at the same time — total time is ~1 second, not ~2.

### Return Values from Coroutines

Coroutines can return values just like regular functions. You get the value by `await`-ing the coroutine:

```python
async def add(a, b):
    await asyncio.sleep(0.1)   # Simulate some async work
    return a + b

async def main():
    result = await add(3, 4)
    print(result)   # 7
```

With `gather()`, you get a list of return values in the same order you passed the coroutines:

```python
results = await asyncio.gather(
    add(1, 2),
    add(3, 4),
    add(5, 6),
)
print(results)   # [3, 7, 11]
```

### When to Use Async

**Great fit (I/O-bound):**

- Making HTTP requests to APIs
- Reading/writing files (with async libraries like `aiofiles`)
- Database queries (with async drivers like `asyncpg`)
- Web scraping multiple pages
- Chat servers, WebSockets
- Any time you're waiting on external resources

**Bad fit (CPU-bound):**

- Number crunching, math-heavy computation
- Image/video processing
- Machine learning training
- Data compression

For CPU-bound work, look at `multiprocessing` or `concurrent.futures.ProcessPoolExecutor` instead.

### Common Mistakes

**1. Forgetting `await`:**

```python
async def main():
    asyncio.sleep(1)   # WRONG — this does nothing! Returns a coroutine object
    await asyncio.sleep(1)   # RIGHT — actually pauses
```

Python will usually give you a "coroutine was never awaited" warning if you forget.

**2. Calling a coroutine without `await`:**

```python
async def greet():
    print("Hi!")

async def main():
    greet()           # WRONG — doesn't run, just creates a coroutine object
    await greet()     # RIGHT — actually runs
```

**3. Using blocking code in async functions:**

```python
import time
import requests   # requests is synchronous!

async def bad():
    time.sleep(5)           # Blocks the event loop
    requests.get("...")     # Also blocks the event loop
```

If you block the event loop, none of your other coroutines can run. Use async-compatible libraries (`aiohttp` instead of `requests`, `asyncio.sleep` instead of `time.sleep`).

**4. Trying to use `await` outside of `async def`:**

```python
def not_async():
    await asyncio.sleep(1)   # SyntaxError!
```

`await` only works inside `async def` functions.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above with real timing comparisons.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Async programming lets you do other work while waiting for I/O operations
- `async def` creates a coroutine function — a function that can pause and resume
- `await` pauses a coroutine until a result is ready, letting the event loop run other tasks
- `asyncio.run()` is your entry point — call it once from synchronous code
- `asyncio.sleep()` is non-blocking (good); `time.sleep()` is blocking (bad in async code)
- `asyncio.gather()` runs multiple coroutines concurrently — perfect for parallel I/O
- Async is great for I/O-bound work (network, files, databases) but doesn't help with CPU-bound work
- Always `await` your coroutines — forgetting `await` is the #1 async mistake
