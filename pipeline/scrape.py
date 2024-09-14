import time
from typing import List
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Scraper:
    """
    Scrapes html from job sites into their respective folders
    """

    def __init__(self, driver: webdriver) -> None:
        print("Starting Chrome driver")
        self.driver = driver

    def connect_axos(self) -> None:
        # connect to axos bank job site
        URL = "https://axos.wd5.myworkdayjobs.com/en-US/Axos"
        self.driver.get(URL)

    def connect_intel(self) -> None:
        # connect to intel job site
        URL = "https://intel.wd1.myworkdayjobs.com/External"
        self.driver.get(URL)

    def scrape_axos(self) -> None:
        self.connect_axos()
        self.axos_html_files = []

        pages_left = True
        page_number = 2
        while pages_left:
            # add html to html_files after every click to next page
            try:
                css_selector = f'button[aria-label="page {page_number}"]'
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, css_selector)
                    )
                )
                button.click()
                page_number += 1
                self.axos_html_files.append(self.driver.page_source)
            except TimeoutException:
                # after exception append last html into html_files
                self.axos_html_files.append(self.driver.page_source)
                pages_left = False

    def scrape_intel(self) -> None:
        self.connect_intel()
        self.intel_html_files = []

        pages_left = True
        page_number = 2
        while pages_left:
            # add html to html_files after every click to next page
            try:
                css_selector = f'button[aria-label="page {page_number}"]'
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, css_selector)
                    )
                )
                button.click()
                page_number += 1
                self.intel_html_files.append(self.driver.page_source)
            except TimeoutException:
                # after exception append last html into html_files
                self.intel_html_files.append(self.driver.page_source)
                pages_left = False

    def save_html(self, scraped_html: List[str], company: str) -> None:
        print("Writing html file of", company)
        for html in scraped_html:
            file_name = datetime.now().strftime("%Y%m%H%M%S") + ".html"
            print(file_name)
            with open(f"./raw_html/{company}/{file_name}", "w") as f:
                f.write(html)
            time.sleep(1)

    def quit_driver(self) -> None:
        print("quitting Chrome driver")
        self.driver.quit()

    def run_all_scrapers(self) -> None:
        """
        Runs all current scrapers then quits current driver
        """
        self.scrape_axos()
        self.scrape_intel()

        self.quit_driver()

    def save_all_html(self) -> None:
        self.save_html(self.axos_html_files, "axos")
        self.save_html(self.intel_html_files, "intel")


"""TODO: Companies to Scrape (Local Only):
    Axos Bank**
    Intel**
    Xifin, Inc.
    Intuit
    Viasat
    SanDag
    Qualcomm
    Amazon
    SDGE
    General Atomics
"""

if __name__ == "__main__":
    scrape_html = Scraper(webdriver.Chrome())
    scrape_html.run_all_scrapers()
    scrape_html.save_all_html()
