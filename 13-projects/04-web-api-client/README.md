# Project 4: Web API Client

## What You'll Build

A command-line tool that fetches and displays data from a public web API. You'll build a weather lookup tool using the free Open-Meteo API (no API key required) that shows current weather for any city.

## Skills Practiced

- HTTP requests with the `requests` library
- JSON parsing and data extraction
- argparse for CLI interface
- Error handling (network errors, bad responses, missing data)
- String formatting for readable output

## Features to Implement

### Core (start here)
1. Accept a city name from the command line
2. Look up the city's coordinates using the Open-Meteo geocoding API
3. Fetch current weather data for those coordinates
4. Display temperature, wind speed, and weather description
5. Handle errors gracefully (city not found, network issues)

### Stretch Goals (once the core works)
- Add a `--forecast` flag to show multi-day forecast
- Add `--units` flag (metric/imperial)
- Cache results to avoid repeated API calls
- Support multiple cities in one command
- Add colored output based on temperature

## Example Session

```bash
$ python3 starter.py London
Weather for London, United Kingdom:
  Temperature:  12.3°C
  Wind speed:   15.2 km/h
  Condition:    Partly cloudy

$ python3 starter.py "New York"
Weather for New York, United States:
  Temperature:  8.1°C
  Wind speed:   22.4 km/h
  Condition:    Overcast

$ python3 starter.py Nowhereville
Error: City 'Nowhereville' not found.
```

## APIs Used

Both APIs are **free and require no API key**.

**Geocoding** (city name → coordinates):
```
https://geocoding-api.open-meteo.com/v1/search?name=London&count=1
```

**Weather** (coordinates → current weather):
```
https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.1&current_weather=true
```

## Hints

- `requests.get(url, params={...})` is cleaner than building URL strings manually
- Check `response.status_code` or use `response.raise_for_status()`
- The geocoding API returns a `results` list — take the first match
- Weather codes (0=clear, 1-3=cloudy, etc.) need to be mapped to descriptions
- Use `try/except requests.RequestException` for network errors
- Install requests with: `pip install requests`

## Files

- **`starter.py`** — skeleton code with function signatures and structure
- **`solution.py`** — complete working implementation
