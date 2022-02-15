from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    # нахождение текста
    str_num1 = num1.text
    str_num2 = num2.text
    # изменение типа данных на инт и нахождение суммы
    int_num1 = int(str_num1)
    int_num2 = int(str_num2)
    answer = int_num1 + int_num2
    str_answer = str(answer)
    # использование метода select для выбора в выпадающем списке
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str_answer)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
