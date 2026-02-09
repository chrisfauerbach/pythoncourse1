# Async API Calls

## Objective

Learn how to make API calls asynchronously so you can interact with web APIs efficiently, fetching data from dozens or hundreds of endpoints in parallel instead of waiting for each one sequentially.

## Concepts Covered

- Why async matters for API calls (I/O-bound work, performance)
- Comparing sync vs async API call patterns
- Using `asyncio.gather()` for parallel API requests
- Rate limiting with `asyncio.Semaphore` (being nice to APIs)
- Error handling and retry logic in async context
- Exponential backoff for resilient API clients
- Async pagination patterns (fetching multiple pages)
- Fan-out pattern (one call triggers many more)
- Building complete async API client classes
- Real-world patterns: webhooks, streaming, data aggregation

## Prerequisites

- Comfortable with `async` / `await` syntax (lesson 07-async-python/01-async-basics)
- Understanding of `asyncio.gather()` and tasks (lesson 07-async-python/02-async-tasks)
- Familiarity with async HTTP concepts (lesson 07-async-python/04-async-http)
- Basic understanding of REST APIs, HTTP methods, JSON

## Lesson

### Why Async API Calls Matter

APIs are everywhere in modern software. You need to:
- Fetch user data from 10 different microservices
- Check inventory across 50 warehouse APIs
- Aggregate weather data from 100 weather stations
- Sync data between your app and third-party services

Here's the problem: APIs are **I/O-bound**. Most of the time is spent waiting for the network, not doing computation. If you make API calls sequentially (one after another), you spend 99% of your time waiting:

```
Sync approach:
Call API 1 → wait 200ms → Call API 2 → wait 200ms → Call API 3 → wait 200ms
Total: 600ms (200ms × 3)

Async approach:
Call API 1 ┐
Call API 2 ├─ all fire at once → wait 200ms
Call API 3 ┘
Total: ~200ms (concurrent!)
```

With 50 API calls, that's the difference between 10 seconds and 200 milliseconds. That's a 50x speedup.

### Sync vs Async: The API Call Pattern

Here's what traditional synchronous API calls look like:

```python
import requests  # The standard sync HTTP library

# Fetch user data from 5 endpoints
user_ids = [1, 2, 3, 4, 5]
users = []

for user_id in user_ids:
    response = requests.get(f"https://api.example.com/users/{user_id}")
    users.append(response.json())
    # Next call doesn't start until this one finishes

print(f"Fetched {len(users)} users")
# Takes: 5 × 200ms = 1000ms (1 second)
```

And here's the async version:

```python
import aiohttp  # The standard async HTTP library
import asyncio

async def fetch_user(session, user_id):
    async with session.get(f"https://api.example.com/users/{user_id}") as response:
        return await response.json()

async def main():
    user_ids = [1, 2, 3, 4, 5]

    async with aiohttp.ClientSession() as session:
        # Fire all requests at once
        tasks = [fetch_user(session, user_id) for user_id in user_ids]
        users = await asyncio.gather(*tasks)

    print(f"Fetched {len(users)} users")
    # Takes: ~200ms (all concurrent!)

asyncio.run(main())
```

The structure is slightly more complex, but the performance difference is dramatic. And as you add more API calls, the gap gets even wider.

### Parallel API Calls with gather()

`asyncio.gather()` is your best friend for parallel API calls. It lets you fire off many requests at once and wait for all of them to complete:

```python
async def fetch_data(session, endpoint):
    async with session.get(f"https://api.example.com/{endpoint}") as response:
        return await response.json()

async def main():
    endpoints = ["users", "posts", "comments", "photos", "albums"]

    async with aiohttp.ClientSession() as session:
        # Create tasks for all endpoints
        tasks = [fetch_data(session, endpoint) for endpoint in endpoints]

        # Execute them all concurrently
        results = await asyncio.gather(*tasks)

        # results is a list in the same order as endpoints
        users, posts, comments, photos, albums = results
```

**Pro tip:** Use `return_exceptions=True` to handle failures gracefully. Without it, one failed request cancels everything:

```python
results = await asyncio.gather(*tasks, return_exceptions=True)

# Now exceptions are returned as values in the list
for endpoint, result in zip(endpoints, results):
    if isinstance(result, Exception):
        print(f"Failed to fetch {endpoint}: {result}")
    else:
        print(f"Fetched {endpoint}: {len(result)} items")
```

