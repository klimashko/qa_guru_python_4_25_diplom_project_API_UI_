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

get_booking_ids = Schema(
    All(
        [
            {"bookingid": All(int, Coerce(str))},
        ],
        Length(min=1),
        extra=PREVENT_EXTRA,
        required=True
    )
)

get_booking = Schema(
    {
        "firstname": str,
        "lastname": str,
        "totalprice": int,
        "depositpaid": bool,
        "bookingdates": {
            "checkin": str,
            "checkout": str
        },
        "additionalneeds": str
    },
    extra=PREVENT_EXTRA,
    required=True
)
