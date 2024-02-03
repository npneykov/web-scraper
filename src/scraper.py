import json
import re

import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    """
    A function to retrieve the HTML content of a given URL.

    Parameters:
        url (str): The URL of the web page to retrieve.

    Returns:
        str: The HTML content of the web page, or an error message if the URL pattern does not match or an exception occurs.
    """
    url_pattern = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"

    try:
        if re.compile(url_pattern).search(url):
            response = requests.get(url)
            return (
                response.text
                if response.status_code == 200
                else f"Got status code {response.status_code}: {response.reason}"
            )
        else:
            return f"The URL pattern does not match: {url}"
    except Exception as err:
        return err


def parse_html(html: str):
    """
    Parse the given HTML string and return a BeautifulSoup object if the string contains '<html>',
    otherwise return a string indicating invalid HTML.

    Args:
        html (str): The HTML string to be parsed.

    Returns:
        BeautifulSoup: The parsed result if successful, If an exception occurs during parsing, return the exception object.
    """
    try:
        return (
            BeautifulSoup(html, "html.parser")
            if "<html>" in html
            else f"Invalid HTML:\n{html}"
        )
    except Exception as err:
        return err


def get_data(soup: BeautifulSoup, selectors: list):
    """
    Function to scrape data from a BeautifulSoup object using a dict of CSS selectors.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the parsed HTML.
        selectors (list): A list of CSS selectors to extract specific elements from the HTML.

    Returns:
        dict: A dictionary containing the scraped data where the keys are the tag names and the values are the scraped text.
        str: If either the soup or selectors are not of the correct type, a message indicating the incorrect types.
        Exception: If any other exception occurs during the function execution.
    """
    scraped_data = {}
    try:
        if isinstance(soup, BeautifulSoup) and isinstance(selectors, list):
            for selector in selectors:
                elements = soup.select(selector)
                if elements:
                    for subelement in elements:
                        scraped_data[subelement.name] = (
                            subelement.get_text().replace("\n", " ").strip()
                        )
            return scraped_data
        else:
            return f"Both or one of the objects are not of the correct type:\\nSoup: {type(soup)}\\nSelectors: {type(selectors)}"
    except TypeError as type_err:
        return type_err
    except Exception as err:
        return err


def web_scraper(url: str, selectors: list):
    """
    Function to scrape a website for data using the provided URL and CSS selector.

    Args:
        url (str): The URL of the website to scrape.
        selector (str): The CSS selector to locate the desired data on the webpage.

    Returns:
        The scraped data if successful, otherwise an Exception object.
    """
    try:
        html = get_html(url)
        soup = parse_html(html)
        return get_data(soup, selectors)
    except Exception as err:
        return err


def write_data_to_file(file_name: str, data: dict):
    """
    Writes data to a JSON file.

    Args:
        file_name (str): The name of the JSON file to write data to.
        data (dict): The dict of data to be written to the JSON file.

    Returns:
        str: A message indicating the status of the write operation.
    """
    file_pattern = "^[^.]+.(json)$"

    try:
        if re.match(file_pattern, file_name):
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
            return f"Done writing in file: {file_name}"
        return f"Invalid file name: {file_name}. Please provide a valid one."
    except Exception as err:
        return err
