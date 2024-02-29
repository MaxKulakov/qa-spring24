# pytest tests/test_4.py -vx --alluredir results
# pytest -vx --alluredir results    
# allure serve results   

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.category_page import CategoryPage


# Ввести в поисковую строку «Жираф», проверить, 
# что название первой картины содержит слово «Жираф».