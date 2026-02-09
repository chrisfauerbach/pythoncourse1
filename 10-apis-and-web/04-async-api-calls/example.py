"""
Async API Calls — Example Code
================================

Run this file:
    python3 example.py

This file demonstrates async API call patterns using SIMULATED requests (asyncio.sleep)
so it runs anywhere without external dependencies. Each section includes commented-out
real aiohttp/httpx code showing what production usage looks like.

Why simulated? aiohttp requires `pip install aiohttp` and a live network. These
simulations teach you the exact same patterns — concurrency, error handling, rate
limiting, retries, pagination — without needing anything installed.
"""

import asyncio
import random
import time
from typing import List, Dict, Any


# =============================================================================
# SIMULATED API LAYER — pretend these are real API calls
# =============================================================================

async def mock_api_get(url: str, delay: float = 0.1, fail_chance: float = 0.0) -> Dict[str, Any]:
    """Simulate an API GET request. Returns fake JSON data."""
    await asyncio.sleep(delay)  # Simulate network latency

    if random.random() < fail_chance:
        raise ConnectionError(f"API request failed: {url}")

    # Simulate different API responses based on URL
    if "/users/" in url:
        user_id = url.split("/users/")[-1].split("?")[0]
        return {"id": user_id, "name": f"User {user_id}", "email": f"user{user_id}@example.com"}
    elif "/products/" in url:
        product_id = url.split("/products/")[-1].split("?")[0]
        return {"id": product_id, "name": f"Product {product_id}", "price": random.randint(10, 100)}
    elif "page=" in url:
        page = url.split("page=")[-1].split("&")[0]
        return {"page": int(page), "items": [f"item_{page}_{i}" for i in range(5)], "has_next": int(page) < 3}
    else:
        return {"url": url, "message": "Success", "data": [1, 2, 3]}


# # Real aiohttp version:
# import aiohttp
# async def api_get(session, url):
#     async with session.get(url) as response:
#         response.raise_for_status()
#         return await response.json()


# =============================================================================
# 1. Single async API call — the basics
# =============================================================================

async def demo_single_api_call():
    """Fetch data from a single API endpoint."""
    print("Fetching user data...")
    user = await mock_api_get("https://api.example.com/users/42")
    print(f"  Got user: {user['name']} ({user['email']})")


# # With real aiohttp:
# async def demo_single_api_call():
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://api.example.com/users/42") as response:
#             user = await response.json()
#             print(f"  Got user: {user['name']}")


# =============================================================================
# 2. Multiple concurrent API calls with gather()
# =============================================================================

async def demo_concurrent_api_calls():
    """Fetch multiple users concurrently — the main benefit of async."""
    user_ids = [1, 2, 3, 4, 5]

    # Sequential (for comparison)
    start = time.time()
    sequential_users = []
    for user_id in user_ids:
        user = await mock_api_get(f"https://api.example.com/users/{user_id}")
        sequential_users.append(user)
    sequential_time = time.time() - start

    # Concurrent (the async way!)
    start = time.time()
    tasks = [mock_api_get(f"https://api.example.com/users/{user_id}") for user_id in user_ids]
    concurrent_users = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start

    print(f"  Sequential: {len(sequential_users)} users in {sequential_time:.3f}s")
    print(f"  Concurrent: {len(concurrent_users)} users in {concurrent_time:.3f}s")
    print(f"  Speedup: {sequential_time / concurrent_time:.1f}x faster!")


# # With real aiohttp:
# async def demo_concurrent_api_calls():
#     user_ids = [1, 2, 3, 4, 5]
#     async with aiohttp.ClientSession() as session:
#         async def fetch_user(user_id):
#             async with session.get(f"https://api.example.com/users/{user_id}") as resp:
#                 return await resp.json()
#         users = await asyncio.gather(*[fetch_user(uid) for uid in user_ids])


# =============================================================================
# 3. Sequential vs concurrent performance comparison
# =============================================================================

async def demo_performance_comparison():
    """Show the dramatic difference between sequential and concurrent API calls."""
    num_calls = 10
    urls = [f"https://api.example.com/products/{i}" for i in range(num_calls)]

    print(f"  Making {num_calls} API calls (each takes ~100ms)...")

    # Sequential
    start = time.time()
    seq_results = []
    for url in urls:
        result = await mock_api_get(url, delay=0.1)
        seq_results.append(result)
    seq_time = time.time() - start

    # Concurrent
    start = time.time()
    tasks = [mock_api_get(url, delay=0.1) for url in urls]
    con_results = await asyncio.gather(*tasks)
    con_time = time.time() - start

    print(f"  Sequential: {seq_time:.3f}s (waited for each one)")
    print(f"  Concurrent: {con_time:.3f}s (all at once!)")
    print(f"  Time saved: {seq_time - con_time:.3f}s ({(1 - con_time/seq_time) * 100:.0f}% faster)")


# =============================================================================
# 4. Rate-limited API calls with Semaphore
# =============================================================================

