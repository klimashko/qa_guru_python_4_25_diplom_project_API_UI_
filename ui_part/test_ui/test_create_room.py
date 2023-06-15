import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser

from models.ui_model import UserMessage, Room
from ui_part.pages.create_room_page import CreateRoomPage
from ui_part.pages.message_page import MessagePage


@pytest.mark.parametrize("type", ["Single", "Double", "Twin", "Family", "Suite"])
def test_create_room(setup_browser, type):
    type = type
    create_room = CreateRoomPage()
    room_features = Room.room_features(type)
    room = Room(type=room_features.get('type'),
                number=room_features.get('number'),
                accessible=room_features.get('accessible'),
                price=room_features.get('price'),
                wifi=room_features.get('wifi'),
                refresh=room_features.get('refresh'),
                safe=room_features.get('safe'),
                views=room_features.get('views'))

    create_room.open(setup_browser)

    create_room.login_admin_panel()
    time.sleep(1)
    create_room.remove_preset_rooms()
    time.sleep(5)
    create_room.create_new_room(room=room)
    time.sleep(3)
    create_room.assert_created_room(type=room.type)
    time.sleep(3)
