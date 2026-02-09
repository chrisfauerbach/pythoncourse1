"""
HTTP Requests Library — Exercises
==================================

Practice problems to test your understanding of HTTP requests in Python.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

NOTE: These exercises use SIMULATED HTTP functions (no external dependencies).
The patterns are identical to the real `requests` library.
"""

import json
from urllib.parse import urlencode

# =============================================================================
# Mock HTTP infrastructure (same as example.py)
# =============================================================================

class MockResponse:
    """Simulates a requests.Response object."""

    def __init__(self, status_code, json_data=None, text=None, headers=None):
        self.status_code = status_code
        self._json_data = json_data
        self.text = text or (json.dumps(json_data) if json_data else "")
        self.headers = headers or {'Content-Type': 'application/json'}
        self.ok = status_code < 400
        self.url = "https://api.example.com/simulated"

    def json(self):
        if self._json_data is not None:
            return self._json_data
        return json.loads(self.text)

    def raise_for_status(self):
        if not self.ok:
            raise HTTPError(f"HTTP {self.status_code} Error")

class HTTPError(Exception):
    pass

class Timeout(Exception):
    pass

class ConnectionError(Exception):
    pass

# Simulated API database
_mock_db = {
    'posts': [
        {'id': 1, 'title': 'First Post', 'author': 'Alice', 'likes': 10},
        {'id': 2, 'title': 'Python Tips', 'author': 'Bob', 'likes': 25},
        {'id': 3, 'title': 'Learning APIs', 'author': 'Charlie', 'likes': 15},
    ],
    'users': [
        {'id': 1, 'username': 'alice', 'email': 'alice@example.com'},
        {'id': 2, 'username': 'bob', 'email': 'bob@example.com'},
    ],
    'products': [
        {'id': 1, 'name': 'Laptop', 'price': 999.99, 'stock': 5},
        {'id': 2, 'name': 'Mouse', 'price': 29.99, 'stock': 50},
        {'id': 3, 'name': 'Keyboard', 'price': 79.99, 'stock': 0},
    ]
}

def simulated_get(url, params=None, headers=None, timeout=None):
    """Simulate requests.get()."""
    if 'posts' in url:
        if url.endswith('/posts'):
            # Return all posts or filtered posts
            posts = _mock_db['posts']
            if params and 'author' in params:
                posts = [p for p in posts if p['author'] == params['author']]
            return MockResponse(200, {'posts': posts})
        else:
            # Get specific post by ID
            post_id = int(url.split('/')[-1])
            post = next((p for p in _mock_db['posts'] if p['id'] == post_id), None)
            if post:
                return MockResponse(200, post)
            else:
                return MockResponse(404, {'error': 'Post not found'})
    elif 'users' in url:
        if url.endswith('/users'):
            return MockResponse(200, {'users': _mock_db['users']})
        else:
            user_id = int(url.split('/')[-1])
            user = next((u for u in _mock_db['users'] if u['id'] == user_id), None)
            if user:
                return MockResponse(200, user)
            else:
                return MockResponse(404, {'error': 'User not found'})
    elif 'products' in url:
        if params and 'in_stock' in params:
            in_stock = params['in_stock'].lower() == 'true'
            products = [p for p in _mock_db['products'] if (p['stock'] > 0) == in_stock]
            return MockResponse(200, {'products': products})
        return MockResponse(200, {'products': _mock_db['products']})
    elif 'weather' in url:
        city = params.get('city', 'Unknown') if params else 'Unknown'
        if city in ['Portland', 'Seattle', 'Phoenix']:
            return MockResponse(200, {
                'city': city,
                'temperature': 20,
                'conditions': 'Sunny'
            })
        return MockResponse(404, {'error': 'City not found'})
    elif 'timeout' in url:
        raise Timeout("Request timed out")
    elif 'server-error' in url:
        return MockResponse(500, {'error': 'Internal server error'})
    else:
        return MockResponse(200, {'status': 'ok'})

def simulated_post(url, json=None, data=None, headers=None, timeout=None):
    """Simulate requests.post()."""
    if 'posts' in url:
        new_post = json or data
        return MockResponse(201, {
            'id': 4,
            'title': new_post.get('title'),
            'author': new_post.get('author'),
            'likes': 0,
            'created': True
        })
    elif 'users' in url:
        new_user = json or data
        return MockResponse(201, {
            'id': 3,
            'username': new_user.get('username'),
            'email': new_user.get('email'),
            'created': True
        })
    else:
        return MockResponse(201, {'status': 'created'})

def simulated_put(url, json=None, headers=None, timeout=None):
    """Simulate requests.put()."""
    return MockResponse(200, {'status': 'updated', 'data': json})

def simulated_delete(url, headers=None, timeout=None):
    """Simulate requests.delete()."""
    if '999' in url:
        return MockResponse(404, {'error': 'Resource not found'})
    return MockResponse(204, {})


