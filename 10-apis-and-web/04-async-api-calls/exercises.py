"""
Async API Calls — Exercises
============================

Practice problems to test your understanding of async API patterns.
Try to solve each exercise before looking at the solutions at the bottom.

Run this file:
    python3 exercises.py
"""

import asyncio
import random
from typing import List, Dict, Any


# Simulated API function (pretend this is a real API call)
async def mock_api_call(endpoint: str, delay: float = 0.1, fail_chance: float = 0.0) -> Dict[str, Any]:
    """Simulate an API call with network latency and potential failures."""
    await asyncio.sleep(delay)

    if random.random() < fail_chance:
        raise ConnectionError(f"API call failed: {endpoint}")

    # Return fake data based on endpoint
    if "/users/" in endpoint:
        user_id = endpoint.split("/users/")[-1]
        return {"id": user_id, "name": f"User {user_id}", "posts": random.randint(1, 50)}
    elif "/products/" in endpoint:
        product_id = endpoint.split("/products/")[-1]
        return {"id": product_id, "name": f"Product {product_id}", "price": random.randint(10, 100)}
    else:
        return {"endpoint": endpoint, "data": "success"}


# =============================================================================
# Exercise 1: Concurrent API calls
# Fetch data from 5 user endpoints concurrently using asyncio.gather()
# =============================================================================

async def exercise_1():
    """
    TASK: Fetch data for users 1-5 concurrently (all at once).
    Use asyncio.gather() to run all API calls in parallel.

    Expected output: List of 5 user dictionaries
    """
    print("Fetching 5 users concurrently...")

    # YOUR CODE HERE
    # Hint: Create a list of tasks for users 1-5, then use asyncio.gather()
    user_ids = [1, 2, 3, 4, 5]
    # users = await ...

    users = []  # Replace this with your solution

    print(f"Fetched {len(users)} users")
    for user in users:
        print(f"  {user['name']}: {user['posts']} posts")


# =============================================================================
# Exercise 2: Rate limiting with Semaphore
# Fetch 10 products but limit to max 3 concurrent requests
# =============================================================================

async def exercise_2():
    """
    TASK: Fetch data for products 1-10, but limit to max 3 concurrent requests.
    Use asyncio.Semaphore to control concurrency.

    Expected: All 10 products fetched, but only 3 at a time
    """
    print("Fetching 10 products with rate limiting (max 3 concurrent)...")

    # YOUR CODE HERE
    # Hint: Create a Semaphore(3), then use it in an async function that fetches products
    product_ids = list(range(1, 11))
    # semaphore = asyncio.Semaphore(...)
    # products = await ...

    products = []  # Replace this with your solution

    print(f"Fetched {len(products)} products")
    print(f"Total price: ${sum(p['price'] for p in products)}")


# =============================================================================
# Exercise 3: Error handling with return_exceptions
# Fetch from multiple endpoints where some will fail
# =============================================================================

async def exercise_3():
    """
    TASK: Fetch from 8 endpoints, some of which will fail (30% failure rate).
    Use asyncio.gather with return_exceptions=True to handle failures gracefully.

    Expected: Mix of successful results and exceptions
    """
    print("Fetching from flaky API (30% failure rate)...")

    random.seed(42)  # For reproducible results

    # YOUR CODE HERE
    # Hint: Use mock_api_call with fail_chance=0.3, and return_exceptions=True
    endpoints = [f"/users/{i}" for i in range(1, 9)]
    # results = await asyncio.gather(..., return_exceptions=True)

    results = []  # Replace this with your solution

    successes = [r for r in results if not isinstance(r, Exception)]
    failures = [r for r in results if isinstance(r, Exception)]

    print(f"Success: {len(successes)}, Failures: {len(failures)}")


# =============================================================================
# Exercise 4: Retry with exponential backoff
# Implement a function that retries failed API calls
# =============================================================================

async def exercise_4():
    """
    TASK: Write a function that retries API calls on failure with exponential backoff.
    If a call fails, wait 0.1s, then 0.2s, then 0.4s between retries (max 3 attempts).

    Expected: Most calls eventually succeed after retries
    """
    print("Testing retry logic with exponential backoff...")

    async def fetch_with_retry(endpoint: str, max_retries: int = 3) -> Dict[str, Any]:
        """Fetch with retry logic."""
        # YOUR CODE HERE
        # Hint: Loop through attempts, catch exceptions, sleep with 0.1 * (2 ** attempt)
        return {}  # Replace with your implementation

    random.seed(99)
    endpoints = [f"/users/{i}" for i in range(1, 6)]

    # Test with 50% failure rate per attempt
    results = await asyncio.gather(
        *[fetch_with_retry(endpoint) for endpoint in endpoints],
        return_exceptions=True
    )

    successes = [r for r in results if not isinstance(r, Exception)]
    print(f"Final results: {len(successes)}/{len(endpoints)} succeeded")


