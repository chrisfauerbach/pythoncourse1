"""
Async/Await Basics — Exercises
================================

Practice problems to test your understanding of async programming.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import asyncio
import time


# =============================================================================
# Exercise 1: Write a coroutine that fetches data
#
# Write an async function called `fetch_data` that:
#   1. Prints "Fetching data..."
#   2. Simulates a network delay with asyncio.sleep(1)
#   3. Prints "Data received!"
#   4. Returns the dictionary: {"status": "ok", "data": [1, 2, 3]}
#
# Then await it and print the result.
#
# =============================================================================

async def exercise_1():
    # YOUR CODE HERE — define fetch_data, then await it and print the result
    pass


# =============================================================================
# Exercise 2: Run 3 coroutines sequentially and time it
#
# Write an async function called `slow_task` that takes a `name` (string)
# and `duration` (number), prints when it starts and finishes, sleeps for
# `duration` seconds, and returns f"{name} complete".
#
# Then call slow_task three times SEQUENTIALLY with:
#   ("Task A", 1), ("Task B", 1), ("Task C", 1)
#
# Time the total and print it. It should take ~3 seconds.
#
# =============================================================================

async def exercise_2():
    start = time.time()
    # YOUR CODE HERE — define slow_task, then call it three times sequentially
    elapsed = time.time() - start
    print(f"  Sequential total: {elapsed:.2f}s")


# =============================================================================
# Exercise 3: Run 3 coroutines concurrently and time it
#
# Using the same slow_task idea from Exercise 2 (define it again here),
# run the same three tasks CONCURRENTLY with asyncio.gather().
#
# Time the total and print it. It should take ~1 second.
# Print the return values from gather.
#
# =============================================================================

async def exercise_3():
    start = time.time()
    # YOUR CODE HERE — use asyncio.gather() to run all three concurrently
    elapsed = time.time() - start
    print(f"  Concurrent total: {elapsed:.2f}s")


# =============================================================================
# Exercise 4: Simulate downloading multiple files
#
# Write an async function `download_file` that takes a filename and size_mb,
# simulates downloading by sleeping for (size_mb * 0.2) seconds, and returns
# a dict with the filename and size.
#
# Then use asyncio.gather() to download all of these concurrently:
#   ("notes.txt", 1)        — takes 0.2s
#   ("photo.jpg", 3)        — takes 0.6s
#   ("movie.mp4", 10)       — takes 2.0s
#   ("song.mp3", 5)         — takes 1.0s
#
# Print each result and the total time. It should take ~2 seconds
# (the duration of the largest file), not ~3.8 seconds.
#
# =============================================================================

async def exercise_4():
    start = time.time()
    # YOUR CODE HERE
    elapsed = time.time() - start
    print(f"  Total download time: {elapsed:.2f}s")


# =============================================================================
# Exercise 5: Process items from a list with delays
#
# Write an async function `process_item` that takes an item (a string),
# prints "Processing {item}...", sleeps for 0.5 seconds, and returns
# the item converted to uppercase.
#
# Then write an async function `process_all` that takes a list of strings
# and uses asyncio.gather() to process ALL of them concurrently.
# Return the list of processed results.
#
# Test it with: ["apple", "banana", "cherry", "date", "elderberry"]
# Print the results and the total time. It should take ~0.5 seconds,
# not ~2.5 seconds.
#
# =============================================================================

async def exercise_5():
    items = ["apple", "banana", "cherry", "date", "elderberry"]
    start = time.time()
    # YOUR CODE HERE
    elapsed = time.time() - start
    print(f"  Processed {len(items)} items in {elapsed:.2f}s")


# =============================================================================
# Exercise 6: Build an async pipeline (fetch -> process -> save)
#
# Build a mini data pipeline with three async stages:
#
#   1. `fetch_record(record_id)` — sleeps 0.3s, returns
#      {"id": record_id, "raw": f"data_{record_id}"}
#
#   2. `process_record(record)` — sleeps 0.2s, returns a new dict with an
#      added "processed" key set to record["raw"].upper()
#
#   3. `save_record(record)` — sleeps 0.1s, prints "Saved record {id}",
#      returns the record with an added "saved" key set to True
#
# Then write `pipeline(record_id)` that chains all three stages
# (fetch -> process -> save) and returns the final record.
#
# Finally, run the pipeline for record IDs 1 through 5 CONCURRENTLY using
# asyncio.gather(). Each individual pipeline takes 0.6s (0.3+0.2+0.1),
# but running 5 concurrently should take ~0.6s total.
#
# Print all saved records and the total time.
#
# =============================================================================

async def exercise_6():
    start = time.time()
    # YOUR CODE HERE
    elapsed = time.time() - start
    print(f"  Pipeline total: {elapsed:.2f}s")


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

async def solution_1():
    async def fetch_data():
        print("  Fetching data...")
        await asyncio.sleep(1)
        print("  Data received!")
        return {"status": "ok", "data": [1, 2, 3]}

    result = await fetch_data()
    print(f"  Result: {result}")


async def solution_2():
    async def slow_task(name, duration):
        print(f"  Starting {name}...")
        await asyncio.sleep(duration)
        print(f"  Finished {name} ({duration}s)")
        return f"{name} complete"

    start = time.time()

    result1 = await slow_task("Task A", 1)
    result2 = await slow_task("Task B", 1)
    result3 = await slow_task("Task C", 1)

    elapsed = time.time() - start
    print(f"  Results: {result1}, {result2}, {result3}")
    print(f"  Sequential total: {elapsed:.2f}s")


async def solution_3():
    async def slow_task(name, duration):
        print(f"  Starting {name}...")
        await asyncio.sleep(duration)
        print(f"  Finished {name} ({duration}s)")
        return f"{name} complete"

    start = time.time()

    results = await asyncio.gather(
        slow_task("Task A", 1),
        slow_task("Task B", 1),
        slow_task("Task C", 1),
    )

    elapsed = time.time() - start
    print(f"  Results: {results}")
    print(f"  Concurrent total: {elapsed:.2f}s")


async def solution_4():
    async def download_file(filename, size_mb):
        duration = size_mb * 0.2
        print(f"  Downloading {filename} ({size_mb}MB)...")
        await asyncio.sleep(duration)
        print(f"  Finished {filename}")
        return {"file": filename, "size_mb": size_mb}

    start = time.time()

    results = await asyncio.gather(
        download_file("notes.txt", 1),
        download_file("photo.jpg", 3),
        download_file("movie.mp4", 10),
        download_file("song.mp3", 5),
    )

    elapsed = time.time() - start
    for r in results:
        print(f"  Downloaded: {r}")
    print(f"  Total download time: {elapsed:.2f}s")


async def solution_5():
    async def process_item(item):
        print(f"  Processing {item}...")
        await asyncio.sleep(0.5)
        return item.upper()

    async def process_all(items):
        return await asyncio.gather(*[process_item(item) for item in items])

    items = ["apple", "banana", "cherry", "date", "elderberry"]
    start = time.time()

    results = await process_all(items)

    elapsed = time.time() - start
    print(f"  Results: {results}")
    print(f"  Processed {len(items)} items in {elapsed:.2f}s")


async def solution_6():
    async def fetch_record(record_id):
        await asyncio.sleep(0.3)
        return {"id": record_id, "raw": f"data_{record_id}"}

    async def process_record(record):
        await asyncio.sleep(0.2)
        return {**record, "processed": record["raw"].upper()}

    async def save_record(record):
        await asyncio.sleep(0.1)
        print(f"  Saved record {record['id']}")
        return {**record, "saved": True}

    async def pipeline(record_id):
        record = await fetch_record(record_id)
        record = await process_record(record)
        record = await save_record(record)
        return record

    start = time.time()

    results = await asyncio.gather(*[pipeline(i) for i in range(1, 6)])

    elapsed = time.time() - start
    for r in results:
        print(f"  Record: {r}")
    print(f"  Pipeline total: {elapsed:.2f}s")


# =============================================================================
# Run it!
# =============================================================================

async def run_exercises():
    exercises = [
        ("Fetch data coroutine", exercise_1),
        ("Sequential execution", exercise_2),
        ("Concurrent execution with gather", exercise_3),
        ("Download multiple files", exercise_4),
        ("Process items from a list", exercise_5),
        ("Async pipeline", exercise_6),
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
