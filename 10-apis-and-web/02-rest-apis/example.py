"""
REST APIs - Example Code

This example demonstrates REST API concepts using a simulated in-memory API.
We'll build a simple user management API with full CRUD operations.

Note: In production, you'd use frameworks like Flask or FastAPI.
We're keeping this stdlib-only for learning purposes.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional, Any

# ============================================================================
# SIMULATED REST API (In-Memory Data Store)
# ============================================================================

# This simulates a database - in production, you'd use a real database
users_db: Dict[int, Dict[str, Any]] = {}
next_user_id = 1

# Simulated API key for authentication
VALID_API_KEY = "demo_key_12345"


def create_user(data: Dict[str, Any], api_key: str) -> Dict[str, Any]:
    """POST /users - Create a new user"""
    global next_user_id

    # Authentication check
    if api_key != VALID_API_KEY:
        return {
            "status": 401,
            "error": {
                "code": "UNAUTHORIZED",
                "message": "Invalid API key"
            }
        }

    # Validation
    if not data.get("name") or not data.get("email"):
        return {
            "status": 400,
            "error": {
                "code": "INVALID_REQUEST",
                "message": "Name and email are required"
            }
        }

    # Check if email already exists
    for user in users_db.values():
        if user["email"] == data["email"]:
            return {
                "status": 409,
                "error": {
                    "code": "EMAIL_EXISTS",
                    "message": f"User with email {data['email']} already exists"
                }
            }

    # Create the user
    user = {
        "id": next_user_id,
        "name": data["name"],
        "email": data["email"],
        "role": data.get("role", "user"),  # Default role
        "created_at": datetime.now().isoformat()
    }
    users_db[next_user_id] = user
    next_user_id += 1

    return {
        "status": 201,
        "data": user
    }


def get_users(params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """GET /users - Get all users (with optional filtering and pagination)"""
    params = params or {}

    # Start with all users
    users = list(users_db.values())

    # Filter by role if provided
    if "role" in params:
        users = [u for u in users if u["role"] == params["role"]]

    # Filter by name (partial match)
    if "name" in params:
        search_name = params["name"].lower()
        users = [u for u in users if search_name in u["name"].lower()]

    # Sorting
    sort_by = params.get("sort", "id")
    reverse = params.get("order", "asc") == "desc"
    if sort_by in ["id", "name", "created_at"]:
        users.sort(key=lambda u: u.get(sort_by, ""), reverse=reverse)

    # Pagination
    page = int(params.get("page", 1))
    limit = int(params.get("limit", 10))
    total = len(users)
    start = (page - 1) * limit
    end = start + limit
    paginated_users = users[start:end]

    return {
        "status": 200,
        "data": paginated_users,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit
        }
    }


def get_user(user_id: int) -> Dict[str, Any]:
    """GET /users/{id} - Get a specific user"""
    if user_id not in users_db:
        return {
            "status": 404,
            "error": {
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} not found"
            }
        }

    return {
        "status": 200,
        "data": users_db[user_id]
    }


def update_user(user_id: int, data: Dict[str, Any], api_key: str) -> Dict[str, Any]:
    """PUT /users/{id} - Update a user"""
    # Authentication
    if api_key != VALID_API_KEY:
        return {
            "status": 401,
            "error": {
                "code": "UNAUTHORIZED",
                "message": "Invalid API key"
            }
        }

    # Check if user exists
    if user_id not in users_db:
        return {
            "status": 404,
            "error": {
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} not found"
            }
        }

    # Update the user
    user = users_db[user_id]
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    user["role"] = data.get("role", user["role"])
    user["updated_at"] = datetime.now().isoformat()

    return {
        "status": 200,
        "data": user
    }


def delete_user(user_id: int, api_key: str) -> Dict[str, Any]:
    """DELETE /users/{id} - Delete a user"""
    # Authentication
    if api_key != VALID_API_KEY:
        return {
            "status": 401,
            "error": {
                "code": "UNAUTHORIZED",
                "message": "Invalid API key"
            }
        }

    # Check if user exists
    if user_id not in users_db:
        return {
            "status": 404,
            "error": {
                "code": "USER_NOT_FOUND",
                "message": f"User with ID {user_id} not found"
            }
        }

    # Delete the user
    del users_db[user_id]

    return {
        "status": 204,
        "message": "User deleted successfully"
    }


# ============================================================================
# EXAMPLE 1: Creating Resources (POST)
# ============================================================================

print("=" * 60)
print("EXAMPLE 1: Creating Resources (POST /users)")
print("=" * 60)

# Successful creation
response = create_user(
    {"name": "Alice", "email": "alice@example.com", "role": "admin"},
    api_key=VALID_API_KEY
)
print(f"Status: {response['status']}")
print(f"Response: {json.dumps(response.get('data'), indent=2)}")
print()

# Create more users
create_user({"name": "Bob", "email": "bob@example.com"}, VALID_API_KEY)
create_user({"name": "Charlie", "email": "charlie@example.com", "role": "admin"}, VALID_API_KEY)
print("Created 2 more users (Bob and Charlie)")
print()


# ============================================================================
# EXAMPLE 2: Error Handling - Missing Fields (400)
# ============================================================================

print("=" * 60)
print("EXAMPLE 2: Error Handling - Missing Required Fields")
print("=" * 60)

response = create_user({"name": "David"}, VALID_API_KEY)  # Missing email
print(f"Status: {response['status']} (400 Bad Request)")
print(f"Error: {json.dumps(response.get('error'), indent=2)}")
print()


# ============================================================================
# EXAMPLE 3: Error Handling - Duplicate Resource (409)
# ============================================================================

print("=" * 60)
print("EXAMPLE 3: Error Handling - Duplicate Email")
print("=" * 60)

response = create_user(
    {"name": "Alice Clone", "email": "alice@example.com"},
    VALID_API_KEY
)
print(f"Status: {response['status']} (409 Conflict)")
print(f"Error: {json.dumps(response.get('error'), indent=2)}")
print()


# ============================================================================
# EXAMPLE 4: Authentication Error (401)
# ============================================================================

print("=" * 60)
print("EXAMPLE 4: Authentication Error")
print("=" * 60)

response = create_user(
    {"name": "Eve", "email": "eve@example.com"},
    api_key="wrong_key"
)
print(f"Status: {response['status']} (401 Unauthorized)")
print(f"Error: {json.dumps(response.get('error'), indent=2)}")
print()


# ============================================================================
# EXAMPLE 5: Reading Resources (GET)
# ============================================================================

print("=" * 60)
print("EXAMPLE 5: Reading All Resources (GET /users)")
print("=" * 60)

response = get_users()
print(f"Status: {response['status']}")
print(f"Total users: {response['pagination']['total']}")
print(f"Users:")
for user in response['data']:
    print(f"  - {user['name']} ({user['email']}) - {user['role']}")
print()


# ============================================================================
# EXAMPLE 6: Reading Single Resource (GET by ID)
# ============================================================================

print("=" * 60)
print("EXAMPLE 6: Reading Single Resource (GET /users/1)")
print("=" * 60)

response = get_user(1)
print(f"Status: {response['status']}")
print(f"User: {json.dumps(response['data'], indent=2)}")
print()


# ============================================================================
# EXAMPLE 7: Resource Not Found (404)
# ============================================================================

print("=" * 60)
print("EXAMPLE 7: Resource Not Found")
print("=" * 60)

response = get_user(999)
print(f"Status: {response['status']} (404 Not Found)")
print(f"Error: {json.dumps(response.get('error'), indent=2)}")
print()


# ============================================================================
# EXAMPLE 8: Filtering Resources
# ============================================================================

print("=" * 60)
print("EXAMPLE 8: Filtering Resources (GET /users?role=admin)")
print("=" * 60)

response = get_users({"role": "admin"})
print(f"Status: {response['status']}")
print(f"Admin users found: {len(response['data'])}")
for user in response['data']:
    print(f"  - {user['name']} ({user['role']})")
print()


# ============================================================================
# EXAMPLE 9: Searching Resources
# ============================================================================

print("=" * 60)
print("EXAMPLE 9: Searching Resources (GET /users?name=ali)")
print("=" * 60)

response = get_users({"name": "ali"})  # Partial match
print(f"Status: {response['status']}")
print(f"Matching users:")
for user in response['data']:
    print(f"  - {user['name']}")
print()


# ============================================================================
# EXAMPLE 10: Pagination
# ============================================================================

print("=" * 60)
print("EXAMPLE 10: Pagination (GET /users?page=1&limit=2)")
print("=" * 60)

response = get_users({"page": 1, "limit": 2})
print(f"Status: {response['status']}")
print(f"Page: {response['pagination']['page']}/{response['pagination']['total_pages']}")
print(f"Users on this page:")
for user in response['data']:
    print(f"  - {user['name']}")
print()


# ============================================================================
# EXAMPLE 11: Sorting
# ============================================================================

print("=" * 60)
print("EXAMPLE 11: Sorting (GET /users?sort=name&order=desc)")
print("=" * 60)

response = get_users({"sort": "name", "order": "desc"})
print(f"Status: {response['status']}")
print(f"Users (sorted by name, descending):")
for user in response['data']:
    print(f"  - {user['name']}")
print()


# ============================================================================
# EXAMPLE 12: Updating Resources (PUT)
# ============================================================================

print("=" * 60)
print("EXAMPLE 12: Updating Resources (PUT /users/2)")
print("=" * 60)

print("Before update:")
response = get_user(2)
print(f"  Name: {response['data']['name']}, Role: {response['data']['role']}")

response = update_user(
    2,
    {"name": "Bob Updated", "role": "admin"},
    VALID_API_KEY
)
print(f"\nStatus: {response['status']}")
print(f"After update:")
print(f"  Name: {response['data']['name']}, Role: {response['data']['role']}")
print()


# ============================================================================
# EXAMPLE 13: Deleting Resources (DELETE)
# ============================================================================

print("=" * 60)
print("EXAMPLE 13: Deleting Resources (DELETE /users/3)")
print("=" * 60)

print(f"Users before delete: {len(users_db)}")
response = delete_user(3, VALID_API_KEY)
print(f"Status: {response['status']} (204 No Content)")
print(f"Users after delete: {len(users_db)}")
print()


# ============================================================================
# EXAMPLE 14: Complete CRUD Workflow
# ============================================================================

print("=" * 60)
print("EXAMPLE 14: Complete CRUD Workflow")
print("=" * 60)

print("1. CREATE a new user")
response = create_user(
    {"name": "Diana", "email": "diana@example.com"},
    VALID_API_KEY
)
user_id = response['data']['id']
print(f"   Created user with ID: {user_id}")

print("\n2. READ the user")
response = get_user(user_id)
print(f"   User: {response['data']['name']}")

print("\n3. UPDATE the user")
response = update_user(user_id, {"name": "Diana Updated"}, VALID_API_KEY)
print(f"   Updated name to: {response['data']['name']}")

print("\n4. DELETE the user")
delete_user(user_id, VALID_API_KEY)
print(f"   User deleted")

print("\n5. TRY TO READ deleted user (should fail)")
response = get_user(user_id)
print(f"   Status: {response['status']} - {response['error']['message']}")
print()


# ============================================================================
# BONUS: What Production Code Looks Like
# ============================================================================

print("=" * 60)
print("BONUS: What This Looks Like in Production")
print("=" * 60)
print("""
# With Flask (popular web framework):
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.name = data.get('name', user.name)
    db.session.commit()
    return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

# With FastAPI (modern async framework):
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

@app.get("/users")
async def get_users():
    return users_db.values()

@app.post("/users", status_code=201)
async def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = {"id": user_id, **user.dict()}
    users_db[user_id] = new_user
    return new_user

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserCreate):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = {"id": user_id, **user.dict()}
    return users_db[user_id]

@app.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return None

# These frameworks handle:
# - Automatic JSON serialization/deserialization
# - Request validation
# - Status code handling
# - Error handling
# - Documentation generation (OpenAPI/Swagger)
# - And much more!
""")

print("\nKey Takeaways:")
print("- REST APIs are resource-oriented (nouns, not verbs)")
print("- HTTP methods map to CRUD operations")
print("- Status codes communicate what happened")
print("- JSON is the standard format")
print("- Authentication protects your API")
print("- Filtering, pagination, and sorting improve usability")
print("- Consistent error handling helps API consumers")
