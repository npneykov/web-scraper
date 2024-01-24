import re

import requests
from bs4 import BeautifulSoup


def get_html(url):
    url_pattern = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"

    try:
        if re.compile(url_pattern).search(url):
            response = requests.get(url)
            return response.text
        return False
    except Exception as err:
        return err


def parse_html(html):
    try:
        if html:
            return BeautifulSoup(html, "html.parser")
        return False
    except Exception as err:
        return err


def extract_data(soup, selectors, title_selector):
    scraped_data = []

    for selector_name, selector in selectors.items():
        elements = soup.select(selector)
        data = [element.text for element in elements]
        title_element = soup.select_one(title_selector)
        scraped_data.append({"title": title_element.text, selector_name: data})

    return scraped_data
