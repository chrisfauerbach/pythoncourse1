"""
Asyncio Tasks — Example Code
==============================

Run this file:
    python3 example.py

This file demonstrates asyncio Tasks — creating them, running them concurrently,
cancelling them, handling timeouts, and practical patterns like producer-consumer
and rate limiting with semaphores. All sleep times are short so it runs fast.
"""

import asyncio
import time


# -----------------------------------------------------------------------------
# 1. create_task() — running coroutines concurrently
# -----------------------------------------------------------------------------

async def fetch_data(name, delay):
    """Simulates an async operation that takes some time."""
    await asyncio.sleep(delay)
    return f"{name}: done (took {delay}s)"


async def demo_create_task():
    print("--- 1. create_task() — concurrent execution ---")

    start = time.perf_counter()

    # Create tasks — they start running immediately in the background
    task1 = asyncio.create_task(fetch_data("Task-A", 0.3))
    task2 = asyncio.create_task(fetch_data("Task-B", 0.1))
    task3 = asyncio.create_task(fetch_data("Task-C", 0.2))

    # Await each task to get its result
    result1 = await task1
    result2 = await task2
    result3 = await task3

    elapsed = time.perf_counter() - start

    print(f"  {result1}")
    print(f"  {result2}")
    print(f"  {result3}")
    print(f"  Total time: {elapsed:.2f}s (concurrent, not 0.6s!)")
    print()


# -----------------------------------------------------------------------------
# 2. Tasks vs coroutines — sequential vs concurrent
# -----------------------------------------------------------------------------

async def demo_tasks_vs_coroutines():
    print("--- 2. Tasks vs coroutines — sequential vs concurrent ---")

    # Sequential: await each coroutine directly
    start = time.perf_counter()
    r1 = await fetch_data("Seq-A", 0.15)
    r2 = await fetch_data("Seq-B", 0.15)
    seq_time = time.perf_counter() - start
    print(f"  Sequential: {r1}, {r2}")
    print(f"  Sequential time: {seq_time:.2f}s")

    # Concurrent: create tasks first
    start = time.perf_counter()
    t1 = asyncio.create_task(fetch_data("Con-A", 0.15))
    t2 = asyncio.create_task(fetch_data("Con-B", 0.15))
    r1 = await t1
    r2 = await t2
    con_time = time.perf_counter() - start
    print(f"  Concurrent: {r1}, {r2}")
    print(f"  Concurrent time: {con_time:.2f}s")
    print()


# -----------------------------------------------------------------------------
# 3. asyncio.gather() — collecting results from multiple tasks
# -----------------------------------------------------------------------------

async def demo_gather():
    print("--- 3. asyncio.gather() — collecting results ---")

    # Basic gather — results come back in the same order as arguments
    results = await asyncio.gather(
        fetch_data("Gather-A", 0.3),
        fetch_data("Gather-B", 0.1),
        fetch_data("Gather-C", 0.2),
    )
    for r in results:
        print(f"  {r}")

    # gather with return_exceptions — errors become return values
    async def might_fail(n):
        if n == 2:
            raise ValueError(f"Task {n} failed!")
        await asyncio.sleep(0.1)
        return f"Task {n} succeeded"

    print("  With return_exceptions=True:")
    results = await asyncio.gather(
        might_fail(1),
        might_fail(2),
        might_fail(3),
        return_exceptions=True,
    )
    for r in results:
        if isinstance(r, Exception):
            print(f"    Error: {r}")
        else:
            print(f"    {r}")
    print()


# -----------------------------------------------------------------------------
# 4. asyncio.TaskGroup (Python 3.11+) — structured concurrency
# -----------------------------------------------------------------------------

async def demo_task_group():
    print("--- 4. asyncio.TaskGroup — structured concurrency ---")

    # Basic TaskGroup usage
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data("TG-A", 0.2))
        task2 = tg.create_task(fetch_data("TG-B", 0.1))
        task3 = tg.create_task(fetch_data("TG-C", 0.15))

    # After the async with block, all tasks are guaranteed done
    print(f"  {task1.result()}")
    print(f"  {task2.result()}")
    print(f"  {task3.result()}")

    # TaskGroup with error handling — uses except* for ExceptionGroups
    async def might_fail_tg(n):
        await asyncio.sleep(0.05)
        if n == 2:
            raise ValueError(f"Task {n} exploded!")
        return f"Task {n} OK"

    print("  TaskGroup with error handling:")
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(might_fail_tg(1))
            tg.create_task(might_fail_tg(2))
            tg.create_task(might_fail_tg(3))
    except* ValueError as eg:
        for exc in eg.exceptions:
            print(f"    Caught: {exc}")
    print()


# -----------------------------------------------------------------------------
# 5. Task cancellation
# -----------------------------------------------------------------------------

async def demo_cancellation():
    print("--- 5. Task cancellation ---")

    async def long_running(name):
        try:
            count = 0
            while True:
                count += 1
                print(f"  {name}: working... (iteration {count})")
                await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            print(f"  {name}: cancelled! Cleaning up...")
            raise  # Always re-raise!

    task = asyncio.create_task(long_running("Worker"))
    await asyncio.sleep(0.25)  # Let it run a couple iterations
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("  Confirmed: task is cancelled")
    print()


