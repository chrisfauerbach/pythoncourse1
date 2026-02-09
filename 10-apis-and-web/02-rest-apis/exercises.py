"""
REST APIs - Exercises

Practice building and interacting with REST APIs.
Try to solve each exercise before looking at the solutions at the bottom!
"""

import json
from typing import Dict, List, Any


# =============================================================================
# EXERCISE 1: Build a Simple Product Catalog API
# Create functions to manage a product catalog with GET all and GET by ID
# =============================================================================

def exercise_1():
    """
    Build a simple product catalog API.

    Create two functions:
    1. get_all_products() - returns all products with status 200
    2. get_product_by_id(product_id) - returns a product or 404 error

    Use this data:
    products = {
        1: {"id": 1, "name": "Laptop", "price": 999.99},
        2: {"id": 2, "name": "Mouse", "price": 29.99},
        3: {"id": 3, "name": "Keyboard", "price": 79.99}
    }
    """
    print("Building a product catalog API...")

    products = {
        1: {"id": 1, "name": "Laptop", "price": 999.99},
        2: {"id": 2, "name": "Mouse", "price": 29.99},
        3: {"id": 3, "name": "Keyboard", "price": 79.99}
    }

    # YOUR CODE HERE
    # Define get_all_products() and get_product_by_id(product_id)

    print("TODO: Implement the API functions")


# =============================================================================
# EXERCISE 2: Add POST Endpoint with Validation
# Extend the product API to create new products with validation
# =============================================================================

def exercise_2():
    """
    Add a create_product function that:
    1. Validates that name and price are provided
    2. Returns 400 if validation fails
    3. Creates the product and returns 201 on success
    4. Generates auto-incrementing IDs

    Validation rules:
    - name must be present and non-empty
    - price must be present and > 0
    """
    print("Adding POST endpoint with validation...")

    products = {}
    next_id = 1

    # YOUR CODE HERE
    # Define create_product(data) that validates and creates products

    print("TODO: Implement create_product with validation")


# =============================================================================
# EXERCISE 3: Implement Filtering
# Add filtering support to get all products (by price range, name search)
# =============================================================================

def exercise_3():
    """
    Extend get_all_products to support filtering:
    1. Filter by min_price (products >= min_price)
    2. Filter by max_price (products <= max_price)
    3. Search by name (partial, case-insensitive match)

    Example:
    get_all_products({"min_price": 50, "max_price": 100})
    get_all_products({"name": "key"})  # matches "Keyboard"
    """
    print("Implementing filtering...")

    products = {
        1: {"id": 1, "name": "Laptop", "price": 999.99},
        2: {"id": 2, "name": "Mouse", "price": 29.99},
        3: {"id": 3, "name": "Keyboard", "price": 79.99},
        4: {"id": 4, "name": "Monitor", "price": 299.99}
    }

    # YOUR CODE HERE
    # Define get_all_products(filters=None) that supports filtering

    print("TODO: Implement filtering")


# =============================================================================
# EXERCISE 4: Add Pagination
# Implement pagination for the product list
# =============================================================================

def exercise_4():
    """
    Add pagination to get_all_products:
    1. Accept page and limit parameters
    2. Return paginated results
    3. Include pagination metadata (page, limit, total, total_pages)

    Default: page=1, limit=10
    """
    print("Implementing pagination...")

    # Create 15 products for testing
    products = {i: {"id": i, "name": f"Product {i}", "price": i * 10.0}
                for i in range(1, 16)}

    # YOUR CODE HERE
    # Define get_all_products(page=1, limit=10) with pagination

    print("TODO: Implement pagination")


# =============================================================================
# EXERCISE 5: Build a Complete CRUD API
# Implement all CRUD operations for a blog post API
# =============================================================================

def exercise_5():
    """
    Build a complete blog post API with:
    1. create_post(data, api_key) - POST with auth
    2. get_posts() - GET all
    3. get_post(post_id) - GET single
    4. update_post(post_id, data, api_key) - PUT with auth
    5. delete_post(post_id, api_key) - DELETE with auth

    Post structure: {id, title, content, author, created_at}
    API key: "blog_secret_123"

    Validation:
    - title and content are required
    - Return appropriate status codes (200, 201, 204, 400, 401, 404)
    """
    print("Building complete CRUD API...")

    # YOUR CODE HERE
    # Implement all 5 functions

    print("TODO: Implement full CRUD API")


