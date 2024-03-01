from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


show_more_button_selector = (By.XPATH, '//*[@id="left_container"]/div/ul[2]/li[15]/div/i')
category_item_button_selector = (By.XPATH, '//*[@id="left_container"]/div/ul[2]/li[5]/a')
first_artwork_name_selector = (By.CSS_SELECTOR, '#sa_container > div:nth-child(3) > a:nth-child(1) > div')
first_artwork_price_selector = (By.CSS_SELECTOR, '#sa_container > div:nth-child(3) > div.price')
add_to_cart_button_selector = (By.CSS_SELECTOR, '#sa_container > div:nth-child(3) > a:nth-last-of-type(1) > div')
go_to_cart_button_selector = (By.XPATH, '//*[@id="cmodal"]/div/p/button[1]')
cart_artwork_name_selector = (By.XPATH, '//*[@id="cart1127052"]/div[3]/div[1]/a')
cart_artwork_price_selector = (By.XPATH, '//*[@id="cart1127052"]/div[3]/div[5]/div[2]')


class CartPage(BasePage):
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
    
    def first_artwork_price(self):
        return self.find(first_artwork_price_selector)
    
    def add_to_cart_button(self):
        return self.find(add_to_cart_button_selector)
    
    def go_to_cart_button(self):
        return self.find(go_to_cart_button_selector)
    
    def cart_artwork_name(self):
        return self.find(cart_artwork_name_selector)
    
    def cart_artwork_price(self):
        return self.find(cart_artwork_price_selector)
    
    