from pages.base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.base_page import BasePage


search_input_selector = (By.XPATH, '//*[@id="MainSearchForm"]/div/div[1]/input[3]')
search_button_selector = (By.XPATH, '//*[@id="MainSearchForm"]/div/div[2]/button')
first_artwork_name_selector = (By.CSS_SELECTOR, '#sa_container > div:nth-child(3) > a:nth-child(1) > div')


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://artnow.ru')

    def search_input(self):
        return self.find(search_input_selector)

    def search_button(self):
        return self.find(search_button_selector)

    def first_artwork_name(self):
        return self.find(first_artwork_name_selector)
    