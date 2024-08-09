from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from termcolor import colored

class  WebScraper():
    def __init__(self) -> None:
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)

    def webscraper(self,url):
        # for holding elements found in a form
        self.driver.get(url)
        
        print(colored("------------------------------","light_cyan"))
        print(colored("Meta data","light_yellow"))
        print(colored("------------------------------","light_cyan"))
        self.find_metadeta()
        print(colored("------------------------------","light_cyan"))
        print(colored("Anchor tag","light_yellow"))
        print(colored("------------------------------","light_cyan"))
        self.find_anchor_tag()
        print(colored("------------------------------","light_cyan"))
        print(colored("Link tag","light_yellow"))
        print(colored("------------------------------","light_cyan"))
        self.find_link_tag()
        print(colored("------------------------------","light_cyan"))
        print(colored("Script tag","light_yellow"))
        print(colored("------------------------------","light_cyan"))
        self.find_script_tag()
        print(colored("------------------------------","light_cyan"))
        print(colored("Img tag","light_yellow"))
        print(colored("------------------------------","light_cyan"))
        self.find_img_tag()

    def find_metadeta(self):
        meta_deta =  WebDriverWait(self.driver,10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME,"meta"))
        )
        if meta_deta:
            for meta in meta_deta:
                meta_name = meta.get_attribute("name")
                meta_content = meta.get_attribute("content")
                print(colored(f"[+] Meta name: {meta_name}","green"))
                print(colored(f"[+] Meta content: {meta_content}","green"))
        else:
            print(colored(f"[+] Meta data not found","light_red"))

    def find_anchor_tag(self):
        anchor_tags = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME,"a"))
        )
        if anchor_tags:
            for anchor_tag in anchor_tags:
                anchor_href = anchor_tag.get_attribute("href")
                anchor_text = anchor_tag.text
                print(colored(f"[+] Anchor text: {anchor_text}","green"))
                print(colored(f"[+] Anchor href: {anchor_href}","green"))
        else:
            print(colored(f"[+] Anchor tag not found","light_red"))

    def find_link_tag(self):
        link_tags = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME,"link"))
        )
        if link_tags:
            for link_tag in link_tags:
                lunk_rel = link_tag.get_attribute("rel")
                link_href = link_tag.get_attribute("href")
                print(colored(f"[+] Link rel: {lunk_rel}","green"))
                print(colored(f"[+] Link href: {link_href}","green"))
        else:
            print(colored(f"[+] Link tag not found","light_red"))

    def find_script_tag(self):
        script_tags = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "script"))
        )
        if script_tags:
            for script_tag in script_tags:
                script_src = script_tag.get_attribute("src")
                print(colored(f"[+] Script src: {script_src}","green"))
            for script in script_tags:
                script_text = script.text
                if script_text:
                    print(colored(f"[+] Script: {script_text}","green"))
        else:
            print(colored(f"[+] Script tag not found","light_red"))

    def find_img_tag(self):
        try:
            img_tags = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
            )
            if img_tags:
                for img_tag in img_tags:
                    img_alt = img_tag.get_attribute("alt")
                    img_src = img_tag.get_attribute("src")
                    print(colored(f"[+] Img alt text: {img_alt}", "green"))
                    print(colored(f"[+] Img src: {img_src}", "green"))
                    print("")
            else:
                print(colored("[-] Img tag not found", "light_red"))
                print("")
        except TimeoutException as TE:
            print(colored(f"[-] Error: {TE}","light_red"))