### Rate Limiting with Semaphore

Here's a harsh truth: if you fire off 10,000 API requests at once, you'll probably get rate-limited, banned, or worse. Most APIs have limits like "100 requests per second" or "10 concurrent connections."

Use `asyncio.Semaphore` to limit how many requests run at the same time:

```python
async def fetch_with_limit(session, url, semaphore):
    async with semaphore:  # Only N requests can be here at once
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls = [f"https://api.example.com/items/{i}" for i in range(1000)]

    # Allow max 10 concurrent requests
    semaphore = asyncio.Semaphore(10)

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_with_limit(session, url, semaphore) for url in urls]
        results = await asyncio.gather(*tasks)
```

The semaphore acts like a bouncer at a club: it only lets 10 requests in at a time. When one finishes, the next one goes in. You get the speed benefits of async without overwhelming the API server.

### Error Handling in Async API Calls

Network requests fail all the time. Servers go down, connections time out, rate limits get hit. Your code needs to handle this gracefully:

```python
async def fetch_safely(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()  # Raises exception for 4xx/5xx
            return {"status": "ok", "data": await response.json()}
    except aiohttp.ClientResponseError as e:
        return {"status": "error", "error": f"HTTP {e.status}: {e.message}"}
    except aiohttp.ClientConnectionError:
        return {"status": "error", "error": "Connection failed"}
    except asyncio.TimeoutError:
        return {"status": "error", "error": "Request timed out"}
    except Exception as e:
        return {"status": "error", "error": str(e)}
```

Now instead of crashing, you get structured error information you can log or retry.

### Retry with Exponential Backoff

When an API call fails, you often want to retry — but not immediately. Exponential backoff waits longer between each retry to give the server time to recover:

```python
async def fetch_with_retry(session, url, max_retries=3):
    for attempt in range(max_retries):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            wait_time = 2 ** attempt  # 1s, 2s, 4s...
            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                print(f"Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                print(f"All {max_retries} retries failed")
                raise
```

This is the standard pattern for resilient API clients. The first retry waits 1 second, the second waits 2, the third waits 4. It gives temporary issues time to resolve without hammering a struggling server.

### Async Pagination

Many APIs return data in pages. You might need to fetch page 1, then page 2, then page 3, and so on. You can do this concurrently:

```python
async def fetch_page(session, page_num):
    url = f"https://api.example.com/items?page={page_num}"
    async with session.get(url) as response:
        data = await response.json()
        return data["items"]

async def fetch_all_pages(session, num_pages):
    # Fetch all pages concurrently
    tasks = [fetch_page(session, page) for page in range(1, num_pages + 1)]
    pages = await asyncio.gather(*tasks)

    # Flatten the list of lists
    all_items = []
    for page_items in pages:
        all_items.extend(page_items)

    return all_items
```

This fetches all pages at once instead of waiting for page 1 before fetching page 2. If you have 10 pages, that's another 10x speedup.

### Fan-Out Pattern

Sometimes one API call tells you what other calls you need to make. For example:
1. Fetch a list of user IDs
2. For each user ID, fetch detailed user info

This is called "fan-out":

```python
async def fetch_user_details(session, user_id):
    url = f"https://api.example.com/users/{user_id}"
    async with session.get(url) as response:
        return await response.json()

async def fetch_all_user_details(session):
    # Step 1: Get list of user IDs
    async with session.get("https://api.example.com/users") as response:
        user_list = await response.json()
        user_ids = [u["id"] for u in user_list]

    # Step 2: Fan out — fetch details for all users concurrently
    tasks = [fetch_user_details(session, user_id) for user_id in user_ids]
    detailed_users = await asyncio.gather(*tasks)

    return detailed_users
```

The key is that the second step happens concurrently even though it depends on the first step.

### Building an Async API Client Class

For production code, wrap all these patterns into a reusable class:

