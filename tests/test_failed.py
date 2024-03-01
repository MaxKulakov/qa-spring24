import allure
from pages.search_page import SearchPage


@allure.feature('Search Page. Failed test')
@allure.story('Поиск картины с трамваем, содержащей в названии "Жираф"')
def test_failed_search_artwork(browser):
    try:
        with allure.step('Открытие главной страницы artnow.ru'):
            search_page = SearchPage(browser)
            search_page.open()

        with allure.step('Ввод слова "Жираф" в поисковую строку'):
            search_page.search_input().clear()
            search_page.search_input().send_keys('Жираф')
            
        with allure.step('Нажатие на кнопку поиска и переход на новую страницу'):
            search_page.search_button().click()
            
        assert 'Трамвай' in search_page.first_artwork_name().text or 'трамвай' in search_page.first_artwork_name().text
    except:
        allure.attach(browser.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
        assert False