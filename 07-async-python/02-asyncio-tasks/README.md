# Asyncio Tasks

## Objective

Understand how `asyncio.Task` objects let you run coroutines concurrently, manage their lifecycles, and handle errors, cancellation, and timeouts.

## Concepts Covered

- What asyncio Tasks are and why they exist
- `asyncio.create_task()` — scheduling coroutines to run concurrently
- Tasks vs coroutines (tasks start immediately in the background)
- Awaiting tasks to get results
- `asyncio.gather()` — collecting results from multiple tasks
- `asyncio.TaskGroup` (Python 3.11+) — structured concurrency
- Task cancellation — `task.cancel()` and `CancelledError`
- Timeouts with `asyncio.wait_for()`
- `asyncio.wait()` — waiting for first completed, all completed, or first exception
- `asyncio.as_completed()` — processing results as they arrive
- Error handling in tasks
- Practical patterns: producer-consumer, semaphores for rate limiting

## Prerequisites

- Understanding of `async`/`await` syntax and basic coroutines
- Familiarity with `asyncio.run()` and `asyncio.sleep()`
- [Async/Await Basics](../01-async-await-basics/)

## Lesson

### What Is a Task?

A **Task** is asyncio's way of saying "go run this coroutine in the background." When you call an async function, you just get a coroutine object — it doesn't start running. Wrapping it in a Task tells the event loop to actually schedule it:

```python
import asyncio

async def say_hello():
    await asyncio.sleep(0.1)
    print("Hello!")

async def main():
    # This creates the coroutine but does NOT start it:
    coro = say_hello()

    # This wraps it in a Task and starts it immediately:
    task = asyncio.create_task(say_hello())

    await task  # Wait for the task to finish
```

A Task is a subclass of `asyncio.Future`. It wraps a coroutine and manages its execution on the event loop. You can check its status, get its result, or cancel it.

### asyncio.create_task()

`asyncio.create_task()` is the standard way to schedule a coroutine to run concurrently. The task begins executing as soon as the current coroutine yields control (hits an `await`):

```python
async def fetch_data(name, delay):
    await asyncio.sleep(delay)
    return f"{name}: done"

async def main():
    # Both tasks start running concurrently
    task1 = asyncio.create_task(fetch_data("A", 0.3))
    task2 = asyncio.create_task(fetch_data("B", 0.1))

    # Wait for both — total time is ~0.3s, not 0.4s
    result1 = await task1
    result2 = await task2
    print(result1, result2)
```

The key insight: `create_task()` returns immediately. The coroutine doesn't block — it runs in the background while your code continues.

### Tasks vs Coroutines

This is a common gotcha. Calling a coroutine directly with `await` runs it **sequentially**. Creating tasks runs them **concurrently**:

```python
async def main():
    # SEQUENTIAL — takes 0.4s total
    result1 = await fetch_data("A", 0.2)
    result2 = await fetch_data("B", 0.2)

    # CONCURRENT — takes 0.2s total
    task1 = asyncio.create_task(fetch_data("A", 0.2))
    task2 = asyncio.create_task(fetch_data("B", 0.2))
    result1 = await task1
    result2 = await task2
```

Think of it this way: `await some_coro()` means "do this now and wait." `create_task(some_coro())` means "start this in the background, I'll collect the result later."

### Awaiting Tasks to Get Results

When you `await` a task, you get back whatever the coroutine returned:

```python
async def compute(x):
    await asyncio.sleep(0.1)
    return x * 2

async def main():
    task = asyncio.create_task(compute(21))
    result = await task  # result is 42
    print(result)
```

If the coroutine raises an exception, awaiting the task re-raises that exception. If you never await a task that raises, Python will warn you about a "Task exception was never retrieved."

### asyncio.gather() — Collecting Results

`asyncio.gather()` is a convenience for running multiple coroutines or tasks concurrently and collecting all their results in order:

```python
async def main():
    results = await asyncio.gather(
        fetch_data("A", 0.3),
        fetch_data("B", 0.1),
        fetch_data("C", 0.2),
    )
    # results is a list: ["A: done", "B: done", "C: done"]
    # Results are in the SAME ORDER as the arguments, not completion order
    print(results)
```

You can pass `return_exceptions=True` to capture exceptions as return values instead of letting them propagate:

```python
async def might_fail(n):
    if n == 2:
        raise ValueError("oops!")
    return n * 10

async def main():
    results = await asyncio.gather(
        might_fail(1),
        might_fail(2),
        might_fail(3),
        return_exceptions=True,
    )
    # results: [10, ValueError("oops!"), 30]
    for r in results:
        if isinstance(r, Exception):
            print(f"Error: {r}")
        else:
            print(f"Result: {r}")
```

### asyncio.TaskGroup (Python 3.11+) — Structured Concurrency

`TaskGroup` is the modern, safer alternative to `gather()`. It uses an `async with` block so tasks have a clear lifecycle. If any task raises, all other tasks in the group get cancelled automatically:

```python
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data("A", 0.2))
        task2 = tg.create_task(fetch_data("B", 0.1))
        task3 = tg.create_task(fetch_data("C", 0.3))

    # When we get here, ALL tasks are guaranteed to be done
    print(task1.result(), task2.result(), task3.result())
```

If any task fails, `TaskGroup` raises an `ExceptionGroup` containing all the exceptions. This is part of Python's push toward **structured concurrency** — the idea that concurrent tasks should have a clear start and end, and no task should outlive its scope.

```python
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(might_fail(1))
            tg.create_task(might_fail(2))  # This raises ValueError
            tg.create_task(might_fail(3))
    except* ValueError as eg:
        # except* catches ExceptionGroups (Python 3.11+)
        for exc in eg.exceptions:
            print(f"Caught: {exc}")
```

