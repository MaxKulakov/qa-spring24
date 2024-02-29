# pytest tests/test_4.py -vx --alluredir results
# pytest -vx -n=4 --alluredir results
# allure serve results   

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.search_page import SearchPage


# Ввести в поисковую строку «Жираф», проверить, 
# что название первой картины содержит слово «Жираф».

@allure.feature('Search Page')
@allure.story('Поиск картины, содержащей в названии "Жираф"')
def test_search_artwork(browser):
    with allure.step('Открытие главной страницы artnow.ru'):
        search_page = SearchPage(browser)
        search_page.open()

    with allure.step('Ввод слова "Жираф" в поисковую строку'):
        search_page.search_input().clear()
        search_page.search_input().send_keys('Жираф')
        
    with allure.step('Нажатие на кнопку поиска и переход на новую страницу'):
        search_page.search_button().click()

    assert 'Жираф' or 'жираф' in search_page.find_artwork_name().text
    allure.attach(browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)