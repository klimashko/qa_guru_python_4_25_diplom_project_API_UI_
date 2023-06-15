import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser


from models.ui_model import UserMessage, Room
from ui_part.pages.create_room_page import CreateRoomPage
from ui_part.pages.message_page import MessagePage


def test_send_message(browser_management):
    message_page = MessagePage()

    user_data = UserMessage.message_data()
    user = UserMessage(name=user_data.get("name"),
                       email=user_data.get("email"),
                       phone=user_data.get("phone"),
                       subject=user_data.get("subject"),
                       message=user_data.get("message"))

    message_page.open(browser_management)

    message_page.fill_message_form(user=user)

    message_page.assert_reply_with_data(name=user.name, subject=user.subject)