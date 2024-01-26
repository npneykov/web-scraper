import unittest

import bs4

import scraper


class TestMain(unittest.TestCase):
    def test_get_html_valid_url(self):
        self.assertTrue(scraper.get_html("https://www.google.com"))

    def test_get_html_invalid_url(self):
        self.assertFalse(scraper.get_html("https//www.google.com"))

    def test_parse_html_valid_html(self):
        self.assertTrue(scraper.parse_html("<html></html>"))

    def test_parse_html_invalid_html(self):
        self.assertFalse(scraper.parse_html(""))

    def test_get_data_invalid_soup(self):
        soup = "Invalid soup"
        test_selector = "span"
        self.assertFalse(scraper.get_data(soup, test_selector))

    def test_get_data_invalid_selector(self):
        soup = bs4.BeautifulSoup()
        test_selector = ""
        self.assertFalse(scraper.get_data(soup, test_selector))

    def test_write_data_to_file(self):
        file_name = "test.txt"
        data = ["test"]
        self.assertTrue(scraper.write_data_to_file(file_name, data))

    def test_write_data_to_file_exception(self):
        file_name = "test"
        data = [1, 2, 3]
        self.assertRaises(Exception, scraper.write_data_to_file(file_name, data))


if __name__ == "__main__":
    unittest.main()
