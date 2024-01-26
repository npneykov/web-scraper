import re

import requests
from bs4 import BeautifulSoup


def get_html(url: str) -> any:
    url_pattern = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"

    try:
        if re.compile(url_pattern).search(url):
            response = requests.get(url)
            return response.text if response.status_code == 200 else False
        return False
    except Exception as err:
        return err


def parse_html(html: str) -> any:
    try:
        return BeautifulSoup(html, "html.parser") if html else False
    except Exception as err:
        return err


def get_data(soup: BeautifulSoup, selector: str) -> any:
    scraped_data = []
    try:
        if isinstance(soup, BeautifulSoup):
            selector_elements = [soup.find_all(selector)]
            for elements in selector_elements:
                [scraped_data.append(tags.get_text()) for tags in elements]
            return scraped_data
        else:
            return False
    except Exception as err:
        return err


def web_scraper(url: str, selector: str) -> any:
    try:
        html = get_html(url)
        soup = parse_html(html)
        return get_data(soup, selector)
    except Exception as err:
        return err
