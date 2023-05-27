from voluptuous import Schema, PREVENT_EXTRA, All, Length, Datetime, Coerce

auth_create_token = Schema(
    {
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

create_new_booking = Schema(
    {
        "bookingid": int,
        "booking": {
            "firstname": str,
            "lastname": str,
            "totalprice": int,
            "depositpaid": bool,
            "bookingdates": {
                "checkin": str,
                "checkout": str
            },
            "additionalneeds": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_unsuccessfull_schema = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user_schema = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

unsuccessfull_login_schema = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)