```python
class AsyncAPIClient:
    def __init__(self, base_url, max_concurrent=10, max_retries=3):
        self.base_url = base_url
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.max_retries = max_retries
        self.session = None

    async def __aenter__(self):
        timeout = aiohttp.ClientTimeout(total=30)
        self.session = aiohttp.ClientSession(timeout=timeout)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"

        async with self.semaphore:
            for attempt in range(self.max_retries):
                try:
                    async with self.session.get(url) as response:
                        response.raise_for_status()
                        return await response.json()
                except Exception as e:
                    if attempt < self.max_retries - 1:
                        await asyncio.sleep(2 ** attempt)
                    else:
                        raise

    async def get_many(self, endpoints):
        tasks = [self.get(endpoint) for endpoint in endpoints]
        return await asyncio.gather(*tasks, return_exceptions=True)

# Usage:
async with AsyncAPIClient("https://api.example.com", max_concurrent=5) as client:
    results = await client.get_many(["users", "posts", "comments"])
```

This client handles:
- Rate limiting (max concurrent requests)
- Retries with exponential backoff
- Proper session management
- Timeout configuration
- Error handling

You can drop this pattern into any project and start making async API calls immediately.

### Real-World Pattern: Data Aggregation

Here's a complete pattern for aggregating data from multiple APIs:

```python
async def aggregate_user_stats(user_id):
    """Fetch user data from multiple services and combine it."""

    async with aiohttp.ClientSession() as session:
        # Fire off multiple API calls at once
        profile_task = session.get(f"https://api.users.com/users/{user_id}")
        posts_task = session.get(f"https://api.posts.com/users/{user_id}/posts")
        comments_task = session.get(f"https://api.comments.com/users/{user_id}/comments")

        # Wait for all to complete
        profile_resp, posts_resp, comments_resp = await asyncio.gather(
            profile_task, posts_task, comments_task
        )

        # Extract data
        profile = await profile_resp.json()
        posts = await posts_resp.json()
        comments = await comments_resp.json()

        # Combine into aggregate stats
        return {
            "user_id": user_id,
            "name": profile["name"],
            "post_count": len(posts),
            "comment_count": len(comments),
            "karma": profile["karma"],
        }
```

This makes 3 API calls concurrently and combines the results. If each call takes 200ms, this completes in ~200ms instead of 600ms.

### Real-World Pattern: Webhooks and Streaming

Some APIs support webhooks (you give them a URL and they call you back) or streaming (they send data continuously). For these, async is essential:

```python
# Simplified streaming example
async def stream_api_updates():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.example.com/stream") as response:
            async for line in response.content:
                data = json.loads(line)
                print(f"Received update: {data}")
                # Process update in the background
                asyncio.create_task(process_update(data))
```

The key is that you're processing updates as they arrive without blocking the stream.

### When NOT to Use Async API Calls

Async adds complexity. Don't use it if:
- You're making 1-2 API calls total
- The API explicitly limits you to 1 request at a time
- Your code is simpler with synchronous calls
- You're prototyping and speed doesn't matter yet

For small scripts or one-off tasks, `requests` is totally fine. But when you need to scale to dozens or hundreds of API calls, async is the way to go.

## Code Example

Check out [`example.py`](example.py) for complete working examples of all these patterns. It uses simulated HTTP calls (no external dependencies needed) so you can run it immediately, with commented-out `aiohttp` code showing what real usage looks like.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding. All exercises use simulated async functions so you don't need `aiohttp` installed.

## Key Takeaways

- **Async API calls provide massive speedups for I/O-bound work** — 10-100x faster than sequential calls
- **Use `asyncio.gather()` for parallel requests** — fire off many requests at once and wait for all to complete
- **Use `asyncio.Semaphore` for rate limiting** — respect API limits by controlling concurrent request count
- **Always implement retry with exponential backoff** — 1s, 2s, 4s wait times between retries
- **Handle errors gracefully** — return structured error info instead of crashing
- **Use `return_exceptions=True` in gather()** — one failed request shouldn't kill everything
- **Reuse `ClientSession` across requests** — creating a new session per request is wasteful
- **Build reusable API client classes** — wrap all these patterns into clean, testable interfaces
- **Async pagination fetches all pages concurrently** — don't wait for page 1 to fetch page 2
- **Fan-out pattern: one call triggers many** — fetch overview first, then details concurrently
- **For production, add timeouts, retries, and logging** — resilient API clients need all three

## Next Steps

- Explore real APIs with `aiohttp` — install it with `pip install aiohttp`
- Learn about GraphQL clients (async-friendly by design)
- Study rate limiting strategies (token bucket, sliding window)
- Implement request caching to reduce API calls
- Build a complete async web scraper
- Learn about async queues for request/response pipelines