# =============================================================================
# Exercise 5: Async pagination
# Fetch multiple pages of data concurrently
# =============================================================================

async def exercise_5():
    """
    TASK: Fetch pages 1-5 of data concurrently and combine all items.
    Each page returns {"page": N, "items": [...]} with 10 items per page.

    Expected: 50 total items from 5 pages
    """
    print("Fetching 5 pages of data concurrently...")

    async def fetch_page(page_num: int) -> Dict[str, Any]:
        """Fetch a single page."""
        await asyncio.sleep(0.1)
        return {"page": page_num, "items": [f"item_{page_num}_{i}" for i in range(10)]}

    # YOUR CODE HERE
    # Hint: Use asyncio.gather to fetch all pages, then extract and combine items
    pages = list(range(1, 6))
    # all_items = ...

    all_items = []  # Replace with your solution

    print(f"Fetched {len(all_items)} items across {len(pages)} pages")


# =============================================================================
# Exercise 6: Fan-out pattern
# Fetch a list, then fetch details for each item concurrently
# =============================================================================

async def exercise_6():
    """
    TASK: Implement the fan-out pattern:
    1. Fetch a list of user IDs
    2. For each user ID, fetch detailed user info concurrently

    Expected: Detailed info for all users
    """
    print("Testing fan-out pattern...")

    async def fetch_user_list() -> List[int]:
        """Fetch list of user IDs."""
        await asyncio.sleep(0.1)
        return [1, 2, 3, 4, 5, 6, 7, 8]

    async def fetch_user_details(user_id: int) -> Dict[str, Any]:
        """Fetch details for one user."""
        return await mock_api_call(f"/users/{user_id}", delay=0.1)

    # YOUR CODE HERE
    # Hint: First await fetch_user_list(), then use gather to fetch all details
    # user_ids = await ...
    # detailed_users = await ...

    user_ids = []  # Replace with your solution
    detailed_users = []  # Replace with your solution

    print(f"Fetched {len(user_ids)} user IDs")
    print(f"Fetched details for {len(detailed_users)} users")
    total_posts = sum(u['posts'] for u in detailed_users)
    print(f"Total posts across all users: {total_posts}")


# =============================================================================
# SOLUTIONS (no peeking until you've tried!)
# =============================================================================

async def solution_1():
    """Solution: Concurrent API calls with gather()"""
    print("Fetching 5 users concurrently...")

    user_ids = [1, 2, 3, 4, 5]
    tasks = [mock_api_call(f"/users/{uid}") for uid in user_ids]
    users = await asyncio.gather(*tasks)

    print(f"Fetched {len(users)} users")
    for user in users:
        print(f"  {user['name']}: {user['posts']} posts")


async def solution_2():
    """Solution: Rate limiting with Semaphore"""
    print("Fetching 10 products with rate limiting (max 3 concurrent)...")

    semaphore = asyncio.Semaphore(3)

    async def fetch_product(product_id: int) -> Dict[str, Any]:
        async with semaphore:
            return await mock_api_call(f"/products/{product_id}", delay=0.1)

    product_ids = list(range(1, 11))
    tasks = [fetch_product(pid) for pid in product_ids]
    products = await asyncio.gather(*tasks)

    print(f"Fetched {len(products)} products")
    print(f"Total price: ${sum(p['price'] for p in products)}")


async def solution_3():
    """Solution: Error handling with return_exceptions"""
    print("Fetching from flaky API (30% failure rate)...")

    random.seed(42)

    endpoints = [f"/users/{i}" for i in range(1, 9)]
    tasks = [mock_api_call(endpoint, delay=0.05, fail_chance=0.3) for endpoint in endpoints]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    successes = [r for r in results if not isinstance(r, Exception)]
    failures = [r for r in results if isinstance(r, Exception)]

    print(f"Success: {len(successes)}, Failures: {len(failures)}")


