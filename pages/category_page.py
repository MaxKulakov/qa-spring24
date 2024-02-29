from pages.base_page import BasePage
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.base_page import BasePage


show_more_button_selector = (By.XPATH, '//*[@id="left_container"]/div/ul[2]/li[15]/div/i')
category_item_button_selector = (By.XPATH, '//*[@id="left_container"]/div/ul[2]/li[8]/a')
filter_button_selector = (By.XPATH, '//*[@id="genre257"]')
submit_filter_button_selector = (By.XPATH, '//*[@id="applymsg"]')
artwork_name_selector = (By.XPATH, '//*[text()="Трамвайный путь"]')
artwork_style_selector = (By.XPATH, '//*[@id="main_container"]/div[3]/div[2]/div[5]/a')


class CategoryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://artnow.ru')

    def show_more_button(self):
        return self.find(show_more_button_selector)
    
    def category_item_button(self):
        return self.find(category_item_button_selector)
    
    def filter_button(self):
        return self.find(filter_button_selector)

    def submit_filter_button(self):
        return self.find(submit_filter_button_selector)

    def find_artwork_name(self):
        return self.find(artwork_name_selector)
    
    def check_artwork_style(self):
        return self.find(artwork_style_selector)


