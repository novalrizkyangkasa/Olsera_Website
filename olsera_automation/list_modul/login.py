from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from olsera_automation.default_page.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    def enter_username(self, username):
        self.driver.implicitly_wait(10)
        """Input username to the username field"""
        username_field = self.driver.find_element(By.XPATH, '//input[@placeholder="Email"]')
        username_field.clear()
        username_field.send_keys("rizkynoval5@gmail.com")

    def enter_password(self, password):
        self.driver.implicitly_wait(10)
        """Input password to the password field"""
        password_field = self.driver.find_element(By.XPATH, '//input[@type="password"]')
        password_field.clear()
        password_field.send_keys("noval123")

    def click_login(self):
        self.driver.implicitly_wait(10)
        """Click on the login button"""
        login_button = self.driver.find_element(By.XPATH, '(//button[@type="button"])[1]')
        login_button.click()