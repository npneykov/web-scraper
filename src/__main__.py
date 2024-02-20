from web_scraper import WebScraper

if __name__ == '__main__':
    # Example usage
    web_scraper = WebScraper(
        'https://example.com', ['div', 'p', 'a'], 'scraped_data.json'
    )
    data = web_scraper.scrape()
    print(web_scraper.write_data_to_json_file(data))
