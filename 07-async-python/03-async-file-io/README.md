# Async File I/O

## Objective

Learn how to perform file operations without blocking the event loop, using both `aiofiles` and Python's built-in `asyncio.to_thread()`.

## Concepts Covered

- Why regular file I/O blocks the event loop
- The `aiofiles` library for async file reading/writing
- `asyncio.to_thread()` for running sync file ops in a thread pool (Python 3.9+)
- Choosing the right approach for your situation
- Combining async file I/O with other async operations
- Practical patterns: async log writers, concurrent file processing

## Prerequisites

- [asyncio Tasks](../02-asyncio-tasks/) and [File I/O](../../03-file-io/)

## Lesson

### The Problem: File I/O Blocks the Event Loop

Here's something that surprises a lot of people — when you do regular file I/O inside an async function, it **blocks the entire event loop**:

```python
import asyncio

async def bad_example():
    # This LOOKS async, but it's NOT!
    # The open/read call blocks the event loop until the file is fully read.
    with open("big_file.txt") as f:
        data = f.read()  # Everything else freezes while this runs

    # No other coroutines can make progress during that read.
    return data
```

Why does this matter? If you're running a web server or handling multiple connections, a single blocking file read can stall **everything**. Your other coroutines — handling HTTP requests, reading from sockets, processing messages — all have to wait.

For small files on a fast SSD, you probably won't notice. But for large files, slow disks, or network-mounted filesystems, this is a real problem.

### Solution 1: aiofiles (Third-Party Library)

The `aiofiles` library wraps standard file operations in an async interface. It runs the actual I/O in a thread pool behind the scenes, so your event loop stays free.

#### Installing aiofiles

```bash
pip install aiofiles
```

#### Reading Files Asynchronously

```python
import aiofiles

async def read_file():
    async with aiofiles.open("myfile.txt", mode="r") as f:
        contents = await f.read()
    print(contents)
```

Notice the pattern: `async with` instead of `with`, and `await` before `f.read()`. This tells the event loop "go do other things while I wait for this I/O to complete."

#### Writing Files Asynchronously

```python
import aiofiles

async def write_file():
    async with aiofiles.open("output.txt", mode="w") as f:
        await f.write("Hello from async land!\n")
        await f.write("Second line.\n")
```

#### Line-by-Line Async Reading

For large files, reading line by line avoids loading everything into memory:

```python
import aiofiles

async def read_lines():
    async with aiofiles.open("big_file.txt", mode="r") as f:
        async for line in f:
            print(line.strip())
```

The `async for` is the key here — it yields control back to the event loop between lines.

### Solution 2: asyncio.to_thread() (Built-In, No Dependencies)

Starting with Python 3.9, you can push **any** blocking function into a thread pool with `asyncio.to_thread()`. No extra packages needed:

```python
import asyncio

def read_file_sync(path):
    """Regular synchronous file read."""
    with open(path) as f:
        return f.read()

async def read_file_async(path):
    """Run the sync read in a thread — doesn't block the event loop."""
    contents = await asyncio.to_thread(read_file_sync, path)
    return contents
```

You write the file operation as a normal sync function, then wrap it with `asyncio.to_thread()`. The event loop hands it off to a worker thread and goes back to processing other coroutines.

This works for writing too:

```python
import asyncio

def write_file_sync(path, data):
    with open(path, "w") as f:
        f.write(data)

async def write_file_async(path, data):
    await asyncio.to_thread(write_file_sync, path, data)
```

### When to Use Which Approach

| Approach | Best For | Tradeoffs |
|---|---|---|
| **Regular sync I/O** | Scripts, one-off tasks, small files in non-async code | Blocks the event loop — fine if nothing else needs to run |
| **`aiofiles`** | Async servers, lots of file operations, line-by-line streaming | Extra dependency, cleaner async API |
| **`asyncio.to_thread()`** | Quick async wrapping, no-dependency environments, occasional file ops | Built-in, works with any sync function, slightly more verbose |

**Rules of thumb:**

- Writing a quick script? Just use regular sync I/O. You don't need async for everything.
- Building an async server that reads/writes files often? `aiofiles` gives you the cleanest code.
- Need to do a file operation inside async code but don't want to install anything? `asyncio.to_thread()` is your friend.

### Combining Async File I/O with Other Async Work

The whole point of async file I/O is that other things can happen at the same time. Here's where it really shines — doing file operations **concurrently** with network calls:

```python
import asyncio

async def fetch_api_data():
    """Simulate an API call."""
    await asyncio.sleep(1)  # Pretend this is an HTTP request
    return {"status": "ok", "data": [1, 2, 3]}

def read_config_sync(path):
    with open(path) as f:
        return f.read()

async def main():
    # These run concurrently — neither blocks the other!
    config, api_result = await asyncio.gather(
        asyncio.to_thread(read_config_sync, "config.txt"),
        fetch_api_data(),
    )
    print(f"Config loaded, API returned: {api_result['status']}")
```

Without async file I/O, the config read would block until complete, and *then* the API call would start. With `asyncio.gather()`, they overlap — your total wait time is the **maximum** of the two, not the **sum**.

### Practical Pattern: Async Log Writer

A common real-world pattern — an async function that appends log entries with timestamps:

```python
import asyncio
from datetime import datetime

def append_log_sync(path, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

async def log_event(path, message):
    await asyncio.to_thread(append_log_sync, path, message)
```

### Practical Pattern: Concurrent File Processing

Process a batch of files at the same time instead of one by one:

```python
import asyncio

def process_file_sync(path):
    with open(path) as f:
        data = f.read()
    # Do some processing...
    return len(data)

async def process_all_files(paths):
    tasks = [asyncio.to_thread(process_file_sync, p) for p in paths]
    results = await asyncio.gather(*tasks)
    return results
```

This is dramatically faster than reading files sequentially when you have many files, especially on network filesystems or when each file also needs CPU processing.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Regular `open()` and `f.read()` **block the event loop** — bad news in async code
- `aiofiles` provides a clean async file API (`async with`, `await f.read()`, `async for`)
- `asyncio.to_thread()` (Python 3.9+) wraps any sync function for async use — no install needed
- Use `asyncio.gather()` to run file operations concurrently with other async work
- For simple scripts, regular sync I/O is perfectly fine — async file I/O matters when you have an event loop to protect
- Concurrent file processing with `gather()` can be dramatically faster than sequential reads
