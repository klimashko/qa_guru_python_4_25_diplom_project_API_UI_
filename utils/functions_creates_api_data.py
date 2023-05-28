import json
from pytest_voluptuous import S
from requests import Response
import allure
from allure_commons.types import Severity
from schemas.booker import auth_create_token, create_new_booking, get_booking_ids, get_booking


# id = test_create_new_booking(booker)

def create_new_bookingid(booker):
    """Creates a new booking, return booking id"""

    headers = {"Content-Type": "application/json"}u
    payload = {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    data = json.dumps(payload)
    response: Response = booker.post('/booking', headers=headers, data=data)

    # assert response.status_code == 200
    # assert S(create_new_booking.schema) == response.json()

    bookingid = response.json()['bookingid']
    print(bookingid)
    return bookingid