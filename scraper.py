import re

import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    """
    Function to retrieve the HTML content from a given URL.

    Args:
        url (str): The URL from which to retrieve the HTML content.

    Returns:
        str or bool: The HTML content if the request is successful, False otherwise.
    """
    url_pattern = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"

    try:
        if re.compile(url_pattern).search(url):
            response = requests.get(url)
            return response.text if response.status_code == 200 else False
        return False
    except Exception as err:
        return err


def parse_html(html: str):
    """
    Parse the given HTML string using BeautifulSoup and return the parsed result.

    Args:
        html (str): The HTML string to be parsed.

    Returns:
        BeautifulSoup: The parsed result if successful, False if the HTML string is empty,
        or the exception if an error occurs during parsing.
    """
    try:
        return BeautifulSoup(html, "html.parser") if html else False
    except Exception as err:
        return err


def get_data(soup: BeautifulSoup, selectors: list):
    """
    Function to extract data from a BeautifulSoup object using a list of selectors.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the HTML to extract data from.
        selectors (list): A list of CSS selectors to extract specific elements from the HTML.

    Returns:
        dict: A dictionary containing the scraped data, where the keys are element names and
        the values are the scraped text.
        bool: False if the input parameters are not of the correct type.
        Exception: If any exception occurs during the data extraction process.
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
            return False
    except Exception as err:
        return err


def web_scraper(url: str, selector: str):
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
        return get_data(soup, selector)
    except Exception as err:
        return err


def write_data_to_file(file_name: str, data: list):
    """
    Writes data to a file.

    Args:
        file_name (str): The name of the file to write data to.
        data (list): The list of data to be written to the file.

    Returns:
        str: A message indicating the status of the write operation.
    """
    file_pattern = "^[^.]+.(txt)$"

    try:
        if re.match(file_pattern, file_name):
            with open(file_name, "w") as file:
                for item in data:
                    file.write(f"{item}\n")
            return f"Done writing in file: {file_name}"
        return f"Invalid file name: {file_name}. Please provide a valid one."
    except Exception as err:
        return err
