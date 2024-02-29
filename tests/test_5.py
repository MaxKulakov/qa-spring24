# pytest tests/test_5.py -vx --alluredir results
# pytest -vx --alluredir results    
# allure serve results   

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import allure
from time import sleep
from pages.category_page import CategoryPage


# Перейти в “Ювелирное искусство”, добавить первое изделие в корзину, 
# проверить, что выбранный товар находится в корзине, стоимость товара не изменилась.