import pytest
import allure
from allure_commons.types import Severity
from selene import browser, be, command

from models.ui_model import Room
from pages.create_room_page import CreateRoomPage


@allure.tag("ui")
@allure.label('owner', 'klimashko')
@allure.feature('Check, admin posting on the site a room of each type in turn')
@allure.story('Crate room')
@allure.severity(Severity.CRITICAL)
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

    create_room.remove_rooms()

    create_room.create_new_room(room=room)

    create_room.second_remove_preset_rooms(type_room=room.type_room)

    create_room.assert_created_room(type_room=room.type_room)

    """Clean admin panel after assert all type rooms"""
    create_room.open(setup_browser)

    create_room.remove_rooms()


@allure.tag("ui")
@allure.label('owner', 'klimashko')
@allure.feature('Check filling user message form and getting confirmation')
@allure.story('Send message')
@allure.severity(Severity.CRITICAL)
def test_all_rooms(setup_browser):
    types_room = ["Single", "Double", "Twin", "Family", "Suite"]
    create_room = CreateRoomPage()

    create_room.open(setup_browser)
    create_room.login_admin_panel()

    create_room.remove_rooms()
    create_room.clean_panel_before_making_allrooms()
    for type_room in types_room:
        room_features = Room.room_features(type_room)
        room = Room(type_room=room_features.get('type_room'),
                    number=room_features.get('number'),
                    accessible=room_features.get('accessible'),
                    price=room_features.get('price'),
                    wifi=room_features.get('wifi'),
                    refresh=room_features.get('refresh'),
                    safe=room_features.get('safe'),
                    views=room_features.get('views'))

        create_room.create_new_room(room=room)

    create_room.go_to_frontpage()

    create_room.assert_all_rooms_on_frontpage(*types_room)

    """Clean admin panel after assert all type rooms"""
    create_room.open(setup_browser)

    create_room.remove_rooms()
