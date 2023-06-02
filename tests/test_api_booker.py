import json
from pytest_voluptuous import S
from requests import Response
import allure
from allure_commons.types import Severity
from models.api_model import BookingData
from schemas.booker import auth_create_token, create_new_booking, get_booking_ids, get_booking
from utils.functions_creates_api_data import create_new_bookingid
import os
from dotenv import load_dotenv
from faker import Faker

fake_data = Faker()

load_dotenv()

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
@allure.severity(Severity.CRITICAL)
def test_auth_create_token(booker):
    """Creates a new auth token to use for access to the PUT and DELETE /booking"""

    USER = os.getenv('user')
    PASSWORD = os.getenv('password')
    payload = {"username": USER, "password": PASSWORD}

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

    headers = BookingData.headers_data()
    payload = BookingData.payload_data()

    data = json.dumps(payload)
    response: Response = booker.post('/booking', headers=headers, data=data)

    assert response.status_code == 200
    assert S(create_new_booking.schema) == response.json()
    assert payload.get("firstname") == response.json()["booking"]["firstname"]
    assert payload.get("lastname") == response.json()["booking"]["lastname"]
    assert payload.get("depositpaid") == response.json()["booking"]["depositpaid"]


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
@allure.severity(Severity.CRITICAL)
def test_update_booking(booker):
    """Updates a current booking"""

    id = create_new_bookingid(booker)
    headers = BookingData.headers_data()
    payload = BookingData.payload_data()
    data = json.dumps(payload)

    response: Response = booker.put(f'/booking/{id}', headers=headers, data=data)

    assert response.status_code == 200
    assert S(get_booking.schema) == response.json()
    assert payload.get("firstname") == response.json()["firstname"]
    assert payload.get("lastname") == response.json()["lastname"]
    assert payload.get("depositpaid") == response.json()["depositpaid"]


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Updates a current booking with a partial payload')
@allure.story('Booking')
@allure.severity(Severity.CRITICAL)
def test_partial_update_booking(booker):
    """Updates a current booking with a partial payload"""

    id = create_new_bookingid(booker)
    headers = BookingData.headers_data()
    payload = BookingData.payload_data_short()
    data = json.dumps(payload)

    response: Response = booker.patch(f'/booking/{id}', headers=headers, data=data)

    assert response.status_code == 200
    assert S(get_booking.schema) == response.json()
    assert payload.get("firstname") == response.json()["firstname"]
    assert payload.get("lastname") == response.json()["lastname"]


@allure.tag("api")
@allure.label('owner', 'klimashko')
@allure.feature('Deletes booking by the specified id')
@allure.story('Booking')
@allure.severity(Severity.NORMAL)
def test_delete_booking(booker):
    """Deletes booking by the specified id"""

    id = create_new_bookingid(booker)
    headers = BookingData.headers_data()

    response: Response = booker.delete(f'/booking/{id}', headers=headers)

    assert response.status_code == 201
    assert response.text == 'Created'