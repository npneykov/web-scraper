import unittest

from bs4 import BeautifulSoup

from src.web_scraper import (
    get_data,
    get_html,
    parse_html,
    run_web_scraper,
    write_data_to_file,
)


class TestMain(unittest.TestCase):
    def test_get_html_valid_url(self):
        self.assertIsInstance(get_html('https://www.google.com'), str)

    def test_get_html_invalid_url(self):
        self.assertRaises(BaseException or ValueError, get_html('ht//www.google.com'))

    def test_parse_html_valid_html(self):
        self.assertIsInstance(parse_html('<html></html>'), BeautifulSoup)

    def test_parse_html_invalid_html(self):
        self.assertIsInstance(parse_html(''), str)

    def test_parse_html_raise_exception(self):
        self.assertRaises(BaseException, parse_html(8))

    def test_get_data_invalid_soup_and_selector(self):
        soup = 'Invalid soup'
        test_selector = 'span'
        self.assertIsInstance(None, type(get_data(soup, test_selector)))

    def test_get_data_raise_exception(self):
        self.assertRaises(BaseException, get_data(1, '2'))

    def test_run_web_scraper_invalid_arguments(self):
        url = ''
        selectors = []
        self.assertRaises(BaseException, run_web_scraper(url, selectors))

    def test_write_data_to_json_file(self):
        file_name = 'test.json'
        data = {'test': 1, 'test2': 'two', 'test3': 'three'}
        self.assertIsInstance(write_data_to_file(file_name, data), str)

    def test_write_data_to_json_file_not_json(self):
        file_name = 'test.json'
        data = ['test', 1, 'test2', 'two', 'test3', 'three']
        self.assertRaises(BaseException, write_data_to_file(file_name, data))

    def test_write_data_to_json_invalid_file_pattern(self):
        file_name = 'test'
        data = {'test': 1, 'test2': 'two', 'test3': 'three'}
        self.assertIsInstance(write_data_to_file(file_name, data), str)

    def test_write_data_to_json_file_raise_exception(self):
        file_name = 'test'
        data = 'test'
        self.assertRaises(Exception, write_data_to_file(file_name, data))


if __name__ == '__main__':
    unittest.main()