# =============================================================================
# EXERCISE 6: Error Handling and Status Codes
# Practice returning appropriate error responses
# =============================================================================

def exercise_6():
    """
    Create an API function that demonstrates different status codes:

    make_api_request(endpoint, method, data=None, api_key=None)

    Should return appropriate status codes for:
    - 200 OK - successful GET
    - 201 Created - successful POST
    - 204 No Content - successful DELETE
    - 400 Bad Request - invalid data
    - 401 Unauthorized - missing/invalid API key
    - 404 Not Found - resource doesn't exist
    - 409 Conflict - duplicate resource

    Use these endpoints:
    - GET /status/ok -> 200
    - POST /status/created -> 201
    - DELETE /status/deleted -> 204
    - GET /status/notfound -> 404
    - POST /status/duplicate -> 409
    - Any request without api_key="test_key" -> 401
    """
    print("Testing error handling and status codes...")

    # YOUR CODE HERE
    # Define make_api_request(endpoint, method, data=None, api_key=None)

    print("TODO: Implement status code handling")


# =============================================================================
# SOLUTIONS (No peeking until you've tried!)
# =============================================================================

def solution_1():
    """Solution: Build a Simple Product Catalog API"""
    print("Building a product catalog API...")

    products = {
        1: {"id": 1, "name": "Laptop", "price": 999.99},
        2: {"id": 2, "name": "Mouse", "price": 29.99},
        3: {"id": 3, "name": "Keyboard", "price": 79.99}
    }

    def get_all_products():
        return {
            "status": 200,
            "data": list(products.values())
        }

    def get_product_by_id(product_id):
        if product_id not in products:
            return {
                "status": 404,
                "error": {
                    "code": "PRODUCT_NOT_FOUND",
                    "message": f"Product with ID {product_id} not found"
                }
            }
        return {
            "status": 200,
            "data": products[product_id]
        }

    # Test it
    response = get_all_products()
    print(f"GET /products -> Status {response['status']}")
    print(f"Found {len(response['data'])} products")

    response = get_product_by_id(2)
    print(f"\nGET /products/2 -> Status {response['status']}")
    print(f"Product: {response['data']['name']} - ${response['data']['price']}")

    response = get_product_by_id(999)
    print(f"\nGET /products/999 -> Status {response['status']}")
    print(f"Error: {response['error']['message']}")


def solution_2():
    """Solution: Add POST Endpoint with Validation"""
    print("Adding POST endpoint with validation...")

    products = {}
    next_id = [1]  # Use list to avoid scope issues

    def create_product(data):
        # Validation
        if not data.get("name") or not isinstance(data.get("name"), str):
            return {
                "status": 400,
                "error": {
                    "code": "INVALID_NAME",
                    "message": "Name is required and must be a string"
                }
            }

        if not data.get("price") or not isinstance(data.get("price"), (int, float)) or data.get("price") <= 0:
            return {
                "status": 400,
                "error": {
                    "code": "INVALID_PRICE",
                    "message": "Price is required and must be greater than 0"
                }
            }

        # Create product
        product = {
            "id": next_id[0],
            "name": data["name"],
            "price": float(data["price"])
        }
        products[next_id[0]] = product
        next_id[0] += 1

        return {
            "status": 201,
            "data": product
        }

    # Test it
    response = create_product({"name": "Laptop", "price": 999.99})
    print(f"POST /products (valid) -> Status {response['status']}")
    print(f"Created: {response['data']}")

    response = create_product({"name": "Mouse"})  # Missing price
    print(f"\nPOST /products (missing price) -> Status {response['status']}")
    print(f"Error: {response['error']['message']}")

    response = create_product({"name": "Keyboard", "price": -10})  # Invalid price
    print(f"\nPOST /products (negative price) -> Status {response['status']}")
    print(f"Error: {response['error']['message']}")


