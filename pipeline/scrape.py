import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Scraper():
    def __init__(self, driver):
        print('Starting Chrome driver')
        self.driver = driver

    def scrape_axos(self):
        URL = 'https://axos.wd5.myworkdayjobs.com/en-US/Axos'
        time.sleep(5)
        self.driver.get(URL)
        html_files = [self.driver.page_source]
        pages_left = True
        page_number = 2
        while pages_left:
            try:
                time.sleep(5)
                print('Finding button', page_number)
                button = self.driver.find_element(
                    By.CSS_SELECTOR, 
                    f'button[aria-label="page {page_number}"]'
                ).click()
                print('Button clicked')
                page_number += 1
                print('Appending html source')
                html_files.append(self.driver.page_source)
            except(NoSuchElementException):
                pages_left = False
                print(len(html_files))
                print('Done')
        return html_files

    def save_axos_html(self):
        for html in self.scrape_axos():
            file_name = datetime.now().strftime('%Y%m%H%M%S') + '.html'
            print(file_name)
            with open(f'./raw_html/axos/{file_name}', 'w') as f:
                print('Writing html file')
                f.write(html)
            time.sleep(1)

    
    def quit_driver(self):
        print('quitting Chrome driver')
        self.driver.quit()

            

        

'''TODO: Companies to Scrape (Local Only):
    Axos Bank
    Intel
    Illumina
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
    scrape_html.save_axos_html()
    scrape_html.quit_driver()