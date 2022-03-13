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
        alert_check = self.browser.find_element(*ProductPageLocators.MASSAGE_NAME_OF_PRODUCT)
        product_name = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        assert alert_check.text == product_name.text, "Text with product in massage is not correct"
        assert add_to_basket_massage.text == price.text, "Text with price in massage is not correct"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSAGE_NAME_OF_PRODUCT), \
            "Success message is presented, but should not be"

    def massage_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MASSAGE_NAME_OF_PRODUCT), "Massage is not disappeared"
