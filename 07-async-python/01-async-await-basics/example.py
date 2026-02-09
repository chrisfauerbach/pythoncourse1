"""
Async/Await Basics — Example Code
====================================

Run this file:
    python3 example.py

This file walks through every core concept of async programming in Python.
We use asyncio.sleep() to simulate I/O operations (like network requests)
and time the results to show the real difference between sync and async.
"""

import asyncio
import time


# =============================================================================
# 1. Your first coroutine — async def
# =============================================================================
# A coroutine is just a function defined with "async def". It can be paused
# and resumed, which is the whole magic of async.

async def say_hello():
    """A simple coroutine that prints a greeting with a delay."""
    print("Hello...")
    await asyncio.sleep(1)     # Pause this coroutine for 1 second (non-blocking)
    print("...World!")


# =============================================================================
# 2. Coroutines return values — just like regular functions
# =============================================================================
# You can return values from coroutines and get them by awaiting.

async def add(a, b):
    """Simulate an async computation that returns a result."""
    await asyncio.sleep(0.1)   # Simulate some async work
    return a + b


async def fetch_username(user_id):
    """Simulate fetching a username from a database."""
    # In real code, this would be an actual database query
    await asyncio.sleep(0.5)
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id, "Unknown")


# =============================================================================
# 3. asyncio.sleep() vs time.sleep() — non-blocking vs blocking
# =============================================================================
# This is THE most important distinction in async programming.
# time.sleep() freezes EVERYTHING. asyncio.sleep() only pauses ONE coroutine.

async def blocking_demo():
    """Show the difference between blocking and non-blocking sleep."""

    print("\n--- time.sleep() vs asyncio.sleep() ---")

    # BLOCKING: time.sleep stops the entire event loop
    print("\nUsing time.sleep(1) — BLOCKING (bad in async code):")
    start = time.time()
    time.sleep(1)   # Nothing else can run during this second
    print(f"  Done in {time.time() - start:.2f}s (event loop was frozen)")

    # NON-BLOCKING: asyncio.sleep only pauses this coroutine
    print("\nUsing asyncio.sleep(1) — NON-BLOCKING (correct):")
    start = time.time()
    await asyncio.sleep(1)   # Event loop is free to do other work
    print(f"  Done in {time.time() - start:.2f}s (event loop was free)")


# =============================================================================
# 4. Sequential execution — one task after another
# =============================================================================
# When you await coroutines one by one, they run sequentially.
# Each one must finish before the next one starts.

async def simulate_api_call(name, delay):
    """Simulate an API call that takes `delay` seconds."""
    print(f"  Starting {name}...")
    await asyncio.sleep(delay)
    print(f"  Finished {name} ({delay}s)")
    return f"{name}: done"


async def run_sequentially():
    """Run three tasks one after another. Total time = sum of all delays."""

    print("\n--- Sequential Execution ---")
    start = time.time()

    # Each await blocks until that coroutine finishes
    result1 = await simulate_api_call("API-1", 1)
    result2 = await simulate_api_call("API-2", 1)
    result3 = await simulate_api_call("API-3", 1)

    elapsed = time.time() - start
    print(f"\n  Results: {result1}, {result2}, {result3}")
    print(f"  Total time: {elapsed:.2f}s (should be ~3s — they ran one by one)")


# =============================================================================
# 5. Concurrent execution with asyncio.gather()
# =============================================================================
# gather() runs multiple coroutines at the same time. While one is waiting,
# the others can make progress. Total time = the LONGEST single delay.

async def run_concurrently():
    """Run three tasks concurrently. Total time = longest single delay."""

    print("\n--- Concurrent Execution with asyncio.gather() ---")
    start = time.time()

    # gather() starts all three and waits for ALL of them to finish
    results = await asyncio.gather(
        simulate_api_call("API-1", 1),
        simulate_api_call("API-2", 1),
        simulate_api_call("API-3", 1),
    )

    elapsed = time.time() - start
    print(f"\n  Results: {results}")
    print(f"  Total time: {elapsed:.2f}s (should be ~1s — they ran concurrently!)")


# =============================================================================
# 6. gather() with different durations
# =============================================================================
# When tasks take different amounts of time, gather() still runs them all
# concurrently. The total time is the duration of the slowest task.

async def download_file(filename, size_mb):
    """Simulate downloading a file. Bigger files take longer."""
    download_time = size_mb * 0.3   # 0.3s per MB (simulated)
    print(f"  Downloading {filename} ({size_mb}MB)...")
    await asyncio.sleep(download_time)
    print(f"  Finished {filename}")
    return {"file": filename, "size": size_mb}


