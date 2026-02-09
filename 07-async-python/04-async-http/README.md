# Async HTTP

## Objective

Learn how to make HTTP requests asynchronously so you can fetch many URLs at the same time instead of waiting for each one to finish before starting the next.

## Concepts Covered

- Why async HTTP matters (concurrent requests vs. sequential)
- Sync vs async HTTP comparison — `requests` vs `aiohttp`
- The `aiohttp` library — Python's async HTTP client
- Installing `aiohttp`
- Making GET and POST requests
- The `ClientSession` pattern (context manager)
- Handling responses — status codes, headers, JSON, text
- Error handling in async HTTP
- Concurrent requests with `asyncio.gather()`
- Rate limiting with `asyncio.Semaphore`
- Timeouts with `aiohttp.ClientTimeout`
- Practical patterns — parallel API fetcher, retry with exponential backoff

## Prerequisites

- Comfortable with `async` / `await` syntax (lesson 01)
- Understanding of `asyncio.gather()` and tasks (lesson 02)
- Basic familiarity with HTTP concepts (URLs, GET, POST, status codes)

## Lesson

### Why Async HTTP Matters

Imagine you need to fetch data from 50 different API endpoints. With regular synchronous code, you'd do them one at a time:

```
Request 1: ------>  (wait 200ms)
Request 2:          ------>  (wait 200ms)
Request 3:                   ------>  (wait 200ms)
...
Total: 50 * 200ms = 10 seconds
```

With async HTTP, you fire them all off at the same time:

```
Request 1:  ------>
Request 2:  ------>
Request 3:  ------>
...all at once...
Total: ~200ms (they all run concurrently!)
```

That's the difference between 10 seconds and less than 1 second. For anything involving network calls — API clients, web scrapers, health checkers — async HTTP is a game-changer.

### Sync vs Async: The Timing Difference

Here's what traditional synchronous HTTP looks like with the `requests` library:

```python
import requests
import time

urls = [
    "https://api.example.com/users/1",
    "https://api.example.com/users/2",
    "https://api.example.com/users/3",
]

start = time.time()
results = []
for url in urls:
    response = requests.get(url)       # Blocks until response comes back
    results.append(response.json())    # Then moves to next URL
elapsed = time.time() - start
print(f"Sync: {elapsed:.2f}s")         # ~0.6s (3 sequential requests)
```

And here's the async version with `aiohttp`:

```python
import aiohttp
import asyncio
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    urls = [
        "https://api.example.com/users/1",
        "https://api.example.com/users/2",
        "https://api.example.com/users/3",
    ]

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    elapsed = time.time() - start
    print(f"Async: {elapsed:.2f}s")     # ~0.2s (3 concurrent requests!)

asyncio.run(main())
```

Same result, fraction of the time. The speedup gets even more dramatic as you add more URLs.

### Installing aiohttp

`aiohttp` is the go-to async HTTP library for Python. It's not in the standard library, so you need to install it:

```bash
pip install aiohttp
```

### Making GET Requests

The basic pattern looks like this:

```python
import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com/data") as response:
            print(f"Status: {response.status}")
            data = await response.json()
            print(data)

asyncio.run(main())
```

There are two `async with` statements here, and both matter:
1. **`async with ClientSession()`** — creates a session (manages connection pooling)
2. **`async with session.get()`** — makes the actual request and ensures cleanup

### The ClientSession Pattern

`ClientSession` is the heart of `aiohttp`. Think of it like a browser — it manages connections, cookies, and headers across multiple requests.

**Always use one session for multiple requests.** Don't create a new session for each request — that's wasteful:

```python
# BAD — creates a new session every time
async def fetch_bad(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# GOOD — reuse the session across requests
async def fetch_good(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        results = []
        for url in urls:
            result = await fetch_good(session, url)
            results.append(result)
```

You can also set default headers, base URLs, and timeouts on the session:

```python
async with aiohttp.ClientSession(
    base_url="https://api.example.com",
    headers={"Authorization": "Bearer my-token"},
) as session:
    async with session.get("/users") as response:  # Appended to base_url
        data = await response.json()
```

### Making POST Requests

Sending data is just as straightforward:

```python
async def create_user(session, user_data):
    async with session.post("/users", json=user_data) as response:
        print(f"Status: {response.status}")
        result = await response.json()
        return result

# Usage:
new_user = {"name": "Alice", "email": "alice@example.com"}
result = await create_user(session, new_user)
```

Other HTTP methods work the same way — `session.put()`, `session.patch()`, `session.delete()`, etc.

### Handling Responses

The response object gives you everything you need:

```python
async with session.get(url) as response:
    # Status code
    print(response.status)          # 200
    print(response.reason)          # 'OK'

    # Headers
    print(response.headers)         # Full header dict
    content_type = response.headers.get("Content-Type")

    # Body — pick the format you need (these are coroutines, so await them)
    text = await response.text()          # Body as string
    data = await response.json()          # Body parsed as JSON
    raw = await response.read()           # Body as raw bytes

    # URL (useful if there were redirects)
    print(response.url)
```

**Important:** You can only read the body once per response. If you call `response.json()`, don't also call `response.text()` on the same response.

