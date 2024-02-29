# pytest tests/test_2.py -vx --alluredir results
# pytest -vx --alluredir results    
# allure serve results   

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.category_page import CategoryPage


# Перейти в “Вышитые картины”, произвести поиск по жанру «Городской пейзаж», 
# открыть подробности картины “Трамвайный путь”, проверить, что стиль картины «Реализм».

@allure.feature('Category Page')
@allure.story('Проверка стиля картины "Трамвайный путь"')
def test_check_artwork_with_category(browser):
    with allure.step('Открытие главной страницы artnow.ru'):
        category_page = CategoryPage(browser)
        category_page.open()
    
    with allure.step('Раскрытие меню навигации и переход в категорию "Вышитые картины"'):
        category_page.show_more_button().click()
        category_page.category_item_button().click()
        
    with allure.step('Поиск по жанру "Городской пейзаж"'): 
        category_page.filter_button().click()   
        category_page.submit_filter_button().click()
    
    with allure.step('Переход внутрь картины'):
        category_page.find_artwork_name().click()

    assert 'Реализм' == category_page.check_artwork_style().text
    allure.attach(browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
