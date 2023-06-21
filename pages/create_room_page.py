import os
import time

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
        if browser.element('.btn.btn-primary').with_(timeout=30).wait_until(be.clickable):
            browser.element('.btn.btn-primary').should(be.clickable).perform(command.js.click)
        login = os.getenv('LOGIN_ADMIN')
        password = os.getenv('PASSWORD_ADMIN')
        browser.element('#username').should(be.visible).type(login)
        browser.element('#password').should(be.visible).type(password)
        browser.element('#doLogin').click()
        return self

    @allure.step("Remove preset rooms")
    def remove_rooms(self):
        if browser.element('.roomDelete').with_(timeout=10).wait_until(be.clickable):
            for element in browser.all('.roomDelete'):
                if element.with_(timeout=10).wait_until(be.clickable):
                    try:
                        browser.element('.roomDelete').perform(command.js.click)
                    finally:
                        pass
        return self

    def second_remove_preset_rooms(self, type_room):
        if browser.element('.row.detail').with_(timeout=10).wait_until(be.visible):
            for element in browser.all('.row.detail'):
                if element.element('.col-sm-2').element('.fa.fa-remove.roomDelete').with_(
                        timeout=10).wait_until(be.clickable):
                    try:
                        if not element.element('.col-sm-2').should(have.text(type_room)):
                            element.element('.col-sm-2').element('.roomDelete').perform(
                                command.js.click)
                    finally:
                        pass
        return self

    # def clean_panel_before_making_allrooms(self):
    #     browser.element('#createRoom').with_(timeout=5).wait_until(be.clickable)
    #     if browser.element('.row.detail').with_(timeout=5).wait_until(be.visible):
    #         for element in browser.all('.row.detail'):
    #             if browser.element('.col-sm-2').element('.roomDelete').with_(
    #                     timeout=5).wait_until(be.clickable):
    #                 browser.element('.col-sm-2').element('.roomDelete').perform(
    #                     command.js.click)
    #     return self

    def clean_panel_before_making_allrooms(self):
        browser.element('#createRoom').with_(timeout=5).wait_until(be.clickable)
        if browser.element('.roomDelete').with_(timeout=5).wait_until(be.clickable):
            for element in browser.all('.roomDelete'):
                if element.with_(timeout=5).wait_until(be.clickable):
                    try:
                        browser.element('.roomDelete').perform(command.js.click)
                    finally:
                        pass
        return self

    def fill_room_number(self, value):
        browser.element('#roomName').with_(timeout=30).should(be.blank).type(value)
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
        browser.element('#createRoom').with_(timeout=30).should(be.clickable).click()
        return self

    @allure.step("Create new room")
    def create_new_room(self, room: Room):

        self.fill_room_number(room.number)

        self.fill_room_type(room.type_room)

        self.fill_room_accessibility(room.accessible)

        self.fill_room_price(room.price)

        self.set_wifi(room.wifi)

        self.set_refresh(room.refresh)

        self.set_safe(room.safe)

        self.set_views(room.views)

        self.create_room_button()

        return self

    def go_to_frontpage(self):
        browser.element('#frontPageLink').with_(timeout=30).should(be.clickable).click()
        return self

    def assert_room_details_texts(self, value):
        browser.element('.col-sm-7').with_(timeout=30).should(be.visible)
        browser.element('.col-sm-7').perform(command.js.scroll_into_view)
        browser.all('.col-sm-7').should(have.texts(
            f'{value}\nPlease enter a description for this room\nWiFi\nRefreshments\nSafe\nViews\nBook this room'))
        return self

    @allure.step("Assert created room")
    def assert_created_room(self, type_room):
        self.go_to_frontpage()
        self.assert_room_details_texts(type_room)
        return self

    @allure.step("Assert created room")
    def assert_all_rooms_on_frontpage(self, *args):
        browser.element('.col-sm-7').perform(command.js.scroll_into_view)
        browser.all('.col-sm-7').should(have.texts(*args))
        return self
