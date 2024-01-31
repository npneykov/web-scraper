import unittest

import bs4

from src.scraper import get_data, get_html, parse_html, write_data_to_file


class TestMain(unittest.TestCase):
    def test_get_html_valid_url(self):
        "Test for getting HTML from a valid URL."
        self.assertTrue(get_html("https://www.google.com"))

    def test_get_html_invalid_url(self):
        "Test the get_html function with an invalid URL."
        self.assertFalse(get_html("ht//www.google.com"))

    def test_parse_html_valid_html(self):
        "Test the parse_html function with valid HTML input."
        self.assertTrue(parse_html("<html></html>"))

    def test_parse_html_invalid_html(self):
        "Test the parse_html function with an invalid HTML input."
        self.assertFalse(parse_html(""))

    def test_get_data_invalid_soup(self):
        "Test for getting data using an invalid soup and selector."
        soup = "Invalid soup"
        test_selector = "span"
        self.assertFalse(get_data(soup, test_selector))

    def test_get_data_invalid_selector(self):
        "Test the get_data function with an invalid selector."
        soup = bs4.BeautifulSoup()
        test_selector = ""
        self.assertFalse(get_data(soup, test_selector))

    def test_write_data_to_file(self):
        "Test writing data to a file."
        file_name = "test.txt"
        data = ["test"]
        self.assertTrue(write_data_to_file(file_name, data))

    def test_write_data_to_file_exception(self):
        "Test the write_data_to_file function for handling exceptions."
        file_name = "test"
        data = [1, 2, 3]
        self.assertRaises(Exception, write_data_to_file(file_name, data))


if __name__ == "__main__":
    unittest.main()
