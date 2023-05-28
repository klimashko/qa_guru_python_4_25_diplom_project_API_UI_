import json
from requests import Response


def create_new_bookingid(booker):
    """Creates a new booking, return booking id"""

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
        "additionalneeds": "Breakfast"
    }
    data = json.dumps(payload)
    response: Response = booker.post('/booking', headers=headers, data=data)
    bookingid = response.json()['bookingid']
    return bookingid
