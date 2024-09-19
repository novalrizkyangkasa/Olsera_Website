from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """Wait for element to be present and return it"""
        return WebDriverWait(self.driver, time).until(
            ExpectedConditions.presence_of_element_located(locator)
        )

    def navigate_to(self, url):
        """Navigate to a given URL"""
        self.driver.get(url)

    def get_title(self):
        """Get the title of the page"""
        return self.driver.title
