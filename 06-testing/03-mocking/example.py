"""
Mocking — Example Code
========================

Run this file:
    python3 example.py

This file demonstrates how to use unittest.mock to isolate code from external
dependencies. We'll define realistic production code that depends on APIs,
databases, and the file system — then write tests that mock those dependencies.

All tests run via unittest when you execute this file.
"""

import json
import unittest
from datetime import datetime as real_datetime
from unittest.mock import Mock, MagicMock, patch, mock_open, call

# We keep a reference to the real datetime class so we can use it inside tests
# even after patching __main__.datetime. This is a common pattern!
datetime = real_datetime


# =============================================================================
# 1. Production code — things we want to test
# =============================================================================
# These functions simulate real-world code that depends on external services.
# In a real project, these would live in separate modules.

def fetch_user_from_api(user_id):
    """Simulate an HTTP call to get user data.

    In real life, this might use `requests.get(...)`. We're pretending
    it does that so we can show how to mock it.
    """
    # Imagine this hits https://api.example.com/users/{user_id}
    import requests
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()
    return response.json()


def get_user_greeting(user_id):
    """Build a greeting message for a user.

    This function depends on fetch_user_from_api — an external dependency.
    We don't want our test to make real HTTP calls, so we'll mock it.
    """
    user = fetch_user_from_api(user_id)
    return f"Hello, {user['name']}! You have {user['unread']} unread messages."


def read_config(filepath):
    """Read a key=value config file and return a dictionary.

    Depends on the file system — we'll mock open() to avoid needing
    a real file during testing.
    """
    config = {}
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if line and "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config


def get_time_greeting():
    """Return a greeting based on the current time of day.

    Depends on datetime.now() — impossible to test reliably without mocking
    because the output changes depending on when you run the test!
    """
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 17:
        return "Good afternoon!"
    else:
        return "Good evening!"


class UserRepository:
    """Simulates a database-backed user store.

    In real life, this would talk to PostgreSQL, MongoDB, etc.
    """

    def find_by_id(self, user_id):
        raise NotImplementedError("Would query the database")

    def save(self, user_data):
        raise NotImplementedError("Would insert/update in the database")


class UserService:
    """Business logic that depends on a UserRepository.

    This is a classic pattern: the service contains logic, the repository
    handles data access. We mock the repository to test the service.
    """

    def __init__(self, repository):
        self.repository = repository

    def get_display_name(self, user_id):
        user = self.repository.find_by_id(user_id)
        if user is None:
            return "Unknown User"
        return f"{user['first_name']} {user['last_name']}"

    def update_email(self, user_id, new_email):
        user = self.repository.find_by_id(user_id)
        if user is None:
            raise ValueError(f"User {user_id} not found")
        user["email"] = new_email
        self.repository.save(user)
        return user


# =============================================================================
# 2. Tests using Mock objects directly
# =============================================================================

class TestMockBasics(unittest.TestCase):
    """Demonstrates creating and using Mock objects by hand."""

    def test_mock_return_value(self):
        """Mock a function and control what it returns."""
        # Create a mock and tell it what to return
        mock_func = Mock()
        mock_func.return_value = 42

        # Call it — it returns our controlled value
        result = mock_func("any", "args", "at all")
        self.assertEqual(result, 42)

        # The mock recorded how it was called
        mock_func.assert_called_once_with("any", "args", "at all")

    def test_mock_method_return_value(self):
        """Mock an object's method."""
        mock_obj = Mock()
        mock_obj.calculate.return_value = 100

        # Call the mock method
        result = mock_obj.calculate(10, 20)
        self.assertEqual(result, 100)

        # Verify the method was called with the right args
        mock_obj.calculate.assert_called_once_with(10, 20)

    def test_mock_side_effect_exception(self):
        """Mock that raises an exception when called."""
        mock_func = Mock()
        mock_func.side_effect = ConnectionError("Network is down")

        # Calling the mock raises the exception
        with self.assertRaises(ConnectionError) as ctx:
            mock_func()
        self.assertIn("Network is down", str(ctx.exception))

    def test_mock_side_effect_sequence(self):
        """Mock that returns different values on each call."""
        mock_func = Mock()
        mock_func.side_effect = ["first", "second", "third"]

        self.assertEqual(mock_func(), "first")
        self.assertEqual(mock_func(), "second")
        self.assertEqual(mock_func(), "third")
        self.assertEqual(mock_func.call_count, 3)

    def test_mock_call_tracking(self):
        """Demonstrate all the ways to inspect mock calls."""
        mock_func = Mock()

        # Make several calls
        mock_func("hello")
        mock_func("world", count=2)
        mock_func("goodbye")

        # Total calls
        self.assertEqual(mock_func.call_count, 3)

        # All calls recorded in order
        expected_calls = [
            call("hello"),
            call("world", count=2),
            call("goodbye"),
        ]
        mock_func.assert_has_calls(expected_calls)

        # Last call
        mock_func.assert_called_with("goodbye")


