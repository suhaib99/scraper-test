# myapp/management/commands/scrape_data.py
from django.core.management.base import BaseCommand
from myapp.scraper import scrape_and_save_quotes  # Adjust the import based on your actual scraper function

class Command(BaseCommand):
    help = 'Scrape and save quotes to the database'

    def handle(self, *args, **options):
        url_to_scrape = 'http://quotes.toscrape.com/'
        scrape_and_save_quotes(url_to_scrape)
        self.stdout.write(self.style.SUCCESS('Quotes successfully scraped and saved.'))