# =============================================================================
# Exercise 1: Basic GET request
#
# Fetch all posts from 'https://api.example.com/posts' and print:
# - The total number of posts
# - Each post's title and author in the format: "Title" by Author
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: GET with query parameters
#
# Fetch posts from 'https://api.example.com/posts' but filter by author "Bob"
# using query parameters. Print the titles of Bob's posts.
#
# Hint: params = {'author': 'Bob'}
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: POST request - create a new resource
#
# Create a new post with:
#   - title: "My API Adventure"
#   - author: "Student"
#
# POST it to 'https://api.example.com/posts' and print the ID of the created
# post and a success message.
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Error handling - 404 Not Found
#
# Try to fetch a post with ID 999 from 'https://api.example.com/posts/999'.
# This will return a 404 error. Handle it gracefully by:
# - Checking if response.ok is False
# - Printing an appropriate error message
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Error handling with exceptions
#
# Try to fetch data from 'https://api.example.com/timeout' which will raise
# a Timeout exception. Also try 'https://api.example.com/server-error' which
# returns a 500 status code.
#
# Use try/except to handle:
# - Timeout exceptions
# - HTTPError (use raise_for_status())
#
# Print appropriate error messages for each case.
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Practical API client
#
# Build a simple product inventory checker:
# 1. Fetch all products from 'https://api.example.com/products'
# 2. Filter for products that are in stock (stock > 0) using query parameters
#    Hint: params = {'in_stock': 'true'}
# 3. Print each in-stock product with: Name - $Price (Stock: N)
# 4. Calculate and print the total value of in-stock inventory
#
# Bonus: Handle errors gracefully with try/except
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    response = simulated_get('https://api.example.com/posts')
    data = response.json()

    posts = data['posts']
    print(f"Total posts: {len(posts)}")
    for post in posts:
        print(f'  "{post["title"]}" by {post["author"]}')


def solution_2():
    params = {'author': 'Bob'}
    response = simulated_get('https://api.example.com/posts', params=params)
    data = response.json()

    print("Bob's posts:")
    for post in data['posts']:
        print(f'  - {post["title"]}')


def solution_3():
    new_post = {
        'title': 'My API Adventure',
        'author': 'Student'
    }

    response = simulated_post('https://api.example.com/posts', json=new_post)
    created = response.json()

    print(f"Success! Created post with ID: {created['id']}")
    print(f'Title: "{created["title"]}"')
    print(f'Author: {created["author"]}')


def solution_4():
    response = simulated_get('https://api.example.com/posts/999')

    if response.ok:
        post = response.json()
        print(f"Post: {post['title']}")
    else:
        print(f"Error: Post not found (status {response.status_code})")
        error_data = response.json()
        print(f"Message: {error_data.get('error', 'Unknown error')}")


def solution_5():
    # Test 1: Timeout
    print("Test 1: Timeout")
    try:
        response = simulated_get('https://api.example.com/timeout', timeout=5)
        data = response.json()
        print(f"Data: {data}")
    except Timeout:
        print("  Error: Request timed out - server took too long to respond")
    except HTTPError as e:
        print(f"  HTTP Error: {e}")
    print()

    # Test 2: Server error (500)
    print("Test 2: Server error")
    try:
        response = simulated_get('https://api.example.com/server-error')
        response.raise_for_status()  # Will raise HTTPError for 500
        data = response.json()
        print(f"Data: {data}")
    except Timeout:
        print("  Error: Request timed out")
    except HTTPError as e:
        print(f"  HTTP Error: {e}")
        print("  The server encountered an internal error")


def solution_6():
    try:
        # Fetch in-stock products
        params = {'in_stock': 'true'}
        response = simulated_get('https://api.example.com/products', params=params)
        response.raise_for_status()

        data = response.json()
        products = data['products']

        print("In-stock products:")
        total_value = 0

        for product in products:
            price = product['price']
            stock = product['stock']
            item_value = price * stock

            print(f"  {product['name']} - ${price:.2f} (Stock: {stock})")
            total_value += item_value

        print()
        print(f"Total inventory value: ${total_value:.2f}")

    except HTTPError as e:
        print(f"HTTP Error: {e}")
    except Timeout:
        print("Request timed out")
    except Exception as e:
        print(f"Unexpected error: {e}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Basic GET request", exercise_1),
        ("GET with query parameters", exercise_2),
        ("POST request - create a resource", exercise_3),
        ("Error handling - 404 Not Found", exercise_4),
        ("Error handling with exceptions", exercise_5),
        ("Practical API client", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 70)
        print(f"EXERCISE {i}: {title}")
        print("=" * 70)
        func()
        print()

    print("-" * 70)
    print("Done! Compare your output with the solutions.")
    print()
    print("To practice with REAL APIs:")
    print("  1. Install requests: pip install requests")
    print("  2. Try these free APIs:")
    print("     - JSONPlaceholder: https://jsonplaceholder.typicode.com")
    print("     - GitHub API: https://api.github.com")
    print("     - OpenWeatherMap: https://openweathermap.org/api")
    print("  3. Replace simulated_get/post with requests.get/post")
