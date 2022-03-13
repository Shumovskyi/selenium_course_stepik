from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ELEMENTS_IN_BASKET), "Basket is not empty"
        assert self.is_element_present(*BasketPageLocators.INFO_BASKET_IS_EMPTY), "No text about empty basket"
