import time
import pytest
from selene import have
from selene.core import command
from selene.support.shared import browser


from models.ui_model import UserMessage, Room
from ui_part.pages.create_room_page import CreateRoomPage
from ui_part.pages.message_page import MessagePage


def test_send_message(setup_browser):
    message_page = MessagePage()

    user_data = UserMessage.message_data()
    user = UserMessage(name=user_data.get("name"),
                       email=user_data.get("email"),
                       phone=user_data.get("phone"),
                       subject=user_data.get("subject"),
                       message=user_data.get("message"))

    message_page.open(setup_browser)

    message_page.fill_message_form(user=user)

    message_page.assert_reply_with_data(name=user.name, subject=user.subject)


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
    time.sleep(3)
    create_room.go_to_frontpage()
    create_room.assert_all_rooms_on_frontpage(*types)
    # browser.element('.col-sm-7').perform(command.js.scroll_into_view)
    # browser.all('.col-sm-7').should(have.texts(*types))

    # def check_types_presence(elements, types):
    #     for t in types:
    #         print(t)
    #         found = False
    #         for element in elements:
    #             if element.should(have.text(t)):
    #                 found = True
    #                 print(t)
    #                 break
    #         if not found:
    #             return False
    #     return True
    #
    # assert check_types_presence(elements, types) == True, ('Нет всех типов комнат на фронтпэйдж')

    # for element in browser.all('.col-sm-7'):
    #     for type in types:
    #
    #         element.should(have.text(type)).element('[type="button"]').click()
    #         time.sleep(5)




# def test_open_browser_with_cookie(setup_browser):
#     # Данные для HTTP-запроса
#     url = "https://restful-booker.herokuapp.com/auth"
#     headers = {"Content-Type": "application/json",
#                "Accept": "application/json",
#                'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='
#                }
#
#     payload = {
#         "username": "admin",
#         "password": "password123"
#     }
#     data = json.dumps(payload)
#     # Отправить HTTP-запрос для открытия страницы
#     response: Response = requests.post(url, headers=headers, data=data)
#     assert response.status_code == 200
#
#     token = response.json()['token']
#     print("ЭТО ТОКЕН", token)
#     #
#     browser.open("/#/admin")
#     browser.driver.add_cookie({"name": "token", "value": token})
#     browser.open("/#/admin")
#     time.sleep(3)
#
#     # Открыть страницу в браузере Selene
#     # browser.driver().get(url)
#     browser.element('.col-sm-10').perform(command.js.scroll_into_view)
#     browser.element('.col-sm-10').should(have.text(
#         'Welcome to Shady Meadows, a delightful Bed & Breakfast nestled in the hills on Newingtonfordburyshire. A place so beautiful you will never want to leave. All our rooms have comfortable beds and we provide breakfast from the locally sourced supermarket. It is a delightful place.'))
#     time.sleep(3)
