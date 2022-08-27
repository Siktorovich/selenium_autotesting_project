from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'basket')


class BasketPageLocators():
    BASKET_TITLE = (By.CSS_SELECTOR, 'div.basket-items h3 > a')
    BASKET_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')
    BASKET_EMPTY_TEXT = (By.XPATH, '//p[contains(text(),"empty")]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class MainPageLocators():
    pass


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_BALANCE = (By.CSS_SELECTOR, 'p.instock')
    MESSAGE_PRICE = (By.CSS_SELECTOR, 'div#messages > div.alert-info strong')
    MESSAGE_TITLE = (By.CSS_SELECTOR, 'div#messages > div.alert-success strong')
    SUCCEED_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')


