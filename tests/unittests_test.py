import unittest

from bs4 import BeautifulSoup

from src.scraper import (
    get_data,
    get_html,
    parse_html,
    run_web_scraper,
    write_data_to_file,
)


class TestMain(unittest.TestCase):
    def test_get_html_valid_url(self):
        'Test for getting HTML from a valid URL.'
        self.assertIsInstance(get_html('https://www.google.com'), str)

    def test_get_html_invalid_url(self):
        'Test the get_html function with an invalid URL.'
        self.assertRaises(BaseException or ValueError, get_html('ht//www.google.com'))

    def test_parse_html_valid_html(self):
        'Test the parse_html function with valid HTML input.'
        self.assertIsInstance(parse_html('<html></html>'), BeautifulSoup)

    def test_parse_html_invalid_html(self):
        'Test the parse_html function with an invalid HTML input.'
        self.assertIsInstance(parse_html(''), str)

    def test_parse_html_raise_exception(self):
        'Test the parse_html function for handling exception.'
        self.assertRaises(BaseException, parse_html(8))

    def test_get_data_invalid_soup_and_selector(self):
        'Test for getting data using an invalid soup and selector.'
        soup = 'Invalid soup'
        test_selector = 'span'
        self.assertIsInstance(None, type(get_data(soup, test_selector)))

    def test_get_data_raise_exception(self):
        'Test the get_data function for raising exception.'
        self.assertRaises(BaseException, get_data(1, '2'))

    def test_run_web_scraper_invalid_arguments(self):
        'Test the run_web_scraper function for raising exception.'
        url = ''
        selectors = []
        self.assertRaises(BaseException, run_web_scraper(url, selectors))

    def test_write_data_to_json_file(self):
        'Test writing data successfully to a JSON file.'
        file_name = 'test.json'
        data = {'test': 1, 'test2': 'two', 'test3': 'three'}
        self.assertIsInstance(write_data_to_file(file_name, data), str)

    def test_write_data_to_json_file_not_json(self):
        'Test the function for handling exceptions.'
        file_name = 'test.json'
        data = ['test', 1, 'test2', 'two', 'test3', 'three']
        self.assertRaises(BaseException, write_data_to_file(file_name, data))

    def test_write_data_to_json_invalid_file_pattern(self):
        'Test the function for handling file pattern mismatch.'
        file_name = 'test'
        data = {'test': 1, 'test2': 'two', 'test3': 'three'}
        self.assertIsInstance(write_data_to_file(file_name, data), str)

    def test_write_data_to_json_file_raise_exception(self):
        'Test the function for raising exception.'
        file_name = 'test'
        data = 'test'
        self.assertRaises(Exception, write_data_to_file(file_name, data))


if __name__ == '__main__':
    unittest.main()
