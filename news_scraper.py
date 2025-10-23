import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML content
url = "https://timesofindia.indiatimes.com/"
response = requests.get(url)

# Step 2: Parse HTML using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Find all headline elements (BBC uses <h2> tags for headlines)
headlines = soup.find_all('h2')

# Step 4: Extract text and clean it
clean_headlines = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

# Step 5: Save headlines to a text file
with open("headlines.txt", "w", encoding="utf-8") as file:
    for i, title in enumerate(clean_headlines, start=1):
        file.write(f"{i}. {title}\n")

print(f" {len(clean_headlines)} headlines scraped and saved to 'headlines.txt'")