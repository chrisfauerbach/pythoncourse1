"""
Web Scraping — Example Code
=============================

Run this file:
    python3 example.py

This file demonstrates web scraping using Python's built-in html.parser module.
We'll work with simulated HTML strings (no network calls) to learn the fundamentals
of parsing, extracting, and processing HTML data.

Note: For real-world projects, most developers use BeautifulSoup, but understanding
the standard library gives you a solid foundation.
"""

from html.parser import HTMLParser
import re

# =============================================================================
# Example 1: Basic HTML Parsing
# =============================================================================

print("=" * 70)
print("EXAMPLE 1: Basic HTML Parsing")
print("=" * 70)

class BasicParser(HTMLParser):
    """A simple parser that prints every tag and data it encounters."""

    def handle_starttag(self, tag, attrs):
        print(f"Start tag: <{tag}>")
        for attr, value in attrs:
            print(f"  Attribute: {attr} = '{value}'")

    def handle_endtag(self, tag):
        print(f"End tag: </{tag}>")

    def handle_data(self, data):
        stripped = data.strip()
        if stripped:
            print(f"Data: {stripped}")

html = """
<div class="container">
    <h1>Welcome to Web Scraping</h1>
    <p>This is a <b>simple</b> example.</p>
</div>
"""

parser = BasicParser()
parser.feed(html)

# With BeautifulSoup, this would be:
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

# =============================================================================
# Example 2: Extracting Links
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 2: Extracting Links from HTML")
print("=" * 70)

class LinkExtractor(HTMLParser):
    """Extract all links and their text from HTML."""

    def __init__(self):
        super().__init__()
        self.links = []
        self.current_link = None
        self.link_text = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.current_link = value
                    self.link_text = []

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_link:
            text = ''.join(self.link_text).strip()
            self.links.append({
                'url': self.current_link,
                'text': text
            })
            self.current_link = None

    def handle_data(self, data):
        if self.current_link is not None:
            self.link_text.append(data)

blog_html = """
<nav>
    <a href="/home">Home</a>
    <a href="/blog">Blog</a>
    <a href="/about">About Us</a>
</nav>
<article>
    <p>Check out <a href="https://python.org">Python's official site</a> for more info.</p>
    <p>Also see <a href="https://docs.python.org/3/">the documentation</a>.</p>
</article>
"""

parser = LinkExtractor()
parser.feed(blog_html)

print(f"Found {len(parser.links)} links:\n")
for link in parser.links:
    print(f"  [{link['text']}] -> {link['url']}")

# With BeautifulSoup:
# soup = BeautifulSoup(blog_html, 'html.parser')
# for link in soup.find_all('a'):
#     print(f"  [{link.text}] -> {link.get('href')}")

# =============================================================================
# Example 3: Extracting Text Content
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 3: Extracting Text Content (Stripping Tags)")
print("=" * 70)

class TextExtractor(HTMLParser):
    """Extract all visible text, ignoring HTML tags."""

    def __init__(self):
        super().__init__()
        self.text_parts = []

    def handle_data(self, data):
        stripped = data.strip()
        if stripped:
            self.text_parts.append(stripped)

    def get_text(self):
        return ' '.join(self.text_parts)

article_html = """
<article>
    <h1>The Rise of Python</h1>
    <p>Python has become one of the <strong>most popular</strong> programming languages.</p>
    <p>Its simplicity and <em>powerful libraries</em> make it ideal for beginners and experts alike.</p>
</article>
"""

parser = TextExtractor()
parser.feed(article_html)
print(parser.get_text())

# With BeautifulSoup:
# soup = BeautifulSoup(article_html, 'html.parser')
# print(soup.get_text())

# =============================================================================
# Example 4: Finding Elements by Tag and Attribute
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 4: Finding Elements by Tag and Attribute")
print("=" * 70)

class PriceExtractor(HTMLParser):
    """Extract prices from elements with class='price'."""

    def __init__(self):
        super().__init__()
        self.prices = []
        self.in_price = False
        self.price_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            for attr, value in attrs:
                if attr == 'class' and 'price' in value:
                    self.in_price = True
                    self.price_data = []

    def handle_endtag(self, tag):
        if tag == 'span' and self.in_price:
            self.in_price = False
            price_text = ''.join(self.price_data).strip()
            self.prices.append(price_text)

    def handle_data(self, data):
        if self.in_price:
            self.price_data.append(data)

product_html = """
<div class="product">
    <h3>Laptop</h3>
    <span class="price">$999.99</span>
    <span class="stock">In Stock</span>
</div>
<div class="product">
    <h3>Mouse</h3>
    <span class="price">$29.99</span>
    <span class="stock">Out of Stock</span>
</div>
<div class="product">
    <h3>Keyboard</h3>
    <span class="price">$79.99</span>
    <span class="stock">In Stock</span>
</div>
"""

parser = PriceExtractor()
parser.feed(product_html)

print("Product prices:")
for price in parser.prices:
    print(f"  {price}")

