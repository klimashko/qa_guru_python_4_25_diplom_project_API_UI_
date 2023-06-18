import time
import pytest

from models.ui_model import Room
from pages.create_room_page import CreateRoomPage


@pytest.mark.parametrize("type_room", ["Single", "Double", "Twin", "Family", "Suite"])
def test_create_room(setup_browser, type_room):
    type_room = type_room
    create_room = CreateRoomPage()
    room_features = Room.room_features(type_room)
    room = Room(type_room=room_features.get('type_room'),
                number=room_features.get('number'),
                accessible=room_features.get('accessible'),
                price=room_features.get('price'),
                wifi=room_features.get('wifi'),
                refresh=room_features.get('refresh'),
                safe=room_features.get('safe'),
                views=room_features.get('views'))

    create_room.open(setup_browser)

    create_room.login_admin_panel()
    # time.sleep(2)
    create_room.remove_preset_rooms()
    # time.sleep(3)
    create_room.create_new_room(room=room)
    # time.sleep(2)
    create_room.second_remove_preset_rooms(type_room=room.type_room)
    # time.sleep(5)
    create_room.assert_created_room(type_room=room.type_room)
    time.sleep(3)
