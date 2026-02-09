"""
Async HTTP — Example Code
===========================

Run this file:
    python3 example.py

This file demonstrates async HTTP patterns using SIMULATED requests (asyncio.sleep)
so it runs anywhere without external dependencies. Each section includes commented-out
real aiohttp code showing what production usage looks like.

Why simulated? aiohttp requires `pip install aiohttp` and a live network. These
simulations teach you the exact same patterns — concurrency, error handling, rate
limiting, retries — without needing anything installed.
"""

import asyncio
import random
import time


# =============================================================================
# Simulated HTTP layer — pretend these are real network calls
# =============================================================================

# These mock functions mimic what aiohttp does under the hood.
# They sleep to simulate network latency and return fake data.

async def mock_get(url, delay=0.1, fail_chance=0.0):
    """Simulate an HTTP GET request. Returns a fake response dict."""
    await asyncio.sleep(delay)  # Simulate network latency
    if random.random() < fail_chance:
        raise ConnectionError(f"Simulated connection failure for {url}")
    return {
        "url": url,
        "status": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {"message": f"Data from {url}", "timestamp": time.time()},
    }


async def mock_post(url, data, delay=0.1):
    """Simulate an HTTP POST request."""
    await asyncio.sleep(delay)
    return {
        "url": url,
        "status": 201,
        "body": {"id": random.randint(1, 1000), "created": True, **data},
    }


# =============================================================================
# 1. Basic GET request — the simplest async HTTP call
# =============================================================================

# What it looks like with our simulation:
async def demo_basic_get():
    print("Fetching data from a single URL...")
    response = await mock_get("https://api.example.com/users/1")
    print(f"  Status: {response['status']}")
    print(f"  Body: {response['body']}")

# # What it looks like with real aiohttp:
# async def demo_basic_get():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.example.com/users/1") as response:
#             print(f"  Status: {response.status}")
#             data = await response.json()
#             print(f"  Body: {data}")


# =============================================================================
# 2. Sequential vs concurrent — the whole point of async HTTP
# =============================================================================

async def demo_sequential_vs_concurrent():
    urls = [f"https://api.example.com/items/{i}" for i in range(8)]

    # --- Sequential (one at a time, like synchronous requests) ---
    start = time.time()
    sequential_results = []
    for url in urls:
        result = await mock_get(url)
        sequential_results.append(result)
    sequential_time = time.time() - start

    # --- Concurrent (all at once, the async way!) ---
    start = time.time()
    tasks = [mock_get(url) for url in urls]
    concurrent_results = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start

    print(f"  Sequential: {len(sequential_results)} requests in {sequential_time:.2f}s")
    print(f"  Concurrent: {len(concurrent_results)} requests in {concurrent_time:.2f}s")
    print(f"  Speedup: {sequential_time / concurrent_time:.1f}x faster!")

# # With real aiohttp:
# async def demo_sequential_vs_concurrent():
#     urls = [f"https://api.example.com/items/{i}" for i in range(8)]
#     async with aiohttp.ClientSession() as session:
#         # Sequential
#         for url in urls:
#             async with session.get(url) as response:
#                 await response.json()
#         # Concurrent
#         async def fetch(url):
#             async with session.get(url) as response:
#                 return await response.json()
#         results = await asyncio.gather(*[fetch(url) for url in urls])


# =============================================================================
# 3. POST requests — sending data to a server
# =============================================================================

async def demo_post_request():
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
        {"name": "Charlie", "email": "charlie@example.com"},
    ]

    print("  Creating users concurrently...")
    tasks = [mock_post("https://api.example.com/users", user) for user in users]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(f"    Created user id={result['body']['id']}: {result['body']['name']}")

# # With real aiohttp:
# async def demo_post_request():
#     async with aiohttp.ClientSession() as session:
#         user_data = {"name": "Alice", "email": "alice@example.com"}
#         async with session.post("https://api.example.com/users", json=user_data) as resp:
#             result = await resp.json()
#             print(f"  Created: {result}")


# =============================================================================
# 4. Handling responses — status, headers, body
# =============================================================================

