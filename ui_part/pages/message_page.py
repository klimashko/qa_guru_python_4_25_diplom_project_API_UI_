import allure
from selene.core import command
from selene.support.shared import browser
from selene import have, be

from models.ui_model import UserMessage


class MessagePage:
    @allure.step("Open page")
    def open(self, browser):
        # browser = setup_browser
        browser.open("/")
        browser.element(".btn.btn-primary").perform(command.js.click)
        return self

    def fill_name(self, value):
        browser.element('#name').perform(command.js.click).type(value)
        return self

    def fill_email(self, value):
        browser.element('#email').perform(command.js.click).type(value)
        return self

    def fill_phone(self, value):
        browser.element('#phone').perform(command.js.click).type(value)
        return self

    def fill_subject(self, value):
        browser.element('#subject').perform(command.js.click).type(value)
        return self

    def fill_message(self, value):
        browser.element('#description').perform(command.js.click).type(value)
        return self

    @property
    def submit_message(self):
        browser.element('#submitContact').perform(command.js.click)
        return self

    @allure.step("Assert reply")
    def assert_reply_with_data(self, name, subject):
        browser.element('.col-sm-5').should(have.text(
            f"Thanks for getting in touch {name}!\nWe'll get back to you about\n{subject}\nas soon as possible."))
        return self

    @allure.step("Fill message form")
    def fill_message_form(self, user: UserMessage):
        self.fill_name(user.name)
        self.fill_email(user.email)
        self.fill_phone(user.phone)
        self.fill_subject(user.subject)
        self.fill_message(user.message)
        self.submit_message
