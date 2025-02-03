from unittest import TestCase

from bs4 import BeautifulSoup

from src.web_scraper import WebScraper

web_scraper = WebScraper('https://www.google.com', ['div', 'p', 'a'], 'test.json')


class ScraperTest(TestCase):
    def test_scrape_get_valid_html(self):
        self.assertIsInstance(web_scraper.get_html(), str)

    def test_scrape_get_invalid_html(self):
        web_scraper.url = 'ht//www.google.com'
        self.assertRaises(BaseException or ValueError, web_scraper.get_html())

    def test_scrape_parse_vaild_html(self):
        web_scraper.url = 'https://www.google.com'
        html = web_scraper.get_html()
        self.assertIsInstance(web_scraper.parse_html(html), BeautifulSoup)

    def test_scrape_parse_invalid_html(self):
        web_scraper.url = 'ht//www.google.com'
        html = web_scraper.get_html()
        self.assertRaises(BaseException or None, web_scraper.parse_html(html))

    def test_scrape_get_valid_data(self):
        web_scraper.url = 'https://www.google.com'
        html = web_scraper.get_html()
        soup = web_scraper.parse_html(html)
        self.assertIsInstance(web_scraper.get_data(soup), dict)

    def test_scrape_get_invalid_data(self):
        soup = None
        self.assertRaises(BaseException or None, web_scraper.get_data(soup))
