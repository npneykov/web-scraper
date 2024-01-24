import unittest

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


if __name__ == "__main__":
    unittest.main()
