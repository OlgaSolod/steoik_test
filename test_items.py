from selenium.webdriver.common.by import By
import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_item_btn_is_on_the_page(browser):
    browser.get(link)

    assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-add-to-basket'), 'There is no element \'add to basket\' on the page'
