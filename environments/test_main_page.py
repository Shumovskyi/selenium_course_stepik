import time
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage

#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
#    page = BasePage(browser, link)
#    page.open()
#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()

#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
#    page = BasePage(browser, link)
#    page.open()
#    page.should_be_login_link()


#def test_guest_should_see_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#    page = LoginPage(browser, link)
#    page.open()
#    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_product_in_basket()

