import json

from pytest_voluptuous import S
from requests import Response

from schemas.booker import auth_create_token, create_new_booking


def test_ping_health_check_api(booker):
    """A simple health check endpoint to confirm whether the API is up and running."""

    response: Response = booker.get('/ping')

    assert response.status_code == 201
    assert response.text == 'Created'


def test_auth_create_token(booker):
    """Creates a new auth token to use for access to the PUT and DELETE /booking"""

    payload = {"username": "admin", "password": "password123"}
    response: Response = booker.post('/auth', data=payload)

    assert response.status_code == 200
    assert S(auth_create_token.schema) == response.json()


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


