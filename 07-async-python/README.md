# Section 07: Async Python

Sometimes your program needs to do multiple things at once — or more accurately, it needs to not sit around waiting while something slow (like a network request) finishes. Async Python lets you write concurrent code that's efficient and readable.

## Lessons

| # | Lesson | Description |
|---|--------|-------------|
| 01 | [async/await Basics](01-async-await-basics/) | Understanding coroutines and the event loop |
| 02 | [asyncio Tasks](02-asyncio-tasks/) | Running multiple coroutines concurrently |
| 03 | [Async File I/O](03-async-file-io/) | Non-blocking file operations with aiofiles |
| 04 | [Async HTTP](04-async-http/) | Making concurrent HTTP requests with aiohttp |

## What You'll Be Able to Do After This Section

- Understand when and why to use async vs. sync code
- Write coroutines with async/await
- Run multiple tasks concurrently with asyncio
- Perform non-blocking file and network operations

## Prerequisites

- [Section 01: Fundamentals](../01-fundamentals/)
- [Section 05: Intermediate](../05-intermediate/) — especially generators and context managers
- [Section 03: File I/O](../03-file-io/) — for the async file I/O lesson
