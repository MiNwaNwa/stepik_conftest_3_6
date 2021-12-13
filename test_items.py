import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait
import time

def test_correct_language_page(browser):
    # Открываем страницу по ссылке
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207//")
# Визуально убедимся, что язык корректный
    time.sleep(15)
# Находим нужную кнопку по классу и убеждаемся, что она станет кликабельной
    button_basket = WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket")))
# Проверим что результат поиска элемента не пустой
    assert button_basket is not None
