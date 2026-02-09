"""
Async File I/O — Example Code
================================

Run this file:
    python3 example.py

Demonstrates how to do file operations without blocking the event loop.
Uses asyncio.to_thread() (built-in, no dependencies) for most examples,
and optionally shows aiofiles if you have it installed.
"""

import asyncio
import os
import time
from datetime import datetime

# We'll create temp files in this directory and clean them up at the end
TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_temp_example")


# =============================================================================
# Helper: sync file operations (these are what we'll wrap with to_thread)
# =============================================================================

def write_file_sync(path, content):
    """Regular synchronous file write."""
    with open(path, "w") as f:
        f.write(content)


def read_file_sync(path):
    """Regular synchronous file read."""
    with open(path) as f:
        return f.read()


def append_file_sync(path, content):
    """Regular synchronous file append."""
    with open(path, "a") as f:
        f.write(content)


def read_lines_sync(path):
    """Read a file and return a list of lines."""
    with open(path) as f:
        return f.readlines()


# =============================================================================
# 1. Basic async write and read with asyncio.to_thread()
# =============================================================================

async def demo_basic_read_write():
    print("=" * 60)
    print("1. Basic async write and read (asyncio.to_thread)")
    print("=" * 60)

    path = os.path.join(TEMP_DIR, "hello.txt")

    # Write asynchronously — the event loop stays free during the write
    await asyncio.to_thread(write_file_sync, path, "Hello from async file I/O!\nThis didn't block the event loop.\n")
    print(f"  Wrote to {os.path.basename(path)}")

    # Read it back asynchronously
    content = await asyncio.to_thread(read_file_sync, path)
    print(f"  Read back: {content.strip()}")
    print()


# =============================================================================
# 2. Why it matters — concurrent file operations vs sequential
# =============================================================================

async def demo_concurrent_vs_sequential():
    print("=" * 60)
    print("2. Concurrent vs sequential file operations")
    print("=" * 60)

    # Create some files to work with
    files = {}
    for i in range(5):
        path = os.path.join(TEMP_DIR, f"data_{i}.txt")
        content = f"File {i}\n" * 100  # Some content to read
        write_file_sync(path, content)
        files[i] = path

    def slow_read(path):
        """Simulate a slow read (like a network filesystem)."""
        time.sleep(0.1)  # Simulate latency
        with open(path) as f:
            return f.read()

    # Sequential — one after another
    start = time.perf_counter()
    for path in files.values():
        await asyncio.to_thread(slow_read, path)
    sequential_time = time.perf_counter() - start

    # Concurrent — all at once with gather
    start = time.perf_counter()
    await asyncio.gather(*(asyncio.to_thread(slow_read, p) for p in files.values()))
    concurrent_time = time.perf_counter() - start

    print(f"  Sequential (5 files): {sequential_time:.2f}s")
    print(f"  Concurrent (5 files): {concurrent_time:.2f}s")
    print(f"  Speedup: {sequential_time / concurrent_time:.1f}x faster")
    print()


# =============================================================================
# 3. Async line-by-line reading with to_thread
# =============================================================================

async def demo_line_by_line():
    print("=" * 60)
    print("3. Async line-by-line reading")
    print("=" * 60)

    # Create a file with numbered lines
    path = os.path.join(TEMP_DIR, "lines.txt")
    lines = [f"Line {i}: The quick brown fox jumps over the lazy dog\n" for i in range(1, 11)]
    await asyncio.to_thread(write_file_sync, path, "".join(lines))

    # Read lines and process them
    all_lines = await asyncio.to_thread(read_lines_sync, path)
    print(f"  Read {len(all_lines)} lines. First 3:")
    for line in all_lines[:3]:
        print(f"    {line.strip()}")
    print(f"    ... and {len(all_lines) - 3} more")
    print()


# =============================================================================
# 4. Async log writer pattern
# =============================================================================