### Error Handling in Async HTTP

Things go wrong with network requests — servers go down, connections time out, APIs return errors. Here's how to handle it:

```python
async def fetch_safely(session, url):
    try:
        async with session.get(url) as response:
            # Raise an exception for 4xx/5xx status codes
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientResponseError as e:
        print(f"HTTP error {e.status}: {e.message}")
    except aiohttp.ClientConnectionError:
        print(f"Connection failed: {url}")
    except asyncio.TimeoutError:
        print(f"Request timed out: {url}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None
```

`raise_for_status()` is your friend — it turns bad HTTP status codes into exceptions so you don't accidentally process error responses as valid data.

### Concurrent Requests with gather()

This is where async HTTP really shines. Use `asyncio.gather()` to run many requests at the same time:

```python
async def fetch(session, url):
    async with session.get(url) as response:
        return {"url": url, "status": response.status, "data": await response.json()}

async def main():
    urls = [f"https://api.example.com/items/{i}" for i in range(100)]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    # Filter out any errors
    successes = [r for r in results if not isinstance(r, Exception)]
    failures = [r for r in results if isinstance(r, Exception)]
    print(f"Success: {len(successes)}, Failed: {len(failures)}")
```

The `return_exceptions=True` flag is important here — without it, one failed request would cancel everything. With it, exceptions are returned as values in the results list so you can handle them individually.

### Rate Limiting with Semaphores

Firing off 10,000 requests at once is a great way to get yourself IP-banned. Use an `asyncio.Semaphore` to limit how many requests run at the same time:

```python
async def fetch_with_limit(session, url, semaphore):
    async with semaphore:           # Wait here if too many requests are active
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = [f"https://api.example.com/items/{i}" for i in range(1000)]
    semaphore = asyncio.Semaphore(10)   # Max 10 concurrent requests

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_limit(session, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
```

The semaphore acts like a bouncer — it only lets 10 requests through at a time. When one finishes, the next one goes in. You get all the speed benefits of async without overwhelming the server.

### Timeouts

Don't let a slow server hang your entire program. Set timeouts:

```python
import aiohttp

# Timeout for the entire session
timeout = aiohttp.ClientTimeout(
    total=30,       # Total timeout for the entire operation
    connect=5,      # Timeout for establishing the connection
    sock_read=10,   # Timeout for reading a chunk of data
)

async with aiohttp.ClientSession(timeout=timeout) as session:
    async with session.get(url) as response:
        data = await response.json()
```

You can also set timeouts per-request:

```python
async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
    data = await response.json()
```

If a timeout is exceeded, you'll get an `asyncio.TimeoutError`.

### Practical Pattern: Retry with Exponential Backoff

When a request fails, you often want to retry — but not immediately. Exponential backoff waits longer between each attempt to give the server time to recover:

```python
async def fetch_with_retry(session, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            wait_time = 2 ** attempt    # 1s, 2s, 4s...
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            if attempt < max_retries - 1:
                await asyncio.sleep(wait_time)
    raise Exception(f"All {max_retries} retries failed for {url}")
```

This tries 3 times, waiting 1 second, then 2, then 4 between attempts. It's the standard pattern for dealing with flaky APIs.

### Practical Pattern: Parallel API Fetcher

Here's a complete pattern that combines everything — session reuse, concurrency limits, error handling, and retries:

```python
async def parallel_fetch(urls, max_concurrent=10, max_retries=3):
    semaphore = asyncio.Semaphore(max_concurrent)
    results = {}

    async def fetch_one(session, url):
        async with semaphore:
            for attempt in range(max_retries):
                try:
                    async with session.get(url) as response:
                        response.raise_for_status()
                        data = await response.json()
                        results[url] = {"status": "ok", "data": data}
                        return
                except Exception as e:
                    if attempt < max_retries - 1:
                        await asyncio.sleep(2 ** attempt)
            results[url] = {"status": "error", "error": str(e)}

    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = [fetch_one(session, url) for url in urls]
        await asyncio.gather(*tasks)

    return results
```

This is production-quality async HTTP. You can drop this pattern into any project.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above. It uses simulated HTTP calls (no external dependencies needed) so you can run it immediately, with commented-out `aiohttp` code showing what real usage looks like.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding. All exercises use simulated async functions so you don't need `aiohttp` installed.

## Key Takeaways

- **Async HTTP lets you make many requests concurrently** — dramatically faster than sequential requests
- **`aiohttp` is the standard async HTTP library** for Python — install it with `pip install aiohttp`
- **Always reuse `ClientSession`** — create one session and pass it to all your request functions
- **`ClientSession` and responses are both async context managers** — use `async with` for both
- **Use `asyncio.gather()` to run requests concurrently** — pass `return_exceptions=True` to handle failures gracefully
- **Use `asyncio.Semaphore` for rate limiting** — don't blast servers with thousands of simultaneous requests
- **Set timeouts with `aiohttp.ClientTimeout`** — never let a slow server hang your program
- **Implement retry with exponential backoff** for resilient API clients
- **Response bodies are coroutines** — always `await` calls to `.json()`, `.text()`, and `.read()`
