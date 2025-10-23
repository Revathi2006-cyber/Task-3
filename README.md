# 📰 Web Scraper for News Headlines

## 📌 Objective
Build a **Python web scraper** that automatically collects the top news headlines from a public news website and saves them into a `.txt` file.

---

## 🧠 Description
This project uses the **requests** and **BeautifulSoup** libraries to:

- Fetch the HTML content of a news website  
- Parse and extract the main headlines (using `<h2>` tags)  
- Save the collected headlines into a text file for offline reading  

It helps automate the process of collecting the latest headlines from news websites.

---

## 🛠️ Tools & Technologies
- Python 3  
- `requests` – for fetching webpage data  
- BeautifulSoup (`bs4`) – for parsing HTML content  
- VS Code – for coding and testing  

---
## 🪜 Steps to Run the Project

1️⃣ Create and activate a virtual environment

2️⃣ Install Dependencies
pip install requests beautifulsoup4

3️⃣ Run the Python Script
python news_scraper.py

4️⃣ Check the Output
A file named headlines.txt will be created in your project folder containing the latest headlines.
