from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, "//input[@placeholder='* Имя']"
    LAST_NAME_FIELD = By.XPATH, "//input[@placeholder='* Фамилия']"
    ADDRESS_FIELD = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    METRO_FIELD = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    STATION_DROP_DOWN = By.XPATH, '//*[text()="{}"]'
    INPUT_FIELD_COLOR = By.XPATH, '//*[@id="{}"]'
    PHONE_FIELD = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    NEXT_BTN = By.XPATH, "//button[text()='Далее']"
    DATE_FIELD = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    DATE_1 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--014']"
    DATE_2 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015']"
    RENTAL_PERIOD_DD = By.XPATH, '//div[@class="Dropdown-control"]'
    RENTAL_PERIOD_BUTTON_IN_DD = By.XPATH, '//*[text()="{}"]'
    COMMENTS = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    ORDER_BTN = By.XPATH, '//*[contains(@class,"Order_Buttons")]//button[text()="Заказать"]'
    YES_BTN = By.XPATH, "//button[text()='Да']"
    ORDER_SUCCESS_WINDOW = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"