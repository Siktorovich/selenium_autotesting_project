from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def valid_basket_data(self, *args, **kwargs):
        basket_price = self.browser.find_element(*BasketPageLocators.BASKET_PRICE).text.strip()
        basket_title = self.browser.find_element(*BasketPageLocators.BASKET_TITLE).text
        try:
            if basket_price == args[0]:
                if basket_title == args[1]:
                    return True
            else:
                return False
        except:
            return False