# scraper.py
import requests
from bs4 import BeautifulSoup
from myapp.models import ScrapedData

def scrape_and_save_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract quotes and authors
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    for quote, author in zip(quotes, authors):
        text = quote.text.strip()
        author_name = author.text.strip()

        # Save to the Django model
        scraped_data = ScrapedData(title=author_name, content=text)
        scraped_data.save()

# Usage
url_to_scrape = 'http://quotes.toscrape.com/'
scrape_and_save_quotes(url_to_scrape)