async def solution_4():
    """Solution: Retry with exponential backoff"""
    print("Testing retry logic with exponential backoff...")

    async def fetch_with_retry(endpoint: str, max_retries: int = 3) -> Dict[str, Any]:
        """Fetch with retry logic and exponential backoff."""
        for attempt in range(max_retries):
            try:
                return await mock_api_call(endpoint, delay=0.05, fail_chance=0.5)
            except ConnectionError:
                if attempt < max_retries - 1:
                    wait_time = 0.1 * (2 ** attempt)  # 0.1s, 0.2s, 0.4s
                    await asyncio.sleep(wait_time)
                else:
                    raise  # Re-raise on final attempt

    random.seed(99)
    endpoints = [f"/users/{i}" for i in range(1, 6)]

    results = await asyncio.gather(
        *[fetch_with_retry(endpoint) for endpoint in endpoints],
        return_exceptions=True
    )

    successes = [r for r in results if not isinstance(r, Exception)]
    print(f"Final results: {len(successes)}/{len(endpoints)} succeeded")


async def solution_5():
    """Solution: Async pagination"""
    print("Fetching 5 pages of data concurrently...")

    async def fetch_page(page_num: int) -> Dict[str, Any]:
        """Fetch a single page."""
        await asyncio.sleep(0.1)
        return {"page": page_num, "items": [f"item_{page_num}_{i}" for i in range(10)]}

    pages_to_fetch = list(range(1, 6))
    tasks = [fetch_page(page) for page in pages_to_fetch]
    pages = await asyncio.gather(*tasks)

    # Combine all items from all pages
    all_items = []
    for page_data in pages:
        all_items.extend(page_data["items"])

    print(f"Fetched {len(all_items)} items across {len(pages)} pages")


async def solution_6():
    """Solution: Fan-out pattern"""
    print("Testing fan-out pattern...")

    async def fetch_user_list() -> List[int]:
        """Fetch list of user IDs."""
        await asyncio.sleep(0.1)
        return [1, 2, 3, 4, 5, 6, 7, 8]

    async def fetch_user_details(user_id: int) -> Dict[str, Any]:
        """Fetch details for one user."""
        return await mock_api_call(f"/users/{user_id}", delay=0.1)

    # Step 1: Get list of user IDs
    user_ids = await fetch_user_list()

    # Step 2: Fan out — fetch details for all users concurrently
    tasks = [fetch_user_details(uid) for uid in user_ids]
    detailed_users = await asyncio.gather(*tasks)

    print(f"Fetched {len(user_ids)} user IDs")
    print(f"Fetched details for {len(detailed_users)} users")
    total_posts = sum(u['posts'] for u in detailed_users)
    print(f"Total posts across all users: {total_posts}")


# =============================================================================
# Test runner
# =============================================================================

async def async_main():
    """Run all exercises."""
    exercises = [
        ("Concurrent API calls with gather()", exercise_1),
        ("Rate limiting with Semaphore", exercise_2),
        ("Error handling with return_exceptions", exercise_3),
        ("Retry with exponential backoff", exercise_4),
        ("Async pagination", exercise_5),
        ("Fan-out pattern", exercise_6),
    ]

    solutions = [
        ("Concurrent API calls with gather()", solution_1),
        ("Rate limiting with Semaphore", solution_2),
        ("Error handling with return_exceptions", solution_3),
        ("Retry with exponential backoff", solution_4),
        ("Async pagination", solution_5),
        ("Fan-out pattern", solution_6),
    ]

    print("=" * 70)
    print("ASYNC API CALLS — EXERCISES")
    print("=" * 70)
    print()

    # Run exercises
    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 70)
        print(f"EXERCISE {i}: {title}")
        print("=" * 70)
        try:
            await func()
        except Exception as e:
            print(f"Exercise incomplete or error: {e}")
        print()

    # Run solutions
    print("\n" + "=" * 70)
    print("SOLUTIONS")
    print("=" * 70)
    print()

    for i, (title, func) in enumerate(solutions, 1):
        print("=" * 70)
        print(f"SOLUTION {i}: {title}")
        print("=" * 70)
        await func()
        print()

    print("-" * 70)
    print("All exercises complete!")
    print()
    print("These exercises used simulated API calls (asyncio.sleep).")
    print("The patterns work exactly the same with real HTTP libraries like aiohttp.")


if __name__ == "__main__":
    asyncio.run(async_main())
