from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait
from element import Element

class TextBox:
    url = 'https://demoqa.com/text-box'

    locator_input_name = (By.ID, 'userName')
    locator_input_email = (By.ID, 'userEmail')
    locator_input_current_address = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/textarea')
    locator_input_permanent_address = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea')

    locator_submit_button = (By.ID, 'submit')

    locator_output_name = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[1]')
    locator_output_email = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[2]')
    locator_output_current_address = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[3]')
    locator_output_permanent_address = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[4]')

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

    def select_input_field_name(self):
        name_field = self.browser.find_element(*self.locator_input_name)
        return Element(name_field)

    def select_input_field_email(self):
        email_field = self.browser.find_element(*self.locator_input_email)
        return Element(email_field)

    def select_input_field_current_address(self):
        current_address_field = self.browser.find_element(*self.locator_input_current_address)
        return Element(current_address_field)

    def select_input_permanent_address(self):
        permanent_address_field = self.browser.find_element(*self.locator_input_permanent_address)
        return Element(permanent_address_field)

    def select_submit_button(self):
        submit_button = self.browser.find_element(*self.locator_submit_button)
        return Element(submit_button)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, 250)")

    def get_result(self):
        data_list = []

        name_result = (self.browser.find_element(*self.locator_output_name)).text
        name_result = re.search(pattern=r'Name:(.{0,})', string=name_result).group(1)
        data_list.append(name_result)

        email_result = (self.browser.find_element(*self.locator_output_email)).text
        email_result = re.search(pattern=r'Email:(.{0,})', string=email_result).group(1)
        data_list.append(email_result)

        current_address_result = (self.browser.find_element(*self.locator_output_current_address)).text
        current_address_result = re.search(pattern='Current Address :(.{0,})', string=current_address_result).group(1)
        data_list.append(current_address_result)

        permanent_address_result = (self.browser.find_element(*self.locator_output_permanent_address)).text
        permanent_address_result = re.search(pattern='Permananet Address :(.{0,})', string=permanent_address_result).group(1)
        data_list.append(permanent_address_result)

        return data_list