async def demo_response_handling():
    response = await mock_get("https://api.example.com/data")

    status = response["status"]
    headers = response["headers"]
    body = response["body"]

    print(f"  Status: {status}")
    print(f"  Content-Type: {headers.get('Content-Type', 'unknown')}")
    print(f"  Body message: {body['message']}")

    # Check status before processing
    if status == 200:
        print("  Success! Processing data...")
    elif status == 404:
        print("  Not found!")
    elif status >= 500:
        print("  Server error!")

# # With real aiohttp:
# async def demo_response_handling():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.example.com/data") as response:
#             print(f"  Status: {response.status}")
#             print(f"  Content-Type: {response.headers.get('Content-Type')}")
#             body = await response.json()   # or response.text(), response.read()
#             print(f"  Body: {body}")


# =============================================================================
# 5. Error handling — things go wrong, and that's okay
# =============================================================================

async def fetch_safely(url):
    """Fetch a URL with proper error handling."""
    try:
        result = await mock_get(url, fail_chance=0.5)  # 50% chance of failure!
        return {"url": url, "status": "ok", "data": result["body"]}
    except ConnectionError as e:
        return {"url": url, "status": "error", "error": str(e)}
    except asyncio.TimeoutError:
        return {"url": url, "status": "timeout", "error": "Request timed out"}
    except Exception as e:
        return {"url": url, "status": "error", "error": f"Unexpected: {e}"}


async def demo_error_handling():
    urls = [f"https://api.example.com/data/{i}" for i in range(6)]

    random.seed(42)  # Reproducible results for the demo
    results = await asyncio.gather(*[fetch_safely(url) for url in urls])

    successes = [r for r in results if r["status"] == "ok"]
    failures = [r for r in results if r["status"] != "ok"]

    print(f"  Results: {len(successes)} succeeded, {len(failures)} failed")
    for r in failures:
        print(f"    FAILED: {r['url']} — {r['error']}")

# # With real aiohttp:
# async def fetch_safely(session, url):
#     try:
#         async with session.get(url) as response:
#             response.raise_for_status()
#             return {"url": url, "status": "ok", "data": await response.json()}
#     except aiohttp.ClientResponseError as e:
#         return {"url": url, "status": "error", "error": f"HTTP {e.status}"}
#     except aiohttp.ClientConnectionError:
#         return {"url": url, "status": "error", "error": "Connection failed"}
#     except asyncio.TimeoutError:
#         return {"url": url, "status": "timeout", "error": "Timed out"}


# =============================================================================
# 6. Rate limiting with Semaphore — be nice to servers
# =============================================================================

async def fetch_with_limit(url, semaphore):
    """Fetch a URL, but only if the semaphore allows it."""
    async with semaphore:
        print(f"    Fetching: {url}")
        result = await mock_get(url, delay=0.2)
        return result


async def demo_rate_limiting():
    urls = [f"https://api.example.com/page/{i}" for i in range(10)]

    # Only allow 3 requests at a time
    semaphore = asyncio.Semaphore(3)

    print("  Fetching 10 URLs with max 3 concurrent...")
    start = time.time()
    tasks = [fetch_with_limit(url, semaphore) for url in urls]
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start

    print(f"  Fetched {len(results)} URLs in {elapsed:.2f}s")
    print(f"  (Without limit it'd be ~0.2s, with limit ~0.8s because of batching)")

# # With real aiohttp:
# async def fetch_with_limit(session, url, semaphore):
#     async with semaphore:
#         async with session.get(url) as response:
#             return await response.json()


# =============================================================================
# 7. Retry with exponential backoff — handle flaky servers
# =============================================================================

