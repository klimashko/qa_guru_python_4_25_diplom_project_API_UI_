import json
from pytest_voluptuous import S
from requests import Response
import allure
from allure_commons.types import Severity
from schemas.booker import auth_create_token, create_new_booking, get_booking_ids, get_booking
from utils.functions_creates_api_data import create_new_bookingid


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('A simple health check endpoint to confirm whether the API is up and running')
@allure.story('Booking')
@allure.severity(Severity.BLOCKER)
def test_ping_health_check_api(booker):
    """A simple health check endpoint to confirm whether the API is up and running"""

    response: Response = booker.get('/ping')

    assert response.status_code == 201
    assert response.text == 'Created'

@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Creates a new auth token')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_auth_create_token(booker):
    """Creates a new auth token to use for access to the PUT and DELETE /booking"""

    payload = {"username": "admin", "password": "password123"}
    response: Response = booker.post('/auth', data=payload)

    assert response.status_code == 200
    assert S(auth_create_token.schema) == response.json()


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Creates a new booking in the API')
@allure.story('Booking')
@allure.severity(Severity.BLOCKER)
def test_create_new_booking(booker):
    """Creates a new booking in the API"""

    headers = {"Content-Type": "application/json"}
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

    assert response.status_code == 200
    assert S(create_new_booking.schema) == response.json()



@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Returns the ids of all the bookings that exist within the API')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_get_booking_ids(booker):
    """Returns the ids of all the bookings that exist within the API"""

    response: Response = booker.get('/booking')

    assert response.status_code == 200
    assert S(get_booking_ids.schema) == response.json()


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Returns a specific booking based upon the booking id provided')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_get_booking(booker):
    """Returns a specific booking based upon the booking id provided"""

    id = create_new_bookingid(booker)

    response: Response = booker.get(f'/booking/{id}')

    assert response.status_code == 200
    assert S(get_booking.schema) == response.json()

@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Updates a current booking')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_update_booking(booker):
    """Updates a current booking"""

    id = create_new_bookingid(booker)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }
    payload = {
    "firstname": "James",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
    }
    data = json.dumps(payload)

    response: Response = booker.put(f'/booking/{id}', headers=headers, data=data)

    assert response.status_code == 200
    assert S(get_booking.schema) == response.json()


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Updates a current booking with a partial payload')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_partial_update_booking(booker):
    """Updates a current booking with a partial payload"""

    id = create_new_bookingid(booker)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }
    payload = {
    "firstname": "James",
    "lastname": "Brown",
    }
    data = json.dumps(payload)

    response: Response = booker.patch(f'/booking/{id}', headers=headers, data=data)

    assert response.status_code == 200
    assert S(get_booking.schema) == response.json()


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Deletes booking by the specified id')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_delete_booking(booker):
    """Deletes booking by the specified id"""

    id = create_new_bookingid(booker)
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }

    response: Response = booker.delete(f'/booking/{id}', headers=headers)

    assert response.status_code == 201
    assert response.text == 'Created'