### Task Cancellation

You can cancel a running task. This injects a `CancelledError` into the coroutine at the next `await` point:

```python
async def long_running():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(0.1)
    except asyncio.CancelledError:
        print("Task was cancelled! Cleaning up...")
        raise  # Always re-raise CancelledError unless you have a good reason

async def main():
    task = asyncio.create_task(long_running())
    await asyncio.sleep(0.3)  # Let it run for a bit
    task.cancel()             # Request cancellation

    try:
        await task
    except asyncio.CancelledError:
        print("Confirmed: task is cancelled")
```

Important: you should almost always re-raise `CancelledError` after cleanup. Swallowing it prevents the cancellation from working properly.

### Timeouts with asyncio.wait_for()

`asyncio.wait_for()` runs a coroutine with a deadline. If it doesn't complete in time, the task is cancelled and `TimeoutError` is raised:

```python
async def slow_operation():
    await asyncio.sleep(5.0)
    return "done"

async def main():
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.2)
        print(result)
    except TimeoutError:
        print("Operation timed out!")
```

This is incredibly useful for network requests, database queries, or anything that might hang.

### asyncio.wait() — Fine-Grained Control

`asyncio.wait()` gives you more control over how you wait for a set of tasks. It returns two sets: `(done, pending)`:

```python
async def main():
    tasks = [
        asyncio.create_task(fetch_data("A", 0.3)),
        asyncio.create_task(fetch_data("B", 0.1)),
        asyncio.create_task(fetch_data("C", 0.2)),
    ]

    # Wait for the first one to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"{len(done)} done, {len(pending)} pending")

    # Wait for all remaining to complete
    done, pending = await asyncio.wait(pending, return_when=asyncio.ALL_COMPLETED)
```

The `return_when` options are:

- **`FIRST_COMPLETED`** — returns as soon as any task finishes (or fails)
- **`FIRST_EXCEPTION`** — returns when a task raises an exception (or all complete successfully)
- **`ALL_COMPLETED`** — waits for every task to finish (this is the default)

### asyncio.as_completed() — Results as They Arrive

`as_completed()` gives you an iterator that yields futures in the order they finish. This is perfect when you want to process results immediately rather than waiting for everything:

```python
async def main():
    coros = [
        fetch_data("A", 0.3),
        fetch_data("B", 0.1),
        fetch_data("C", 0.2),
    ]

    for future in asyncio.as_completed(coros):
        result = await future
        print(result)  # Prints B first (fastest), then C, then A
```

### Error Handling in Tasks

There are a few ways task errors can bite you:

**1. Unhandled exceptions in tasks produce warnings:**

```python
async def broken():
    raise RuntimeError("boom")

async def main():
    task = asyncio.create_task(broken())
    # If you never await this task, Python will log:
    # "Task exception was never retrieved"
```

Always await your tasks, or use `gather()` / `TaskGroup` to manage them.

**2. gather() with return_exceptions:**

```python
# Without return_exceptions — first exception propagates immediately
results = await asyncio.gather(task1, task2, task3)

# With return_exceptions — exceptions become return values
results = await asyncio.gather(task1, task2, task3, return_exceptions=True)
```

**3. TaskGroup automatically cancels siblings on error** — this is usually what you want. When one task fails, the rest are cancelled and the errors are bundled in an `ExceptionGroup`.

### Practical Pattern: Producer-Consumer

A common async pattern is having producers push items into a queue and consumers pull from it. `asyncio.Queue` handles all the synchronization for you:

```python
async def producer(queue, name, count):
    for i in range(count):
        item = f"{name}-item-{i}"
        await queue.put(item)
        await asyncio.sleep(0.1)

async def consumer(queue, name):
    while True:
        item = await queue.get()
        print(f"{name} processed: {item}")
        await asyncio.sleep(0.05)
        queue.task_done()

async def main():
    queue = asyncio.Queue(maxsize=5)

    producers = [asyncio.create_task(producer(queue, "P1", 5))]
    consumers = [asyncio.create_task(consumer(queue, "C1"))]

    await asyncio.gather(*producers)  # Wait for producers to finish
    await queue.join()                # Wait for all items to be processed
    for c in consumers:
        c.cancel()                    # Cancel consumers (they loop forever)
```

### Practical Pattern: Semaphore for Rate Limiting

A semaphore limits how many tasks can access a resource at once. Perfect for API rate limiting:

```python
async def rate_limited_fetch(sem, url):
    async with sem:  # Only N tasks can be inside this block at once
        print(f"Fetching {url}")
        await asyncio.sleep(0.1)  # Simulate network request
        return f"Data from {url}"

async def main():
    sem = asyncio.Semaphore(3)  # Max 3 concurrent requests
    urls = [f"https://api.example.com/{i}" for i in range(10)]

    tasks = [rate_limited_fetch(sem, url) for url in urls]
    results = await asyncio.gather(*tasks)
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- A **Task** wraps a coroutine and schedules it to run concurrently on the event loop
- `asyncio.create_task()` starts a coroutine in the background immediately
- `await`ing a coroutine directly is sequential; creating tasks makes things concurrent
- `asyncio.gather()` runs multiple coroutines concurrently and returns all results in order
- `asyncio.TaskGroup` (3.11+) is the safer, structured-concurrency approach — if one task fails, siblings are cancelled
- Cancel tasks with `task.cancel()` — always re-raise `CancelledError` after cleanup
- `asyncio.wait_for()` sets a timeout — raises `TimeoutError` if exceeded
- `asyncio.wait()` returns `(done, pending)` sets with flexible `return_when` options
- `asyncio.as_completed()` yields results in completion order, not submission order
- Use `asyncio.Queue` for producer-consumer patterns
- Use `asyncio.Semaphore` to limit concurrency (rate limiting)
