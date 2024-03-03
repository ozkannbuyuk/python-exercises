from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

username = "xxx"
password = "xxx"

next_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div'
password_input_css = '[autocomplete="current-password"]'

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.twitter.com/login'
driver.get(url)
wait = WebDriverWait(driver, 20)

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="username"]'))).send_keys(username)

next_button = wait.until(EC.presence_of_element_located((By.XPATH, next_button_xpath)))
next_button.click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, password_input_css))).send_keys(password)

login_button = wait.until(EC.presence_of_element_located((By.XPATH, login_button_xpath)))

login_button.click()
