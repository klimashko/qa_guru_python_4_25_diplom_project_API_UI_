import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser

from models.ui_model import UserMessage, Room
from ui_part.pages.create_room_page import CreateRoomPage
from ui_part.pages.message_page import MessagePage


def test_all_rooms_on_frontpage(setup_browser):
    types = ["Single", "Double", "Twin", "Family", "Suite"]

    create_room = CreateRoomPage()
    create_room.open(setup_browser)
    create_room.login_admin_panel()
    if browser.element('.fa.fa-remove.roomDelete'):
        print("Есть предустановленная комната")
    time.sleep(5)
    create_room.remove_preset_rooms()
    time.sleep(5)
    for type in types:
        room_features = Room.room_features(type)
        room = Room(type=room_features.get('type'),
                    number=room_features.get('number'),
                    accessible=room_features.get('accessible'),
                    price=room_features.get('price'),
                    wifi=room_features.get('wifi'),
                    refresh=room_features.get('refresh'),
                    safe=room_features.get('safe'),
                    views=room_features.get('views'))

        create_room.create_new_room(room=room)
        time.sleep(3)
    time.sleep(5)
    # if browser.element('#typesingle'):
    #     browser.element('.fa.fa-remove.roomDelete').click()
    create_room.go_to_frontpage()
    create_room.assert_all_rooms_on_frontpage(*types)
