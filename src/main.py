from scraper import run_web_scraper, write_data_to_file

if __name__ == "__main__":
    # Example usage
    print(
        write_data_to_file(
            "website_data.json",
            run_web_scraper("https://example.com", ["div", "p", "a"]),
        )
    )
