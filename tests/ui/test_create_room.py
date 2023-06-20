import time

import allure
import pytest
from allure_commons.types import Severity

from models.ui_model import Room
from pages.create_room_page import CreateRoomPage


@allure.tag("ui")
@allure.label('owner', 'klimashko')
@allure.feature('Check, admin posting on the site a room of each type in turn')
@allure.story('Crate room')
@allure.severity(Severity.CRITICAL)
@pytest.mark.parametrize("type_room", ["Single", "Double", "Twin", "Family", "Suite"])
def test_create_room(browser_management, type_room):
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

    create_room.open(browser_management)

    create_room.login_admin_panel()

    create_room.remove_preset_rooms()

    create_room.create_new_room(room=room)

    create_room.second_remove_preset_rooms(type_room=room.type_room)

    create_room.assert_created_room(type_room=room.type_room)

