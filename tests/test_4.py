import allure
from pages.search_page import SearchPage


# Ввести в поисковую строку «Жираф», проверить, 
# что название первой картины содержит слово «Жираф».

@allure.feature('Search Page')
@allure.story('Поиск картины, содержащей в названии "Жираф"')
def test_search_artwork(browser):
    try:
        with allure.step('Открытие главной страницы artnow.ru'):
            search_page = SearchPage(browser)
            search_page.open()

        with allure.step('Ввод слова "Жираф" в поисковую строку'):
            search_page.search_input().clear()
            search_page.search_input().send_keys('Жираф')
            
        with allure.step('Нажатие на кнопку поиска и переход на новую страницу'):
            search_page.search_button().click()

        assert 'Жираф' in search_page.first_artwork_name().text or 'жираф' in search_page.first_artwork_name().text
    except:
        allure.attach(browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        assert False