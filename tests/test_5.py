import allure
from pages.cart_page import CartPage


# Перейти в “Ювелирное искусство”, добавить первое изделие в корзину, 
# проверить, что выбранный товар находится в корзине, стоимость товара не изменилась.

@allure.feature('Cart Page')
@allure.story('Проверка нахождения товара в корзине')
def test_cart_artwork(browser):
    try:
        with allure.step('Открытие главной страницы artnow.ru'):
            cart_page = CartPage(browser)
            cart_page.open()

        with allure.step('Переход в категорию "Ювелирное искусство"'):
            cart_page.show_more_button().click()
            cart_page.category_item_button().click()

        with allure.step('Добавление первого изделия в корзину и запоминание его названия и цены'):
            artwork_name = cart_page.first_artwork_name().text
            artwork_price = cart_page.first_artwork_price().text
            cart_page.add_to_cart_button().click()

        with allure.step('Переход на страницу корзины'):
            cart_page.go_to_cart_button().click()
            
        assert cart_page.cart_artwork_name().text in artwork_name
        assert artwork_price == cart_page.cart_artwork_price().text
    except:
        allure.attach(browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        assert False
