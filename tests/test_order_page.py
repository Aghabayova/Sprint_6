from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from data import OrderData
import allure


class TestOrderPage:
    @allure.title('Проверка оформления заказа через кнопку "Заказать" в шапке главной страницы')
    def test_create_order_header_btn(self, driver):
        main_page = MainPage(driver) #Создание экземпляра класса MainPage
        order_page = OrderPage(driver) #Создание экземпляра класса OrderPage
        main_page.get_cookies(MainPageLocators.COOKIES_BTN)
        order_page.click_header_order_btn()
        order_page.create_order(OrderPageLocators.DATE_1)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text

    @allure.title('Проверка оформления заказа через кнопку "Заказать" в середине главной страницы')
    def test_create_order_main_page_btn(self, driver):
        main_page = MainPage(driver) #Создание экземпляра класса MainPage
        order_page = OrderPage(driver) #Создание экземпляра класса OrderPage
        main_page.get_cookies(MainPageLocators.COOKIES_BTN)
        order_page.click_main_order_btn()
        order_page.create_order(OrderPageLocators.DATE_2)
        text = order_page.check_success_order()
        assert 'Заказ оформлен' in text
