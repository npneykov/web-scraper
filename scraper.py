import re

import requests
from bs4 import BeautifulSoup


def get_html(url: str):
    url_pattern = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"

    try:
        if re.compile(url_pattern).search(url):
            response = requests.get(url)
            return response.text if response.status_code == 200 else False
        return False
    except Exception as err:
        return err


def parse_html(html: str):
    try:
        return BeautifulSoup(html, "html.parser") if html else False
    except Exception as err:
        return err


def get_data(soup: BeautifulSoup, selectors: list):
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
    try:
        html = get_html(url)
        soup = parse_html(html)
        return get_data(soup, selector)
    except Exception as err:
        return err


def write_data_to_file(file_name: str, data: list):
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
