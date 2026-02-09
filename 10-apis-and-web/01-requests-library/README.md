# HTTP Requests in Python

Welcome! This lesson covers making HTTP requests in Python - one of the most common tasks in modern programming. Whether you're consuming APIs, scraping data, or building integrations, you'll use these patterns constantly.

## What Are HTTP Requests?

HTTP (HyperText Transfer Protocol) is how computers talk to each other on the web. When you visit a website, your browser makes HTTP requests to servers. Your Python code can do the same thing!

Think of it like ordering at a restaurant:
- **You (client)** make a request to the **waiter (HTTP)**
- The **kitchen (server)** processes your order
- The **waiter** brings back a **response** (your food, or maybe "we're out of that")

## HTTP Methods (Verbs)

Different types of requests do different things:

### GET - Retrieve data
- Like asking "show me the menu"
- Most common request type
- Data goes in the URL (query parameters)
- Safe and idempotent (doesn't change server state)

### POST - Create new data
- Like placing an order
- Data goes in the request body
- Not idempotent (doing it twice creates two orders)

### PUT - Update existing data
- Like modifying your order
- Usually replaces the entire resource
- Idempotent (doing it twice has same effect as once)

### DELETE - Remove data
- Like canceling your order
- Idempotent

### Others
- **PATCH**: Partial update (change just one field)
- **HEAD**: Like GET but only returns headers
- **OPTIONS**: Ask what methods are allowed

## Anatomy of an HTTP Request

### URL Components
```
https://api.example.com/users?page=2&limit=10
  ^         ^              ^         ^
  |         |              |         |
scheme   domain         path    query parameters
```

### Headers
Key-value pairs with metadata about the request:
```
Content-Type: application/json
Authorization: Bearer abc123token
User-Agent: MyPythonApp/1.0
```

### Body
Data you're sending (POST/PUT/PATCH):
```json
{
  "name": "Alice",
  "email": "alice@example.com"
}
```

## HTTP Response

### Status Codes
Tell you what happened:
- **2xx Success**: 200 OK, 201 Created, 204 No Content
- **3xx Redirect**: 301 Moved Permanently, 302 Found
- **4xx Client Error**: 400 Bad Request, 401 Unauthorized, 404 Not Found
- **5xx Server Error**: 500 Internal Server Error, 503 Service Unavailable

### Response Headers
Metadata from the server:
```
Content-Type: application/json
Content-Length: 1234
Set-Cookie: session=xyz789
```

### Response Body
The actual data (JSON, HTML, text, binary, etc.)

## The `requests` Library

Python's most popular HTTP library. Clean, simple, and powerful.

### Installation
```bash
pip install requests
```

### Basic Usage

**Real `requests` library code:**
```python
import requests

# GET request
response = requests.get('https://api.github.com/users/python')
print(response.status_code)  # 200
print(response.json())        # Parsed JSON data

# POST request
data = {'name': 'Alice', 'age': 30}
response = requests.post('https://api.example.com/users', json=data)

# Custom headers
headers = {'Authorization': 'Bearer token123'}
response = requests.get('https://api.example.com/private', headers=headers)

# Query parameters
params = {'page': 2, 'limit': 10}
response = requests.get('https://api.example.com/items', params=params)
# Requests: https://api.example.com/items?page=2&limit=10
```

### Response Object

```python
response = requests.get('https://api.example.com/data')

# Status
response.status_code        # 200, 404, etc.
response.ok                 # True if status < 400
response.raise_for_status() # Raises exception if status >= 400

# Headers
response.headers            # Dict-like object
response.headers['Content-Type']

# Body
response.text               # String
response.content            # Bytes
response.json()             # Parsed JSON (if applicable)

# Metadata
response.url                # Final URL (after redirects)
response.encoding           # Character encoding
response.elapsed            # Time taken
```

## Error Handling

Always handle errors! Networks are unreliable.

```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

try:
    response = requests.get('https://api.example.com/data', timeout=5)
    response.raise_for_status()  # Raises HTTPError for bad status
    data = response.json()
except Timeout:
    print("Request timed out")
except ConnectionError:
    print("Failed to connect")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except RequestException as e:
    print(f"Request failed: {e}")
```

## Common Patterns

### Working with JSON APIs

```python
# GET with JSON response
response = requests.get('https://api.example.com/users/123')
user = response.json()
print(user['name'])

# POST with JSON body
new_user = {'name': 'Bob', 'email': 'bob@example.com'}
response = requests.post('https://api.example.com/users', json=new_user)
created = response.json()
print(f"Created user with ID: {created['id']}")
```

### Authentication

```python
# Bearer token (most common for APIs)
headers = {'Authorization': 'Bearer your_token_here'}
response = requests.get('https://api.example.com/private', headers=headers)

# Basic auth
from requests.auth import HTTPBasicAuth
response = requests.get(
    'https://api.example.com/private',
    auth=HTTPBasicAuth('username', 'password')
)
# Or shorthand:
response = requests.get('https://api.example.com/private', auth=('username', 'password'))

# API key in query params (less secure, avoid if possible)
params = {'api_key': 'your_key_here'}
response = requests.get('https://api.example.com/data', params=params)
```

### Handling Pagination

```python
def fetch_all_pages(base_url):
    all_items = []
    page = 1

    while True:
        response = requests.get(base_url, params={'page': page, 'per_page': 100})
        data = response.json()

        if not data['items']:
            break

        all_items.extend(data['items'])
        page += 1

        if page > data['total_pages']:
            break

    return all_items
```

## Session Objects

For making multiple requests to the same host, use a Session. It reuses the underlying TCP connection and persists cookies/headers.

```python
session = requests.Session()
session.headers.update({'Authorization': 'Bearer token123'})

# All requests in this session will include the Authorization header
response1 = session.get('https://api.example.com/users')
response2 = session.get('https://api.example.com/posts')
response3 = session.post('https://api.example.com/comments', json={'text': 'Hello'})

session.close()  # Or use context manager:

with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer token123'})
    response = session.get('https://api.example.com/users')
```

## Request Timeouts

Always set timeouts! Otherwise your program might hang forever.

```python
# Timeout after 5 seconds
response = requests.get('https://api.example.com/data', timeout=5)

# Separate connect and read timeouts
response = requests.get('https://api.example.com/data', timeout=(3.05, 27))
# 3.05 seconds to connect, 27 seconds to read
```

## Query Parameters

```python
# Manual string building (don't do this!)
url = 'https://api.example.com/search?q=python&page=2'  # What about spaces? Special chars?

# Let requests handle it
params = {'q': 'python programming', 'page': 2, 'sort': 'newest'}
response = requests.get('https://api.example.com/search', params=params)
# URL: https://api.example.com/search?q=python+programming&page=2&sort=newest
```

## Custom Headers

```python
headers = {
    'User-Agent': 'MyApp/1.0',
    'Accept': 'application/json',
    'Accept-Language': 'en-US',
    'Authorization': 'Bearer token123'
}

response = requests.get('https://api.example.com/data', headers=headers)
```

## Simulated Examples (No Dependencies)

Since `requests` is an external library, our example and exercise files use **simulated HTTP functions** that demonstrate the exact same patterns without requiring installation. This is for learning purposes.

```python
# Simulated function that mimics requests.get()
def simulated_get(url, params=None, headers=None, timeout=None):
    # Returns a mock response object
    return MockResponse(200, {'data': 'example'})

# In real code, you'd use:
# import requests
# response = requests.get('https://api.example.com/data')
```

The patterns are identical - just swap the simulated functions for real `requests` calls when you install the library!

## Best Practices

1. **Always set timeouts** - Don't let your program hang forever
2. **Handle errors gracefully** - Networks fail, APIs change, servers go down
3. **Use sessions for multiple requests** - More efficient
4. **Check status codes** - Don't assume success
5. **Use `response.raise_for_status()`** - Automatic error checking
6. **Be respectful** - Don't hammer APIs, respect rate limits
7. **Keep secrets secret** - Never hardcode API keys in code
8. **Log requests in production** - Essential for debugging

## Real-World Example

```python
import requests
import os
from requests.exceptions import RequestException

def fetch_github_user(username):
    """Fetch GitHub user info with proper error handling."""
    url = f'https://api.github.com/users/{username}'

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        user = response.json()
        return {
            'name': user['name'],
            'bio': user['bio'],
            'public_repos': user['public_repos'],
            'followers': user['followers']
        }
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return {'error': 'User not found'}
        return {'error': f'HTTP error: {e}'}
    except Timeout:
        return {'error': 'Request timed out'}
    except RequestException as e:
        return {'error': f'Request failed: {e}'}

# Usage
result = fetch_github_user('python')
if 'error' in result:
    print(f"Error: {result['error']}")
else:
    print(f"{result['name']} has {result['public_repos']} public repos")
```

## Common Pitfalls

1. **Forgetting to check status codes** - Always verify the request succeeded
2. **Not handling exceptions** - Networks are unreliable
3. **No timeouts** - Your program might hang forever
4. **Hardcoding URLs** - Use constants or config files
5. **Ignoring rate limits** - You'll get blocked
6. **Not closing sessions** - Resource leaks in long-running apps
7. **Exposing API keys** - Keep them in environment variables

## Alternative: Built-in `urllib`

Python has a built-in HTTP library, but it's more verbose:

```python
import urllib.request
import json

# GET request
with urllib.request.urlopen('https://api.example.com/data') as response:
    data = json.loads(response.read())

# POST request
data = json.dumps({'name': 'Alice'}).encode('utf-8')
req = urllib.request.Request(
    'https://api.example.com/users',
    data=data,
    headers={'Content-Type': 'application/json'}
)
with urllib.request.urlopen(req) as response:
    result = json.loads(response.read())
```

Most people prefer `requests` for its simplicity!

## Next Steps

- Check out `example.py` for hands-on examples
- Complete the exercises in `exercises.py`
- Install `requests` and try it with real APIs
- Explore the [requests documentation](https://requests.readthedocs.io/)
- Try more advanced features: sessions, retries, streaming

Happy requesting!
