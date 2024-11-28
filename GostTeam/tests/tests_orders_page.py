import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
@allure.epic('Тестирование элементов сайта')
@allure.feature('_')

#Вот эта реализация мне нравится больше всего, чем дерганье функций open_orders, email_input и т.д. Смысла я в этом не вижу,
#т.к для каждого теста приходится создавать новые функции в папках main_page_elements и gostteam_page.
#Не понимаю в чем смысл этого, если можно весь тест расписать в этом файле методом ниже
# def tests_site():
#     driver = webdriver.Firefox()
#     driver.get('https://gost.team/orders')
#     element = driver.find_element(By.XPATH, '//*[@id="input_1496238230199"]')
#     placeholder_text = element.get_attribute('placeholder')
#     assert placeholder_text == "Ваш e-mail", f"Ожидалось 'Ваш e-mail', но получено '{placeholder_text}'"
#     driver.quit()



class TestGostTeamPage:

    @pytest.fixture(autouse=True)
    def setup(self, gost_team_page):
        self.gost_team_page = gost_team_page
        self.gost_team_page.open_orders()  # Открытие страницы с заказами до каждого теста

    @allure.story('Тестирование элемента email')
    def test_email_input(self):
        with allure.step('Проверка поиска элемент поля ввода e-mail'):
            email_input = self.gost_team_page.elems.email_input
        with allure.step('Проверка получения текста плейсхолдера для поля ввода'):
            placeholder_text = email_input.get_attribute('placeholder')
        with allure.step('Сравниваем полученный текст с ожидаемым значением'):
            assert placeholder_text == "Ваш e-mail", f"Ожидалось 'Ваш e-mail', но получено '{placeholder_text}'"
        print(f"Ожидалось 'Ваш e-mail', но получено '{placeholder_text}'")

    @allure.story('Тестирование элемента name')
    def test_name_input(self):
        with allure.step('Проверка поиска элемент поля ввода name'):
            name_input = self.gost_team_page.elems.name_input
        with allure.step('Проверка получения текста плейсхолдера для поля ввода'):
            placeholder_text = name_input.get_attribute('placeholder')
        with allure.step('Сравниваем полученный текст с ожидаемым значением'):
            assert placeholder_text == "Ваше имя",  f"Ожидалось 'Ваше имя', но получено '{placeholder_text}'"
        print(f"Ожидалось 'Ваше имя', но получено '{placeholder_text}'")

    @allure.story('Тестирование элемента telegram')
    def test_telegram_input(self):
        with allure.step('Проверка поиска элемент поля ввода telegram'):
            telegram_input = self.gost_team_page.elems.telegram_input
        with allure.step('Проверка получения текста плейсхолдера для поля ввода'):
            placeholder_text = telegram_input.get_attribute('placeholder')
        with allure.step('Сравниваем полученный текст с ожидаемым значением'):
            assert placeholder_text == "Telegram", f"Ожидалось 'Telegram', но получено '{placeholder_text}'"
        print(f"Ожидалось 'Telegram', но получено '{placeholder_text}'")

    @allure.story('Тестирование элемента comment')
    def test_comment_input(self):
        with allure.step('Проверка поиска элемент поля ввода comment'):
            comment_input = self.gost_team_page.elems.comment_input
        with allure.step('Проверка получения текста плейсхолдера для поля ввода'):
            placeholder_text = comment_input.get_attribute('placeholder')
        with allure.step('Сравниваем полученный текст с ожидаемым значением'):
            assert placeholder_text == "Ваш комментарий", f"Ожидалось 'Ваш комментарий', но получено '{placeholder_text}'"
        print(f"Ожидалось 'Ваш комментарий', но получено '{placeholder_text}'")

    @allure.story('Тестирование элемента sent_button')
    def test_sent_button_is_visibility(self):
        with allure.step('Проверка поиска кнопки sent_button'):
            sent_button = self.gost_team_page.elems.sent_button
        with allure.step('Проверка наличия кнопки sent_button'):
            assert sent_button is not None
        with allure.step('Сравниваем найденную кнопку'):
            assert sent_button.aria_role == 'button', f"Ожидалось 'button', но получено '{sent_button.aria_role}'"
        print(f"Ожидалось 'button', но получено '{sent_button.aria_role}'")
