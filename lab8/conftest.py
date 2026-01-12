import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
    options = Options()
    options.page_load_strategy = 'eager'
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    #browser.implicitly_wait(2)
    yield browser
    browser.close()