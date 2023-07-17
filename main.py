import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


endpoint = 'https://www.linkedin.com/jobs/search/?currentJobId=3636493668&f_WT=2&geoId=92000000&keywords=nodejs%20developer&location=Worldwide&refresh=true'
chrome_driver_path = '/Users/cheza/Drivers/chromedriver'
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))

driver.get(endpoint)

link = driver.find_element(by=By.LINK_TEXT, value='Sign in')

link.click()

username_field = driver.find_element(by=By.NAME, value='session_key')
password_field = driver.find_element(by=By.NAME, value='session_password')
signin_button = driver.find_element(by=By.CLASS_NAME, value='btn__primary--large')

username_field.send_keys('')
password_field.send_keys('')
signin_button.click()

time.sleep(3)
apply_button_card = driver.find_element(by=By.CLASS_NAME, value='jobs-apply-button--top-card')
apply_button = apply_button_card.find_element(by=By.TAG_NAME, value='button')
apply_button.click()

footer = driver.find_element(by=By.TAG_NAME, value='footer')
submit_button = footer.find_element(by=By.TAG_NAME, value='button')
submit_button.click()

time.sleep(15)
