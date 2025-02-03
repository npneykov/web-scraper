import json
import re

import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url: str, selectors: list, file_name: str):
        self.url = url
        self.selectors = selectors
        self.file_name = file_name

    def get_html(self):
        """
        A method to retrieve the HTML content of a given URL.

        Returns:
            str: The HTML content of the web page, or an error message if the URL pattern does not match or an exception occurs.
        """
        url_pattern = '^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$'

        try:
            if re.compile(url_pattern).search(self.url):
                response = requests.get(self.url)
                return (
                    response.text
                    if response.status_code == 200
                    else f'Got status code {response.status_code}: {response.reason}'
                )
            else:
                raise ValueError(
                    f'Method get_html():The URL pattern does not match. Passed URL: {self.url}',
                )
        except Exception as err:
            print(err.args)

    def parse_html(self, html: str):
        """
        A method for parsing the given HTML string and return a BeautifulSoup object ,
        otherwise return an error message.

        Args:
            html (str): The HTML string to be parsed.

        Returns:
            BeautifulSoup: The parsed result if successful, If an exception occurs during parsing, return the exception object.
        """
        try:
            return BeautifulSoup(markup=html, features='html.parser') if html else None
        except Exception as err:
            print(err.args)

    def get_data(self, soup: BeautifulSoup):
        """
        Method for scraping data from a BeautifulSoup object using a dict of CSS selectors.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.

        Returns:
            dict: A dictionary containing the scraped data where the keys are the tag names and the values are the scraped text.
            str: If either the soup or selectors are not of the correct type, raises a message indicating the incorrect types.
            Exception: If any other exception occurs during the function execution.
        """
        scraped_data = {}
        try:
            if isinstance(soup, BeautifulSoup) and isinstance(self.selectors, list):
                for selector in self.selectors:
                    elements = soup.select(selector)
                    if elements:
                        for subelement in elements:
                            scraped_data[subelement.name] = (
                                subelement.get_text().replace('\n', ' ').strip()
                            )
                return scraped_data
            else:
                raise ValueError(
                    f'Method get_data(): Both or one of the objects are not of the correct type: Soup: {type(soup)} , Selectors: {type(self.selectors)}',
                )
        except Exception as err:
            print(err.args)

    def scrape(self):
        """
        Method for scraping a website for data using the provided URL and CSS selector.

        Returns:
            The scraped data if successful, otherwise an Exception object.
        """
        try:
            html = self.get_html()
            soup = self.parse_html(html)
            return self.get_data(soup)
        except Exception as err:
            print(err.args)

    def write_data_to_json_file(self, data: dict):
        """
        Writes data to a JSON file.

        Args:
            data (dict): The dict of data to be written to the JSON file.

        Returns:
            str: A message indicating the status of the write operation.
        """
        file_pattern = '^[^.]+.(json)$'

        try:
            if re.match(file_pattern, self.file_name) and isinstance(data, dict):
                file_path = f'{self.file_name}'

                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=4)

                return f'Done writing in file: {self.file_name}'
            return f'Method write_data_to_json_file(): Invalid file name: {self.file_name} or data type: {type(data)}'
        except Exception as err:
            print(err.args)
