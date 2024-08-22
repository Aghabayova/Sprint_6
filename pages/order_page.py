from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
import generators
import allure


class OrderPage(BasePage):
    @allure.step('Клик на кнопку "Заказать" в шапке главной')
    def click_header_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_HEADER)

    @allure.step('Клик на кнопку "Заказать" в середине главной страницы')
    def click_main_order_btn(self):
        self.click_to_element(MainPageLocators.ORDER_BTN_PAGE)

    @allure.step('Заполнение поля "Имя"')
    def set_name(self):
        name = generators.generate_name()
        self.set_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_last_name(self):
        last_name = generators.generate_lastname()
        self.set_text(OrderPageLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполнение поля "Адрес"')
    def set_address(self):
        address = generators.generate_address()
        self.set_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбор станции метро')
    def set_metro(self):
        station = generators.generate_station()
        self.find_element(OrderPageLocators.METRO_FIELD)
        self.click_to_element(OrderPageLocators.METRO_FIELD)
        locator = self.reformat_locator(OrderPageLocators.STATION_DROP_DOWN, station)
        self.click_to_element(locator)

    @allure.step('Заполнение поля "Телефон"')
    def set_phone(self):
        phone = generators.generate_phone()
        self.set_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_btn(self):
        self.click_to_element(OrderPageLocators.NEXT_BTN)

    @allure.step('Выбор даты доставки')
    def set_date(self, date):
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        self.find_element(date)
        self.click_to_element(date)

    @allure.step('Выбираем срок аренды самоката')
    def set_term(self):
        rental_period = generators.generate_rental_period()
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_DD)
        locator = self.reformat_locator(OrderPageLocators.RENTAL_PERIOD_BUTTON_IN_DD, rental_period)
        self.click_to_element(locator)

    @allure.step('Выбор цвета')
    def set_color(self):
        color = generators.generate_color()
        locator = self.reformat_locator(OrderPageLocators.INPUT_FIELD_COLOR, color)
        self.click_to_element(locator)

    @allure.step('Заполнение поля "Комментарии"')
    def set_comments(self):
        comment = generators.generate_comment()
        self.set_text(OrderPageLocators.COMMENTS, comment)

    @allure.step('Появление модального окна "Заказ оформлен"')
    def check_success_order(self):
        return self.find_element(OrderPageLocators.ORDER_SUCCESS_WINDOW).text

    def create_order(self,
                     date):
        self.set_name()
        self.set_last_name()
        self.set_address()
        self.set_metro()
        self.set_phone()
        self.click_next_btn()
        self.set_date(date)
        self.set_term()
        self.set_color()
        self.set_comments()
        self.click_to_element(OrderPageLocators.ORDER_BTN)
        self.click_to_element(OrderPageLocators.YES_BTN)
