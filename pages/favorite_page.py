from pages.base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.base_page import BasePage


show_more_button_selector = (By.XPATH, '//*[@id="left_container"]/div/ul[2]/li[15]/div/i')
category_item_button_selector = (By.XPATH, '//*[@id="left_container"]/div/ul[2]/li[3]/a')
first_artwork_name_selector = (By.CSS_SELECTOR, '#sa_container > div:nth-child(3) > a:nth-child(1) > div')
favorite_button_selector = (By.CSS_SELECTOR, '#sa_container > div:nth-child(3) > div.heart')
favorite_page_button_selector = (By.CSS_SELECTOR, 'body > div.topheader > span.fvtico')
first_artwork_name_in_favorite_selector = (By.CSS_SELECTOR, '#sa_container > div.post > a:nth-child(1) > div')


class FavoritePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://artnow.ru')

    def show_more_button(self):
        return self.find(show_more_button_selector)
    
    def category_item_button(self):
        return self.find(category_item_button_selector)
    
    def first_artwork_name(self):
        return self.find(first_artwork_name_selector)
    
    def favorite_button(self):
        return self.find(favorite_button_selector)
    
    def favorite_page_button(self):
        return self.find(favorite_page_button_selector)
    
    def first_artwork_name_in_favorite(self):
        return self.find(first_artwork_name_in_favorite_selector)
    
