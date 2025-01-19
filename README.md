
# Web Scraper

A generic web scraper with a graphical user interface (GUI) designed to extract and process data from websites efficiently.

## Features

- **User-Friendly GUI**: Interact with the scraper through an intuitive graphical interface.

- **Customizable Scraping Parameters**: Define target URLs, data fields, and scraping frequency.

- **Data Export**: Save scraped data in various formats such as CSV, JSON, or Excel.

- **Error Handling**: Robust mechanisms to handle exceptions and ensure continuous operation.

## Prerequisites

- **Python 3.8+**: Ensure Python is installed on your system.

- **Dependencies**: Install required packages using the provided `requirements.txt`.

##

## Installation

1.**Clone the Repository**:

`git clone https://github.com/npneykov/web-scraper.git`

2.**Navigate to the Project Directory**:

`cd web-scraper`

3.**Set Up a Virtual Environment** (Optional but recommended):

- **For Windows**:

`python -m venv <venv name>`

`source <venv name>\Scripts\activate`

- **For Linux**:

`python -m venv <venv name>`

`source <venv name>/bin/activate`

4.**Install Dependencies**:

`pip install -r requirements.txt`

## Usage

- **Run the Application**:

`python src/main.py`

- **Using the GUI**:

- **Enter Target URL**: Specify the website you wish to scrape.

- **Select Data Fields**: Choose the specific data points to extract.

- **Set Scraping Parameters**: Configure options like frequency and depth.

- **Start Scraping**: Click the 'Start' button to initiate the process.

- **Exporting Data**:

- After scraping, use the 'Export' option to save data in your preferred format.

## Docker Deployment

A `Dockerfile` is included for containerized deployment.

1. **Build the Docker Image**:

`docker compose up --build`.

Access the application through your web browser at `http://localhost:8000`.

# Deploying your application to the cloud

First, build your image, e.g.: `docker build -t myapp .`.

If your cloud uses a different CPU architecture than your development

machine (e.g., you are on a Mac M1 and your cloud provider is amd64), you'll want to build the image for that platform, e.g.:

`docker build --platform=linux/amd64 -t myapp .`.

Then, push it to your registry, e.g. `docker push myregistry.com/myapp`.

## Testing

Unit tests are located in the `tests/unit` directory.

1. **Run Tests**:

`pytest tests/unit`

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/npneykov/web-scraper/blob/main/LICENSE) file for details.
