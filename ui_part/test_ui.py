import json
import time
import pytest
from requests import Response
from selene import have, be
from selene.core import command
from selene.support.shared import browser
import allure
from allure_commons.types import Severity
from allure import step
import requests

from models.ui_model import FakeClient


# def test_send_client_message(setup_browser):
#     browser = setup_browser
#     browser.open("/")
#     time.sleep(3)
#     browser.element(".btn.btn-primary").perform(command.js.click)
#     time.sleep(3)
#
#     browser.element('#name').perform(command.js.click).type("Eddy Grant")
#     browser.element('#email').perform(command.js.click).type("eddyfake@fakeemail.com")
#     time.sleep(3)
#     browser.element('#phone').perform(command.js.click).type("123456789789")
#     browser.element('#subject').perform(command.js.click).type("booking")
#     browser.element('#description').perform(command.js.click).type(
#         "Hi, I interesting in family number on holiday")
#     time.sleep(3)
#     browser.element('#submitContact').perform(command.js.click)
#     time.sleep(5)
#
#
#
#     browser.element('.col-sm-5').should(have.text(
#         "Thanks for getting in touch Eddy Grant!\nWe'll get back to you about\nbooking\nas soon as possible."))

def test_send_client_message(setup_browser):
    with step("Preparing client data"):
        client_data = FakeClient.message_data()
        name = client_data.get("name")
        email = client_data.get("email")
        phone = client_data.get("phone")
        subject = client_data.get("subject")
        message = client_data.get("message")

    with step("Open message form"):
        browser = setup_browser
        browser.open("/")
        time.sleep(3)

    with step("Fill form"):
        browser.element(".btn.btn-primary").perform(command.js.click)
        time.sleep(3)

        browser.element('#name').perform(command.js.click).type(name)
        browser.element('#email').perform(command.js.click).type(email)
        time.sleep(3)
        browser.element('#phone').perform(command.js.click).type(phone)
        browser.element('#subject').perform(command.js.click).type(subject)
        browser.element('#description').perform(command.js.click).type(message)
        time.sleep(3)
        browser.element('#submitContact').perform(command.js.click)
        time.sleep(5)

    with step("Check reply"):
        browser.element('.col-sm-5').should(have.text(
            f"Thanks for getting in touch {name}!\nWe'll get back to you about\n{subject}\nas soon as possible."))


def test_admin_create_rooms(setup_browser):
    with step("Open Admin panel"):
        browser = setup_browser
        browser.open("/#/admin")
        time.sleep(3)

    with step("Login to Admin panel"):
        browser.element('#username').should(be.visible).type('admin')
        browser.element('#password').should(be.visible).type('password')
        browser.element('#doLogin').click()
        time.sleep(5)

    with step("Create room"):
        browser.element('#roomName').should(be.visible).type(102)
        browser.element('#type').click()
        browser.element('[value = "Twin"]').should(be.visible).click()  #Single, Twin, Double, Family, Suite
        browser.element('#accessible').click()
        browser.element('[value = "true"]').should(be.visible).click()  #false
        browser.element('#roomPrice').type(200)
        browser.element('#wifiCheckbox').click()  #refreshCheckbox, safeCheckbox, viewsCheckbox, radioCheckbox,
        browser.element('#refreshCheckbox').click()
        browser.element('#safeCheckbox').click()
        browser.element('#viewsCheckbox').click()
        browser.element('#createRoom').should(be.visible).click()

        time.sleep(5)
    with step("Check created room"):
        browser.element('#frontPageLink').click()
        time.sleep(5)

        browser.element('.col-sm-7').should(have.text('Twin'))
        # 'WiFi', 'Refreshments', 'Safe', 'Views'
        time.sleep(15)

    #     browser.element('.container').should(have.text("Admin panel")).click()
    #     time.sleep(600)

    # # Данные для HTTP-запроса
    # url = "https://restful-booker.herokuapp.com/auth"
    # headers = {"Content-Type": "application/json",
    #     "Accept": "application/json",
    #     'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
    # }
    #
    # payload = {
    #     "username": "admin",
    #     "password": "password123"
    # }
    # data = json.dumps(payload)
    # # Отправить HTTP-запрос для открытия страницы
    # response: Response = requests.post(url, data=data)
    # assert response.status_code == 200
    #
    # token = response.json()
    # print("ЭТО ТОКЕН", token)
    # #
    # browser.open("/#/admin")
    # browser.driver.add_cookie({"name": "token", "value": token})
    # browser.open("/#/admin")
    # Проверка статуса ответа
    # assert response.status_code == 200
    # Открыть страницу в браузере Selene
    # browser.driver().get(url)
    #
    #     # Проверить видимость элемента #adminPanel
    #     s('#adminPanel').should(be.visible)
    # else:
    #     print('Ошибка при выполнении запроса:', response.status_code)
