# coding =utf-8
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
class Base():

    def __init__(self,driver):
        self.driver = driver

    def open_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def find_element(self,locator):
        element = WebDriverWait(self.driver, timeout=30).until(EC.presence_of_element_located(locator))
        return element

    def click(self,locator):
        self.find_element(locator).click()

    def sendkeys(self,locator,text):
        self.find_element(locator).send_keys(text)


if __name__ == "__main__":
    pass