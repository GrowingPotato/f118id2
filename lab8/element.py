from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

class Element:
    web_element: WebElement
    def __init__(self, web_element: WebElement):
        self.web_element = web_element

    def click(self, browser):
        ActionChains(browser).click(self.web_element).perform()

    def double_click(self, browser):
        ActionChains(browser).double_click(self.web_element).perform()

    def right_click(self, browser):
        ActionChains(browser).context_click(self.web_element).perform()

    def insert_value(self, value: str):
        self.web_element.send_keys(value)