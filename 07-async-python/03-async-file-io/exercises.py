"""
Async File I/O — Exercises
============================

Practice problems to test your understanding of async file operations.
Try to solve each exercise before looking at the solutions below!

All exercises use asyncio.to_thread() — no external dependencies needed.

Run this file:
    python3 exercises.py
"""

import asyncio
import os
import time
from datetime import datetime

# Temp directory for exercise files — cleaned up at the end
TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_temp_exercises")


# =============================================================================
# Exercise 1: Async write and read
#
# Write an async function that:
#   1. Writes "Hello, async world!" to a file called "greeting.txt"
#   2. Reads the content back from the file
#   3. Returns the content
#
# Use asyncio.to_thread() to avoid blocking the event loop.
#
# Hint: Write two sync helper functions (one for writing, one for reading),
# then call them with asyncio.to_thread().
# =============================================================================

async def exercise_1():
    path = os.path.join(TEMP_DIR, "greeting.txt")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Process multiple files concurrently
#
# Given a list of file paths and contents (provided below), write ALL files
# concurrently using asyncio.gather(), then read ALL files concurrently,
# and print each filename with its content.
#
# The goal: use gather() so all writes happen at the same time, then all
# reads happen at the same time.
# =============================================================================

async def exercise_2():
    files = {
        os.path.join(TEMP_DIR, "file_a.txt"): "Alpha content",
        os.path.join(TEMP_DIR, "file_b.txt"): "Bravo content",
        os.path.join(TEMP_DIR, "file_c.txt"): "Charlie content",
        os.path.join(TEMP_DIR, "file_d.txt"): "Delta content",
    }
    # YOUR CODE HERE — write all files concurrently, then read all concurrently
    pass


# =============================================================================
# Exercise 3: Async line counter
#
# Write an async function that takes a list of file paths and returns a
# dictionary mapping each filename to its line count.
#
# Process all files concurrently. Use os.path.basename() for the filename keys.
#
# Test files are created for you below.
# =============================================================================

async def exercise_3():
    # Create test files with different numbers of lines
    test_files = {}
    for name, num_lines in [("short.txt", 3), ("medium.txt", 10), ("long.txt", 25)]:
        path = os.path.join(TEMP_DIR, name)
        content = "\n".join(f"Line {i}" for i in range(1, num_lines + 1)) + "\n"
        with open(path, "w") as f:
            f.write(content)
        test_files[name] = path

    paths = list(test_files.values())
    # YOUR CODE HERE — count lines in all files concurrently
    # Should return something like: {"short.txt": 3, "medium.txt": 10, "long.txt": 25}
    pass


# =============================================================================
# Exercise 4: Concurrent file copy
#
# Write an async function that copies multiple files concurrently.
# Given a list of (source, destination) tuples, copy all files at the same time.
#
# Each copy should: read the source, then write to the destination.
# Use asyncio.to_thread() for each copy operation.
#
# Print a message for each file copied with its size in bytes.
# =============================================================================

async def exercise_4():
    # Create source files
    sources_and_dests = []
    for i in range(4):
        src = os.path.join(TEMP_DIR, f"original_{i}.txt")
        dst = os.path.join(TEMP_DIR, f"copy_{i}.txt")
        with open(src, "w") as f:
            f.write(f"Original file {i}\n" * (i + 1))
        sources_and_dests.append((src, dst))

    # YOUR CODE HERE — copy all files concurrently
    pass


# =============================================================================
# Exercise 5: Async log writer
#
# Write an async function `write_logs` that:
#   1. Creates a log file
#   2. Launches 3 "worker" coroutines concurrently (use asyncio.gather)
#   3. Each worker writes 3 log entries with short sleeps between them
#   4. Each log entry has format: "[HH:MM:SS] Worker N: message"
#   5. After all workers finish, read and print the log file contents
#
# The log entries should be interleaved because the workers run concurrently.
# =============================================================================

async def exercise_5():
    log_path = os.path.join(TEMP_DIR, "workers.log")
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: File processing + simulated API calls
#
# Simulate a real-world scenario: you need to read 3 data files AND make 2
# API calls, all concurrently. Then combine the results.
#
# Steps:
#   1. Create 3 data files (provided below)
#   2. Define a fake async API function that sleeps 0.1s and returns data
#   3. Use asyncio.gather() to read all 3 files AND call 2 APIs concurrently
#   4. Print how many total characters were in the files and what the APIs returned
#   5. Time the whole operation — it should be ~0.1s, not ~0.5s
# =============================================================================

async def exercise_6():
    # Create data files
    data_files = []
    for i in range(3):
        path = os.path.join(TEMP_DIR, f"data_{i}.csv")
        with open(path, "w") as f:
            f.write("id,name,value\n")
            for j in range(5):
                f.write(f"{j},item_{j},{j * 10}\n")
        data_files.append(path)

    # YOUR CODE HERE — read files + call APIs concurrently, time it
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def _write_sync(path, content):
    with open(path, "w") as f:
        f.write(content)


def _read_sync(path):
    with open(path) as f:
        return f.read()


def _append_sync(path, content):
    with open(path, "a") as f:
        f.write(content)


def _copy_sync(src, dst):
    with open(src) as f:
        data = f.read()
    with open(dst, "w") as f:
        f.write(data)
    return len(data)


def _count_lines_sync(path):
    with open(path) as f:
        return sum(1 for _ in f)