def solution_3():
    """Solution: Implement Filtering"""
    print("Implementing filtering...")

    products = {
        1: {"id": 1, "name": "Laptop", "price": 999.99},
        2: {"id": 2, "name": "Mouse", "price": 29.99},
        3: {"id": 3, "name": "Keyboard", "price": 79.99},
        4: {"id": 4, "name": "Monitor", "price": 299.99}
    }

    def get_all_products(filters=None):
        filters = filters or {}
        result = list(products.values())

        # Filter by min_price
        if "min_price" in filters:
            min_price = float(filters["min_price"])
            result = [p for p in result if p["price"] >= min_price]

        # Filter by max_price
        if "max_price" in filters:
            max_price = float(filters["max_price"])
            result = [p for p in result if p["price"] <= max_price]

        # Search by name
        if "name" in filters:
            search = filters["name"].lower()
            result = [p for p in result if search in p["name"].lower()]

        return {
            "status": 200,
            "data": result
        }

    # Test it
    response = get_all_products()
    print(f"GET /products -> {len(response['data'])} products")

    response = get_all_products({"min_price": 50, "max_price": 300})
    print(f"\nGET /products?min_price=50&max_price=300 -> {len(response['data'])} products")
    for p in response['data']:
        print(f"  - {p['name']}: ${p['price']}")

    response = get_all_products({"name": "key"})
    print(f"\nGET /products?name=key -> {len(response['data'])} products")
    for p in response['data']:
        print(f"  - {p['name']}")


def solution_4():
    """Solution: Add Pagination"""
    print("Implementing pagination...")

    products = {i: {"id": i, "name": f"Product {i}", "price": i * 10.0}
                for i in range(1, 16)}

    def get_all_products(page=1, limit=10):
        all_products = list(products.values())
        total = len(all_products)

        # Calculate pagination
        start = (page - 1) * limit
        end = start + limit
        paginated = all_products[start:end]

        return {
            "status": 200,
            "data": paginated,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "total_pages": (total + limit - 1) // limit
            }
        }

    # Test it
    response = get_all_products(page=1, limit=5)
    print(f"GET /products?page=1&limit=5")
    print(f"Page {response['pagination']['page']}/{response['pagination']['total_pages']}")
    print(f"Showing {len(response['data'])} of {response['pagination']['total']} products")

    response = get_all_products(page=2, limit=5)
    print(f"\nGET /products?page=2&limit=5")
    print(f"Products on page 2:")
    for p in response['data']:
        print(f"  - {p['name']}")


def solution_5():
    """Solution: Build a Complete CRUD API"""
    print("Building complete CRUD API...")

    from datetime import datetime

    posts = {}
    next_id = [1]
    API_KEY = "blog_secret_123"

    def create_post(data, api_key):
        if api_key != API_KEY:
            return {"status": 401, "error": {"code": "UNAUTHORIZED", "message": "Invalid API key"}}

        if not data.get("title") or not data.get("content"):
            return {"status": 400, "error": {"code": "INVALID_POST", "message": "Title and content required"}}

        post = {
            "id": next_id[0],
            "title": data["title"],
            "content": data["content"],
            "author": data.get("author", "Anonymous"),
            "created_at": datetime.now().isoformat()
        }
        posts[next_id[0]] = post
        next_id[0] += 1
        return {"status": 201, "data": post}

    def get_posts():
        return {"status": 200, "data": list(posts.values())}

    def get_post(post_id):
        if post_id not in posts:
            return {"status": 404, "error": {"code": "POST_NOT_FOUND", "message": "Post not found"}}
        return {"status": 200, "data": posts[post_id]}

    def update_post(post_id, data, api_key):
        if api_key != API_KEY:
            return {"status": 401, "error": {"code": "UNAUTHORIZED", "message": "Invalid API key"}}
        if post_id not in posts:
            return {"status": 404, "error": {"code": "POST_NOT_FOUND", "message": "Post not found"}}

        post = posts[post_id]
        post["title"] = data.get("title", post["title"])
        post["content"] = data.get("content", post["content"])
        return {"status": 200, "data": post}

    def delete_post(post_id, api_key):
        if api_key != API_KEY:
            return {"status": 401, "error": {"code": "UNAUTHORIZED", "message": "Invalid API key"}}
        if post_id not in posts:
            return {"status": 404, "error": {"code": "POST_NOT_FOUND", "message": "Post not found"}}

        del posts[post_id]
        return {"status": 204}

    # Test it
    print("1. CREATE")
    r = create_post({"title": "Hello World", "content": "My first post", "author": "Alice"}, API_KEY)
    print(f"   Status: {r['status']} - Created post {r['data']['id']}")

    print("\n2. READ")
    r = get_posts()
    print(f"   Status: {r['status']} - Found {len(r['data'])} posts")

    print("\n3. UPDATE")
    r = update_post(1, {"title": "Hello World Updated"}, API_KEY)
    print(f"   Status: {r['status']} - New title: {r['data']['title']}")

    print("\n4. DELETE")
    r = delete_post(1, API_KEY)
    print(f"   Status: {r['status']} - Post deleted")


