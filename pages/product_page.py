from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def product_data(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_balance = self.browser.find_element(*ProductPageLocators.PRODUCT_BALANCE).text
        return product_price, product_title, product_balance

    def add_to_basket_product(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def valid_messages_after_add_product_to_basket(self, *args, **kwargs):
        message_price = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE).text
        message_title = self.browser.find_element(*ProductPageLocators.MESSAGE_TITLE).text
        try:
            if message_price == args[0]:
                if message_title == args[1]:
                    return True
            else:
                return False
        except:
            return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCEED_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCEED_MESSAGE), \
            "Success message is not disappeared"