async def fetch_with_retry(url, max_retries=3):
    """Try fetching a URL, retrying on failure with increasing wait times."""
    for attempt in range(max_retries):
        try:
            # High failure chance to demonstrate retries
            result = await mock_get(url, delay=0.05, fail_chance=0.6)
            print(f"    {url} succeeded on attempt {attempt + 1}")
            return result
        except ConnectionError:
            wait_time = 0.1 * (2 ** attempt)  # 0.1s, 0.2s, 0.4s (short for demo)
            if attempt < max_retries - 1:
                print(f"    {url} failed attempt {attempt + 1}, retrying in {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
            else:
                print(f"    {url} failed all {max_retries} attempts!")
                return None


async def demo_retry_backoff():
    urls = [f"https://api.example.com/flaky/{i}" for i in range(4)]

    random.seed(123)  # Reproducible results
    results = await asyncio.gather(*[fetch_with_retry(url) for url in urls])

    successes = [r for r in results if r is not None]
    print(f"  Final results: {len(successes)}/{len(urls)} succeeded")

# # With real aiohttp:
# async def fetch_with_retry(session, url, max_retries=3):
#     for attempt in range(max_retries):
#         try:
#             async with session.get(url) as response:
#                 response.raise_for_status()
#                 return await response.json()
#         except (aiohttp.ClientError, asyncio.TimeoutError):
#             if attempt < max_retries - 1:
#                 await asyncio.sleep(2 ** attempt)
#     return None


# =============================================================================
# 8. Full pattern — parallel fetcher with all the bells and whistles
# =============================================================================

async def parallel_fetch(urls, max_concurrent=3, max_retries=2):
    """
    Production-quality parallel fetcher.
    Combines: concurrency limits + retries + error handling.
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    results = {}

    async def fetch_one(url):
        async with semaphore:
            last_error = None
            for attempt in range(max_retries):
                try:
                    response = await mock_get(url, delay=0.1, fail_chance=0.3)
                    results[url] = {"status": "ok", "data": response["body"]}
                    return
                except Exception as e:
                    last_error = e
                    if attempt < max_retries - 1:
                        await asyncio.sleep(0.1 * (2 ** attempt))
            results[url] = {"status": "error", "error": str(last_error)}

    tasks = [fetch_one(url) for url in urls]
    await asyncio.gather(*tasks)
    return results


async def demo_parallel_fetcher():
    urls = [f"https://api.example.com/products/{i}" for i in range(12)]

    random.seed(99)
    start = time.time()
    results = await parallel_fetch(urls, max_concurrent=4, max_retries=2)
    elapsed = time.time() - start

    ok = sum(1 for r in results.values() if r["status"] == "ok")
    failed = sum(1 for r in results.values() if r["status"] == "error")

    print(f"  Fetched {len(urls)} URLs in {elapsed:.2f}s")
    print(f"  Success: {ok}, Failed: {failed}")
    if failed > 0:
        for url, r in results.items():
            if r["status"] == "error":
                print(f"    FAILED: {url} — {r['error']}")

# # With real aiohttp, the structure is identical — just swap mock_get for session.get:
# async def parallel_fetch(urls, max_concurrent=10, max_retries=3):
#     semaphore = asyncio.Semaphore(max_concurrent)
#     results = {}
#     timeout = aiohttp.ClientTimeout(total=30)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         async def fetch_one(url):
#             async with semaphore:
#                 for attempt in range(max_retries):
#                     try:
#                         async with session.get(url) as response:
#                             response.raise_for_status()
#                             data = await response.json()
#                             results[url] = {"status": "ok", "data": data}
#                             return
#                     except Exception as e:
#                         if attempt < max_retries - 1:
#                             await asyncio.sleep(2 ** attempt)
#                 results[url] = {"status": "error", "error": str(e)}
#         await asyncio.gather(*[fetch_one(url) for url in urls])
#     return results


# =============================================================================
# Run all demos
# =============================================================================

async def main():
    demos = [
        ("Basic GET request", demo_basic_get),
        ("Sequential vs concurrent", demo_sequential_vs_concurrent),
        ("POST requests", demo_post_request),
        ("Response handling", demo_response_handling),
        ("Error handling", demo_error_handling),
        ("Rate limiting with Semaphore", demo_rate_limiting),
        ("Retry with exponential backoff", demo_retry_backoff),
        ("Full parallel fetcher pattern", demo_parallel_fetcher),
    ]

    for i, (title, demo) in enumerate(demos, 1):
        print("=" * 60)
        print(f"DEMO {i}: {title}")
        print("=" * 60)
        await demo()
        print()

    print("-" * 60)
    print("All demos complete!")
    print()
    print("These examples used simulated HTTP requests (asyncio.sleep).")
    print("To use real HTTP, install aiohttp: pip install aiohttp")
    print("Then swap the mock functions for real aiohttp calls —")
    print("the async patterns are exactly the same!")


if __name__ == "__main__":
    asyncio.run(main())
