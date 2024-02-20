import unittest

from bs4 import BeautifulSoup

from src.web_scraper import WebScraper

web_scraper = WebScraper(
    'https://www.google.com', ['div', 'p', 'a'], 'scraped_data.json'
)


class TestMain(unittest.TestCase):
    def test_get_html_valid_url(self):
        self.assertIsInstance(web_scraper.get_html(), str)

    def test_get_html_invalid_url(self):
        web_scraper.url = 'ht//www.google.com'
        self.assertRaises(BaseException or ValueError, web_scraper.get_html())

    def test_parse_html_valid_html(self):
        html = '<html></html>'
        self.assertIsInstance(web_scraper.parse_html(html), BeautifulSoup)

    def test_parse_html_invalid_html(self):
        html = ''
        self.assertIsInstance(web_scraper.parse_html(html), str)

    def test_parse_html_raise_exception(self):
        html = 8
        self.assertRaises(BaseException, web_scraper.parse_html(html))

    def test_get_data_invalid_soup_and_selector(self):
        soup = 'Invalid soup'
        web_scraper.selector = 'span'
        self.assertIsInstance(None, type(web_scraper.get_data(soup)))

    def test_get_data_raise_exception(self):
        soup = 1
        self.assertRaises(BaseException, web_scraper.get_data(soup))

    def test_scrape_invalid_arguments(self):
        web_scraper.url = ''
        web_scraper.selectors = []
        self.assertRaises(BaseException, web_scraper.scrape())

    def test_write_data_to_json_file(self):
        web_scraper.file_name = 'test.json'
        data = {'test': 1, 'test2': 'two', 'test3': 'three'}
        self.assertIsInstance(web_scraper.write_data_to_json_file(data), str)

    def test_write_data_to_json_file_not_json(self):
        web_scraper.file_name = 'test.json'
        data = ['test', 1, 'test2', 'two', 'test3', 'three']
        self.assertRaises(BaseException, web_scraper.write_data_to_json_file(data))

    def test_write_data_to_json_invalid_file_pattern(self):
        web_scraper.file_name = 'test'
        data = {'test': 1, 'test2': 'two', 'test3': 'three'}
        self.assertIsInstance(web_scraper.write_data_to_json_file(data), str)

    def test_write_data_to_json_file_raise_exception(self):
        web_scraper.file_name = 'test'
        data = 'test'
        self.assertRaises(Exception, web_scraper.write_data_to_json_file(data))


if __name__ == '__main__':
    unittest.main()
