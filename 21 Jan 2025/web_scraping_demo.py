# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = "https://quotes.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Parse the content 
soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('div', class_ = 'quote')

# print(quotes)

for quote in quotes:

    text = quote.find('span', class_ = 'text').get_text(strip = True)

    author = quote.find('small', class_ = 'author').get_text(strip = True)

    print(f"Quote: {text}")
    print(f"Author: {author}")
    print('-' * 50)