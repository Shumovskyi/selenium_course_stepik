from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_massage(self):
        add_to_basket_massage = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MASSAGE)
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        massage = add_to_basket_massage.text
        assert massage == f"Your basket total is now {price.text}", "Text in massage is not correct"


