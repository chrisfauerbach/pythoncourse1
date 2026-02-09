"""
Mocking — Exercises
====================

Practice problems to test your understanding of mocking.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

Each exercise gives you some production code that depends on something external
(an API, a file, the clock, etc.). Your job is to write tests that mock those
dependencies so the tests are fast, reliable, and don't touch the real world.
"""

import json
import unittest
import requests
from datetime import datetime as real_datetime
from unittest.mock import Mock, MagicMock, patch, mock_open, call

# We keep a reference to the real datetime class so we can use it inside tests
# even after patching __main__.datetime. This is a common pattern!
datetime = real_datetime


# =============================================================================
# Production code used by the exercises
# =============================================================================
# Don't modify this section — these are the functions/classes you'll be testing.

def fetch_stock_price(symbol):
    """Calls an external API to get the current stock price.
    In real life, this hits a financial data service.
    """
    response = requests.get(f"https://api.stocks.example.com/price/{symbol}")
    data = response.json()
    return data["price"]


def calculate_portfolio_value(symbols):
    """Calculate total value of a portfolio by looking up each stock price.
    Depends on fetch_stock_price for each symbol.
    """
    total = 0.0
    for symbol in symbols:
        price = fetch_stock_price(symbol)
        total += price
    return total


def get_weather_report(city):
    """Calls a weather API and returns a formatted report.
    In real life, this would use requests to hit a weather service.
    """
    response = requests.get(
        f"https://api.weather.example.com/current?city={city}"
    )
    if response.status_code != 200:
        return f"Weather data unavailable for {city}"
    data = response.json()
    return f"{city}: {data['temp']}°C, {data['condition']}"


def get_day_type():
    """Returns whether today is a weekday or weekend.
    Depends on datetime.now() — changes depending on when you run it!
    """
    day = datetime.now().weekday()  # 0=Monday, 6=Sunday
    if day < 5:
        return "weekday"
    return "weekend"


def generate_daily_message():
    """Generates a message based on day type and current hour.
    Depends on datetime.now() for both the day and the hour.
    """
    now = datetime.now()
    day_name = now.strftime("%A")
    hour = now.hour

    if hour < 12:
        time_of_day = "morning"
    elif hour < 17:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    if now.weekday() < 5:
        return f"Good {time_of_day}! Happy {day_name}. Time to be productive!"
    return f"Good {time_of_day}! Happy {day_name}. Enjoy your weekend!"


def fetch_data_with_retry(url, max_retries=3):
    """Tries to fetch data from a URL with retries on failure.
    Depends on requests.get — we'll use side_effect to simulate flaky APIs.
    """
    last_error = None
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            last_error = e
    raise last_error


def read_user_settings(filepath):
    """Reads a JSON settings file and returns it as a dictionary.
    Depends on the file system — we'll mock open() to avoid real files.
    """
    with open(filepath, "r") as f:
        data = json.load(f)
    # Apply defaults for missing keys
    data.setdefault("theme", "light")
    data.setdefault("language", "en")
    data.setdefault("notifications", True)
    return data


class EmailSender:
    """Sends emails. In real life, connects to an SMTP server."""
    def send(self, to, subject, body):
        raise NotImplementedError("Would connect to SMTP server")


class SMSSender:
    """Sends SMS messages. In real life, calls Twilio or similar."""
    def send(self, phone_number, message):
        raise NotImplementedError("Would call SMS API")


class NotificationService:
    """Sends notifications via email and/or SMS.
    Depends on EmailSender and SMSSender — perfect for mocking.
    """

    def __init__(self, email_sender, sms_sender):
        self.email_sender = email_sender
        self.sms_sender = sms_sender

    def notify_user(self, user, message):
        """Send notification to a user via their preferred channels.
        user dict has: name, email, phone, preferences (list of 'email'/'sms')
        """
        results = []
        if "email" in user.get("preferences", []):
            self.email_sender.send(
                user["email"],
                f"Notification for {user['name']}",
                message
            )
            results.append("email")
        if "sms" in user.get("preferences", []):
            self.sms_sender.send(user["phone"], message)
            results.append("sms")
        return results

    def broadcast(self, users, message):
        """Send a notification to multiple users. Returns count of notifications sent."""
        total = 0
        for user in users:
            channels = self.notify_user(user, message)
            total += len(channels)
        return total


