from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента на страницы и ожидание загрузки')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Клик на элемент')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step('Ввод текста в поле')
    def set_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Скролл страницы до нужного элемента')
    def scroll(self, locator):
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Принимаем куки')
    def get_cookies(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).click()

    @allure.step('Получение url страницы')
    def wait_navigating_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Форматирование локатора')
    def reformat_locator(self, locator, number):
        method, locator = locator
        locator = locator.format(number)
        return method, locator
