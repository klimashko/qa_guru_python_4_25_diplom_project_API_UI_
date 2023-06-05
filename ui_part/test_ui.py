import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser

import requests

# def test_admin_something(setup_browser):
#     url = "https://automationintesting.online/#/admin"
#     login_data = {
#         "login": "admin",
#         "password": "password"
#     }
#
#     # Отправка POST-запроса для входа в систему
#     response = requests.post(url, data=login_data)
#
#     time.sleep(3)
#
#     # Проверка статуса ответа
#     if response.status_code == 200:
#         print("Вход выполнен успешно!")
#     else:
#         print("Ошибка при выполнении входа:", response.status_code)


def test_send_client_message(browser_management):
    browser.open('/')
    time.sleep(3)
    browser.element(".btn.btn-primary").perform(command.js.click)
    time.sleep(10)
    browser.element('#name').perform(command.js.click).type("Eddy Grant")
    browser.element('#email').perform(command.js.click).type("eddyfake@fakeemail.com")
    time.sleep(3)





