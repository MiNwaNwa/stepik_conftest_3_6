import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait
import time

def test_big_decision(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//")
# Визуально убедимся, что язык корректный
    time.sleep(5)
    WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket")))
    # browser.find_element_by_class_name("btn-add-to-basket")