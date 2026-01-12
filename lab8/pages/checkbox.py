from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from element import Element

class Checkbox:
    url = 'https://demoqa.com/checkbox'

    locator_expand_button = (By.CSS_SELECTOR, "svg.rct-icon.rct-icon-expand-all")
    locator_checkbox_button = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/ol/li/ol/li[2]/ol/li[2]/ol/li[1]/span/label')
    locator_result_field = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/span[2]')

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

    def select_expand_button(self):
        button = self.browser.find_element(*self.locator_expand_button)
        return Element(button)

    def select_checkbox_button(self):
        button = self.browser.find_element(*self.locator_checkbox_button)
        return Element(button)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 250)")

    def get_result(self):
        result = self.browser.find_element(*self.locator_result_field).text
        return result