from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_NAME), "Login user name is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.SING_IN_BUTTON), "Sing in button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password 1 form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password 2 form is not presented"
        assert self.is_element_present(
            *LoginPageLocators.SING_UP_BUTTON), "Sing in button is not presented"