def solution_6():
    """Solution: Error Handling and Status Codes"""
    print("Testing error handling and status codes...")

    def make_api_request(endpoint, method, data=None, api_key=None):
        # Auth check (except for specific test endpoints)
        if not endpoint.startswith("/status/") and api_key != "test_key":
            return {
                "status": 401,
                "error": {"code": "UNAUTHORIZED", "message": "API key required"}
            }

        # Route handling
        if endpoint == "/status/ok" and method == "GET":
            return {"status": 200, "data": {"message": "OK"}}

        elif endpoint == "/status/created" and method == "POST":
            return {"status": 201, "data": {"message": "Created"}}

        elif endpoint == "/status/deleted" and method == "DELETE":
            return {"status": 204}

        elif endpoint == "/status/notfound":
            return {
                "status": 404,
                "error": {"code": "NOT_FOUND", "message": "Resource not found"}
            }

        elif endpoint == "/status/duplicate" and method == "POST":
            return {
                "status": 409,
                "error": {"code": "DUPLICATE", "message": "Resource already exists"}
            }

        else:
            return {
                "status": 404,
                "error": {"code": "NOT_FOUND", "message": "Endpoint not found"}
            }

    # Test all status codes
    tests = [
        ("GET", "/status/ok", None, None, 200, "OK"),
        ("POST", "/status/created", {}, None, 201, "Created"),
        ("DELETE", "/status/deleted", None, None, 204, "No Content"),
        ("GET", "/status/notfound", None, None, 404, "Not Found"),
        ("POST", "/status/duplicate", {}, None, 409, "Conflict"),
        ("GET", "/users", None, None, 401, "Unauthorized"),
    ]

    for method, endpoint, data, api_key, expected_status, description in tests:
        response = make_api_request(endpoint, method, data, api_key)
        status_match = "✓" if response['status'] == expected_status else "✗"
        print(f"{status_match} {method} {endpoint} -> {response['status']} {description}")


# =============================================================================
# Test Runner
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Build a Simple Product Catalog API", exercise_1),
        ("Add POST Endpoint with Validation", exercise_2),
        ("Implement Filtering", exercise_3),
        ("Add Pagination", exercise_4),
        ("Build a Complete CRUD API", exercise_5),
        ("Error Handling and Status Codes", exercise_6),
    ]

    solutions = [
        ("Build a Simple Product Catalog API", solution_1),
        ("Add POST Endpoint with Validation", solution_2),
        ("Implement Filtering", solution_3),
        ("Add Pagination", solution_4),
        ("Build a Complete CRUD API", solution_5),
        ("Error Handling and Status Codes", solution_6),
    ]

    # Run exercises
    print("=" * 70)
    print("EXERCISES - Try these first!")
    print("=" * 70)
    for i, (title, func) in enumerate(exercises, 1):
        print(f"\n{'=' * 70}")
        print(f"EXERCISE {i}: {title}")
        print("=" * 70)
        func()

    # Run solutions
    print("\n\n" + "=" * 70)
    print("SOLUTIONS - Check your work!")
    print("=" * 70)
    for i, (title, func) in enumerate(solutions, 1):
        print(f"\n{'=' * 70}")
        print(f"SOLUTION {i}: {title}")
        print("=" * 70)
        func()
        print()
