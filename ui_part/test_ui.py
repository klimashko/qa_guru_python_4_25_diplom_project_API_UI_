import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser

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

    client_data = FakeClient.message_data()
    name = client_data.get("name")
    email = client_data.get("email")
    phone = client_data.get("phone")
    subject = client_data.get("subject")
    message = client_data.get("message")


    browser = setup_browser
    browser.open("/")
    time.sleep(3)
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


    browser.element('.col-sm-5').should(have.text(
        f"Thanks for getting in touch {name}!\nWe'll get back to you about\n{subject}\nas soon as possible."))
