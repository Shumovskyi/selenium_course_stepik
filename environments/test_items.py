from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_basket_button is not None, "Button is not found"