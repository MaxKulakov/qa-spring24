import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser

    firefox_browser = webdriver.Firefox()
    firefox_browser.implicitly_wait(10)
    return firefox_browser
