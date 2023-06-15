import os

from dotenv import load_dotenv
from selene import have, be
from selene.core import command
from selene.support.shared import browser
import allure

from models.ui_model import Room

load_dotenv()


class CreateRoomPage:
    @allure.step("Open Admin panel")
    def open(self, browser):
        # browser = setup_browser
        browser.open("/#/admin")
        return self

    @allure.step("Login")
    def login_admin_panel(self):
        login = os.getenv('LOGIN_ADMIN')
        password = os.getenv('PASSWORD_ADMIN')
        browser.element('#username').should(be.visible).type(login)
        browser.element('#password').should(be.visible).type(password)
        browser.element('#doLogin').click()
        return self

    @allure.step("Remove preset rooms")
    def remove_preset_rooms(self):
        if browser.all('.fa.fa-remove.roomDelete'):
            for element in browser.all('.fa.fa-remove.roomDelete'):
                element.click()
        return self

    def fill_room_number(self, value):
        browser.element('#roomName').should(be.visible).type(value)
        return self

    def fill_room_type(self, value):
        browser.element('#type').click()
        browser.element(f'[value = {value}]').should(
            be.visible).click()  # Single, Twin, Double, Family, Suite
        return self

    def fill_room_accessibility(self, value):
        browser.element('#accessible').click()
        if value:
            browser.element('[value = "true"]').should(be.visible).click()  # false
        else:
            browser.element('[value = "false"]').should(be.visible).click()
        return self

    def fill_room_price(self, value):
        browser.element('#roomPrice').type(value)
        return self

    def set_wifi(self, value):
        if value:
            browser.element('#wifiCheckbox').click()
        return self

    def set_refresh(self, value):
        if value:
            browser.element('#refreshCheckbox').click()
        return self

    def set_safe(self, value):
        if value:
            browser.element('#safeCheckbox').click()
        return self

    def set_views(self, value):
        if value:
            browser.element('#viewsCheckbox').click()
        return self

    def create_room_button(self):
        browser.element('#createRoom').should(be.visible).click()
        return self

    @allure.step("Create new room")
    def create_new_room(self, room: Room):

        self.fill_room_number(room.number)

        self.fill_room_type(room.type)

        self.fill_room_accessibility(room.accessible)

        self.fill_room_price(room.price)

        self.set_wifi(room.wifi)

        self.set_refresh(room.refresh)

        self.set_safe(room.safe)

        self.set_views(room.views)

        self.create_room_button()

        return self

    def go_to_frontpage(self):
        browser.element('#frontPageLink').click()
        return self

    def assert_room_details_texts(self, value):
        browser.element('.col-sm-7').perform(command.js.scroll_into_view)
        browser.all('.col-sm-7').should(have.texts(
            f'{value}\nPlease enter a description for this room\nWiFi\nRefreshments\nSafe\nViews\nBook this room'))
        return self

    @allure.step("Assert created room")
    def assert_created_room(self, type):
        self.go_to_frontpage()
        self.assert_room_details_texts(type)
        return self

    @allure.step("Assert created room")
    def assert_all_rooms_on_frontpage(self, *args):
        browser.element('.col-sm-7').perform(command.js.scroll_into_view)
        browser.all('.col-sm-7').should(have.texts(*args))
        return self