async def solution_1():
    path = os.path.join(TEMP_DIR, "greeting.txt")
    await asyncio.to_thread(_write_sync, path, "Hello, async world!")
    content = await asyncio.to_thread(_read_sync, path)
    print(f"  Wrote and read back: {content}")
    return content


async def solution_2():
    files = {
        os.path.join(TEMP_DIR, "file_a.txt"): "Alpha content",
        os.path.join(TEMP_DIR, "file_b.txt"): "Bravo content",
        os.path.join(TEMP_DIR, "file_c.txt"): "Charlie content",
        os.path.join(TEMP_DIR, "file_d.txt"): "Delta content",
    }

    # Write all files concurrently
    await asyncio.gather(*(
        asyncio.to_thread(_write_sync, path, content)
        for path, content in files.items()
    ))
    print("  All files written concurrently!")

    # Read all files concurrently
    paths = list(files.keys())
    results = await asyncio.gather(*(
        asyncio.to_thread(_read_sync, path)
        for path in paths
    ))

    for path, content in zip(paths, results):
        print(f"  {os.path.basename(path)}: {content}")


async def solution_3():
    test_files = {}
    for name, num_lines in [("short.txt", 3), ("medium.txt", 10), ("long.txt", 25)]:
        path = os.path.join(TEMP_DIR, name)
        content = "\n".join(f"Line {i}" for i in range(1, num_lines + 1)) + "\n"
        with open(path, "w") as f:
            f.write(content)
        test_files[name] = path

    paths = list(test_files.values())

    counts = await asyncio.gather(*(
        asyncio.to_thread(_count_lines_sync, path)
        for path in paths
    ))

    result = {os.path.basename(path): count for path, count in zip(paths, counts)}
    print(f"  Line counts: {result}")
    return result


async def solution_4():
    sources_and_dests = []
    for i in range(4):
        src = os.path.join(TEMP_DIR, f"original_{i}.txt")
        dst = os.path.join(TEMP_DIR, f"copy_{i}.txt")
        with open(src, "w") as f:
            f.write(f"Original file {i}\n" * (i + 1))
        sources_and_dests.append((src, dst))

    sizes = await asyncio.gather(*(
        asyncio.to_thread(_copy_sync, src, dst)
        for src, dst in sources_and_dests
    ))

    for (src, dst), size in zip(sources_and_dests, sizes):
        print(f"  Copied {os.path.basename(src)} -> {os.path.basename(dst)} ({size} bytes)")


async def solution_5():
    log_path = os.path.join(TEMP_DIR, "workers.log")
    await asyncio.to_thread(_write_sync, log_path, "")  # Clear the file

    async def worker(worker_id, messages):
        for msg in messages:
            timestamp = datetime.now().strftime("%H:%M:%S")
            entry = f"[{timestamp}] Worker {worker_id}: {msg}\n"
            await asyncio.to_thread(_append_sync, log_path, entry)
            await asyncio.sleep(0.02)

    await asyncio.gather(
        worker(1, ["Starting up", "Processing data", "Done"]),
        worker(2, ["Connecting", "Fetching results", "Finished"]),
        worker(3, ["Initializing", "Running checks", "Complete"]),
    )

    log_content = await asyncio.to_thread(_read_sync, log_path)
    print("  Log file contents:")
    for line in log_content.strip().split("\n"):
        print(f"    {line}")


async def solution_6():
    data_files = []
    for i in range(3):
        path = os.path.join(TEMP_DIR, f"data_{i}.csv")
        with open(path, "w") as f:
            f.write("id,name,value\n")
            for j in range(5):
                f.write(f"{j},item_{j},{j * 10}\n")
        data_files.append(path)

    async def fake_api_call(endpoint):
        await asyncio.sleep(0.1)
        return {"endpoint": endpoint, "status": "ok"}

    start = time.perf_counter()

    # Read all 3 files + 2 API calls — all 5 operations at once
    results = await asyncio.gather(
        asyncio.to_thread(_read_sync, data_files[0]),
        asyncio.to_thread(_read_sync, data_files[1]),
        asyncio.to_thread(_read_sync, data_files[2]),
        fake_api_call("/api/users"),
        fake_api_call("/api/products"),
    )

    elapsed = time.perf_counter() - start

    file_contents = results[:3]
    api_results = results[3:]

    total_chars = sum(len(c) for c in file_contents)
    print(f"  Read {len(file_contents)} files ({total_chars} total characters)")
    for api in api_results:
        print(f"  API {api['endpoint']}: {api['status']}")
    print(f"  Total time: {elapsed:.2f}s (all 5 operations ran concurrently)")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    os.makedirs(TEMP_DIR, exist_ok=True)

    exercises = [
        ("Async write and read", exercise_1, solution_1),
        ("Process multiple files concurrently", exercise_2, solution_2),
        ("Async line counter", exercise_3, solution_3),
        ("Concurrent file copy", exercise_4, solution_4),
        ("Async log writer", exercise_5, solution_5),
        ("File processing + simulated API calls", exercise_6, solution_6),
    ]

    async def run_all():
        for i, (title, exercise, solution) in enumerate(exercises, 1):
            print("=" * 50)
            print(f"EXERCISE {i}: {title}")
            print("=" * 50)

            print("  [Your answer]")
            await exercise()

            print("  [Solution]")
            await solution()
            print()

        print("-" * 50)
        print("Done! Compare your output with the solutions.")

    try:
        asyncio.run(run_all())
    finally:
        # Clean up temp files
        import shutil
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
            print(f"Cleaned up temp directory: {os.path.basename(TEMP_DIR)}")
