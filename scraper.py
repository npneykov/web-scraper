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


def get_data(soup, selector):
    scraped_data = []
    try:
        if soup:
            selector_elements = [soup.find_all(selector)]
            for elements in selector_elements:
                for tags in elements:
                    print(f"Tags:{tags}")
                    scraped_data.append(tags.get_text())
            return scraped_data
        else:
            return False
    except Exception as err:
        return err


def web_scraper(url, selector):
    html = get_html(url)
    soup = parse_html(html)

    return get_data(soup, selector)
