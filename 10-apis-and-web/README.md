# Section 10: APIs & Web

The modern world runs on APIs. This section teaches you how to talk to web services, pull data from the internet, and even scrape websites when no API is available. We'll also cover async HTTP for when you need speed.

**Note:** This section requires installing third-party packages. Each lesson includes setup instructions.

## Lessons

| # | Lesson | Description |
|---|--------|-------------|
| 01 | [Requests Library](01-requests-library/) | Making HTTP requests the easy way |
| 02 | [REST APIs](02-rest-apis/) | Understanding and consuming RESTful services |
| 03 | [Web Scraping](03-web-scraping/) | Extracting data from web pages with BeautifulSoup |
| 04 | [Async API Calls](04-async-api-calls/) | High-performance concurrent HTTP with aiohttp |

## Setup

```bash
pip install requests beautifulsoup4 aiohttp
```

## What You'll Be Able to Do After This Section

- Make GET/POST requests to any API
- Parse JSON responses and handle errors
- Scrape data from web pages
- Make many API calls concurrently with async

## Prerequisites

- [Section 03: File I/O](../03-file-io/) — especially JSON
- [Section 05: Intermediate](../05-intermediate/) — error handling
- [Section 07: Async Python](../07-async-python/) — for the async lesson