# =============================================================================
# 3. Tests using @patch decorator
# =============================================================================

class TestPatchDecorator(unittest.TestCase):
    """Demonstrates @patch to replace real functions during tests."""

    @patch("__main__.fetch_user_from_api")
    def test_user_greeting(self, mock_fetch):
        """Patch the API call so we never hit the network."""
        # Tell the mock what to return
        mock_fetch.return_value = {"name": "Alice", "unread": 5}

        # Call the function under test — it uses our mock, not the real API
        result = get_user_greeting(42)

        # Assert on the result
        self.assertEqual(result, "Hello, Alice! You have 5 unread messages.")

        # Verify the mock was called correctly
        mock_fetch.assert_called_once_with(42)

    @patch("__main__.fetch_user_from_api")
    def test_user_greeting_different_data(self, mock_fetch):
        """Same function, different mock data — easy to test edge cases."""
        mock_fetch.return_value = {"name": "Bob", "unread": 0}

        result = get_user_greeting(99)

        self.assertEqual(result, "Hello, Bob! You have 0 unread messages.")
        mock_fetch.assert_called_once_with(99)


# =============================================================================
# 4. Tests using patch as a context manager
# =============================================================================

class TestPatchContextManager(unittest.TestCase):
    """Demonstrates using `with patch(...)` instead of the decorator."""

    def test_greeting_with_context_manager(self):
        """Same test as above, but using the `with` syntax."""
        with patch("__main__.fetch_user_from_api") as mock_fetch:
            mock_fetch.return_value = {"name": "Charlie", "unread": 12}

            result = get_user_greeting(7)

            self.assertEqual(result, "Hello, Charlie! You have 12 unread messages.")
            mock_fetch.assert_called_once_with(7)

        # Outside the `with` block, fetch_user_from_api is restored to normal


# =============================================================================
# 5. Mocking datetime — testing time-dependent code
# =============================================================================

class TestTimeGreeting(unittest.TestCase):
    """Demonstrates mocking datetime.now() to control time in tests."""

    @patch("__main__.datetime")
    def test_morning_greeting(self, mock_dt):
        """Simulate running the code at 9 AM."""
        # Use real_datetime to create the object — __main__.datetime is mocked!
        mock_dt.now.return_value = real_datetime(2025, 6, 15, 9, 0, 0)

        result = get_time_greeting()
        self.assertEqual(result, "Good morning!")

    @patch("__main__.datetime")
    def test_afternoon_greeting(self, mock_dt):
        """Simulate running the code at 2 PM."""
        mock_dt.now.return_value = real_datetime(2025, 6, 15, 14, 0, 0)

        result = get_time_greeting()
        self.assertEqual(result, "Good afternoon!")

    @patch("__main__.datetime")
    def test_evening_greeting(self, mock_dt):
        """Simulate running the code at 8 PM."""
        mock_dt.now.return_value = real_datetime(2025, 6, 15, 20, 0, 0)

        result = get_time_greeting()
        self.assertEqual(result, "Good evening!")


# =============================================================================
# 6. Mocking file operations with mock_open
# =============================================================================

