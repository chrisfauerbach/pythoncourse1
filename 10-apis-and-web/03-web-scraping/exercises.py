"""
Web Scraping — Exercises
=========================

Practice problems to test your understanding of web scraping.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

from html.parser import HTMLParser
import re


# =============================================================================
# Exercise 1: Extract All Headings
#
# Write a parser that extracts all heading tags (h1, h2, h3, h4, h5, h6)
# and their text content from the HTML below.
#
# Expected output:
#   h1: Introduction to Python
#   h2: Why Learn Python?
#   h2: Getting Started
#   h3: Installation
#   h3: Your First Program
#
# =============================================================================

def exercise_1():
    html = """
    <article>
        <h1>Introduction to Python</h1>
        <p>Python is a versatile programming language.</p>
        <h2>Why Learn Python?</h2>
        <p>It's beginner-friendly and powerful.</p>
        <h2>Getting Started</h2>
        <h3>Installation</h3>
        <p>Download from python.org</p>
        <h3>Your First Program</h3>
        <p>Try printing "Hello, World!"</p>
    </article>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Extract Image Information
#
# Write a parser that extracts all images (<img> tags) from HTML and
# collects their src and alt attributes.
#
# Expected output:
#   Image: logo.png (Company Logo)
#   Image: product1.jpg (Wireless Mouse)
#   Image: product2.jpg (Mechanical Keyboard)
#   Image: banner.jpg (Sale Banner)
#
# =============================================================================

def exercise_2():
    html = """
    <div class="page">
        <img src="logo.png" alt="Company Logo">
        <div class="products">
            <img src="product1.jpg" alt="Wireless Mouse">
            <img src="product2.jpg" alt="Mechanical Keyboard">
        </div>
        <img src="banner.jpg" alt="Sale Banner">
    </div>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Parse a Simple Product List
#
# Extract product names and prices from the HTML below. Each product is in
# a div with class="item", containing a span with class="name" and another
# span with class="cost".
#
# Expected output:
#   Laptop: $899.99
#   Mouse: $24.99
#   Keyboard: $59.99
#   Monitor: $299.99
#
# =============================================================================

def exercise_3():
    html = """
    <div class="store">
        <div class="item">
            <span class="name">Laptop</span>
            <span class="cost">$899.99</span>
        </div>
        <div class="item">
            <span class="name">Mouse</span>
            <span class="cost">$24.99</span>
        </div>
        <div class="item">
            <span class="name">Keyboard</span>
            <span class="cost">$59.99</span>
        </div>
        <div class="item">
            <span class="name">Monitor</span>
            <span class="cost">$299.99</span>
        </div>
    </div>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Extract Data from a List (ul/ol and li)
#
# Parse the HTML and extract all list items, distinguishing between
# ordered lists (ol) and unordered lists (ul).
#
# Expected output:
#   Unordered list:
#     - Eggs
#     - Milk
#     - Bread
#   Ordered list:
#     1. Preheat oven
#     2. Mix ingredients
#     3. Bake for 30 minutes
#
# =============================================================================

def exercise_4():
    html = """
    <div>
        <h3>Shopping List</h3>
        <ul>
            <li>Eggs</li>
            <li>Milk</li>
            <li>Bread</li>
        </ul>
        <h3>Recipe Steps</h3>
        <ol>
            <li>Preheat oven</li>
            <li>Mix ingredients</li>
            <li>Bake for 30 minutes</li>
        </ol>
    </div>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Extract Comments with Usernames and Timestamps
#
# Parse a simple comment section where each comment has a username
# (class="user"), timestamp (class="time"), and text (class="message").
#
# Expected output:
#   [2024-01-15 10:30] alice: Great article!
#   [2024-01-15 11:45] bob: Thanks for sharing.
#   [2024-01-15 14:20] charlie: Very informative.
#
# =============================================================================

def exercise_5():
    html = """
    <div class="comments">
        <div class="comment">
            <span class="user">alice</span>
            <span class="time">2024-01-15 10:30</span>
            <p class="message">Great article!</p>
        </div>
        <div class="comment">
            <span class="user">bob</span>
            <span class="time">2024-01-15 11:45</span>
            <p class="message">Thanks for sharing.</p>
        </div>
        <div class="comment">
            <span class="user">charlie</span>
            <span class="time">2024-01-15 14:20</span>
            <p class="message">Very informative.</p>
        </div>
    </div>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Combine Parsing and Regex
#
# Extract all article titles and publication dates from the HTML.
# Then use regex to parse the dates and group articles by year.
#
# Expected output:
#   2023:
#     - Introduction to Python
#     - Web Scraping Basics
#   2024:
#     - Advanced Python Techniques
#     - Building REST APIs
#
# Hint: Use regex to extract the year from dates like "2024-01-15"
# =============================================================================