# =============================================================================
# Exercise 1: Mock a function's return value and verify it was called
#
# Write a test for calculate_portfolio_value. Mock fetch_stock_price so it
# returns controlled prices. Verify:
#   - The total is calculated correctly
#   - fetch_stock_price was called once for each symbol
#   - fetch_stock_price was called with the right arguments
#
# Hint: Use @patch to mock __main__.fetch_stock_price
# =============================================================================

class TestExercise1(unittest.TestCase):
    # YOUR CODE HERE — write test method(s)
    pass


# =============================================================================
# Exercise 2: Use @patch to mock an API call in a weather service
#
# Write tests for get_weather_report. Mock requests.get to return:
#   a) A successful response (status_code=200, json with temp and condition)
#   b) A failed response (status_code=500)
#
# Verify the function returns the correct formatted string for success
# and the "unavailable" message for failure.
#
# Hint: You need to mock the return value of requests.get(), which is a
# response object. That response object needs .status_code and .json() method.
# Patch "__main__.requests.get" since requests is imported inside the function.
# =============================================================================

class TestExercise2(unittest.TestCase):
    # YOUR CODE HERE — write test method(s)
    pass


# =============================================================================
# Exercise 3: Mock datetime.now() to test time-dependent code
#
# Write tests for get_day_type and generate_daily_message.
#   a) Test get_day_type returns "weekday" for a Wednesday
#   b) Test get_day_type returns "weekend" for a Saturday
#   c) Test generate_daily_message for a Monday morning
#   d) Test generate_daily_message for a Sunday evening
#
# Hint: Patch "__main__.datetime" and set mock_dt.now.return_value to a
# specific datetime object. Use real_datetime(...) (defined at the top of this
# file) to create the object — since __main__.datetime is mocked during the test!
# =============================================================================

class TestExercise3(unittest.TestCase):
    # YOUR CODE HERE — write test method(s)
    pass


# =============================================================================
# Exercise 4: Use side_effect to simulate a sequence of API responses
#
# Write tests for fetch_data_with_retry:
#   a) First call fails, second call succeeds — verify data is returned
#   b) All 3 calls fail — verify the exception is raised
#   c) First call succeeds immediately — verify only 1 call was made
#
# Hint: Use side_effect with a list. For failures, put exception instances
# in the list. For success, put a Mock with .json() and .raise_for_status().
# =============================================================================

class TestExercise4(unittest.TestCase):
    # YOUR CODE HERE — write test method(s)
    pass


# =============================================================================
# Exercise 5: Mock file operations to test a config reader
#
# Write tests for read_user_settings:
#   a) File contains {"theme": "dark", "language": "fr"} — verify defaults
#      are applied for "notifications" but "theme" and "language" keep their values
#   b) File contains {} (empty JSON object) — verify all defaults are applied
#   c) File contains full settings — verify nothing is overwritten
#
# Hint: Use mock_open with read_data set to a JSON string.
#       json.load reads from the file handle, so mock_open works perfectly.
# =============================================================================

class TestExercise5(unittest.TestCase):
    # YOUR CODE HERE — write test method(s)
    pass


# =============================================================================
# Exercise 6: Test NotificationService with mocked EmailSender and SMSSender
#
# Write tests for NotificationService:
#   a) User with email preference only — verify email sent, SMS not sent
#   b) User with SMS preference only — verify SMS sent, email not sent
#   c) User with both preferences — verify both sent with correct arguments
#   d) User with no preferences — verify nothing sent
#   e) Test broadcast with 3 users — verify correct total count
#
# Hint: Create Mock(spec=EmailSender) and Mock(spec=SMSSender) and pass
# them to NotificationService. Then check .send was called with right args.
# =============================================================================

class TestExercise6(unittest.TestCase):
    # YOUR CODE HERE — write test method(s)
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

class Solution1(unittest.TestCase):

    @patch("__main__.fetch_stock_price")
    def test_portfolio_value(self, mock_fetch):
        # Make the mock return different prices for different symbols
        mock_fetch.side_effect = lambda symbol: {
            "AAPL": 150.0,
            "GOOG": 2800.0,
            "TSLA": 900.0,
        }[symbol]

        result = calculate_portfolio_value(["AAPL", "GOOG", "TSLA"])

        self.assertEqual(result, 3850.0)
        self.assertEqual(mock_fetch.call_count, 3)
        mock_fetch.assert_any_call("AAPL")
        mock_fetch.assert_any_call("GOOG")
        mock_fetch.assert_any_call("TSLA")

    @patch("__main__.fetch_stock_price")
    def test_empty_portfolio(self, mock_fetch):
        result = calculate_portfolio_value([])

        self.assertEqual(result, 0.0)
        mock_fetch.assert_not_called()


