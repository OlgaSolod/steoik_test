import pytest
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_item_btn(browser):
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    
