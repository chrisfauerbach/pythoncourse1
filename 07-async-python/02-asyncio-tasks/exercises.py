"""
Asyncio Tasks — Exercises
==========================

Practice problems to test your understanding of asyncio Tasks.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

All sleep times are short so exercises run quickly.
"""

import asyncio
import time


# =============================================================================
# Exercise 1: Create tasks and gather results
#
# Write an async function that simulates downloading 4 files concurrently.
# Each "download" should:
#   - Accept a filename and a delay (simulating download time)
#   - Sleep for the delay amount
#   - Return a string like "Downloaded: report.pdf"
#
# Use asyncio.gather() to download all 4 files concurrently:
#   ("report.pdf", 0.3), ("photo.jpg", 0.1), ("data.csv", 0.2), ("notes.txt", 0.15)
#
# Print each result and the total elapsed time.
# Total time should be ~0.3s (the longest single download), not ~0.75s.
#
# =============================================================================

async def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Timeout handling with asyncio.wait_for()
#
# Write an async function `unreliable_api(delay)` that sleeps for `delay`
# seconds, then returns "API response".
#
# Call it 3 times with different delays using asyncio.wait_for() and a
# timeout of 0.2 seconds:
#   - delay=0.1 (should succeed)
#   - delay=0.5 (should time out)
#   - delay=0.15 (should succeed)
#
# For each call, print either the result or "Timed out!" if it exceeds
# the timeout.
#
# =============================================================================

async def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Process results as they complete with as_completed()
#
# Write an async function `process_job(job_id, delay)` that:
#   - Sleeps for `delay` seconds
#   - Returns a dict: {"job_id": job_id, "result": job_id * 10}
#
# Create these jobs:
#   (1, 0.3), (2, 0.1), (3, 0.4), (4, 0.05), (5, 0.2)
#
# Use asyncio.as_completed() to print results as soon as each job finishes.
# The output should show jobs completing in order of speed (fastest first),
# not in order of submission.
#
# =============================================================================

async def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Task cancellation
#
# Write an async function `heartbeat(name, interval)` that:
#   - Prints "{name}: beat" every `interval` seconds in a loop
#   - Catches CancelledError, prints "{name}: stopped", and re-raises
#
# In your exercise function:
#   1. Start two heartbeat tasks: ("Heart-A", 0.1) and ("Heart-B", 0.15)
#   2. Let them run for 0.35 seconds
#   3. Cancel both tasks
#   4. Await both tasks (handling CancelledError)
#   5. Print "All heartbeats stopped"
#
# =============================================================================

async def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Rate-limited fetcher with asyncio.Semaphore
#
# Write an async function `fetch_page(sem, page_num)` that:
#   - Acquires the semaphore
#   - Prints "Fetching page {page_num}..."
#   - Sleeps for 0.1 seconds (simulating a network request)
#   - Returns "Page {page_num} content"
#
# In your exercise function:
#   1. Create a Semaphore with a limit of 2 (max 2 concurrent fetches)
#   2. Fetch pages 1 through 6 concurrently using gather
#   3. Print all results
#
# Even though all 6 are "concurrent," only 2 should be fetching at any
# given time. The total time should be ~0.3s (3 batches of 2).
#
# =============================================================================

async def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Producer-consumer with asyncio.Queue
#
# Build a system with:
#   - 2 producers: each puts 4 items into a queue (8 items total)
#     - Each item is a string like "P1-0", "P1-1", "P2-0", "P2-1", etc.
#     - Producers sleep 0.05s between puts
#   - 3 consumers: each pulls items from the queue and "processes" them
#     - Processing means: sleep 0.08s, then print the item
#     - Track how many items each consumer processed
#
# Use queue.join() to wait until all items are processed, then cancel
# the consumers. Print how many items each consumer handled.
#
# Hint: Use a dict or list to track consumer counts.
#
# =============================================================================

async def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