class TestReadConfig(unittest.TestCase):
    """Demonstrates mocking open() to test file-reading code."""

    def test_read_simple_config(self):
        """Mock a config file without needing a real file on disk."""
        fake_file_content = "host=localhost\nport=5432\ndb_name=myapp\n"

        with patch("builtins.open", mock_open(read_data=fake_file_content)):
            config = read_config("fake_path.conf")

        self.assertEqual(config["host"], "localhost")
        self.assertEqual(config["port"], "5432")
        self.assertEqual(config["db_name"], "myapp")

    def test_read_config_with_empty_lines(self):
        """Config files often have blank lines and spacing."""
        fake_file_content = "\nname = Alice\n\nrole = admin\n\n"

        with patch("builtins.open", mock_open(read_data=fake_file_content)):
            config = read_config("whatever.conf")

        self.assertEqual(config["name"], "Alice")
        self.assertEqual(config["role"], "admin")


# =============================================================================
# 7. Mocking with spec — catching typos and interface mismatches
# =============================================================================

class TestUserService(unittest.TestCase):
    """Demonstrates mocking a dependency with spec for safety."""

    def test_get_display_name(self):
        """Mock the repository to test service logic."""
        # Create a mock that matches UserRepository's interface
        mock_repo = Mock(spec=UserRepository)
        mock_repo.find_by_id.return_value = {
            "first_name": "Alice",
            "last_name": "Smith",
        }

        # Inject the mock into the service
        service = UserService(mock_repo)
        result = service.get_display_name(42)

        self.assertEqual(result, "Alice Smith")
        mock_repo.find_by_id.assert_called_once_with(42)

    def test_get_display_name_user_not_found(self):
        """Test the 'not found' path."""
        mock_repo = Mock(spec=UserRepository)
        mock_repo.find_by_id.return_value = None

        service = UserService(mock_repo)
        result = service.get_display_name(999)

        self.assertEqual(result, "Unknown User")

    def test_update_email(self):
        """Test updating a user's email — verify save was called."""
        mock_repo = Mock(spec=UserRepository)
        mock_repo.find_by_id.return_value = {
            "first_name": "Bob",
            "last_name": "Jones",
            "email": "old@example.com",
        }

        service = UserService(mock_repo)
        updated_user = service.update_email(1, "new@example.com")

        # Verify the email was changed
        self.assertEqual(updated_user["email"], "new@example.com")

        # Verify save was called with the updated user data
        mock_repo.save.assert_called_once()
        saved_user = mock_repo.save.call_args[0][0]
        self.assertEqual(saved_user["email"], "new@example.com")

    def test_update_email_user_not_found(self):
        """Test that updating a nonexistent user raises an error."""
        mock_repo = Mock(spec=UserRepository)
        mock_repo.find_by_id.return_value = None

        service = UserService(mock_repo)

        with self.assertRaises(ValueError):
            service.update_email(999, "nope@example.com")

        # save should NOT have been called
        mock_repo.save.assert_not_called()

    def test_spec_catches_typos(self):
        """Demonstrate that spec prevents accessing nonexistent methods."""
        mock_repo = Mock(spec=UserRepository)

        # This works — find_by_id exists on UserRepository
        mock_repo.find_by_id(1)

        # This would raise AttributeError because find_by_name doesn't exist:
        # mock_repo.find_by_name("Alice")  # AttributeError!
        with self.assertRaises(AttributeError):
            mock_repo.find_by_name("Alice")


# =============================================================================
# 8. MagicMock — mocking objects that use magic methods
# =============================================================================

class TestMagicMock(unittest.TestCase):
    """Demonstrates MagicMock for objects that use __len__, __iter__, etc."""

    def test_magic_mock_length(self):
        """MagicMock supports len() out of the box."""
        mock_list = MagicMock()
        mock_list.__len__.return_value = 3

        self.assertEqual(len(mock_list), 3)

    def test_magic_mock_iteration(self):
        """MagicMock supports iteration."""
        mock_collection = MagicMock()
        mock_collection.__iter__.return_value = iter(["a", "b", "c"])

        result = list(mock_collection)
        self.assertEqual(result, ["a", "b", "c"])

    def test_magic_mock_context_manager(self):
        """MagicMock supports the `with` statement."""
        mock_cm = MagicMock()
        mock_cm.__enter__.return_value = "fake resource"

        with mock_cm as resource:
            self.assertEqual(resource, "fake resource")


# =============================================================================
# Run all the tests!
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  Mocking — Example Tests")
    print("  Running all demonstrations with unittest...")
    print("=" * 60)
    print()

    # Run with verbosity=2 so you can see each test name and result
    unittest.main(verbosity=2)
