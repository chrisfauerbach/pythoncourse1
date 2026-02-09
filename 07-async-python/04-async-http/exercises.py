"""
Async HTTP — Exercises
=======================

Practice problems to test your understanding of async HTTP patterns.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

All exercises use SIMULATED async functions (asyncio.sleep-based mocks) so you
don't need aiohttp or any external dependencies. The patterns are identical to
what you'd use with real HTTP — just swap the mock functions for aiohttp calls.
"""

import asyncio
import random
import time


# =============================================================================
# Shared mock functions — these simulate HTTP requests
# =============================================================================
# Use these in your exercises. They're already written for you.

async def mock_fetch(url, delay=0.1):
    """
    Simulate fetching a URL. Returns a dict with status, url, and body.
    Sleeps for `delay` seconds to simulate network latency.
    """
    await asyncio.sleep(delay)
    return {
        "status": 200,
        "url": url,
        "body": f"Content from {url}",
    }


async def mock_fetch_unreliable(url, delay=0.1, fail_chance=0.5):
    """
    Like mock_fetch, but randomly fails to simulate flaky servers.
    Raises ConnectionError on failure.
    """
    await asyncio.sleep(delay)
    if random.random() < fail_chance:
        raise ConnectionError(f"Failed to connect to {url}")
    return {
        "status": 200,
        "url": url,
        "body": f"Content from {url}",
    }


async def mock_fetch_page(url, delay=0.1):
    """
    Simulate fetching a web page. Returns a dict with HTML-like content
    containing 'links' and 'title' that you can extract data from.
    """
    await asyncio.sleep(delay)
    # Simulate different pages with different data
    page_num = url.split("/")[-1] if "/" in url else "0"
    return {
        "status": 200,
        "url": url,
        "title": f"Page {page_num}",
        "links": [f"{url}/item/{j}" for j in range(3)],
        "word_count": random.randint(100, 2000),
    }


# =============================================================================
# Exercise 1: Fetch a single URL
#
# Write an async function `fetch_one` that:
# - Takes a URL string as its argument
# - Calls mock_fetch() to get the response
# - Returns a string in the format: "[STATUS] url — body"
#   For example: "[200] https://example.com — Content from https://example.com"
#
# Then call it in exercise_1() and print the result.
# =============================================================================

async def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Fetch multiple URLs concurrently
#
# Write an async function `fetch_all` that:
# - Takes a list of URL strings
# - Fetches ALL of them concurrently using asyncio.gather()
# - Returns a list of response dicts (the raw return values from mock_fetch)
#
# In exercise_2(), call fetch_all with the provided URLs, then print how
# many were fetched and how long it took.
#
# Hint: 5 URLs at 0.1s each should take ~0.1s total (not ~0.5s)
# =============================================================================

async def exercise_2():
    urls = [f"https://api.example.com/data/{i}" for i in range(5)]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Error handling for failed requests
#
# Write an async function `fetch_with_error_handling` that:
# - Takes a URL string
# - Calls mock_fetch_unreliable() to simulate a flaky server
# - On success: returns {"url": url, "status": "ok", "body": response["body"]}
# - On ConnectionError: returns {"url": url, "status": "error", "error": str(e)}
# - On any other exception: returns {"url": url, "status": "error", "error": "Unknown"}
#
# In exercise_3(), fetch 8 URLs concurrently with this function, then print
# a summary: how many succeeded, how many failed, and which ones failed.
#
# Set random.seed(42) before the gather call for reproducible results.
# =============================================================================

async def exercise_3():
    urls = [f"https://api.example.com/resource/{i}" for i in range(8)]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Rate limiting with Semaphore
#
# Write an async function `fetch_rate_limited` that:
# - Takes a URL and a semaphore
# - Uses the semaphore to limit concurrency
# - Calls mock_fetch(url, delay=0.2) inside the semaphore
# - Returns the response dict
#
# In exercise_4(), create 10 URLs and a Semaphore(3), then fetch them all.
# Time the operation and print the elapsed time.
#
# Think about it: 10 URLs, max 3 at a time, 0.2s each.
# That's ceil(10/3) = 4 batches * 0.2s = ~0.8s total.
# =============================================================================

async def exercise_4():
    urls = [f"https://api.example.com/limited/{i}" for i in range(10)]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Retry with exponential backoff
#
# Write an async function `fetch_with_retry` that:
# - Takes a URL and max_retries (default 3)
# - Tries to call mock_fetch_unreliable(url, delay=0.05, fail_chance=0.6)
# - On failure, waits 0.1 * (2 ** attempt) seconds before retrying
#   (attempt 0 waits 0.1s, attempt 1 waits 0.2s, attempt 2 waits 0.4s)
# - Returns the response dict on success
# - Returns None if all retries are exhausted
#
# In exercise_5(), set random.seed(77), then try fetching 5 URLs with retry.
# Print which ones succeeded and which ones gave up.
# =============================================================================

async def exercise_5():
    urls = [f"https://api.example.com/flaky/{i}" for i in range(5)]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Concurrent web scraper simulation