async def solution_1():
    async def download(filename, delay):
        await asyncio.sleep(delay)
        return f"Downloaded: {filename}"

    start = time.perf_counter()
    results = await asyncio.gather(
        download("report.pdf", 0.3),
        download("photo.jpg", 0.1),
        download("data.csv", 0.2),
        download("notes.txt", 0.15),
    )
    elapsed = time.perf_counter() - start

    for r in results:
        print(f"  {r}")
    print(f"  Total time: {elapsed:.2f}s")


async def solution_2():
    async def unreliable_api(delay):
        await asyncio.sleep(delay)
        return "API response"

    delays = [0.1, 0.5, 0.15]
    for delay in delays:
        try:
            result = await asyncio.wait_for(unreliable_api(delay), timeout=0.2)
            print(f"  delay={delay}s -> {result}")
        except TimeoutError:
            print(f"  delay={delay}s -> Timed out!")


async def solution_3():
    async def process_job(job_id, delay):
        await asyncio.sleep(delay)
        return {"job_id": job_id, "result": job_id * 10}

    jobs = [
        process_job(1, 0.3),
        process_job(2, 0.1),
        process_job(3, 0.4),
        process_job(4, 0.05),
        process_job(5, 0.2),
    ]

    for future in asyncio.as_completed(jobs):
        result = await future
        print(f"  Job {result['job_id']} completed: result={result['result']}")


async def solution_4():
    async def heartbeat(name, interval):
        try:
            while True:
                print(f"  {name}: beat")
                await asyncio.sleep(interval)
        except asyncio.CancelledError:
            print(f"  {name}: stopped")
            raise

    task_a = asyncio.create_task(heartbeat("Heart-A", 0.1))
    task_b = asyncio.create_task(heartbeat("Heart-B", 0.15))

    await asyncio.sleep(0.35)

    task_a.cancel()
    task_b.cancel()

    for task in [task_a, task_b]:
        try:
            await task
        except asyncio.CancelledError:
            pass

    print("  All heartbeats stopped")


async def solution_5():
    async def fetch_page(sem, page_num):
        async with sem:
            print(f"  Fetching page {page_num}...")
            await asyncio.sleep(0.1)
            return f"Page {page_num} content"

    sem = asyncio.Semaphore(2)
    start = time.perf_counter()

    results = await asyncio.gather(
        *(fetch_page(sem, i) for i in range(1, 7))
    )

    elapsed = time.perf_counter() - start
    for r in results:
        print(f"  {r}")
    print(f"  Total time: {elapsed:.2f}s (rate limited to 2 concurrent)")


async def solution_6():
    counts = {}

    async def producer(queue, name, count):
        for i in range(count):
            item = f"{name}-{i}"
            await queue.put(item)
            await asyncio.sleep(0.05)

    async def consumer(queue, name):
        counts[name] = 0
        while True:
            item = await queue.get()
            await asyncio.sleep(0.08)
            print(f"  {name} processed: {item}")
            counts[name] += 1
            queue.task_done()

    queue = asyncio.Queue()

    # Start producers and consumers
    producers = [
        asyncio.create_task(producer(queue, "P1", 4)),
        asyncio.create_task(producer(queue, "P2", 4)),
    ]
    consumers = [
        asyncio.create_task(consumer(queue, "C1")),
        asyncio.create_task(consumer(queue, "C2")),
        asyncio.create_task(consumer(queue, "C3")),
    ]

    # Wait for producers to finish, then wait for queue to drain
    await asyncio.gather(*producers)
    await queue.join()

    # Cancel consumers
    for c in consumers:
        c.cancel()

    print(f"  Items processed per consumer: {dict(counts)}")


# =============================================================================
# Run it!
# =============================================================================

async def run_exercises():
    exercises = [
        ("Create tasks and gather results", exercise_1),
        ("Timeout handling with wait_for", exercise_2),
        ("Process results with as_completed", exercise_3),
        ("Task cancellation", exercise_4),
        ("Rate-limited fetcher with Semaphore", exercise_5),
        ("Producer-consumer with Queue", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        await func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")


if __name__ == "__main__":
    asyncio.run(run_exercises())
