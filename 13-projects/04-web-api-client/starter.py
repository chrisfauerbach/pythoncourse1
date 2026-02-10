"""
Web API Client — Starter Code
================================

Run this file:
    python3 starter.py London
    python3 starter.py "New York"
    python3 starter.py Tokyo --units imperial

Requires the requests library:
    pip install requests

Fill in the functions below to build a weather lookup CLI tool.
Start with geocode_city(), then get_weather(), then wire it up in main().
"""

import argparse
import sys

try:
    import requests
except ImportError:
    print("This project requires the 'requests' library.")
    print("Install it with: pip install requests")
    sys.exit(0)


# Weather code descriptions from the Open-Meteo API docs
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Foggy",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def geocode_city(city_name):
    """Look up a city's coordinates using the Open-Meteo geocoding API.

    API: https://geocoding-api.open-meteo.com/v1/search?name=London&count=1

    Args:
        city_name: Name of the city to look up.

    Returns:
        A dict with 'name', 'country', 'latitude', 'longitude' keys,
        or None if the city wasn't found.
    """
    # YOUR CODE HERE
    # 1. Make a GET request to the geocoding API
    # 2. Parse the JSON response
    # 3. If 'results' is in the response, return the first match
    # 4. Return None if not found
    pass


def get_weather(latitude, longitude):
    """Fetch current weather for the given coordinates.

    API: https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.1&current_weather=true

    Args:
        latitude: Latitude of the location.
        longitude: Longitude of the location.

    Returns:
        A dict with 'temperature', 'windspeed', 'weathercode' keys,
        or None if the request failed.
    """
    # YOUR CODE HERE
    # 1. Make a GET request to the weather API
    # 2. Parse the JSON response
    # 3. Return the 'current_weather' dict
    pass


def format_weather(city_info, weather):
    """Format weather data into a readable string.

    Args:
        city_info: Dict from geocode_city() with 'name' and 'country'.
        weather: Dict from get_weather() with 'temperature', 'windspeed', 'weathercode'.

    Returns:
        A formatted multi-line string.
    """
    # YOUR CODE HERE
    # Use the WEATHER_CODES dict to look up the weather description
    # Format it nicely with aligned labels
    pass


def main():
    """Parse arguments and display weather for the given city.

    Arguments:
        city (positional) — City name to look up
    """
    # YOUR CODE HERE
    # 1. Set up argparse with a 'city' argument
    # 2. Call geocode_city() — handle city not found
    # 3. Call get_weather() — handle API errors
    # 4. Call format_weather() and print the result
    pass


if __name__ == "__main__":
    main()
