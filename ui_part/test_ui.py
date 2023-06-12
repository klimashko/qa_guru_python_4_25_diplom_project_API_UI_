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

from models.ui_model import UserMessage
from ui_part.conftest import setup_browser
from ui_part.pages.message_page import MessagePage


def test_send_message(setup_browser):
    message_page = MessagePage()

    user_data = UserMessage.message_data()
    user = UserMessage(name=user_data.get("name"),
                       email=user_data.get("email"),
                       phone=user_data.get("phone"),
                       subject=user_data.get("subject"),
                       message=user_data.get("message"))

    message_page.open(setup_browser)

    message_page.fill_message_form(user=user)

    message_page.assert_reply_with_data(name=user.name, subject=user.subject)


class CreateRoomPage:
    @allure.step("Open Admin panel")
    def open(self, browser):
        # browser = setup_browser
        browser.open("/#/admin")
        return self

    @allure.step("Login")
    def login_admin_panel(self):  # Добавить аргументы логин ипароль, брать их из .env!!!!!!!!!!!!!!!!!!!!!!!!!!
        browser.element('#username').should(be.visible).type('admin')
        browser.element('#password').should(be.visible).type('password')
        browser.element('#doLogin').click()
        return self

    @allure.step("Remove preset room")
    def remove_preset_room(self):
        browser.element('.fa.fa-remove.roomDelete').click()
        return self

    def fill_room_number(self):
        browser.element('#roomName').should(be.visible).type(102)
        return self
    def fill_room_type(self):
        browser.element('#type').click()
        type = "Twin"
        browser.element(f'[value = {type}]').should(
            be.visible).click()  # Single, Twin, Double, Family, Suite
        return self
    def fill_room_accessibility(self):
        browser.element('#accessible').click()
        browser.element('[value = "true"]').should(be.visible).click()  # false
        return self
    def fill_room_price(self):
        browser.element('#roomPrice').type(200)
        return self
    def choose_wifi(self):
        browser.element('#wifiCheckbox').click()
        return self
    def choose_refresh(self):
        browser.element('#refreshCheckbox').click()
        return self
    def choose_safe(self):
        browser.element('#safeCheckbox').click()
        return self
    def choose_views(self):
        browser.element('#viewsCheckbox').click()
        return self
    def create_room_button(self):
        browser.element('#createRoom').should(be.visible).click()
        return self
    @allure.step("Create room")
    def create_room(self):
        self.fill_room_number()
        # browser.element('#roomName').should(be.visible).type(102)
        self.fill_room_type()
        # browser.element('#type').click()
        # type = "Twin"
        # browser.element(f'[value = {type}]').should(
        #     be.visible).click()  # Single, Twin, Double, Family, Suite
        self.fill_room_accessibility()
        # browser.element('#accessible').click()
        # browser.element('[value = "true"]').should(be.visible).click()  # false
        self.fill_room_price()
        # browser.element('#roomPrice').type(200)
        self.choose_wifi()
        # browser.element('#wifiCheckbox').click()
        self.choose_refresh()
        # browser.element('#refreshCheckbox').click()
        self.choose_safe()
        # browser.element('#safeCheckbox').click()
        self.choose_views()
        # browser.element('#viewsCheckbox').click()
        self.create_room_button()
        # browser.element('#createRoom').should(be.visible).click()
        return self

    def go_to_frontpage(self):
        browser.element('#frontPageLink').click()
        return self

    def assert_room_details_texts(self):
        browser.element('.col-sm-7').perform(command.js.scroll_into_view)
        browser.all('.col-sm-7').should(have.texts(
            'Twin\nPlease enter a description for this room\nWiFi\nRefreshments\nSafe\nViews\nBook this room'))
        return self

    @allure.step("Assert created room")
    def assert_created_room(self): #  добавить аргумкенты какой текст должен быть, в зависимости от типа комнаты
        self.go_to_frontpage()
        self.assert_room_details_texts()
        return self


def test_create_room(setup_browser):
    create_room = CreateRoomPage()

    create_room.open(setup_browser)
    create_room.login_admin_panel()
    create_room.remove_preset_room()
    create_room.create_room()
    time.sleep(5)
    create_room.assert_created_room()
    time.sleep(5)


def test_open_browser_with_cookie(setup_browser):
    # Данные для HTTP-запроса
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
               }

    payload = {
        "username": "admin",
        "password": "password123"
    }
    data = json.dumps(payload)
    # Отправить HTTP-запрос для открытия страницы
    response: Response = requests.post(url, headers=headers, data=data)
    assert response.status_code == 200

    token = response.json()['token']
    print("ЭТО ТОКЕН", token)
    #
    browser.open("/#/admin")
    browser.driver.add_cookie({"name": "token", "value": token})
    browser.open("/#/admin")
    time.sleep(3)

    # Открыть страницу в браузере Selene
    # browser.driver().get(url)
    browser.element('.col-sm-10').perform(command.js.scroll_into_view)
    browser.element('.col-sm-10').should(have.text(
        'Welcome to Shady Meadows, a delightful Bed & Breakfast nestled in the hills on Newingtonfordburyshire. A place so beautiful you will never want to leave. All our rooms have comfortable beds and we provide breakfast from the locally sourced supermarket. It is a delightful place.'))
    time.sleep(3)
