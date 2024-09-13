import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://axos.wd5.myworkdayjobs.com/en-US/Axos')
time.sleep(5) # Let the user actually see something!
with open('./raw_html/html1.html', 'w') as f:
    f.write(driver.page_source)
button = driver.find_elements(By.CSS_SELECTOR, 'button[aria-label="page 2"]')[0].click()
with open('./raw_html/html2.html', 'w') as f:
    f.write(driver.page_source)
time.sleep(5) # Let the user actually see something!
driver.quit()