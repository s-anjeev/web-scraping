from termcolor import colored
import argparse
import re
import os
from web_scraper import WebScraper

class URLAnalyzer:
    def __init__(self) -> None:
        # creating object of WebScraper class
        self.scraper = WebScraper()
        # calling get_user_input()
        self.get_user_input()

    # this function will take input from user
    def get_user_input(self):
        parser = argparse.ArgumentParser(description="Usage")
        parser.add_argument('-u', '--url', type=str, help=colored("Single URL you want to analyze.", "green"))
        parser.add_argument('-f', '--file', type=str, help=colored("File containing multiple URLs to analyze.", "green"))
        args = parser.parse_args()

        if args.url and args.file:
            print(colored("[-] Invalid operation: Choose either a URL or a file, not both.", "light_red"))
            exit()

        if args.url:
            url = args.url
            print(colored(f"[+] Analyzing URL: {url}","yellow"))
            self.is_valid_url(url)

        if args.file:
            file_path = args.file
            self.file_exists(file_path)

    # check if URL is valid
    def is_valid_url(self, url):
        # Regular expression pattern to match URLs
        url_pattern = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https:// or ftp://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(url_pattern, url):
            print(colored(f"[+] Valid URL: {url}", "green"))
            
            # calling webscraper() function and passing a valid url as argument
            self.scraper.webscraper(url)
        else:
            print(colored(f"[-] Invalid URL: {url}", "light_red"))
    
    def file_exists(self, file_path):
        # Check if the file ends with .txt
        pattern = r'\.txt$'
        match = re.search(pattern, file_path)

        if not match:
            print(colored("[-] Invalid file, check your file path.", "light_red"))
            print(colored("[-] Only .txt files are allowed.", "light_red"))
            return

        # Check if the file exists with an absolute path
        if os.path.isfile(file_path):
            print(colored(f"[+] Analyzing file: {file_path}", "yellow"))
            # sorting unique urls
            self.unique_urls(file_path)
            return

        # Check if the file exists in the current directory
        current_dir = os.getcwd()
        complete_file_path = os.path.join(current_dir, file_path)
        if os.path.isfile(complete_file_path):
            print(colored(f"[+] Analyzing file: {complete_file_path}", "yellow"))

            # sorting unique urls
            self.unique_urls(complete_file_path)
            return

        # Error message if the file is not found
        print(colored("[-] File not found, check your file path.", "light_red"))

    # this function will remove duplicate urls from file
    def unique_urls(self,file_path):
        try:
            # opening file in read mode
            with open(file_path,'r') as file:
                lines = file.readlines()
                unique_lines = list(dict.fromkeys(line.strip() for line in lines))
            
            # Open the file in write mode
            with open(file_path,'w') as file:
                for url in unique_lines:
                    file.write(url + '\n')

            # read urls from file
            self.reading_url_from_file(file_path)

        except FileNotFoundError as f_er:
            print(colored(f"[-] Error: {f_er}","light_red"))
        except Exception as e:
            print(colored(f"[-] Error: {e}","light_red"))

    # reading urls from file line by line
    def reading_url_from_file(self,file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    url = line.strip()
                    # pass url through regex to check wether its a valid url or not
                    self.is_valid_url(url)
        except FileNotFoundError as f_er:
            print(colored(f"[-] Error: {f_er}","light_red"))
        except Exception as e:
            print(colored(f"[-] Error: {e}","light_red"))

def main():
    print("")
    print(colored("WebScraper 101","light_cyan"))
    print("")
    print(colored("***************************************","light_yellow"))
    print("")
    obj = URLAnalyzer()

if __name__ == "__main__":
    main()

# Potential Enhancements:
# Enhanced Error Handling: You might consider adding more specific exception handling to cover other potential issues, such as network errors or invalid URLs that don't lead to a valid webpage.
# Customization: Allowing the user to specify which tags they want to scrape via command-line arguments could add flexibility.
# Performance Improvements: For large-scale scraping, consider optimizing by parallelizing requests or reducing the amount of data processed.