import time
from selene.support.shared import browser

from models.ui_model import Room
from pages.create_room_page import CreateRoomPage


def test_all_rooms_on_frontpage(setup_browser):
    types_room = ["Single", "Double", "Twin", "Family", "Suite"]
    create_room = CreateRoomPage()

    create_room.open(setup_browser)
    create_room.login_admin_panel()

    # create_room.remove_preset_rooms()
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
