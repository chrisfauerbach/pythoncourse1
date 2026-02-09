"""
HTTP Requests Library — Example Code
=====================================

Run this file:
    python3 example.py

Learn how to make HTTP requests in Python. This file uses SIMULATED HTTP
functions (no external dependencies needed!). In real code, you'd use the
`requests` library - the patterns are identical.

To use the real requests library:
    pip install requests

Then replace the simulated functions with:
    import requests
    response = requests.get('https://api.example.com/data')
"""

import json
from urllib.parse import urlencode

# =============================================================================
# Mock HTTP infrastructure (for demonstration without external dependencies)
# In real code, you'd just: import requests
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
        """Parse response body as JSON."""
        if self._json_data is not None:
            return self._json_data
        return json.loads(self.text)

    def raise_for_status(self):
        """Raise an exception if status code indicates an error."""
        if not self.ok:
            raise HTTPError(f"HTTP {self.status_code} Error")

class HTTPError(Exception):
    """Simulates requests.exceptions.HTTPError."""
    pass

class Timeout(Exception):
    """Simulates requests.exceptions.Timeout."""
    pass

class ConnectionError(Exception):
    """Simulates requests.exceptions.ConnectionError."""
    pass

# Simulated HTTP functions (mimic the requests library API)

def simulated_get(url, params=None, headers=None, timeout=None):
    """Simulate requests.get() - returns mock data based on URL."""
    print(f"  [Simulated GET] {url}", end="")

    if params:
        query_string = urlencode(params)
        print(f"?{query_string}", end="")
    print()

    # Simulate different API endpoints
    if 'users/1' in url:
        return MockResponse(200, {
            'id': 1,
            'name': 'Alice Johnson',
            'email': 'alice@example.com',
            'role': 'admin'
        })
    elif 'users/999' in url:
        return MockResponse(404, {'error': 'User not found'})
    elif 'users' in url:
        # List of users with pagination
        page = params.get('page', 1) if params else 1
        return MockResponse(200, {
            'users': [
                {'id': 1, 'name': 'Alice', 'role': 'admin'},
                {'id': 2, 'name': 'Bob', 'role': 'editor'},
                {'id': 3, 'name': 'Charlie', 'role': 'viewer'},
            ],
            'page': page,
            'total_pages': 3
        })
    elif 'search' in url:
        query = params.get('q', '') if params else ''
        return MockResponse(200, {
            'query': query,
            'results': [
                {'title': 'Python Tutorial', 'url': 'https://example.com/1'},
                {'title': 'Python Best Practices', 'url': 'https://example.com/2'},
            ]
        })
    elif 'timeout' in url:
        raise Timeout("Request timed out")
    elif 'error' in url:
        raise ConnectionError("Failed to connect")
    else:
        return MockResponse(200, {'status': 'ok', 'message': 'Hello from simulated API!'})

def simulated_post(url, json=None, data=None, headers=None, timeout=None):
    """Simulate requests.post() - creates a new resource."""
    print(f"  [Simulated POST] {url}")
    if json:
        print(f"  Body: {json}")

    # Simulate creating a user
    if 'users' in url:
        new_user = json or data
        return MockResponse(201, {
            'id': 42,
            'name': new_user.get('name'),
            'email': new_user.get('email'),
            'created': True
        })
    else:
        return MockResponse(201, {'status': 'created'})

def simulated_put(url, json=None, headers=None, timeout=None):
    """Simulate requests.put() - update a resource."""
    print(f"  [Simulated PUT] {url}")
    if json:
        print(f"  Body: {json}")

    return MockResponse(200, {'status': 'updated', 'data': json})

def simulated_delete(url, headers=None, timeout=None):
    """Simulate requests.delete() - remove a resource."""
    print(f"  [Simulated DELETE] {url}")
    return MockResponse(204, {})  # 204 No Content

# =============================================================================
# 1. Basic GET request
# =============================================================================

print("=" * 70)
print("1. Basic GET request")
print("=" * 70)

# Simulated version (what we're using in this file)
response = simulated_get('https://api.example.com/status')

print(f"Status code: {response.status_code}")
print(f"Response OK: {response.ok}")
print(f"Response body: {response.json()}")
print()

# Real requests library code (commented out - install requests to use):
# import requests
# response = requests.get('https://api.github.com/users/python')
# print(response.status_code)
# print(response.json())

# =============================================================================
# 2. GET request with query parameters
# =============================================================================

print("=" * 70)
print("2. GET request with query parameters")
print("=" * 70)

# Query parameters are key-value pairs added to the URL
params = {
    'q': 'python programming',
    'page': 2,
    'sort': 'newest'
}

response = simulated_get('https://api.example.com/search', params=params)
data = response.json()

print(f"Searching for: {data['query']}")
print(f"Found {len(data['results'])} results:")
for result in data['results']:
    print(f"  - {result['title']}")
print()

