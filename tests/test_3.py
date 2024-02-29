# pytest tests/test_3.py -vx --alluredir results
# pytest -vx --alluredir results    
# allure serve results   

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.category_page import CategoryPage


# Перейти в “Батик”, добавить первую картину в избранное, 
# проверить, что выбранная картина сохранилась в разделе «Избранное».