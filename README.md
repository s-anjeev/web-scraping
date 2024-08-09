# Web Scraper

## Overview
This project consists of a Python-based tool that allows you to analyze URLs by validating them and scraping specific HTML elements from the webpages. It supports both single URL analysis and bulk analysis through a file containing multiple URLs. The script leverages Selenium for web scraping and argparse for command-line argument handling.

## Features
1. Single URL Analysis: Analyze and scrape data from a single URL.
2. Bulk URL Analysis: Analyze and scrape data from multiple URLs provided in a .txt file.
3. Validation: Checks if the URLs are valid and removes duplicates from the file.
4. Web Scraping: Extracts meta tags, anchor tags, link tags, script tags, and image tags from webpages.


## Usage
Run the script with the following command-line arguments:

1. Analyze a single URL:
```python scraper.py -u http://example.com```

2. Analyze URLs from a File:
```python scraper.py -f urls.txt```