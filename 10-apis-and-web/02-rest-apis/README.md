# REST APIs

Learn how to build and interact with REST APIs - the backbone of modern web services!

## What is a REST API?

REST (Representational State Transfer) is an architectural style for designing networked applications. A REST API lets different applications communicate over HTTP using standard methods.

Think of it like a restaurant:
- **Resources** are menu items (users, posts, products)
- **Endpoints** are table numbers where you order
- **HTTP methods** are how you order (GET = read menu, POST = place order, etc.)
- **JSON** is the language you speak

## Core Concepts

### Resources and Endpoints

Resources are the "things" your API manages. Each resource has a URL endpoint:

```
GET    /users          # Get all users
GET    /users/123      # Get user with ID 123
POST   /users          # Create a new user
PUT    /users/123      # Update user 123
DELETE /users/123      # Delete user 123
```

### HTTP Methods (CRUD Operations)

REST maps database operations (CRUD) to HTTP methods:

| Operation | HTTP Method | Example | What it does |
|-----------|-------------|---------|--------------|
| **Create** | POST | `POST /users` | Add a new resource |
| **Read** | GET | `GET /users/123` | Retrieve resource(s) |
| **Update** | PUT | `PUT /users/123` | Update entire resource |
| **Update** | PATCH | `PATCH /users/123` | Update part of resource |
| **Delete** | DELETE | `DELETE /users/123` | Remove a resource |

### JSON Format

APIs typically send and receive data as JSON:

```json
{
  "id": 123,
  "name": "Alice",
  "email": "alice@example.com",
  "created_at": "2026-01-15T10:30:00Z"
}
```

## HTTP Status Codes

Status codes tell you what happened with your request:

### Success Codes (2xx)
- **200 OK** - Request succeeded, here's your data
- **201 Created** - New resource was created successfully
- **204 No Content** - Success, but no data to return (common for DELETE)

### Client Error Codes (4xx)
- **400 Bad Request** - Your request was malformed or invalid
- **401 Unauthorized** - You need to authenticate first
- **403 Forbidden** - You're authenticated but don't have permission
- **404 Not Found** - Resource doesn't exist
- **409 Conflict** - Resource already exists or conflicts with current state

### Server Error Codes (5xx)
- **500 Internal Server Error** - Something broke on the server
- **503 Service Unavailable** - Server is down or overloaded

## API Design Best Practices

### 1. Use Nouns for Resources (Not Verbs)

```
✅ GET /users/123
❌ GET /getUser/123

✅ DELETE /posts/456
❌ POST /deletePost/456
```

### 2. Use Plural Nouns

```
✅ /users
❌ /user
```

### 3. Use Nested Routes for Relationships

```
GET /users/123/posts          # Get all posts by user 123
GET /users/123/posts/789      # Get post 789 by user 123
```

### 4. Support Filtering, Sorting, and Pagination

```
GET /users?role=admin&sort=created_at&page=2&limit=20
```

### 5. Version Your API

```
/v1/users
/v2/users
```

### 6. Return Consistent Error Responses

```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with ID 123 does not exist",
    "status": 404
  }
}
```

## Authentication Basics

APIs need to know who's making requests. Common methods:

### API Keys
Simple but less secure. Pass a key in the request:

```
GET /users
Authorization: ApiKey abc123xyz456
```

### Bearer Tokens (OAuth, JWT)
More secure. Server issues a token after login:

```
GET /users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### Basic Auth
Username and password (base64 encoded):

```
GET /users
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

## Request/Response Cycle

Here's what happens when you call an API:

1. **Client sends request**: HTTP method + endpoint + headers + body (if needed)
2. **Server processes**: Validates request, performs operation, prepares response
3. **Server sends response**: Status code + headers + body (usually JSON)

Example:

```
→ Request:
POST /users HTTP/1.1
Content-Type: application/json

{
  "name": "Bob",
  "email": "bob@example.com"
}

← Response:
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 124,
  "name": "Bob",
  "email": "bob@example.com",
  "created_at": "2026-02-09T14:30:00Z"
}
```

## Common Patterns

### Pagination

```python
# Request
GET /users?page=2&limit=20

# Response
{
  "data": [...],
  "page": 2,
  "limit": 20,
  "total": 100,
  "total_pages": 5
}
```

### Searching/Filtering

```python
GET /users?name=Alice&role=admin
```

### Sorting

```python
GET /users?sort=created_at&order=desc
```

### Partial Responses (Field Selection)

```python
GET /users?fields=id,name,email
```

## Real-World Examples

Popular APIs you might use:
- **GitHub API**: Manage repos, issues, pull requests
- **Twitter API**: Read/post tweets, manage followers
- **Stripe API**: Process payments
- **OpenWeather API**: Get weather data
- **Google Maps API**: Geocoding, directions

## Quick Reference

```python
# Python stdlib (urllib)
import urllib.request
import json

# Making a GET request
response = urllib.request.urlopen('https://api.example.com/users')
data = json.loads(response.read())

# Making a POST request
data = json.dumps({"name": "Alice"}).encode('utf-8')
req = urllib.request.Request(
    'https://api.example.com/users',
    data=data,
    headers={'Content-Type': 'application/json'},
    method='POST'
)
response = urllib.request.urlopen(req)
```

With third-party libraries (not used in this lesson, but good to know):

```python
# Using requests library (popular but not stdlib)
import requests

# GET
response = requests.get('https://api.example.com/users')
users = response.json()

# POST
response = requests.post('https://api.example.com/users',
                        json={"name": "Alice"})

# PUT
response = requests.put('https://api.example.com/users/123',
                       json={"name": "Alice Updated"})

# DELETE
response = requests.delete('https://api.example.com/users/123')
```

## Next Steps

- Practice with public APIs (many offer free tiers)
- Learn about API documentation (OpenAPI/Swagger)
- Explore GraphQL as an alternative to REST
- Study API rate limiting and caching
- Build your own API with Flask or FastAPI!

Remember: Good APIs are intuitive, consistent, and well-documented. Think about your API from the user's perspective!

## Code Example

Check out [`example.py`](example.py) for a complete working example.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.
