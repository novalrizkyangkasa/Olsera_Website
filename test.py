from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://dashboard.olsera.co.id/login')

username = driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
username.send_keys('rizkynoval5@gmail.com')

password = driver.find_element(By.XPATH, '//input[@type="password"]')
password.send_keys('noval123')

login_button = driver.find_element(By.XPATH, '(//button[@type="button"])[1]')
login_button.click()

                              
loginstore_button = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, '//body/div[@id="app"]/div/div/div/div/div/div/div/div[1]/button[1]/span[1]'))
)
loginstore_button.click()


katalog_button = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/aside/section/div[2]/ul/li[1]/div/i'))
)
time.sleep(5)
katalog_button.click()

input("Press Enter to close the browser...")
