# pytest tests/test_3.py -vx --alluredir results
# pytest -vx -n=4 --alluredir results
# allure serve results   

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.favorite_page import FavoritePage


# Перейти в “Батик”, добавить первую картину в избранное, 
# проверить, что выбранная картина сохранилась в разделе «Избранное».

@allure.feature('Favorite Page')
@allure.story('Проверка сохранения картины в избранном')
def test_check_favorite_artwork(browser):
    with allure.step('Открытие главной страницы artnow.ru'):
        favorite_page = FavoritePage(browser)
        favorite_page.open()

    with allure.step('Раскрытие меню навигации и переход в категорию "Батик"'):
        favorite_page.show_more_button().click()
        favorite_page.category_item_button().click()
        
    with allure.step('Добавление первой картины в избранное и запоминание её названия'):
        artwork_name = favorite_page.first_artwork_name().text
        favorite_page.favorite_button().click()

    with allure.step('Переход на страницу избранного'):
        favorite_page.favorite_page_button().click()

    assert artwork_name == favorite_page.first_artwork_name_in_favorite().text
    allure.attach(browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
