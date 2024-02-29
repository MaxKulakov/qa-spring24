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