class Solution2(unittest.TestCase):

    @patch("__main__.requests.get")
    def test_successful_weather_report(self, mock_get):
        # Set up the mock response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"temp": 22, "condition": "Sunny"}
        mock_get.return_value = mock_response

        result = get_weather_report("London")

        self.assertEqual(result, "London: 22°C, Sunny")
        mock_get.assert_called_once_with(
            "https://api.weather.example.com/current?city=London"
        )

    @patch("__main__.requests.get")
    def test_failed_weather_report(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        result = get_weather_report("Unknown")

        self.assertEqual(result, "Weather data unavailable for Unknown")


class Solution3(unittest.TestCase):

    @patch("__main__.datetime")
    def test_weekday(self, mock_dt):
        # Wednesday = weekday (weekday() returns 2)
        # Use real_datetime to create the object — __main__.datetime is mocked!
        mock_dt.now.return_value = real_datetime(2025, 6, 11, 10, 0, 0)  # Wednesday

        result = get_day_type()
        self.assertEqual(result, "weekday")

    @patch("__main__.datetime")
    def test_weekend(self, mock_dt):
        # Saturday (weekday() returns 5)
        mock_dt.now.return_value = real_datetime(2025, 6, 14, 10, 0, 0)  # Saturday

        result = get_day_type()
        self.assertEqual(result, "weekend")

    @patch("__main__.datetime")
    def test_monday_morning_message(self, mock_dt):
        mock_dt.now.return_value = real_datetime(2025, 6, 9, 9, 0, 0)  # Monday 9 AM

        result = generate_daily_message()
        self.assertEqual(
            result,
            "Good morning! Happy Monday. Time to be productive!"
        )

    @patch("__main__.datetime")
    def test_sunday_evening_message(self, mock_dt):
        mock_dt.now.return_value = real_datetime(2025, 6, 15, 19, 0, 0)  # Sunday 7 PM

        result = generate_daily_message()
        self.assertEqual(
            result,
            "Good evening! Happy Sunday. Enjoy your weekend!"
        )


class Solution4(unittest.TestCase):

    @patch("__main__.requests.get")
    def test_retry_then_success(self, mock_get):
        # First call raises, second call succeeds
        fail_response = Mock()
        fail_response.raise_for_status.side_effect = requests.RequestException("timeout")

        success_response = Mock()
        success_response.raise_for_status.return_value = None
        success_response.json.return_value = {"data": "success"}

        mock_get.side_effect = [fail_response, success_response]

        result = fetch_data_with_retry("https://api.example.com/data")

        self.assertEqual(result, {"data": "success"})
        self.assertEqual(mock_get.call_count, 2)

    @patch("__main__.requests.get")
    def test_all_retries_fail(self, mock_get):
        fail_response = Mock()
        fail_response.raise_for_status.side_effect = requests.RequestException("timeout")

        mock_get.return_value = fail_response

        with self.assertRaises(requests.RequestException):
            fetch_data_with_retry("https://api.example.com/data", max_retries=3)

        self.assertEqual(mock_get.call_count, 3)

    @patch("__main__.requests.get")
    def test_first_call_succeeds(self, mock_get):
        success_response = Mock()
        success_response.raise_for_status.return_value = None
        success_response.json.return_value = {"data": "instant"}

        mock_get.return_value = success_response

        result = fetch_data_with_retry("https://api.example.com/data")

        self.assertEqual(result, {"data": "instant"})
        self.assertEqual(mock_get.call_count, 1)


class Solution5(unittest.TestCase):

    def test_partial_settings(self):
        fake_json = '{"theme": "dark", "language": "fr"}'

        with patch("builtins.open", mock_open(read_data=fake_json)):
            result = read_user_settings("settings.json")

        self.assertEqual(result["theme"], "dark")
        self.assertEqual(result["language"], "fr")
        self.assertTrue(result["notifications"])  # default applied

    def test_empty_settings(self):
        fake_json = '{}'

        with patch("builtins.open", mock_open(read_data=fake_json)):
            result = read_user_settings("settings.json")

        self.assertEqual(result["theme"], "light")       # default
        self.assertEqual(result["language"], "en")        # default
        self.assertTrue(result["notifications"])          # default

    def test_full_settings(self):
        fake_json = '{"theme": "dark", "language": "de", "notifications": false}'

        with patch("builtins.open", mock_open(read_data=fake_json)):
            result = read_user_settings("settings.json")

        self.assertEqual(result["theme"], "dark")
        self.assertEqual(result["language"], "de")
        self.assertFalse(result["notifications"])  # not overwritten


class Solution6(unittest.TestCase):

    def _make_service(self):
        """Helper to create service with mocked senders."""
        mock_email = Mock(spec=EmailSender)
        mock_sms = Mock(spec=SMSSender)
        service = NotificationService(mock_email, mock_sms)
        return service, mock_email, mock_sms

    def test_email_only(self):
        service, mock_email, mock_sms = self._make_service()
        user = {
            "name": "Alice",
            "email": "alice@example.com",
            "phone": "+1234567890",
            "preferences": ["email"],
        }

        result = service.notify_user(user, "Hello!")

        self.assertEqual(result, ["email"])
        mock_email.send.assert_called_once_with(
            "alice@example.com", "Notification for Alice", "Hello!"
        )
        mock_sms.send.assert_not_called()

    def test_sms_only(self):
        service, mock_email, mock_sms = self._make_service()
        user = {
            "name": "Bob",
            "email": "bob@example.com",
            "phone": "+9876543210",
            "preferences": ["sms"],
        }

        result = service.notify_user(user, "Hi Bob!")

        self.assertEqual(result, ["sms"])
        mock_email.send.assert_not_called()
        mock_sms.send.assert_called_once_with("+9876543210", "Hi Bob!")

    def test_both_channels(self):
        service, mock_email, mock_sms = self._make_service()
        user = {
            "name": "Charlie",
            "email": "charlie@example.com",
            "phone": "+5555555555",
            "preferences": ["email", "sms"],
        }

        result = service.notify_user(user, "Important!")

        self.assertEqual(result, ["email", "sms"])
        mock_email.send.assert_called_once_with(
            "charlie@example.com", "Notification for Charlie", "Important!"
        )
        mock_sms.send.assert_called_once_with("+5555555555", "Important!")

    def test_no_preferences(self):
        service, mock_email, mock_sms = self._make_service()
        user = {
            "name": "Dave",
            "email": "dave@example.com",
            "phone": "+1111111111",
            "preferences": [],
        }

        result = service.notify_user(user, "You won't see this")

        self.assertEqual(result, [])
        mock_email.send.assert_not_called()
        mock_sms.send.assert_not_called()

    def test_broadcast(self):
        service, mock_email, mock_sms = self._make_service()
        users = [
            {"name": "A", "email": "a@test.com", "phone": "+1", "preferences": ["email"]},
            {"name": "B", "email": "b@test.com", "phone": "+2", "preferences": ["sms"]},
            {"name": "C", "email": "c@test.com", "phone": "+3", "preferences": ["email", "sms"]},
        ]

        total = service.broadcast(users, "Big announcement!")

        # A=1 (email) + B=1 (sms) + C=2 (email+sms) = 4
        self.assertEqual(total, 4)
        self.assertEqual(mock_email.send.call_count, 2)  # A and C
        self.assertEqual(mock_sms.send.call_count, 2)    # B and C


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    # Run solution tests to verify they pass, and exercise stubs to show structure
    print("=" * 60)
    print("  Mocking — Exercises")
    print("  Running solution tests to verify they work...")
    print("=" * 60)
    print()

    # Build a test suite with just the solutions (and empty exercise stubs)
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add exercise classes (they're empty, so they'll show 0 tests)
    suite.addTests(loader.loadTestsFromTestCase(TestExercise1))
    suite.addTests(loader.loadTestsFromTestCase(TestExercise2))
    suite.addTests(loader.loadTestsFromTestCase(TestExercise3))
    suite.addTests(loader.loadTestsFromTestCase(TestExercise4))
    suite.addTests(loader.loadTestsFromTestCase(TestExercise5))
    suite.addTests(loader.loadTestsFromTestCase(TestExercise6))

    # Add solution classes
    suite.addTests(loader.loadTestsFromTestCase(Solution1))
    suite.addTests(loader.loadTestsFromTestCase(Solution2))
    suite.addTests(loader.loadTestsFromTestCase(Solution3))
    suite.addTests(loader.loadTestsFromTestCase(Solution4))
    suite.addTests(loader.loadTestsFromTestCase(Solution5))
    suite.addTests(loader.loadTestsFromTestCase(Solution6))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print()
    if result.wasSuccessful():
        print("-" * 60)
        print("All solution tests passed!")
        print("Now try filling in the exercise classes yourself.")
        print("-" * 60)
    else:
        print("-" * 60)
        print("Some tests failed — check the output above.")
        print("-" * 60)
