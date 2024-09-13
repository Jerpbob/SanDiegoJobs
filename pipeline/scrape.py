import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://axos.wd5.myworkdayjobs.com/en-US/Axos')
time.sleep(5) # Let the user actually see something!
button = driver.find_elements(By.CSS_SELECTOR, 'button[class="css-1jrbae2"]')[0].click()
time.sleep(5) # Let the user actually see something!
driver.quit()