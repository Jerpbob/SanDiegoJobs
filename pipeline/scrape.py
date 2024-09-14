import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Scraper():
    def __init__(self, driver: webdriver) -> None:
        print('Starting Chrome driver')
        self.driver = driver
        self.axos_html_files = []
        self.intel_html_files = []

    def connect_axos(self) -> None:
        URL = 'https://axos.wd5.myworkdayjobs.com/en-US/Axos'
        self.driver.get(URL)
    
    def connect_intel(self) -> None:
        URL = 'https://intel.wd1.myworkdayjobs.com/External'
        self.driver.get(URL)

    def scrape_axos(self) -> None:
        self.connect_axos()
        pages_left = True
        page_number = 2
        while pages_left:
            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 
                        f'button[aria-label="page {page_number}"]'
                    ))
                )
                button.click()
                page_number += 1
                self.axos_html_files.append(self.driver.page_source)
            except(NoSuchElementException, TimeoutException):
                self.axos_html_files.append(self.driver.page_source)
                pages_left = False
    
    def scrape_intel(self) -> None:
        self.connect_intel()
        pages_left = True
        page_number = 2
        while pages_left:
            try:
                button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.CSS_SELECTOR, 
                        f'button[aria-label="page {page_number}"]'
                    ))
                )
                button.click()
                page_number += 1
                self.intel_html_files.append(self.driver.page_source)
            except(NoSuchElementException, TimeoutException):
                self.intel_html_files.append(self.driver.page_source)
                pages_left = False

    def save_html(self, scraped_html: list[str], company: str) -> None:
        print('Writing html file of', company)
        for html in scraped_html:
            file_name = datetime.now().strftime('%Y%m%H%M%S') + '.html'
            print(file_name)
            with open(f'./raw_html/{company}/{file_name}', 'w') as f:
                f.write(html)
            time.sleep(1)

    def quit_driver(self) -> None:
        print('quitting Chrome driver')
        self.driver.quit()

    def run_all_scrapers(self) -> None:
        self.scrape_axos()
        self.scrape_intel()

        self.quit_driver()

    def save_all_html(self) -> None:
        self.save_html(self.axos_html_files, 'axos')
        self.save_html(self.intel_html_files, 'intel')

'''TODO: Companies to Scrape (Local Only):
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
'''

if __name__ == '__main__':
    scrape_html = Scraper(webdriver.Chrome())
    scrape_html.run_all_scrapers()
    scrape_html.save_all_html()