# Real requests:
# response = requests.get('https://api.example.com/search', params=params)
# Becomes: https://api.example.com/search?q=python+programming&page=2&sort=newest

# =============================================================================
# 3. GET request - fetching a specific resource
# =============================================================================

print("=" * 70)
print("3. GET request - fetching a specific resource")
print("=" * 70)

# Get a specific user by ID
user_id = 1
response = simulated_get(f'https://api.example.com/users/{user_id}')

if response.ok:
    user = response.json()
    print(f"User #{user['id']}")
    print(f"  Name: {user['name']}")
    print(f"  Email: {user['email']}")
    print(f"  Role: {user['role']}")
else:
    print(f"Error: {response.status_code}")
print()

# Real requests:
# response = requests.get(f'https://api.example.com/users/{user_id}')
# user = response.json()

# =============================================================================
# 4. POST request - creating a new resource
# =============================================================================

print("=" * 70)
print("4. POST request - creating a new resource")
print("=" * 70)

# POST sends data in the request body (not the URL)
new_user = {
    'name': 'Diana Prince',
    'email': 'diana@example.com',
    'role': 'editor'
}

response = simulated_post('https://api.example.com/users', json=new_user)

print(f"Status: {response.status_code} (201 = Created)")
created = response.json()
print(f"Created user with ID: {created['id']}")
print(f"Name: {created['name']}")
print()

# Real requests:
# response = requests.post('https://api.example.com/users', json=new_user)
# The json= parameter automatically:
#   1. Converts the dict to JSON
#   2. Sets Content-Type: application/json header
#   3. Encodes as UTF-8

# =============================================================================
# 5. PUT request - updating a resource
# =============================================================================

print("=" * 70)
print("5. PUT request - updating a resource")
print("=" * 70)

# PUT typically replaces the entire resource
updated_user = {
    'name': 'Alice Johnson (Updated)',
    'email': 'alice.new@example.com',
    'role': 'super_admin'
}

response = simulated_put('https://api.example.com/users/1', json=updated_user)

print(f"Status: {response.status_code}")
result = response.json()
print(f"Update status: {result['status']}")
print()

# Real requests:
# response = requests.put('https://api.example.com/users/1', json=updated_user)

# =============================================================================
# 6. DELETE request - removing a resource
# =============================================================================

print("=" * 70)
print("6. DELETE request - removing a resource")
print("=" * 70)

response = simulated_delete('https://api.example.com/users/42')

print(f"Status: {response.status_code} (204 = No Content, success!)")
print("User deleted successfully")
print()

# Real requests:
# response = requests.delete('https://api.example.com/users/42')
# 204 No Content is common for DELETE - nothing to return

# =============================================================================
# 7. Custom headers (authentication, content-type, etc.)
# =============================================================================

print("=" * 70)
print("7. Custom headers (authentication, content-type, etc.)")
print("=" * 70)

# Headers are metadata about the request
headers = {
    'Authorization': 'Bearer abc123token456',
    'User-Agent': 'MyPythonApp/1.0',
    'Accept': 'application/json',
    'X-Custom-Header': 'custom-value'
}

response = simulated_get('https://api.example.com/private/data', headers=headers)

print("Request sent with custom headers:")
print(f"  Authorization: Bearer abc123token456")
print(f"  User-Agent: MyPythonApp/1.0")
print(f"Status: {response.status_code}")
print()

# Real requests:
# headers = {'Authorization': 'Bearer your_token_here'}
# response = requests.get('https://api.example.com/private', headers=headers)

# Common authentication patterns:
# 1. Bearer token (most common for APIs):
#    headers = {'Authorization': 'Bearer token123'}
#
# 2. API key in header:
#    headers = {'X-API-Key': 'your_api_key_here'}
#
# 3. Basic auth (requests has a helper):
#    from requests.auth import HTTPBasicAuth
#    response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
#    # Or shorthand:
#    response = requests.get(url, auth=('user', 'pass'))

# =============================================================================
# 8. Response handling - status codes and headers
# =============================================================================

print("=" * 70)
print("8. Response handling - status codes and headers")
print("=" * 70)

response = simulated_get('https://api.example.com/users')

print(f"Status code: {response.status_code}")
print(f"OK (< 400): {response.ok}")
print(f"URL: {response.url}")
print(f"Content-Type: {response.headers.get('Content-Type')}")
print()

# Checking specific status codes
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Not found")
elif response.status_code >= 500:
    print("Server error")
print()

# Real requests has the same attributes:
# response.status_code, response.ok, response.headers, response.url

# =============================================================================
# 9. Error handling - handling failures gracefully
# =============================================================================

print("=" * 70)
print("9. Error handling - handling failures gracefully")
print("=" * 70)

# Example 1: 404 Not Found
print("Example 1: Requesting non-existent user")
response = simulated_get('https://api.example.com/users/999')

if response.ok:
    user = response.json()
    print(f"User: {user['name']}")
else:
    print(f"Error {response.status_code}: {response.json()}")
print()

