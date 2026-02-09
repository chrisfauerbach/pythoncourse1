# Web Scraping

## Objective

Learn how to extract data from HTML web pages using Python's built-in tools, understand when web scraping is appropriate, and follow ethical scraping practices.

## Concepts Covered

- What web scraping is and when to use it
- HTML structure basics (tags, attributes, nesting)
- Python's built-in `html.parser` module
- Parsing strategies (finding tags, extracting attributes, getting text)
- Pattern matching with regex for simple extraction tasks
- Ethical scraping considerations (robots.txt, rate limiting, terms of service)
- Alternative libraries (BeautifulSoup, Scrapy) for real-world projects

## Prerequisites

- [Working with Files](../../05-file-handling/01-reading-and-writing/)
- [Regular Expressions](../../04-functions-modules/03-regular-expressions/)
- [Requests Library](../01-requests-library/) — helpful for real-world scraping

## Lesson

### What Is Web Scraping?

Web scraping is the process of **automatically extracting data from websites**. Instead of manually copying and pasting information, you write a program that:

1. Fetches HTML content (from a file, string, or web request)
2. Parses the HTML structure
3. Extracts the specific data you need
4. Processes and stores that data

Common use cases:
- Collecting product prices from e-commerce sites
- Aggregating news articles or blog posts
- Gathering research data from public websites
- Monitoring changes to web pages
- Building datasets for analysis or machine learning

### When Should You Use Web Scraping?

**Use web scraping when:**
- No API is available for the data you need
- The API is too limited or expensive
- You need public data that's only available via HTML

**DON'T use web scraping when:**
- An API is available — always prefer the official API!
- The website's Terms of Service prohibit scraping
- You'd be scraping private/authenticated content without permission
- You'd be causing excessive load on a server

### HTML Basics

HTML (HyperText Markup Language) is the backbone of web pages. It's made up of **tags** that define the structure and content.

#### Tags

Tags are enclosed in angle brackets. Most come in pairs (opening and closing):

```html
<p>This is a paragraph.</p>
<a href="https://example.com">This is a link</a>
<h1>This is a heading</h1>
```

Some tags are self-closing:

```html
<img src="image.jpg" alt="Description">
<br>
<hr>
```

#### Attributes

Tags can have **attributes** that provide additional information:

```html
<a href="https://example.com" class="external">Link</a>
<div id="main-content" class="container">Content here</div>
<img src="photo.jpg" alt="A photo" width="500">
```

Common attributes:
- `href` — the URL for links (`<a>` tags)
- `src` — the source for images, scripts, etc.
- `class` — CSS class name(s) for styling
- `id` — unique identifier for an element
- `alt` — alternative text for images

#### Nesting

HTML elements can be nested inside each other:

```html
<div class="article">
    <h2>Article Title</h2>
    <p>First paragraph with a <a href="#">link</a>.</p>
    <p>Second paragraph.</p>
</div>
```

This creates a tree structure (the "DOM" — Document Object Model), which is what we navigate when scraping.

### Python's Built-in HTML Parser

Python's standard library includes `html.parser.HTMLParser`, a basic but functional HTML parser. It's perfect for learning and simple tasks.

#### How It Works

You create a subclass of `HTMLParser` and override methods that get called when the parser encounters different parts of the HTML:

```python
from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start tag: {tag}")
        for attr in attrs:
            print(f"  Attribute: {attr[0]} = {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End tag: {tag}")

    def handle_data(self, data):
        print(f"Data: {data.strip()}")

parser = MyParser()
parser.feed("<p>Hello <b>world</b>!</p>")
```

This is low-level and verbose, but it gives you complete control.

#### A More Practical Approach

For most scraping tasks, you'll want to **build up data structures** as you parse:

```python
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.links.append(value)

html = '<a href="/page1">Link 1</a> <a href="/page2">Link 2</a>'
parser = LinkExtractor()
parser.feed(html)
print(parser.links)  # ['/page1', '/page2']
```

### Alternative: BeautifulSoup

For real-world projects, most developers use **BeautifulSoup** (via the `beautifulsoup4` package). It's much more user-friendly:

```python
# This requires: pip install beautifulsoup4
# from bs4 import BeautifulSoup
#
# html = "<p>Hello <b>world</b>!</p>"
# soup = BeautifulSoup(html, 'html.parser')
#
# # Find elements
# p_tag = soup.find('p')
# print(p_tag.text)  # "Hello world!"
#
# # Find all links
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))
```

We'll show BeautifulSoup examples in comments throughout this lesson, but we'll focus on the standard library for the exercises.

### Parsing Strategies

#### 1. Extract Links

Find all `<a>` tags and get their `href` attributes:

```python
from html.parser import HTMLParser

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.links.append(value)
```

#### 2. Extract Text Content

