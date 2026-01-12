from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from conftest import browser
from element import Element

class Buttons:
    url = 'https://demoqa.com/buttons'

    locator_choose_right_click_button = (By.ID, 'rightClickBtn')
    locator_choose_double_click_button = (By.ID, 'doubleClickBtn')
    locator_choose_click_button = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')

    locator_result_right_click = (By.ID, 'rightClickMessage')
    locator_result_double_click = (By.ID, 'doubleClickMessage')
    locator_result_click = (By.ID, 'dynamicClickMessage')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.url)
        try:
            WebDriverWait(self.browser, 3).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
        except TimeoutException:
            pass

    def choose_double_click_button(self):
        double_click_button = self.browser.find_element(*self.locator_choose_double_click_button)
        return Element(double_click_button)

    def choose_right_click_button(self):
        right_click_button = self.browser.find_element(*self.locator_choose_right_click_button)
        return Element(right_click_button)

    def choose_click_button(self):
        click_button = self.browser.find_element(*self.locator_choose_click_button)
        return Element(click_button)

    def check_right_click(self):
        text = self.browser.find_element(*self.locator_result_right_click).text
        return text

    def check_click(self):
        text = self.browser.find_element(*self.locator_result_click).text
        return text

    def check_double_click(self):
        text = self.browser.find_element(*self.locator_result_double_click).text
        return text