# Example 2: Using raise_for_status() for automatic error checking
print("Example 2: Using raise_for_status()")
try:
    response = simulated_get('https://api.example.com/users/999')
    response.raise_for_status()  # Raises HTTPError if status >= 400
    user = response.json()
    print(f"User: {user['name']}")
except HTTPError as e:
    print(f"HTTP Error: {e}")
print()

# Example 3: Network errors (timeout, connection errors)
print("Example 3: Handling timeout")
try:
    response = simulated_get('https://api.example.com/timeout', timeout=5)
    data = response.json()
except Timeout:
    print("Request timed out - server too slow or unreachable")
except ConnectionError:
    print("Failed to connect - check network or URL")
except HTTPError as e:
    print(f"HTTP Error: {e}")
print()

# Real requests error handling:
# from requests.exceptions import RequestException, Timeout, ConnectionError
#
# try:
#     response = requests.get(url, timeout=5)
#     response.raise_for_status()
#     data = response.json()
# except Timeout:
#     print("Request timed out")
# except ConnectionError:
#     print("Failed to connect")
# except requests.exceptions.HTTPError as e:
#     print(f"HTTP error: {e}")
# except RequestException as e:
#     print(f"Request failed: {e}")

# =============================================================================
# 10. Pagination - fetching multiple pages of results
# =============================================================================

print("=" * 70)
print("10. Pagination - fetching multiple pages of results")
print("=" * 70)

# Many APIs return data in pages (like search results)
all_users = []
current_page = 1
total_pages = 3

while current_page <= total_pages:
    response = simulated_get('https://api.example.com/users', params={'page': current_page})
    data = response.json()

    all_users.extend(data['users'])
    print(f"Fetched page {current_page}/{total_pages} - got {len(data['users'])} users")

    current_page += 1

print(f"Total users collected: {len(all_users)}")
for user in all_users:
    print(f"  - {user['name']} ({user['role']})")
print()

# =============================================================================
# 11. Practical example - weather API client (simulated)
# =============================================================================

print("=" * 70)
print("11. Practical example - weather API client (simulated)")
print("=" * 70)

def get_weather(city):
    """
    Simulated weather API client with proper error handling.
    In real code, this would call a real weather API like OpenWeatherMap.
    """
    # Simulate API endpoint
    url = f'https://api.weather.com/current'
    params = {'city': city, 'units': 'metric'}

    # Simulate weather data
    weather_data = {
        'Portland': {'temp': 18, 'conditions': 'Rainy', 'humidity': 85},
        'Seattle': {'temp': 16, 'conditions': 'Cloudy', 'humidity': 80},
        'Phoenix': {'temp': 35, 'conditions': 'Sunny', 'humidity': 20},
    }

    # Simulate the response
    if city in weather_data:
        return MockResponse(200, {
            'city': city,
            'temperature': weather_data[city]['temp'],
            'conditions': weather_data[city]['conditions'],
            'humidity': weather_data[city]['humidity']
        })
    else:
        return MockResponse(404, {'error': 'City not found'})

# Use the weather client
cities = ['Portland', 'Seattle', 'Phoenix', 'InvalidCity']

for city in cities:
    try:
        response = get_weather(city)
        response.raise_for_status()

        weather = response.json()
        print(f"{weather['city']}: {weather['temperature']}°C, {weather['conditions']}")
        print(f"  Humidity: {weather['humidity']}%")
    except HTTPError:
        print(f"{city}: City not found")
    except Exception as e:
        print(f"{city}: Error - {e}")

print()

# =============================================================================
# 12. Best practices summary
# =============================================================================

print("=" * 70)
print("12. Best practices summary")
print("=" * 70)

print("""
Key takeaways for making HTTP requests:

1. ALWAYS set timeouts
   response = requests.get(url, timeout=10)

2. ALWAYS handle errors
   try/except with specific exception types

3. Use raise_for_status() for automatic error checking
   response.raise_for_status()

4. Use json= parameter for POST/PUT
   requests.post(url, json=data)  # Auto-converts and sets headers

5. Use params= for query parameters
   requests.get(url, params={'page': 2})  # Handles encoding

6. Check response.ok before using data
   if response.ok:
       data = response.json()

7. Never hardcode API keys
   Use environment variables or config files

8. Be respectful of rate limits
   Don't hammer APIs, add delays if needed

9. Use sessions for multiple requests
   session = requests.Session()
   session.headers.update({'Authorization': 'Bearer token'})

10. Log your requests in production
    Essential for debugging API issues
""")

print("=" * 70)
print("HTTP REQUESTS EXAMPLE COMPLETE!")
print("=" * 70)
print()
print("To use the real requests library:")
print("  1. Install it: pip install requests")
print("  2. Replace simulated_get/post/etc with requests.get/post/etc")
print("  3. Use real API endpoints (GitHub API, JSONPlaceholder, etc.)")
print()
print("Try the exercises in exercises.py to practice!")