# With BeautifulSoup:
# soup = BeautifulSoup(product_html, 'html.parser')
# for price in soup.find_all('span', class_='price'):
#     print(f"  {price.text}")

# =============================================================================
# Example 5: Parsing Tables
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 5: Parsing HTML Tables")
print("=" * 70)

class TableParser(HTMLParser):
    """Parse HTML tables into a list of rows."""

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
            cell_text = ''.join(self.cell_data).strip()
            self.current_row.append(cell_text)
        elif tag == 'tr':
            if self.current_row:
                self.rows.append(self.current_row)
                self.current_row = []

    def handle_data(self, data):
        if self.in_cell:
            self.cell_data.append(data)

table_html = """
<table>
    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>
    <tr>
        <td>Alice</td>
        <td>30</td>
        <td>New York</td>
    </tr>
    <tr>
        <td>Bob</td>
        <td>25</td>
        <td>San Francisco</td>
    </tr>
    <tr>
        <td>Charlie</td>
        <td>35</td>
        <td>Chicago</td>
    </tr>
</table>
"""

parser = TableParser()
parser.feed(table_html)

print("Parsed table data:\n")
for i, row in enumerate(parser.rows):
    if i == 0:
        print("Headers:", " | ".join(row))
        print("-" * 40)
    else:
        print(f"Row {i}:   {' | '.join(row)}")

# With BeautifulSoup:
# soup = BeautifulSoup(table_html, 'html.parser')
# table = soup.find('table')
# for row in table.find_all('tr'):
#     cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
#     print(cells)

# =============================================================================
# Example 6: Handling Nested HTML Structures
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 6: Handling Nested Structures (Blog Posts)")
print("=" * 70)

class BlogPostExtractor(HTMLParser):
    """Extract blog posts with titles, authors, and content."""

    def __init__(self):
        super().__init__()
        self.posts = []
        self.current_post = None
        self.in_title = False
        self.in_author = False
        self.in_content = False
        self.data_buffer = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'article' and attrs_dict.get('class') == 'post':
            self.current_post = {'title': '', 'author': '', 'content': ''}
        elif self.current_post is not None:
            if tag == 'h2' and attrs_dict.get('class') == 'title':
                self.in_title = True
                self.data_buffer = []
            elif tag == 'span' and attrs_dict.get('class') == 'author':
                self.in_author = True
                self.data_buffer = []
            elif tag == 'p' and attrs_dict.get('class') == 'content':
                self.in_content = True
                self.data_buffer = []

    def handle_endtag(self, tag):
        if self.in_title and tag == 'h2':
            self.current_post['title'] = ''.join(self.data_buffer).strip()
            self.in_title = False
        elif self.in_author and tag == 'span':
            self.current_post['author'] = ''.join(self.data_buffer).strip()
            self.in_author = False
        elif self.in_content and tag == 'p':
            self.current_post['content'] = ''.join(self.data_buffer).strip()
            self.in_content = False
        elif tag == 'article' and self.current_post is not None:
            self.posts.append(self.current_post)
            self.current_post = None

    def handle_data(self, data):
        if self.in_title or self.in_author or self.in_content:
            self.data_buffer.append(data)

blog_posts_html = """
<div class="blog">
    <article class="post">
        <h2 class="title">Getting Started with Python</h2>
        <span class="author">Alice Smith</span>
        <p class="content">Python is an amazing language for beginners...</p>
    </article>
    <article class="post">
        <h2 class="title">Web Scraping Tutorial</h2>
        <span class="author">Bob Johnson</span>
        <p class="content">Learn how to extract data from websites...</p>
    </article>
    <article class="post">
        <h2 class="title">Data Science with Python</h2>
        <span class="author">Charlie Brown</span>
        <p class="content">Explore pandas, numpy, and matplotlib...</p>
    </article>
</div>
"""

parser = BlogPostExtractor()
parser.feed(blog_posts_html)

print(f"Found {len(parser.posts)} blog posts:\n")
for i, post in enumerate(parser.posts, 1):
    print(f"{i}. {post['title']}")
    print(f"   By: {post['author']}")
    print(f"   {post['content'][:50]}...")
    print()

# =============================================================================
# Example 7: Using Regex as a Supplement
# =============================================================================

print("=" * 70)
print("EXAMPLE 7: Using Regex for Simple Pattern Extraction")
print("=" * 70)

contact_html = """
<div class="contact-info">
    <p>Email us at: support@example.com</p>
    <p>Sales: sales@example.com</p>
    <p>Phone: (555) 123-4567</p>
    <p>Alternate: (555) 987-6543</p>
</div>
"""

# Extract email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', contact_html)
print("Emails found:")
for email in emails:
    print(f"  {email}")

# Extract phone numbers
phones = re.findall(r'\(\d{3}\)\s*\d{3}-\d{4}', contact_html)
print("\nPhone numbers found:")
for phone in phones:
    print(f"  {phone}")