Capture all text data, ignoring tags:

```python
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        stripped = data.strip()
        if stripped:
            self.text.append(stripped)
```

#### 3. Find Elements by Tag and Attribute

Only extract data from specific elements:

```python
class ProductPriceExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.prices = []
        self.in_price_tag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for attr, value in attrs:
                if attr == 'class' and value == 'price':
                    self.in_price_tag = True

    def handle_endtag(self, tag):
        if tag == 'span':
            self.in_price_tag = False

    def handle_data(self, data):
        if self.in_price_tag:
            self.prices.append(data.strip())
```

#### 4. Parse Tables

Extract rows and columns from HTML tables:

```python
class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.current_row = []
        self.in_cell = False
        self.cell_data = []

    def handle_starttag(self, tag, attrs):
        if tag in ('td', 'th'):
            self.in_cell = True
            self.cell_data = []

    def handle_endtag(self, tag):
        if tag in ('td', 'th'):
            self.in_cell = False
            self.current_row.append(''.join(self.cell_data).strip())
        elif tag == 'tr':
            if self.current_row:
                self.rows.append(self.current_row)
                self.current_row = []

    def handle_data(self, data):
        if self.in_cell:
            self.cell_data.append(data)
```

### Using Regex as a Supplement

For simple patterns, regex can complement HTML parsing:

```python
import re

# Extract email addresses from HTML
html = "<p>Contact: user@example.com or admin@test.com</p>"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html)
print(emails)  # ['user@example.com', 'admin@test.com']

# Extract prices
html = "<div>Price: $29.99</div><div>Was: $49.99</div>"
prices = re.findall(r'\$(\d+\.\d{2})', html)
print(prices)  # ['29.99', '49.99']
```

**Warning:** Don't use regex alone to parse complex HTML! Regex can't handle nested structures properly. Use it for **simple patterns** after you've already extracted the relevant section.

### Ethical Scraping

Just because you *can* scrape a website doesn't mean you *should*. Follow these guidelines:

#### 1. Check robots.txt

Most websites have a `/robots.txt` file that specifies which parts of the site can be scraped:

```
User-agent: *
Disallow: /admin/
Disallow: /private/
Allow: /public/
```

Respect these rules. If you're disallowed, don't scrape.

#### 2. Read the Terms of Service

Many websites explicitly prohibit scraping in their Terms of Service. Violating these terms could get you banned or even lead to legal issues.

#### 3. Rate Limiting

Don't hammer a server with requests. Add delays between requests:

```python
import time

# In a real scraping loop:
# for url in urls:
#     fetch_and_parse(url)
#     time.sleep(1)  # Wait 1 second between requests
```

A good rule of thumb: no more than 1 request per second, and much slower for small sites.

#### 4. Identify Yourself

Use a proper User-Agent header when making requests:

```python
# With the requests library:
# headers = {
#     'User-Agent': 'MyBot/1.0 (contact@example.com)'
# }
# response = requests.get(url, headers=headers)
```

This lets site owners contact you if there's an issue.

#### 5. Use APIs When Available

If a site offers an API, use it! APIs are:
- More reliable (structured data)
- More efficient (no HTML parsing)
- Explicitly allowed (unlike scraping)
- Often better documented

### Real-World Workflow

1. **Inspect the page** — Use your browser's DevTools to examine the HTML structure
2. **Identify patterns** — Find the tags/classes/IDs that contain your target data
3. **Write a parser** — Build a custom HTMLParser subclass or use BeautifulSoup
4. **Test on samples** — Verify your parser works on representative HTML
5. **Handle edge cases** — Missing data, malformed HTML, etc.
6. **Add error handling** — Websites change; your scraper should fail gracefully
7. **Respect limits** — Rate limit, check robots.txt, monitor your impact

### Common Pitfalls

1. **Fragile selectors** — Websites change their structure frequently. Scraping is inherently fragile.
2. **JavaScript-rendered content** — Some sites load content dynamically with JavaScript. You won't see this content in the raw HTML. For these, you'd need tools like Selenium or Playwright.
3. **CAPTCHAs and bot detection** — Many sites actively block scrapers. Don't try to circumvent these protections.
4. **Legal issues** — Scraping can violate Terms of Service or copyright. Be careful, especially with commercial use.

### Summary

- Web scraping extracts data from HTML
- Python's `html.parser` is built-in and works for simple tasks
- BeautifulSoup is the industry standard for more complex scraping
- Always check robots.txt and Terms of Service
- Rate limit your requests to be respectful
- Prefer APIs when available
- Scraping is fragile — websites change often

Web scraping is a powerful tool, but it comes with responsibility. Use it wisely, respect the websites you're scraping, and always consider whether an API might be a better option.

## Code Example

Check out [`example.py`](example.py) for a complete working example.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.