def exercise_6():
    html = """
    <div class="blog">
        <article>
            <h2 class="title">Introduction to Python</h2>
            <span class="date">2023-05-10</span>
        </article>
        <article>
            <h2 class="title">Web Scraping Basics</h2>
            <span class="date">2023-08-22</span>
        </article>
        <article>
            <h2 class="title">Advanced Python Techniques</h2>
            <span class="date">2024-01-15</span>
        </article>
        <article>
            <h2 class="title">Building REST APIs</h2>
            <span class="date">2024-03-08</span>
        </article>
    </div>
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    html = """
    <article>
        <h1>Introduction to Python</h1>
        <p>Python is a versatile programming language.</p>
        <h2>Why Learn Python?</h2>
        <p>It's beginner-friendly and powerful.</p>
        <h2>Getting Started</h2>
        <h3>Installation</h3>
        <p>Download from python.org</p>
        <h3>Your First Program</h3>
        <p>Try printing "Hello, World!"</p>
    </article>
    """

    class HeadingExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.headings = []
            self.current_heading = None
            self.heading_data = []

        def handle_starttag(self, tag, attrs):
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
                self.current_heading = tag
                self.heading_data = []

        def handle_endtag(self, tag):
            if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') and self.current_heading:
                text = ''.join(self.heading_data).strip()
                self.headings.append((self.current_heading, text))
                self.current_heading = None

        def handle_data(self, data):
            if self.current_heading:
                self.heading_data.append(data)

    parser = HeadingExtractor()
    parser.feed(html)

    for tag, text in parser.headings:
        print(f"{tag}: {text}")


def solution_2():
    html = """
    <div class="page">
        <img src="logo.png" alt="Company Logo">
        <div class="products">
            <img src="product1.jpg" alt="Wireless Mouse">
            <img src="product2.jpg" alt="Mechanical Keyboard">
        </div>
        <img src="banner.jpg" alt="Sale Banner">
    </div>
    """

    class ImageExtractor(HTMLParser):
        def __init__(self):
            super().__init__()
            self.images = []

        def handle_starttag(self, tag, attrs):
            if tag == 'img':
                attrs_dict = dict(attrs)
                src = attrs_dict.get('src', '')
                alt = attrs_dict.get('alt', '')
                self.images.append({'src': src, 'alt': alt})

    parser = ImageExtractor()
    parser.feed(html)

    for img in parser.images:
        print(f"Image: {img['src']} ({img['alt']})")


def solution_3():
    html = """
    <div class="store">
        <div class="item">
            <span class="name">Laptop</span>
            <span class="cost">$899.99</span>
        </div>
        <div class="item">
            <span class="name">Mouse</span>
            <span class="cost">$24.99</span>
        </div>
        <div class="item">
            <span class="name">Keyboard</span>
            <span class="cost">$59.99</span>
        </div>
        <div class="item">
            <span class="name">Monitor</span>
            <span class="cost">$299.99</span>
        </div>
    </div>
    """

    class ProductParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.products = []
            self.in_name = False
            self.in_cost = False
            self.current_product = {}
            self.data_buffer = []

        def handle_starttag(self, tag, attrs):
            if tag == 'span':
                attrs_dict = dict(attrs)
                if attrs_dict.get('class') == 'name':
                    self.in_name = True
                    self.data_buffer = []
                elif attrs_dict.get('class') == 'cost':
                    self.in_cost = True
                    self.data_buffer = []

        def handle_endtag(self, tag):
            if tag == 'span':
                if self.in_name:
                    self.current_product['name'] = ''.join(self.data_buffer).strip()
                    self.in_name = False
                elif self.in_cost:
                    self.current_product['cost'] = ''.join(self.data_buffer).strip()
                    self.in_cost = False
            elif tag == 'div' and self.current_product:
                if 'name' in self.current_product and 'cost' in self.current_product:
                    self.products.append(self.current_product)
                    self.current_product = {}

        def handle_data(self, data):
            if self.in_name or self.in_cost:
                self.data_buffer.append(data)

    parser = ProductParser()
    parser.feed(html)

    for product in parser.products:
        print(f"{product['name']}: {product['cost']}")


def solution_4():
    html = """
    <div>
        <h3>Shopping List</h3>
        <ul>
            <li>Eggs</li>
            <li>Milk</li>
            <li>Bread</li>
        </ul>
        <h3>Recipe Steps</h3>
        <ol>
            <li>Preheat oven</li>
            <li>Mix ingredients</li>
            <li>Bake for 30 minutes</li>
        </ol>
    </div>
    """

    class ListParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.lists = []
            self.current_list = None
            self.in_li = False
            self.li_data = []

        def handle_starttag(self, tag, attrs):
            if tag in ('ul', 'ol'):
                self.current_list = {'type': tag, 'items': []}
            elif tag == 'li' and self.current_list is not None:
                self.in_li = True
                self.li_data = []

        def handle_endtag(self, tag):
            if tag == 'li' and self.in_li:
                item_text = ''.join(self.li_data).strip()
                self.current_list['items'].append(item_text)
                self.in_li = False
            elif tag in ('ul', 'ol') and self.current_list:
                self.lists.append(self.current_list)
                self.current_list = None

        def handle_data(self, data):
            if self.in_li:
                self.li_data.append(data)

    parser = ListParser()
    parser.feed(html)

    for lst in parser.lists:
        if lst['type'] == 'ul':
            print("Unordered list:")
            for item in lst['items']:
                print(f"  - {item}")
        else:  # ol
            print("Ordered list:")
            for i, item in enumerate(lst['items'], 1):
                print(f"  {i}. {item}")


def solution_5():
    html = """
    <div class="comments">
        <div class="comment">
            <span class="user">alice</span>
            <span class="time">2024-01-15 10:30</span>
            <p class="message">Great article!</p>
        </div>
        <div class="comment">
            <span class="user">bob</span>
            <span class="time">2024-01-15 11:45</span>
            <p class="message">Thanks for sharing.</p>
        </div>
        <div class="comment">
            <span class="user">charlie</span>
            <span class="time">2024-01-15 14:20</span>
            <p class="message">Very informative.</p>
        </div>
    </div>
    """

    class CommentParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.comments = []
            self.current_comment = None
            self.in_user = False
            self.in_time = False
            self.in_message = False
            self.data_buffer = []

        def handle_starttag(self, tag, attrs):
            attrs_dict = dict(attrs)

            if tag == 'div' and attrs_dict.get('class') == 'comment':
                self.current_comment = {'user': '', 'time': '', 'message': ''}
            elif self.current_comment is not None:
                if tag == 'span' and attrs_dict.get('class') == 'user':
                    self.in_user = True
                    self.data_buffer = []
                elif tag == 'span' and attrs_dict.get('class') == 'time':
                    self.in_time = True
                    self.data_buffer = []
                elif tag == 'p' and attrs_dict.get('class') == 'message':
                    self.in_message = True
                    self.data_buffer = []

        def handle_endtag(self, tag):
            if self.in_user and tag == 'span':
                self.current_comment['user'] = ''.join(self.data_buffer).strip()
                self.in_user = False
            elif self.in_time and tag == 'span':
                self.current_comment['time'] = ''.join(self.data_buffer).strip()
                self.in_time = False
            elif self.in_message and tag == 'p':
                self.current_comment['message'] = ''.join(self.data_buffer).strip()
                self.in_message = False
            elif tag == 'div' and self.current_comment is not None:
                if self.current_comment['user']:  # Only add if we have data
                    self.comments.append(self.current_comment)
                    self.current_comment = None

        def handle_data(self, data):
            if any([self.in_user, self.in_time, self.in_message]):
                self.data_buffer.append(data)

    parser = CommentParser()
    parser.feed(html)

    for comment in parser.comments:
        print(f"[{comment['time']}] {comment['user']}: {comment['message']}")


def solution_6():
    html = """
    <div class="blog">
        <article>
            <h2 class="title">Introduction to Python</h2>
            <span class="date">2023-05-10</span>
        </article>
        <article>
            <h2 class="title">Web Scraping Basics</h2>
            <span class="date">2023-08-22</span>
        </article>
        <article>
            <h2 class="title">Advanced Python Techniques</h2>
            <span class="date">2024-01-15</span>
        </article>
        <article>
            <h2 class="title">Building REST APIs</h2>
            <span class="date">2024-03-08</span>
        </article>
    </div>
    """

    class ArticleParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.articles = []
            self.current_article = None
            self.in_title = False
            self.in_date = False
            self.data_buffer = []

        def handle_starttag(self, tag, attrs):
            attrs_dict = dict(attrs)

            if tag == 'article':
                self.current_article = {'title': '', 'date': ''}
            elif self.current_article is not None:
                if tag == 'h2' and attrs_dict.get('class') == 'title':
                    self.in_title = True
                    self.data_buffer = []
                elif tag == 'span' and attrs_dict.get('class') == 'date':
                    self.in_date = True
                    self.data_buffer = []

        def handle_endtag(self, tag):
            if self.in_title and tag == 'h2':
                self.current_article['title'] = ''.join(self.data_buffer).strip()
                self.in_title = False
            elif self.in_date and tag == 'span':
                self.current_article['date'] = ''.join(self.data_buffer).strip()
                self.in_date = False
            elif tag == 'article' and self.current_article is not None:
                self.articles.append(self.current_article)
                self.current_article = None

        def handle_data(self, data):
            if self.in_title or self.in_date:
                self.data_buffer.append(data)

    parser = ArticleParser()
    parser.feed(html)

    # Group articles by year using regex
    articles_by_year = {}
    for article in parser.articles:
        # Extract year from date (format: YYYY-MM-DD)
        year_match = re.match(r'(\d{4})-', article['date'])
        if year_match:
            year = year_match.group(1)
            if year not in articles_by_year:
                articles_by_year[year] = []
            articles_by_year[year].append(article['title'])

    # Print grouped articles
    for year in sorted(articles_by_year.keys()):
        print(f"{year}:")
        for title in articles_by_year[year]:
            print(f"  - {title}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Extract All Headings", exercise_1),
        ("Extract Image Information", exercise_2),
        ("Parse a Simple Product List", exercise_3),
        ("Extract Data from a List", exercise_4),
        ("Extract Comments with Usernames and Timestamps", exercise_5),
        ("Combine Parsing and Regex", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
