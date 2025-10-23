📰 Web Scraper for News Headlines
📌 Objective

To build a simple Python web scraper that automatically collects the top news headlines from a public news website and saves them into a text file.

🧠 Description

This project uses the requests and BeautifulSoup libraries to:

Fetch the HTML content of a news website.

Parse and extract the main headlines (<h2> tags).

Save those headlines into a .txt file for later reading.

🛠️ Tools & Technologies

Python 3

requests — for fetching webpage data

BeautifulSoup — for parsing HTML

VS Code — IDE used for coding and testing

🪜 Steps to Run the Project
1️⃣ Create and activate a virtual environment:
python -m venv .venv
.venv\Scripts\activate   # Windows

2️⃣ Install dependencies:
pip install requests beautifulsoup4

3️⃣ Run the Python script:
python news_scraper.py

4️⃣ Check the output:

A file named headlines.txt will be created in your folder.

It contains all scraped headlines.

💡 Interview Questions & Answers
1️⃣ What is a GET request?

A GET request is an HTTP method used to fetch data from a server (like a webpage).
Example: When you open a website, your browser sends a GET request to get that page’s content.

2️⃣ How do you install external packages in Python?

Use the pip command in the terminal:

pip install requests

3️⃣ What is a User-Agent in HTTP?

A User-Agent is a small text string sent by your browser (or program) that tells the website who is requesting the page — e.g., Chrome, Firefox, or a Python script.

4️⃣ What is soup.find_all() used for?

soup.find_all() finds all HTML elements that match a tag or condition.
Example:

soup.find_all('h2')  # finds all <h2> tags

5️⃣ What are the risks of web scraping?

Violating a website’s terms of service

Overloading the server with too many requests

Legal issues if data is copyrighted or private

Website structure changes can break your scraper

6️⃣ What’s the difference between id and class in HTML?
Attribute	Purpose	Usage
id	Unique identifier for one element	Used only once per page
class	Group multiple elements	Can be used many times

Example:

<p id="intro">...</p>
<p class="news">...</p>

7️⃣ What is an HTML tag?

An HTML tag is a code element that tells the browser how to display content.
Example:

<h1>Headline</h1>


Here, <h1> is the tag and “Headline” is the content.

8️⃣ What does .text return in BeautifulSoup?

.text returns the visible text inside an HTML element, removing all HTML tags.
Example:

headline.text  # returns only the text, not <h2> tags

9️⃣ What is a try-except block?

A try-except block is used to handle errors in Python and prevent crashes.
Example:

try:
    print(10/0)
except:
    print("Error occurred")

🔟 What are HTTP status codes?

HTTP status codes are numbers returned by a web server to show the result of a request.

Code	Meaning
200	OK (Success)
404	Page not found
500	Server error
403	Forbidden
301	Redirected
