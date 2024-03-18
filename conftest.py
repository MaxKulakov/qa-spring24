import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser')
    if browser_name == 'chrome':
        chrome_browser = webdriver.Chrome()
        chrome_browser.implicitly_wait(10)
        return chrome_browser
    elif browser_name == 'firefox':
        firefox_browser = webdriver.Firefox()
        firefox_browser.implicitly_wait(10)
        return firefox_browser
