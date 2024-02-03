from scraper import web_scraper, write_data_to_file

if __name__ == "__main__":
    # Example usage
    print(
        write_data_to_file(
            "website_data.json",
            web_scraper("https://www.example.com", ["div", "p", "a"]),
        )
    )