# Extract prices from product descriptions
price_html = """
<div>
    <p>Laptop - Was: $1,299.99 Now: $999.99</p>
    <p>Mouse - $29.99</p>
    <p>Keyboard - Sale Price: $79.99 (Regular: $99.99)</p>
</div>
"""

prices = re.findall(r'\$([0-9,]+\.\d{2})', price_html)
print("\nPrices found:")
for price in prices:
    print(f"  ${price}")

# =============================================================================
# Example 8: Complete Scraping Example - Product Catalog
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 8: Complete Scraping Example - Product Catalog")
print("=" * 70)

class ProductCatalogParser(HTMLParser):
    """
    A complete example that extracts product information:
    - Name
    - Price
    - Rating
    - Availability
    - Product URL
    """

    def __init__(self):
        super().__init__()
        self.products = []
        self.current_product = None
        self.in_name = False
        self.in_price = False
        self.in_rating = False
        self.in_stock = False
        self.data_buffer = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Start of a new product
        if tag == 'div' and attrs_dict.get('class') == 'product-card':
            self.current_product = {
                'name': '',
                'price': '',
                'rating': '',
                'in_stock': '',
                'url': ''
            }

        # Inside a product, capture specific fields
        elif self.current_product is not None:
            if tag == 'a' and attrs_dict.get('class') == 'product-link':
                self.current_product['url'] = attrs_dict.get('href', '')
                self.in_name = True
                self.data_buffer = []
            elif tag == 'span' and attrs_dict.get('class') == 'price':
                self.in_price = True
                self.data_buffer = []
            elif tag == 'span' and attrs_dict.get('class') == 'rating':
                self.in_rating = True
                self.data_buffer = []
            elif tag == 'span' and attrs_dict.get('class') == 'stock':
                self.in_stock = True
                self.data_buffer = []

    def handle_endtag(self, tag):
        if self.in_name and tag == 'a':
            self.current_product['name'] = ''.join(self.data_buffer).strip()
            self.in_name = False
        elif self.in_price and tag == 'span':
            self.current_product['price'] = ''.join(self.data_buffer).strip()
            self.in_price = False
        elif self.in_rating and tag == 'span':
            self.current_product['rating'] = ''.join(self.data_buffer).strip()
            self.in_rating = False
        elif self.in_stock and tag == 'span':
            self.current_product['in_stock'] = ''.join(self.data_buffer).strip()
            self.in_stock = False
        elif tag == 'div' and self.current_product is not None:
            # Check if we're closing the product-card div
            self.products.append(self.current_product)
            self.current_product = None

    def handle_data(self, data):
        if any([self.in_name, self.in_price, self.in_rating, self.in_stock]):
            self.data_buffer.append(data)

catalog_html = """
<div class="catalog">
    <div class="product-card">
        <a href="/products/laptop-pro" class="product-link">Laptop Pro 15</a>
        <span class="price">$1,299.99</span>
        <span class="rating">4.5/5</span>
        <span class="stock">In Stock</span>
    </div>
    <div class="product-card">
        <a href="/products/wireless-mouse" class="product-link">Wireless Mouse</a>
        <span class="price">$29.99</span>
        <span class="rating">4.8/5</span>
        <span class="stock">In Stock</span>
    </div>
    <div class="product-card">
        <a href="/products/mechanical-keyboard" class="product-link">Mechanical Keyboard RGB</a>
        <span class="price">$149.99</span>
        <span class="rating">4.7/5</span>
        <span class="stock">Out of Stock</span>
    </div>
    <div class="product-card">
        <a href="/products/usb-hub" class="product-link">USB-C Hub 7-Port</a>
        <span class="price">$49.99</span>
        <span class="rating">4.3/5</span>
        <span class="stock">In Stock</span>
    </div>
</div>
"""

parser = ProductCatalogParser()
parser.feed(catalog_html)

print(f"Product Catalog ({len(parser.products)} items):\n")
for product in parser.products:
    print(f"Name:     {product['name']}")
    print(f"Price:    {product['price']}")
    print(f"Rating:   {product['rating']}")
    print(f"Stock:    {product['in_stock']}")
    print(f"URL:      {product['url']}")
    print("-" * 50)

# Additional processing: filter in-stock items under $100
print("\nIn-Stock Items Under $100:")
for product in parser.products:
    if product['in_stock'] == 'In Stock':
        # Extract numeric price
        price_match = re.search(r'\$([0-9,]+\.\d{2})', product['price'])
        if price_match:
            price = float(price_match.group(1).replace(',', ''))
            if price < 100:
                print(f"  {product['name']} - {product['price']}")

print("\n" + "=" * 70)
print("Examples complete!")
print("=" * 70)
print("\nKey takeaways:")
print("  1. HTMLParser is event-driven - override handle_* methods")
print("  2. Track state with flags (in_title, in_price, etc.)")
print("  3. Use data buffers to accumulate text across multiple data events")
print("  4. Parse attributes with dict(attrs) for easier access")
print("  5. Regex can supplement parsing for simple pattern extraction")
print("  6. For production, consider BeautifulSoup for easier syntax")