# -----------------------------------------------------------------------------
# 6. Timeouts with asyncio.wait_for()
# -----------------------------------------------------------------------------

async def demo_timeout():
    print("--- 6. Timeouts with asyncio.wait_for() ---")

    async def slow_operation():
        await asyncio.sleep(1.0)
        return "finally done"

    # This one will time out
    try:
        result = await asyncio.wait_for(slow_operation(), timeout=0.15)
        print(f"  Result: {result}")
    except TimeoutError:
        print("  Timed out! (as expected, 0.15s timeout for a 1.0s task)")

    # This one will succeed
    async def fast_operation():
        await asyncio.sleep(0.05)
        return "quick result"

    result = await asyncio.wait_for(fast_operation(), timeout=0.5)
    print(f"  Success: {result}")
    print()


# -----------------------------------------------------------------------------
# 7. asyncio.wait() — fine-grained control
# -----------------------------------------------------------------------------

async def demo_wait():
    print("--- 7. asyncio.wait() — fine-grained control ---")

    tasks = [
        asyncio.create_task(fetch_data("Wait-A", 0.3), name="Wait-A"),
        asyncio.create_task(fetch_data("Wait-B", 0.1), name="Wait-B"),
        asyncio.create_task(fetch_data("Wait-C", 0.2), name="Wait-C"),
    ]

    # FIRST_COMPLETED — returns as soon as one task finishes
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"  FIRST_COMPLETED: {len(done)} done, {len(pending)} pending")
    for t in done:
        print(f"    Finished: {t.result()}")

    # ALL_COMPLETED — wait for the rest
    done, pending = await asyncio.wait(pending, return_when=asyncio.ALL_COMPLETED)
    print(f"  ALL_COMPLETED: {len(done)} done, {len(pending)} pending")
    for t in done:
        print(f"    Finished: {t.result()}")
    print()


# -----------------------------------------------------------------------------
# 8. asyncio.as_completed() — process results as they arrive
# -----------------------------------------------------------------------------

async def demo_as_completed():
    print("--- 8. asyncio.as_completed() — results in completion order ---")

    coros = [
        fetch_data("AC-A", 0.3),
        fetch_data("AC-B", 0.1),
        fetch_data("AC-C", 0.2),
    ]

    # Results come back in the order tasks FINISH, not the order you submitted
    order = 1
    for future in asyncio.as_completed(coros):
        result = await future
        print(f"  #{order} completed: {result}")
        order += 1
    print()


# -----------------------------------------------------------------------------
# 9. Producer-consumer pattern with asyncio.Queue
# -----------------------------------------------------------------------------

async def demo_producer_consumer():
    print("--- 9. Producer-consumer pattern ---")

    async def producer(queue, name, count):
        for i in range(count):
            item = f"{name}-item-{i}"
            await queue.put(item)
            print(f"  [Producer {name}] put: {item}")
            await asyncio.sleep(0.05)

    async def consumer(queue, name):
        while True:
            item = await queue.get()
            print(f"  [Consumer {name}] processing: {item}")
            await asyncio.sleep(0.08)  # Processing takes a bit longer
            queue.task_done()

    queue = asyncio.Queue(maxsize=3)

    # Start producers and consumers
    producers = [
        asyncio.create_task(producer(queue, "P1", 3)),
        asyncio.create_task(producer(queue, "P2", 3)),
    ]
    consumers = [
        asyncio.create_task(consumer(queue, "C1")),
        asyncio.create_task(consumer(queue, "C2")),
    ]

    # Wait for all producers to finish adding items
    await asyncio.gather(*producers)

    # Wait for all items in the queue to be processed
    await queue.join()

    # Cancel consumers (they loop forever, so we stop them manually)
    for c in consumers:
        c.cancel()

    print("  All items produced and consumed!")
    print()


# -----------------------------------------------------------------------------
# 10. Semaphore for rate limiting
# -----------------------------------------------------------------------------

async def demo_semaphore():
    print("--- 10. Semaphore for rate limiting ---")

    active = 0

    async def rate_limited_fetch(sem, url_id):
        nonlocal active
        async with sem:
            active += 1
            print(f"  Fetching URL {url_id} (active: {active})")
            await asyncio.sleep(0.1)
            active -= 1
            return f"Data from URL {url_id}"

    # Only 3 concurrent "requests" at a time
    sem = asyncio.Semaphore(3)
    tasks = [rate_limited_fetch(sem, i) for i in range(8)]
    results = await asyncio.gather(*tasks)

    print(f"  Got {len(results)} results")
    print()


# -----------------------------------------------------------------------------
# Run everything!
# -----------------------------------------------------------------------------

async def main():
    print("=" * 60)
    print("   ASYNCIO TASKS — COMPLETE EXAMPLE")
    print("=" * 60)
    print()

    await demo_create_task()
    await demo_tasks_vs_coroutines()
    await demo_gather()
    await demo_task_group()
    await demo_cancellation()
    await demo_timeout()
    await demo_wait()
    await demo_as_completed()
    await demo_producer_consumer()
    await demo_semaphore()

    print("=" * 60)
    print("   ALL DEMOS COMPLETE!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