#
# Build a two-phase scraper:
#
# Phase 1 — Fetch pages:
#   - Use mock_fetch_page() to fetch these 4 URLs concurrently:
#     https://example.com/page/1 through /page/4
#   - Each returns a dict with "title", "links", and "word_count"
#
# Phase 2 — Extract and aggregate:
#   - Collect ALL the links from ALL the pages into a flat list
#   - Calculate the total word count across all pages
#   - Find the page with the highest word count
#
# Print a summary:
#   - Total pages fetched
#   - Total links found across all pages
#   - Total word count
#   - Which page had the most words
#
# Bonus: Use a Semaphore(2) so only 2 pages are fetched at a time.
#
# Set random.seed(55) before fetching for reproducible word counts.
# =============================================================================

async def exercise_6():
    urls = [f"https://example.com/page/{i}" for i in range(1, 5)]
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

async def solution_1():
    async def fetch_one(url):
        response = await mock_fetch(url)
        return f"[{response['status']}] {response['url']} — {response['body']}"

    result = await fetch_one("https://api.example.com/hello")
    print(f"  {result}")


async def solution_2():
    async def fetch_all(urls):
        tasks = [mock_fetch(url) for url in urls]
        return await asyncio.gather(*tasks)

    urls = [f"https://api.example.com/data/{i}" for i in range(5)]

    start = time.time()
    results = await fetch_all(urls)
    elapsed = time.time() - start

    print(f"  Fetched {len(results)} URLs in {elapsed:.2f}s")
    for r in results:
        print(f"    [{r['status']}] {r['url']}")


async def solution_3():
    async def fetch_with_error_handling(url):
        try:
            response = await mock_fetch_unreliable(url)
            return {"url": url, "status": "ok", "body": response["body"]}
        except ConnectionError as e:
            return {"url": url, "status": "error", "error": str(e)}
        except Exception:
            return {"url": url, "status": "error", "error": "Unknown"}

    urls = [f"https://api.example.com/resource/{i}" for i in range(8)]

    random.seed(42)
    results = await asyncio.gather(*[fetch_with_error_handling(url) for url in urls])

    successes = [r for r in results if r["status"] == "ok"]
    failures = [r for r in results if r["status"] == "error"]

    print(f"  Results: {len(successes)} succeeded, {len(failures)} failed")
    for r in failures:
        print(f"    FAILED: {r['url']} — {r['error']}")


async def solution_4():
    async def fetch_rate_limited(url, semaphore):
        async with semaphore:
            return await mock_fetch(url, delay=0.2)

    urls = [f"https://api.example.com/limited/{i}" for i in range(10)]
    semaphore = asyncio.Semaphore(3)

    start = time.time()
    tasks = [fetch_rate_limited(url, semaphore) for url in urls]
    results = await asyncio.gather(*tasks)
    elapsed = time.time() - start

    print(f"  Fetched {len(results)} URLs in {elapsed:.2f}s (limited to 3 concurrent)")
    print(f"  Expected ~0.8s (4 batches of 3 at 0.2s each)")


async def solution_5():
    async def fetch_with_retry(url, max_retries=3):
        for attempt in range(max_retries):
            try:
                response = await mock_fetch_unreliable(url, delay=0.05, fail_chance=0.6)
                return response
            except ConnectionError:
                wait_time = 0.1 * (2 ** attempt)
                if attempt < max_retries - 1:
                    await asyncio.sleep(wait_time)
        return None

    urls = [f"https://api.example.com/flaky/{i}" for i in range(5)]

    random.seed(77)
    results = await asyncio.gather(*[fetch_with_retry(url) for url in urls])

    for url, result in zip(urls, results):
        if result is not None:
            print(f"    {url} — succeeded")
        else:
            print(f"    {url} — gave up after retries")

    successes = sum(1 for r in results if r is not None)
    print(f"  Total: {successes}/{len(urls)} succeeded")


async def solution_6():
    urls = [f"https://example.com/page/{i}" for i in range(1, 5)]
    semaphore = asyncio.Semaphore(2)

    async def fetch_limited(url):
        async with semaphore:
            return await mock_fetch_page(url)

    # Phase 1: Fetch pages concurrently
    random.seed(55)
    tasks = [fetch_limited(url) for url in urls]
    pages = await asyncio.gather(*tasks)

    # Phase 2: Extract and aggregate
    all_links = []
    total_words = 0
    max_words_page = None
    max_words = 0

    for page in pages:
        all_links.extend(page["links"])
        total_words += page["word_count"]
        if page["word_count"] > max_words:
            max_words = page["word_count"]
            max_words_page = page["title"]

    print(f"  Pages fetched: {len(pages)}")
    print(f"  Total links found: {len(all_links)}")
    print(f"  Total word count: {total_words}")
    print(f"  Most words: {max_words_page} ({max_words} words)")


# =============================================================================
# Run it!
# =============================================================================

async def async_main():
    exercises = [
        ("Fetch a single URL", exercise_1),
        ("Fetch multiple URLs concurrently", exercise_2),
        ("Error handling for failed requests", exercise_3),
        ("Rate limiting with Semaphore", exercise_4),
        ("Retry with exponential backoff", exercise_5),
        ("Concurrent web scraper simulation", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        await func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")


if __name__ == "__main__":
    asyncio.run(async_main())