async def download_all_files():
    """Download multiple files concurrently."""

    print("\n--- Concurrent Downloads (different durations) ---")
    start = time.time()

    results = await asyncio.gather(
        download_file("photo.jpg", 2),      # Takes 0.6s
        download_file("video.mp4", 5),      # Takes 1.5s (slowest)
        download_file("document.pdf", 1),   # Takes 0.3s
    )

    elapsed = time.time() - start
    print(f"\n  Downloaded {len(results)} files in {elapsed:.2f}s")
    print(f"  (Sequential would have taken ~{0.6 + 1.5 + 0.3:.1f}s)")


# =============================================================================
# 7. Return values from gather()
# =============================================================================
# gather() returns a list of results in the SAME ORDER you passed the
# coroutines — regardless of which one finishes first.

async def gather_with_returns():
    """Show that gather() preserves return order."""

    print("\n--- Return Values from gather() ---")

    # These finish in different orders, but results match input order
    results = await asyncio.gather(
        fetch_username(1),   # Alice (0.5s)
        fetch_username(2),   # Bob (0.5s)
        fetch_username(3),   # Charlie (0.5s)
    )

    print(f"  User 1: {results[0]}")
    print(f"  User 2: {results[1]}")
    print(f"  User 3: {results[2]}")

    # You can also unpack directly
    alice, bob, charlie = await asyncio.gather(
        fetch_username(1),
        fetch_username(2),
        fetch_username(3),
    )
    print(f"  Unpacked: {alice}, {bob}, {charlie}")


# =============================================================================
# 8. Putting it all together — a realistic example
# =============================================================================
# A common real-world pattern: fetch data from multiple sources, combine it,
# and return the result. All the fetching happens concurrently.

async def fetch_user_profile(user_id):
    """Simulate fetching a complete user profile from multiple services."""

    print(f"\n--- Building Profile for User {user_id} ---")
    start = time.time()

    # Fetch from three different "services" at the same time
    username, posts, followers = await asyncio.gather(
        fetch_from_user_service(user_id),
        fetch_from_post_service(user_id),
        fetch_from_follower_service(user_id),
    )

    profile = {
        "username": username,
        "posts": posts,
        "followers": followers,
    }

    elapsed = time.time() - start
    print(f"  Profile built in {elapsed:.2f}s:")
    for key, value in profile.items():
        print(f"    {key}: {value}")

    return profile


async def fetch_from_user_service(user_id):
    """Simulate: fetch username (takes 0.3s)."""
    await asyncio.sleep(0.3)
    return "Alice"


async def fetch_from_post_service(user_id):
    """Simulate: fetch user's posts (takes 0.5s — slowest)."""
    await asyncio.sleep(0.5)
    return ["Hello World", "My second post", "Python is great"]


async def fetch_from_follower_service(user_id):
    """Simulate: fetch follower count (takes 0.2s)."""
    await asyncio.sleep(0.2)
    return 1024


# =============================================================================
# Main — run everything
# =============================================================================
# asyncio.run() is the bridge from synchronous to asynchronous code.
# Call it once, and everything async flows from there.

async def main():
    """Run all the examples in order."""

    print("=" * 60)
    print("   ASYNC/AWAIT BASICS — EXAMPLES")
    print("=" * 60)

    # 1. Simple coroutine
    print("\n--- 1. Simple Coroutine ---")
    await say_hello()

    # 2. Return values
    print("\n--- 2. Return Values ---")
    result = await add(3, 4)
    print(f"  add(3, 4) = {result}")

    name = await fetch_username(1)
    print(f"  User 1 is: {name}")

    # 3. Blocking vs non-blocking
    await blocking_demo()

    # 4. Sequential execution
    await run_sequentially()

    # 5. Concurrent execution
    await run_concurrently()

    # 6. Different durations
    await download_all_files()

    # 7. Return values from gather
    await gather_with_returns()

    # 8. Realistic example
    await fetch_user_profile(1)

    # Wrap up
    print()
    print("=" * 60)
    print("   ALL EXAMPLES COMPLETE!")
    print("=" * 60)
    print()
    print("Key observation: Sequential took ~3s, concurrent took ~1s.")
    print("That's the power of async — do other work while you wait!")


if __name__ == "__main__":
    asyncio.run(main())