async def demo_log_writer():
    print("=" * 60)
    print("4. Async log writer pattern")
    print("=" * 60)

    log_path = os.path.join(TEMP_DIR, "app.log")

    # Clear the log file
    await asyncio.to_thread(write_file_sync, log_path, "")

    async def log_event(message):
        """Write a timestamped log entry without blocking the event loop."""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        entry = f"[{timestamp}] {message}\n"
        await asyncio.to_thread(append_file_sync, log_path, entry)

    # Simulate some application events happening concurrently
    async def user_login(user):
        await log_event(f"User '{user}' logging in...")
        await asyncio.sleep(0.05)  # Simulate auth check
        await log_event(f"User '{user}' authenticated successfully")

    async def process_order(order_id):
        await log_event(f"Processing order #{order_id}")
        await asyncio.sleep(0.03)  # Simulate processing
        await log_event(f"Order #{order_id} complete")

    # Run these concurrently — log entries interleave naturally
    await asyncio.gather(
        user_login("alice"),
        user_login("bob"),
        process_order(42),
    )

    # Show what the log looks like
    log_content = await asyncio.to_thread(read_file_sync, log_path)
    print("  Log file contents:")
    for line in log_content.strip().split("\n"):
        print(f"    {line}")
    print()


# =============================================================================
# 5. Combining file I/O with other async operations
# =============================================================================

async def demo_combined_operations():
    print("=" * 60)
    print("5. File I/O + other async work running concurrently")
    print("=" * 60)

    config_path = os.path.join(TEMP_DIR, "config.txt")
    await asyncio.to_thread(write_file_sync, config_path, "database=localhost\nport=5432\ntimeout=30\n")

    async def fake_api_call(endpoint):
        """Simulate an API call that takes some time."""
        await asyncio.sleep(0.1)
        return {"endpoint": endpoint, "status": "ok", "items": 42}

    async def fake_db_query():
        """Simulate a database query."""
        await asyncio.sleep(0.08)
        return [{"id": 1, "name": "Widget"}, {"id": 2, "name": "Gadget"}]

    # Run all three concurrently — file read, API call, and DB query
    start = time.perf_counter()
    config, api_data, db_rows = await asyncio.gather(
        asyncio.to_thread(read_file_sync, config_path),
        fake_api_call("/api/products"),
        fake_db_query(),
    )
    elapsed = time.perf_counter() - start

    print(f"  Config: {config.strip().split(chr(10))[0]}...")
    print(f"  API response: {api_data['status']} ({api_data['items']} items)")
    print(f"  DB rows: {len(db_rows)} records")
    print(f"  Total time: {elapsed:.2f}s (all three ran concurrently!)")
    print()


# =============================================================================
# 6. (Optional) aiofiles — if installed
# =============================================================================

async def demo_aiofiles():
    print("=" * 60)
    print("6. aiofiles (third-party library)")
    print("=" * 60)

    try:
        import aiofiles
    except ImportError:
        print("  aiofiles is not installed. Install it with:")
        print("    pip install aiofiles")
        print("  Skipping this section.")
        print()
        return

    # Write with aiofiles
    path = os.path.join(TEMP_DIR, "aiofiles_demo.txt")
    async with aiofiles.open(path, mode="w") as f:
        await f.write("Written with aiofiles!\n")
        await f.write("Line 2 from aiofiles.\n")
        await f.write("Line 3 — async for can iterate over these.\n")
    print(f"  Wrote to {os.path.basename(path)} with aiofiles")

    # Read with aiofiles
    async with aiofiles.open(path, mode="r") as f:
        content = await f.read()
    print(f"  Full read: {content.strip().split(chr(10))[0]}...")

    # Line-by-line with async for
    print("  Line-by-line with 'async for':")
    async with aiofiles.open(path, mode="r") as f:
        async for line in f:
            print(f"    {line.strip()}")
    print()


# =============================================================================
# Main — run all demos
# =============================================================================

async def main():
    print()
    print("Async File I/O — Examples")
    print("=" * 60)
    print()

    # Create temp directory
    os.makedirs(TEMP_DIR, exist_ok=True)

    try:
        await demo_basic_read_write()
        await demo_concurrent_vs_sequential()
        await demo_line_by_line()
        await demo_log_writer()
        await demo_combined_operations()
        await demo_aiofiles()

        print("=" * 60)
        print("All examples complete!")
        print("=" * 60)
    finally:
        # Clean up temp files
        import shutil
        if os.path.exists(TEMP_DIR):
            shutil.rmtree(TEMP_DIR)
            print(f"Cleaned up temp directory: {os.path.basename(TEMP_DIR)}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