async def fetch_with_limit(url: str, semaphore: asyncio.Semaphore) -> Dict[str, Any]:
    """Fetch URL with rate limiting — only N requests can run at once."""
    async with semaphore:
        return await mock_api_get(url, delay=0.1)


async def demo_rate_limiting():
    """Use Semaphore to limit concurrent requests (be nice to APIs!)"""
    urls = [f"https://api.example.com/products/{i}" for i in range(20)]

    # Without rate limiting (all at once)
    print("  Without rate limiting: 20 requests fire simultaneously...")
    start = time.time()
    results = await asyncio.gather(*[mock_api_get(url, delay=0.1) for url in urls])
    no_limit_time = time.time() - start
    print(f"    Completed in {no_limit_time:.3f}s")

    # With rate limiting (max 5 concurrent)
    print("  With rate limiting: max 5 concurrent requests...")
    semaphore = asyncio.Semaphore(5)
    start = time.time()
    results = await asyncio.gather(*[fetch_with_limit(url, semaphore) for url in urls])
    limited_time = time.time() - start
    print(f"    Completed in {limited_time:.3f}s")
    print(f"    (Took longer but respects API limits — prevents rate limiting/bans)")


# # With real aiohttp:
# async def fetch_with_limit(session, url, semaphore):
#     async with semaphore:
#         async with session.get(url) as response:
#             return await response.json()


# =============================================================================
# 5. Retry logic with exponential backoff
# =============================================================================

async def fetch_with_retry(url: str, max_retries: int = 3) -> Dict[str, Any]:
    """Try fetching a URL, retrying on failure with exponential backoff."""
    for attempt in range(max_retries):
        try:
            # High failure chance to demonstrate retries
            result = await mock_api_get(url, delay=0.05, fail_chance=0.5)
            if attempt > 0:
                print(f"      SUCCESS on attempt {attempt + 1}")
            return result
        except ConnectionError as e:
            wait_time = 0.1 * (2 ** attempt)  # 0.1s, 0.2s, 0.4s
            if attempt < max_retries - 1:
                print(f"      Attempt {attempt + 1} failed, retrying in {wait_time:.1f}s...")
                await asyncio.sleep(wait_time)
            else:
                print(f"      All {max_retries} attempts failed!")
                raise


async def demo_retry_backoff():
    """Show how retry with exponential backoff handles flaky APIs."""
    urls = [f"https://api.example.com/flaky/{i}" for i in range(5)]

    random.seed(42)  # Reproducible results
    print("  Fetching from flaky API (50% failure rate per request)...")

    results = await asyncio.gather(
        *[fetch_with_retry(url) for url in urls],
        return_exceptions=True
    )

    successes = [r for r in results if not isinstance(r, Exception)]
    failures = [r for r in results if isinstance(r, Exception)]

    print(f"  Final results: {len(successes)} succeeded, {len(failures)} failed")


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
#             else:
#                 raise


# =============================================================================
# 6. Async pagination (fetching multiple pages)
# =============================================================================

async def fetch_page(page_num: int) -> Dict[str, Any]:
    """Fetch a single page of data."""
    url = f"https://api.example.com/items?page={page_num}"
    return await mock_api_get(url, delay=0.1)


async def demo_pagination():
    """Fetch multiple pages of data concurrently instead of sequentially."""

    # Sequential pagination (traditional way)
    print("  Sequential pagination (one page at a time)...")
    start = time.time()
    all_items = []
    for page in range(1, 4):
        data = await fetch_page(page)
        all_items.extend(data["items"])
    seq_time = time.time() - start
    print(f"    Got {len(all_items)} items in {seq_time:.3f}s")

    # Concurrent pagination (async way!)
    print("  Concurrent pagination (all pages at once)...")
    start = time.time()
    pages = await asyncio.gather(*[fetch_page(page) for page in range(1, 4)])
    all_items = []
    for page_data in pages:
        all_items.extend(page_data["items"])
    con_time = time.time() - start
    print(f"    Got {len(all_items)} items in {con_time:.3f}s")
    print(f"    Speedup: {seq_time / con_time:.1f}x faster!")


# # With real aiohttp:
# async def fetch_all_pages(session, num_pages):
#     async def fetch_page(page_num):
#         url = f"https://api.example.com/items?page={page_num}"
#         async with session.get(url) as response:
#             return await response.json()
#     pages = await asyncio.gather(*[fetch_page(p) for p in range(1, num_pages + 1)])
#     return [item for page in pages for item in page["items"]]


# =============================================================================
# 7. Fan-out pattern (one call triggers many)
# =============================================================================

async def fetch_user_list() -> List[int]:
    """Fetch list of user IDs (first API call)."""
    await asyncio.sleep(0.1)  # Simulate API call
    return [1, 2, 3, 4, 5, 6, 7, 8]


async def fetch_user_details(user_id: int) -> Dict[str, Any]:
    """Fetch detailed info for one user (subsequent API calls)."""
    return await mock_api_get(f"https://api.example.com/users/{user_id}", delay=0.1)


