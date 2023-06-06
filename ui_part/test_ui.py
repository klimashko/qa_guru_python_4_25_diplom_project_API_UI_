import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser




def test_send_client_message(setup_browser):
    browser = setup_browser
    browser.open("/")
    time.sleep(3)
    browser.element(".btn.btn-primary").perform(command.js.click)
    time.sleep(3)

    browser.element('#name').perform(command.js.click).type("Eddy Grant")
    browser.element('#email').perform(command.js.click).type("eddyfake@fakeemail.com")
    time.sleep(3)
    browser.element('#phone').perform(command.js.click).type("123456789789")
    browser.element('#subject').perform(command.js.click).type("booking")
    browser.element('#description').perform(command.js.click).type(
        "Hi, I interesting in family number on holiday")
    time.sleep(3)
    browser.element('#submitContact').perform(command.js.click)
    time.sleep(5)



    browser.element('.col-sm-5').should(have.text(
        "Thanks for getting in touch Eddy Grant!\nWe'll get back to you about\nbooking\nas soon as possible."))
