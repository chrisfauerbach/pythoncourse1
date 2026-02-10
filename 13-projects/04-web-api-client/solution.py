"""
Web API Client — Solution
============================

Run this file:
    python3 solution.py London
    python3 solution.py "New York"
    python3 solution.py Tokyo

Requires the requests library:
    pip install requests

Fetches current weather for any city using the free Open-Meteo API
(no API key required).
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

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def geocode_city(city_name):
    """Look up a city's coordinates using the Open-Meteo geocoding API."""
    try:
        response = requests.get(GEOCODE_URL, params={
            "name": city_name,
            "count": 1,
        }, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "results" not in data or not data["results"]:
            return None

        result = data["results"][0]
        return {
            "name": result["name"],
            "country": result.get("country", "Unknown"),
            "latitude": result["latitude"],
            "longitude": result["longitude"],
        }

    except requests.RequestException as e:
        print(f"Error looking up city: {e}")
        return None


def get_weather(latitude, longitude):
    """Fetch current weather for the given coordinates."""
    try:
        response = requests.get(WEATHER_URL, params={
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
        }, timeout=10)
        response.raise_for_status()
        data = response.json()

        return data.get("current_weather")

    except requests.RequestException as e:
        print(f"Error fetching weather: {e}")
        return None


def format_weather(city_info, weather):
    """Format weather data into a readable string."""
    condition = WEATHER_CODES.get(weather["weathercode"], "Unknown")
    temp = weather["temperature"]
    wind = weather["windspeed"]

    lines = [
        f"Weather for {city_info['name']}, {city_info['country']}:",
        f"  Temperature:  {temp}\u00b0C",
        f"  Wind speed:   {wind} km/h",
        f"  Condition:    {condition}",
    ]

    return "\n".join(lines)


def main():
    """Parse arguments and display weather for the given city."""
    parser = argparse.ArgumentParser(
        description="Get current weather for any city",
        epilog="Example: %(prog)s London"
    )
    parser.add_argument("city", help="City name to look up")

    args = parser.parse_args()

    # Step 1: Look up the city
    city_info = geocode_city(args.city)
    if city_info is None:
        print(f"Error: City '{args.city}' not found.")
        sys.exit(1)

    # Step 2: Get the weather
    weather = get_weather(city_info["latitude"], city_info["longitude"])
    if weather is None:
        print("Error: Could not fetch weather data.")
        sys.exit(1)

    # Step 3: Display it
    print(format_weather(city_info, weather))


if __name__ == "__main__":
    main()