async def demo_fan_out():
    """First call gets list, then fan out to fetch details concurrently."""

    print("  Step 1: Fetch user list...")
    start = time.time()
    user_ids = await fetch_user_list()
    print(f"    Got {len(user_ids)} user IDs")

    print("  Step 2: Fan out — fetch all user details concurrently...")
    tasks = [fetch_user_details(uid) for uid in user_ids]
    detailed_users = await asyncio.gather(*tasks)

    total_time = time.time() - start
    print(f"    Got details for {len(detailed_users)} users")
    print(f"    Total time: {total_time:.3f}s (vs ~{0.1 * (len(user_ids) + 1):.1f}s sequential)")


# # With real aiohttp:
# async def demo_fan_out():
#     async with aiohttp.ClientSession() as session:
#         # Step 1: Get list
#         async with session.get("https://api.example.com/users") as response:
#             user_list = await response.json()
#             user_ids = [u["id"] for u in user_list]
#
#         # Step 2: Fan out
#         async def fetch_details(user_id):
#             async with session.get(f"https://api.example.com/users/{user_id}") as resp:
#                 return await resp.json()
#         details = await asyncio.gather(*[fetch_details(uid) for uid in user_ids])


# =============================================================================
# 8. Complete real-world example: async API client class
# =============================================================================

class AsyncAPIClient:
    """Production-quality async API client with all the bells and whistles."""

    def __init__(self, base_url: str, max_concurrent: int = 10, max_retries: int = 3):
        self.base_url = base_url
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.max_retries = max_retries

    async def get(self, endpoint: str) -> Dict[str, Any]:
        """GET request with rate limiting and retry logic."""
        url = f"{self.base_url}/{endpoint}"

        async with self.semaphore:
            for attempt in range(self.max_retries):
                try:
                    return await mock_api_get(url, delay=0.05, fail_chance=0.2)
                except Exception as e:
                    if attempt < self.max_retries - 1:
                        await asyncio.sleep(0.05 * (2 ** attempt))
                    else:
                        return {"error": str(e), "endpoint": endpoint}

    async def get_many(self, endpoints: List[str]) -> List[Dict[str, Any]]:
        """Fetch multiple endpoints concurrently."""
        tasks = [self.get(endpoint) for endpoint in endpoints]
        return await asyncio.gather(*tasks)


async def demo_api_client_class():
    """Show how to use a complete async API client class."""

    client = AsyncAPIClient(
        base_url="https://api.example.com",
        max_concurrent=5,
        max_retries=2
    )

    print("  Fetching multiple endpoints with API client...")
    endpoints = ["users/1", "users/2", "products/10", "products/11", "users/3"]

    random.seed(99)
    start = time.time()
    results = await client.get_many(endpoints)
    elapsed = time.time() - start

    print(f"    Fetched {len(results)} endpoints in {elapsed:.3f}s")

    successes = [r for r in results if "error" not in r]
    failures = [r for r in results if "error" in r]
    print(f"    Success: {len(successes)}, Failed: {len(failures)}")

    if failures:
        for result in failures:
            print(f"      FAILED: {result['endpoint']} — {result['error']}")


# # With real aiohttp:
# class AsyncAPIClient:
#     def __init__(self, base_url, max_concurrent=10, max_retries=3):
#         self.base_url = base_url
#         self.semaphore = asyncio.Semaphore(max_concurrent)
#         self.max_retries = max_retries
#         self.session = None
#
#     async def __aenter__(self):
#         timeout = aiohttp.ClientTimeout(total=30)
#         self.session = aiohttp.ClientSession(timeout=timeout)
#         return self
#
#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         await self.session.close()
#
#     async def get(self, endpoint):
#         url = f"{self.base_url}/{endpoint}"
#         async with self.semaphore:
#             for attempt in range(self.max_retries):
#                 try:
#                     async with self.session.get(url) as response:
#                         response.raise_for_status()
#                         return await response.json()
#                 except Exception as e:
#                     if attempt < self.max_retries - 1:
#                         await asyncio.sleep(2 ** attempt)
#                     else:
#                         raise


# =============================================================================
# Run all demos
# =============================================================================

async def main():
    """Run all examples in sequence."""

    demos = [
        ("Single async API call", demo_single_api_call),
        ("Multiple concurrent API calls with gather()", demo_concurrent_api_calls),
        ("Sequential vs concurrent performance", demo_performance_comparison),
        ("Rate-limited API calls with Semaphore", demo_rate_limiting),
        ("Retry logic with exponential backoff", demo_retry_backoff),
        ("Async pagination (fetching multiple pages)", demo_pagination),
        ("Fan-out pattern (one call triggers many)", demo_fan_out),
        ("Complete async API client class", demo_api_client_class),
    ]

    for i, (title, demo) in enumerate(demos, 1):
        print("=" * 70)
        print(f"DEMO {i}: {title}")
        print("=" * 70)
        await demo()
        print()

    print("-" * 70)
    print("All demos complete!")
    print()
    print("These examples used simulated API calls (asyncio.sleep).")
    print("To use real HTTP, install aiohttp: pip install aiohttp")
    print("Then swap mock_api_get for real aiohttp calls —")
    print("the async patterns are exactly the same!")


if __name__ == "__main__":
    asyncio.run(main())
